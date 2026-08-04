// Read each row's filterable fields once instead of re-reading and re-parsing
// data-tags for every row on every keystroke.
function buildPaperIndex() {
    window.paperIndex = Array.from(document.querySelectorAll('.paper-row')).map(row => ({
        row,
        id: row.getAttribute('data-id'),
        title: row.getAttribute('data-title').toLowerCase(),
        authors: row.getAttribute('data-authors').toLowerCase(),
        year: row.getAttribute('data-year'),
        tags: JSON.parse(row.getAttribute('data-tags'))
    }));
    return window.paperIndex;
}

// Single place that keeps a tag button's class, pressed state and label in sync.
function setTagState(el, mode) {
    if (!el) return;
    el.classList.toggle('include', mode === 'include');
    el.classList.toggle('exclude', mode === 'exclude');
    el.setAttribute('aria-pressed', mode === 'include' ? 'true' : 'false');
    const tag = el.getAttribute('data-tag');
    const described = mode === 'include' ? 'included' : mode === 'exclude' ? 'excluded' : 'not filtered';
    el.setAttribute('aria-label', `${tag}: ${described}`);
}

function tagStateOf(el) {
    if (el.classList.contains('include')) return 'include';
    if (el.classList.contains('exclude')) return 'exclude';
    return 'none';
}

function debounce(fn, delay) {
    let timeout;
    return (...args) => {
        if (timeout) clearTimeout(timeout);
        timeout = setTimeout(() => fn(...args), delay);
    };
}

function updateURL() {
    const params = new URLSearchParams();
    if (searchInput.value) {
        params.set('search', searchInput.value);
    }
    if (yearFilter.value !== 'all') {
        params.set('year', yearFilter.value);
    }
    if (state.includeTags.size > 0) {
        params.set('include', Array.from(state.includeTags).join(','));
    }
    if (state.excludeTags.size > 0) {
        params.set('exclude', Array.from(state.excludeTags).join(','));
    }
    if (state.selectedPapers.size > 0) {
        params.set('selected', Array.from(state.selectedPapers).join(','));
        if (state.onlyShowSelected) {
            params.set('show_selected', 'true');
        }
    }
    const newSearch = params.toString() ? `?${params.toString()}` : '';
    window.history.replaceState(
        { filters: params.toString() },
        '',
        `${window.location.pathname}${newSearch}`
    );
}

function updatePaperNumbers() {
    let num = 1;
    document.querySelectorAll('.paper-row:not(.hidden)').forEach(row => {
        const numElem = row.querySelector('.paper-number');
        numElem.textContent = num++;
    });
}