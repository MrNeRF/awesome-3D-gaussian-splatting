"""Sweep every URL in the paper database and report the ones that need attention.

The PR validator only inspects entries changed in that PR, so a link that rots
after it was merged is never looked at again. This walks the whole file.
"""
import os
import re
import sys
import time
import yaml
import requests
from concurrent.futures import ThreadPoolExecutor

URL_FIELDS = ['paper', 'project_page', 'code', 'video']
WORKERS = 8
TIMEOUT = 25

# 403 and 429 are overwhelmingly bot protection rather than a rotten link, so
# they are listed separately instead of being reported as broken.
BLOCKED_CODES = {401, 403, 429}
OK_CODES = {200, 201, 202, 203, 204, 206, 300, 301, 302, 303, 304, 307, 308}

HEADERS = {
    'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/143.0 Safari/537.36'),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}

session = requests.Session()
session.headers.update(HEADERS)


def collect(entries):
    targets, malformed = [], []
    for entry in entries:
        for field in URL_FIELDS:
            value = entry.get(field)
            if value is None or str(value).strip().lower() in ('none', ''):
                continue
            raw = str(value)
            url = raw.strip()
            problems = []
            if raw != url:
                problems.append('leading/trailing whitespace')
            if not re.match(r'^https?://', url):
                problems.append('missing http(s) scheme')
            if ' ' in url:
                problems.append('contains a space')
            if problems:
                malformed.append((entry['id'], field, raw, problems))
            else:
                targets.append((entry['id'], field, url))
    return targets, malformed


def probe(url):
    try:
        r = session.head(url, timeout=TIMEOUT, allow_redirects=True)
        if r.status_code not in OK_CODES:
            r = session.get(url, timeout=TIMEOUT, allow_redirects=True, stream=True)
            r.close()
        return r.status_code
    except requests.RequestException as e:
        return type(e).__name__


def check(targets):
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        results = list(pool.map(lambda t: (t, probe(t[2])), targets))

    # Retry anything that failed, serially and spaced out, so that a rate limit
    # or a blip during the parallel pass is not reported as a broken link.
    confirmed = []
    for target, status in results:
        if status in OK_CODES:
            continue
        time.sleep(1)
        confirmed.append((target, probe(target[2])))

    dead = [(t, s) for t, s in confirmed if s not in OK_CODES and s not in BLOCKED_CODES]
    blocked = [(t, s) for t, s in confirmed if s in BLOCKED_CODES]
    return dead, blocked


def report(malformed, dead, blocked, total):
    lines = [f'Swept {total} URLs across the paper database.', '']

    if malformed:
        lines += [f'## Malformed ({len(malformed)})', '',
                  'These are not usable URLs and render as broken links.', '',
                  '| Paper | Field | Problem | Value |', '| --- | --- | --- | --- |']
        for pid, field, value, problems in malformed:
            lines.append(f'| `{pid}` | {field} | {", ".join(problems)} | `{value[:80]}` |')
        lines.append('')

    if dead:
        lines += [f'## Unreachable ({len(dead)})', '',
                  'Failed twice, including a spaced-out retry.', '',
                  '| Paper | Field | Status | URL |', '| --- | --- | --- | --- |']
        for (pid, field, url), status in dead:
            lines.append(f'| `{pid}` | {field} | {status} | {url} |')
        lines.append('')

    if blocked:
        lines += [f'<details><summary>Blocked by bot protection ({len(blocked)}) '
                  '— usually fine in a browser</summary>', '',
                  '| Paper | Field | Status | URL |', '| --- | --- | --- | --- |']
        for (pid, field, url), status in blocked:
            lines.append(f'| `{pid}` | {field} | {status} | {url} |')
        lines += ['', '</details>', '']

    if not (malformed or dead):
        lines.append('No malformed or unreachable URLs found.')
    return '\n'.join(lines)


def main():
    with open('awesome_3dgs_papers.yaml', encoding='utf-8') as f:
        entries = yaml.safe_load(f)

    targets, malformed = collect(entries)
    print(f'Checking {len(targets)} URLs from {len(entries)} papers '
          f'({len(malformed)} malformed, not checked)')

    dead, blocked = check(targets)
    body = report(malformed, dead, blocked, len(targets))
    print(body)

    with open('link-report.md', 'w', encoding='utf-8') as f:
        f.write(body)

    if os.getenv('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as f:
            f.write(f'has_issues={"true" if (malformed or dead) else "false"}\n')
            f.write(f'malformed={len(malformed)}\n')
            f.write(f'dead={len(dead)}\n')


if __name__ == '__main__':
    sys.exit(main())
