import json
import yaml
import sys
from typing import List, Dict, Any

def generate_html(entries: List[Dict[str, Any]], output_file: str) -> None:
    """Generate optimized HTML page while preserving design."""
    # Gather unique tags, etc.
    all_tags = sorted(set(tag for entry in entries for tag in entry["tags"]))
    year_options = generate_year_options(entries)
    tag_filters = generate_tag_filters(all_tags)
    paper_cards = generate_paper_cards(entries)

    html = f"""<!DOCTYPE HTML>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Awesome 3D Gaussian Splatting Paper List</title>

    <!-- Preconnects -->
    <link rel="preconnect" href="https://cdnjs.cloudflare.com">
    <link rel="preconnect" href="https://raw.githubusercontent.com">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

    <!-- Lazy load -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vanilla-lazyload/17.8.3/lazyload.min.js"></script>

    <style>
        :root {{
            --primary-color: #1772d0;
            --hover-color: #f09228;
            --bg-color: #ffffff;
            --card-bg: #ffffff;
            --border-color: #e5e7eb;
            --text-color: #1f2937;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.5;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }}

        h1 {{
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 2rem;
            color: var(--text-color);
        }}

        /* Donation Box */
        .donate-box {{
            background-color: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: 0.5rem;
            padding: 1.5rem;
            margin-bottom: 2rem;
            text-align: center;
        }}
        .donate-box h3 {{
            margin-top: 0;
            color: var(--primary-color);
            font-size: 1.25rem;
            margin-bottom: 0.5rem;
        }}
        .donate-box p {{
            margin: 0.5rem 0 1rem;
            color: #4b5563;
        }}
        .bitcoin-info {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1rem;
            flex-wrap: wrap;
            margin-top: 1rem;
        }}
        .bitcoin-label {{
            font-weight: 600;
            color: #4b5563;
        }}
        .bitcoin-address {{
            background: #fff;
            padding: 0.5rem 1rem;
            border-radius: 0.25rem;
            border: 1px solid var(--border-color);
            font-family: monospace;
            font-size: 0.9rem;
        }}
        .copy-button {{
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: 0.25rem;
            padding: 0.5rem 1rem;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: background-color 0.2s;
        }}
        .copy-button:hover {{
            background-color: var(--hover-color);
        }}

        /* Filter Info */
        .filter-info {{
            background-color: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: 0.5rem;
            padding: 1rem 1.5rem;
            margin-bottom: 2rem;
        }}
        .filter-info h3 {{
            margin-top: 0;
            color: var(--primary-color);
            font-size: 1.1rem;
        }}
        .filter-info p {{
            margin: 0.5rem 0;
            color: #4b5563;
        }}

        /* Filters Bar to avoid overlap */
        .filters {{
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            margin-bottom: 2rem;
            align-items: center;
        }}
        .search-wrapper {{
            position: relative;
            flex: 1 1 200px; /* flexible width, min 200px */
        }}
        .search-box {{
            width: 100%;
            padding: 0.75rem 1rem;
            border: 1px solid var(--border-color);
            border-radius: 0.5rem;
            font-size: 1rem;
        }}
        .clear-search-btn {{
            position: absolute;
            right: 10px;
            top: 50%;
            transform: translateY(-50%);
            background: none;
            border: none;
            cursor: pointer;
            color: #9ca3af;
            font-size: 1.2rem;
        }}
        .clear-search-btn:hover {{
            color: #dc2626;
        }}

        .filter-select {{
            padding: 0.75rem 1rem;
            border: 1px solid var(--border-color);
            border-radius: 0.5rem;
            background-color: white;
        }}

        .tag-filters {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 2rem;
        }}
        .tag-filter {{
            background: #f3f4f6;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            cursor: pointer;
            font-size: 0.9rem;
            transition: all 0.2s;
            color: var(--text-color);
        }}
        .tag-filter:hover {{
            background: #e5e7eb;
        }}
        .tag-filter.include {{
            background: var(--primary-color);
            color: white;
        }}
        .tag-filter.exclude {{
            background: #dc2626;
            color: white;
        }}

        /* Selection Controls */
        .selection-controls {{
            display: none;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1rem;
            padding: 1rem;
            background-color: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: 0.5rem;
        }}
        .selection-mode .selection-controls {{
            display: flex;
            flex-wrap: wrap;
        }}
        .selection-checkbox {{
            display: none;
            position: absolute;
            top: 1rem;
            right: 1rem;
            width: 2rem;
            height: 2rem;
            z-index: 2;
            cursor: pointer;
            opacity: 1;
            appearance: none;
            -webkit-appearance: none;
            background: white;
            border: 2px solid #e5e7eb;
            border-radius: 50%;
            transition: all 0.2s ease;
        }}
        .selection-checkbox:checked {{
            background: #10b981;
            border-color: #10b981;
        }}
        .selection-checkbox:checked::before {{
            content: '✓';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: white;
            font-size: 1.2rem;
        }}
        .selection-mode .selection-checkbox {{
            display: block !important;
            pointer-events: auto !important;
        }}
        .paper-card.selected {{
            border: 2px solid var(--primary-color);
            box-shadow: 0 0 0 1px var(--primary-color);
        }}

        .control-button {{
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            border: none;
            cursor: pointer;
            font-size: 0.9rem;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.2s;
        }}
        .control-button.primary {{
            background-color: var(--primary-color);
            color: white;
        }}
        .control-button.secondary {{
            background-color: #f3f4f6;
            color: var(--text-color);
        }}
        .control-button:hover {{
            opacity: 0.9;
            transform: translateY(-1px);
        }}

        .selection-counter {{
            padding: 0.5rem 1rem;
            background-color: #f3f4f6;
            border-radius: 0.5rem;
            font-size: 0.9rem;
            color: var(--text-color);
        }}

        /* Selection Preview */
        .selection-preview {{
            position: fixed;
            right: 20px;
            top: 50%;
            transform: translateY(-50%);
            width: 300px;
            max-height: 80vh;
            background: white;
            border: 1px solid var(--border-color);
            border-radius: 0.75rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            z-index: 1000;
            display: none;
            flex-direction: column;
        }}
        .selection-mode .selection-preview {{
            display: flex;
        }}
        .preview-header {{
            padding: 1rem;
            border-bottom: 1px solid var(--border-color);
            font-weight: bold;
            background: #f8fafc;
            border-radius: 0.75rem 0.75rem 0 0;
        }}
        .preview-container {{
            padding: 1rem;
            overflow-y: auto;
            max-height: calc(80vh - 60px);
        }}
        .preview-item {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            padding: 0.75rem;
            border: 1px solid var(--border-color);
            border-radius: 0.5rem;
            margin-bottom: 0.5rem;
            background: white;
        }}
        .preview-content {{
            cursor: pointer;
            flex: 1;
            min-width: 0;
            padding: 0.5rem;
        }}
        .preview-content:hover {{
            background-color: #f3f4f6;
            border-radius: 0.375rem;
        }}
        .preview-title {{
            font-weight: 600;
            margin-bottom: 0.25rem;
            font-size: 0.9rem;
            color: var(--text-color);
        }}
        .preview-authors {{
            font-size: 0.8rem;
            color: #4b5563;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}
        .preview-remove {{
            background: none;
            border: none;
            color: #6b7280;
            cursor: pointer;
            padding: 0.25rem;
            margin-left: 0.5rem;
            border-radius: 0.25rem;
        }}
        .preview-remove:hover {{
            color: #dc2626;
            background: #f3f4f6;
        }}

        /* Share Modal */
        .share-modal {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            z-index: 1000;
            justify-content: center;
            align-items: center;
        }}
        .share-modal.show {{
            display: flex;
        }}
        .share-modal-content {{
            background-color: white;
            padding: 2rem;
            border-radius: 0.75rem;
            max-width: 600px;
            width: 90%;
            position: relative;
        }}
        .share-modal-header {{
            margin-bottom: 1.5rem;
        }}
        .share-modal-header h2 {{
            margin: 0;
            font-size: 1.5rem;
            color: var(--text-color);
        }}
        .share-url-container {{
            display: flex;
            gap: 1rem;
            margin-bottom: 1.5rem;
        }}
        .share-url-input {{
            flex: 1;
            padding: 0.75rem 1rem;
            border: 1px solid var(--border-color);
            border-radius: 0.5rem;
            font-size: 0.9rem;
        }}
        .share-modal-close {{
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: none;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            color: #6b7280;
        }}

        /* Paper Cards */
        .papers-grid {{
            display: grid;
            gap: 2rem;
        }}
        .paper-card {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 0.75rem;
            padding: 2rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            display: flex;
            gap: 1.5rem;
            position: relative;
        }}
        .paper-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        .paper-number {{
            position: absolute;
            top: -1rem;
            left: -1rem;
            background-color: var(--primary-color);
            color: white;
            width: 2rem;
            height: 2rem;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            z-index: 1;
        }}
        .paper-thumbnail {{
            flex: 0 0 200px;
            height: 283px;
            border-radius: 0.5rem;
            overflow: hidden;
            border: 1px solid var(--border-color);
            background-color: #f3f4f6;
            position: relative;
        }}
        .paper-thumbnail img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.2s;
        }}
        .paper-thumbnail img:hover {{
            transform: scale(1.05);
        }}
        .paper-content {{
            flex: 1;
            min-width: 0;
        }}
        .paper-title {{
            font-size: 1.25rem;
            font-weight: 600;
            margin: 0 0 1rem 0;
            color: var(--text-color);
        }}
        .paper-authors {{
            color: #4b5563;
            margin-bottom: 1rem;
        }}
        .paper-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 1rem;
        }}
        .paper-tag {{
            background: #f3f4f6;
            padding: 0.25rem 0.75rem;
            border-radius: 0.5rem;
            font-size: 0.85rem;
            color: #4b5563;
        }}
        .paper-links {{
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            margin-top: 1rem;
        }}
        .paper-link {{
            color: var(--primary-color);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 1rem;
            background: #f3f4f6;
            border-radius: 0.5rem;
            transition: all 0.2s;
            font-size: 0.9rem;
        }}
        .paper-link:hover {{
            background: #e5e7eb;
            color: var(--hover-color);
        }}
        .paper-abstract {{
            margin-top: 1rem;
            display: none;
            background: #f9fafb;
            padding: 1rem;
            border-radius: 0.5rem;
            color: #4b5563;
            line-height: 1.6;
        }}
        .paper-abstract.show {{
            display: block;
        }}
        .paper-row {{
            display: none;
        }}
        .paper-row.visible {{
            display: block;
        }}

        @media (max-width: 768px) {{
            .filters {{
                flex-direction: column;
            }}
            .search-wrapper {{
                margin-right: 0;
            }}
            .selection-controls {{
                flex-direction: column;
                align-items: stretch;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>MrNeRF's Awesome-3D-Gaussian-Splatting-Paper-List</h1>

        <div class="donate-box">
            <h3>Support This Project</h3>
            <p>If you find this resource helpful, consider supporting its development and maintenance.</p>
            <div class="bitcoin-info">
                <span class="bitcoin-label">Bitcoin:</span>
                <code class="bitcoin-address">bc1qz7z4c2cn46t7rkgsh7mr8tw9ssgctepzxrtqfw</code>
                <button class="copy-button" onclick="copyBitcoinAddress()">
                    <i class="fas fa-copy"></i> Copy
                </button>
                <a href="https://github.com/sponsors/MrNeRF" class="sponsor-button" target="_blank" rel="noopener">
                    <i class="fas fa-heart"></i> Sponsor
                </a>
            </div>
        </div>

        <div class="filter-info">
            <h3>Filter Options</h3>
            <p><strong>Search:</strong> Enter paper title or author names, then click <i class="fas fa-times"></i> to clear.</p>
            <p><strong>Year:</strong> Filter by publication year</p>
            <p><strong>Tags:</strong> Click once to include (blue), twice to exclude (red), third time to remove filter</p>
            <p><strong>Selection:</strong> Use selection mode to pick and share specific papers</p>
        </div>

        <div class="selection-controls">
            <button class="control-button secondary" onclick="toggleSelectionMode()">
                <i class="fas fa-times"></i> Exit Selection Mode
            </button>
            <div class="selection-counter">0 papers selected</div>
            <button class="control-button secondary" onclick="clearSelection()">
                <i class="fas fa-trash"></i> Clear Selection
            </button>
            <button class="control-button primary" onclick="showShareModal()">
                <i class="fas fa-share"></i> Share Selection
            </button>
        </div>

        <div class="selection-preview">
            <div class="preview-header">
                Selected Papers
            </div>
            <div class="preview-container" id="selectionPreview"></div>
        </div>

        <!-- Share Modal -->
        <div class="share-modal" id="shareModal">
            <div class="share-modal-content">
                <button class="share-modal-close" onclick="hideShareModal()">&times;</button>
                <div class="share-modal-header">
                    <h2>Share Selected Papers</h2>
                </div>
                <div class="share-url-container">
                    <input type="text" class="share-url-input" id="shareUrl" readonly>
                    <button class="control-button primary" onclick="copyShareLink()">
                        <i class="fas fa-copy"></i> Copy Link
                    </button>
                </div>
            </div>
        </div>

        <!-- Filters Bar -->
        <div class="filters">
            <div class="search-wrapper">
                <input type="text" id="searchInput" class="search-box" placeholder="Search papers by title or authors...">
                <button class="clear-search-btn" onclick="clearSearch()" title="Clear search">
                    <i class="fas fa-times"></i>
                </button>
            </div>
            <select id="yearFilter" class="filter-select">
                <option value="all">All Years</option>
                {year_options}
            </select>
            <button class="control-button secondary" onclick="toggleSelectionMode()">
                <i class="fas fa-check-square"></i> Selection Mode
            </button>
        </div>

        <!-- Tag Filters -->
        <div class="tag-filters" id="tagFilters">
            {tag_filters}
        </div>

        <!-- Paper Cards -->
        <div class="papers-grid">
            {paper_cards}
        </div>
    </div>

    <script>
    document.addEventListener('DOMContentLoaded', function() {{
        // LazyLoad
        const lazyLoadInstance = new LazyLoad({{
            elements_selector: ".lazy",
            callback_error: (img) => {{
                if (img.dataset.fallback) {{
                    img.src = img.dataset.fallback;
                }}
            }},
            callback_loaded: (img) => {{
                img.classList.add('loaded');
            }}
        }});

        const paperCards = document.querySelectorAll('.paper-row');
        const searchInput = document.getElementById('searchInput');
        const yearFilter = document.getElementById('yearFilter');
        const tagFilters = document.querySelectorAll('.tag-filter');

        let selectedPapers = new Set();
        let isSelectionMode = false;
        let includeTags = new Set();
        let excludeTags = new Set();
        let onlyShowSelected = false; // If opened via shared link

        /* Copy Bitcoin */
        function copyBitcoinAddress() {{
            const address = document.querySelector('.bitcoin-address').textContent;
            navigator.clipboard.writeText(address).then(() => {{
                const button = document.querySelector('.copy-button');
                const originalText = button.innerHTML;
                button.innerHTML = '<i class="fas fa-check"></i> Copied!';
                setTimeout(() => {{
                    button.innerHTML = originalText;
                }}, 2000);
            }});
        }}

        /* Clear search */
        function clearSearch() {{
            searchInput.value = '';
            filterPapers();
            updateURL();
        }}

        /* Update URL bar */
        function updateURL() {{
            const params = new URLSearchParams();
            if (searchInput.value) {{
                params.set('search', searchInput.value);
            }}
            if (yearFilter.value !== 'all') {{
                params.set('year', yearFilter.value);
            }}
            if (includeTags.size > 0) {{
                params.set('include', Array.from(includeTags).join(','));
            }}
            if (excludeTags.size > 0) {{
                params.set('exclude', Array.from(excludeTags).join(','));
            }}
            if (selectedPapers.size > 0) {{
                params.set('selected', Array.from(selectedPapers).join(','));
            }}
            const newSearch = params.toString() ? `?${{params.toString()}}` : '';
            window.history.replaceState(
                {{ filters: params.toString() }},
                '',
                `${{window.location.pathname}}${{newSearch}}`
            );
        }}

        /* Remove from selection */
        function removeFromSelection(paperId) {{
            const checkbox = document.querySelector(`.paper-row[data-id="${{paperId}}"] .selection-checkbox`);
            if (checkbox) {{
                checkbox.checked = false;
                selectedPapers.delete(paperId);

                // Remove highlight
                const paperCard = checkbox.closest('.paper-card');
                if (paperCard) {{
                    paperCard.classList.remove('selected');
                }}

                // Remove from preview
                const previewItem = document.querySelector(`.preview-item[data-paper-id="${{paperId}}"]`);
                if (previewItem) {{
                    previewItem.remove();
                }}

                updateSelectionCount();
                updateURL();

                if (onlyShowSelected) {{
                    // Hide that card
                    const row = checkbox.closest('.paper-row');
                    row.classList.remove('visible');
                    updatePaperNumbers();
                }}
            }}
        }}

        /* Selection count */
        function updateSelectionCount() {{
            const counter = document.querySelector('.selection-counter');
            counter.textContent = `${{selectedPapers.size}} paper${{selectedPapers.size === 1 ? '' : 's'}} selected`;
        }}

        /* Toggle selection */
        function togglePaperSelection(paperId, checkbox) {{
            if (!isSelectionMode) return;
            
            const paperCard = checkbox.closest('.paper-card');
            const paperRow = paperCard.closest('.paper-row');

            if (checkbox.checked) {{
                // Add
                selectedPapers.add(paperId);
                paperCard.classList.add('selected');

                // Create preview
                const title = paperRow.getAttribute('data-title');
                const authors = paperRow.getAttribute('data-authors');
                const year = paperRow.getAttribute('data-year');

                const previewItem = document.createElement('div');
                previewItem.className = 'preview-item';
                previewItem.setAttribute('data-paper-id', paperId);
                previewItem.innerHTML = `
                    <div class="preview-content" style="cursor: pointer;" onclick="scrollToPaper('${{paperId}}')">
                        <div class="preview-title">${{title}} (${{year}})</div>
                        <div class="preview-authors">${{authors}}</div>
                    </div>
                    <button class="preview-remove" onclick="event.stopPropagation(); removeFromSelection('${{paperId}}')">
                        <i class="fas fa-times"></i>
                    </button>
                `;
                document.getElementById('selectionPreview').appendChild(previewItem);

                // If onlyShowSelected is set, ensure visible
                if (onlyShowSelected) {{
                    paperRow.classList.add('visible');
                    updatePaperNumbers();
                }}
            }} else {{
                // Remove
                removeFromSelection(paperId);
            }}
            updateSelectionCount();
            updateURL();
        }}

        /* Checkbox click */
        function handleCheckboxClick(ev, paperId, checkbox) {{
            ev.stopPropagation();
            togglePaperSelection(paperId, checkbox);
        }}

        /* Scroll to paper */
        function scrollToPaper(paperId) {{
            const paperRow = document.querySelector(`.paper-row[data-id="${{paperId}}"]`);
            if (paperRow) {{
                paperRow.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                
                const paperCard = paperRow.querySelector('.paper-card');
                if (paperCard) {{
                    paperCard.style.transition = 'background-color 0.3s ease';
                    paperCard.style.backgroundColor = '#f0f9ff';
                    setTimeout(() => {{
                        paperCard.style.backgroundColor = '';
                    }}, 1500);
                }}
            }}
        }}

        /* Clear entire selection */
        function clearSelection() {{
            selectedPapers.clear();
            document.querySelectorAll('.paper-card').forEach(card => {{
                card.classList.remove('selected');
                const checkbox = card.querySelector('.selection-checkbox');
                if (checkbox) checkbox.checked = false;
            }});
            document.getElementById('selectionPreview').innerHTML = '';
            updateSelectionCount();
            updateURL();

            // If only showing selected, hide all
            if (onlyShowSelected) {{
                paperCards.forEach(row => row.classList.remove('visible'));
            }}
        }}

        /* Toggle selection mode */
        function toggleSelectionMode() {{
            isSelectionMode = !isSelectionMode;
            document.body.classList.toggle('selection-mode', isSelectionMode);

            const controls = document.querySelector('.selection-controls');
            controls.style.display = isSelectionMode ? 'flex' : 'none';

            const selectionButtons = document.querySelectorAll('[onclick="toggleSelectionMode()"]');
            selectionButtons.forEach(button => {{
                button.innerHTML = isSelectionMode
                    ? '<i class="fas fa-times"></i> Exit Selection Mode'
                    : '<i class="fas fa-check-square"></i> Selection Mode';
            }});

            // If we are exiting selection mode and we had onlyShowSelected, reload the base page
            if (!isSelectionMode && onlyShowSelected) {{
                // Remove all query params and reload
                const baseUrl = window.location.href.split('?')[0];
                window.location.href = baseUrl;
            }}
        }}

        /* Share */
        function showShareModal() {{
            if (selectedPapers.size === 0) {{
                alert('Please select at least one paper to share.');
                return;
            }}
            const shareUrl = new URL(window.location.href);
            shareUrl.searchParams.set('selected', Array.from(selectedPapers).join(','));
            document.getElementById('shareUrl').value = shareUrl.toString();
            document.getElementById('shareModal').classList.add('show');
        }}
        function hideShareModal() {{
            document.getElementById('shareModal').classList.remove('show');
        }}
        async function copyShareLink() {{
            const shareUrl = document.getElementById('shareUrl');
            try {{
                await navigator.clipboard.writeText(shareUrl.value);
                const copyButton = document.querySelector('.share-url-container .control-button');
                const origText = copyButton.innerHTML;
                copyButton.innerHTML = '<i class="fas fa-check"></i> Copied!';
                setTimeout(() => {{
                    copyButton.innerHTML = origText;
                }}, 2000);
            }} catch(e) {{
                alert('Failed to copy link. Please copy manually.');
            }}
        }}

        /* Tag filter clicks */
        tagFilters.forEach(tagFilter => {{
            tagFilter.addEventListener('click', () => {{
                const tag = tagFilter.getAttribute('data-tag');
                if (!tagFilter.classList.contains('include') && !tagFilter.classList.contains('exclude')) {{
                    tagFilter.classList.add('include');
                    includeTags.add(tag);
                }} else if (tagFilter.classList.contains('include')) {{
                    tagFilter.classList.remove('include');
                    tagFilter.classList.add('exclude');
                    includeTags.delete(tag);
                    excludeTags.add(tag);
                }} else {{
                    tagFilter.classList.remove('exclude');
                    excludeTags.delete(tag);
                }}
                filterPapers();
                updateURL();
            }});
        }});

        /* Filter papers */
        const debounce = (fn, delay) => {{
            let timeout;
            return (...args) => {{
                if (timeout) clearTimeout(timeout);
                timeout = setTimeout(() => fn(...args), delay);
            }};
        }};
        const filterPapersDebounced = debounce(filterPapers, 150);

        function filterPapers() {{
            if (onlyShowSelected) {{
                paperCards.forEach(row => {{
                    const id = row.getAttribute('data-id');
                    row.classList.toggle('visible', selectedPapers.has(id));
                }});
                updatePaperNumbers();
                lazyLoadInstance.update();
                updateURL();
                return;
            }}

            // Normal filter
            const sTerm = searchInput.value.toLowerCase();
            const selYear = yearFilter.value;
            paperCards.forEach(row => {{
                const title = row.getAttribute('data-title').toLowerCase();
                const authors = row.getAttribute('data-authors').toLowerCase();
                const year = row.getAttribute('data-year');
                const tags = JSON.parse(row.getAttribute('data-tags'));

                const matchSearch = title.includes(sTerm) || authors.includes(sTerm);
                const matchYear = (selYear === 'all') || (year === selYear);
                const matchInc = (includeTags.size === 0) || [...includeTags].every(t => tags.includes(t));
                const matchExc = (excludeTags.size === 0) || ![...excludeTags].some(t => tags.includes(t));

                const visible = matchSearch && matchYear && matchInc && matchExc;
                row.classList.toggle('visible', visible);
            }});
            updatePaperNumbers();
            lazyLoadInstance.update();
            updateURL();
        }}

        function updatePaperNumbers() {{
            let num = 1;
            document.querySelectorAll('.paper-row.visible').forEach(row => {{
                const numElem = row.querySelector('.paper-number');
                numElem.textContent = num++;
            }});
        }}

        // Listen
        searchInput.addEventListener('input', filterPapersDebounced);
        yearFilter.addEventListener('change', filterPapersDebounced);

        // Abstract toggle
        document.querySelectorAll('.abstract-toggle').forEach(btn => {{
            btn.addEventListener('click', () => {{
                const abstract = btn.nextElementSibling;
                const open = abstract.classList.toggle('show');
                btn.textContent = open ? 'Hide Abstract' : 'Show Abstract';
            }});
        }});

        // Clicking on a card toggles selection if in selection mode
        document.querySelectorAll('.paper-card').forEach(card => {{
            card.addEventListener('click', (ev) => {{
                if (!isSelectionMode) return;
                // if click on link or abstract btn, ignore
                if (
                    ev.target.classList.contains('paper-link') ||
                    ev.target.closest('.paper-link') ||
                    ev.target.classList.contains('abstract-toggle')
                ) {{
                    return;
                }}
                const checkbox = card.querySelector('.selection-checkbox');
                if (checkbox && ev.target !== checkbox) {{
                    checkbox.checked = !checkbox.checked;
                    const pid = card.parentElement.getAttribute('data-id');
                    togglePaperSelection(pid, checkbox);
                }}
            }});
        }});

        /* Parse URL */
        function applyURLParams() {{
            const params = new URLSearchParams(window.location.search);
            const searchTerm = params.get('search');
            if (searchTerm) {{
                searchInput.value = searchTerm;
            }}
            const yr = params.get('year');
            if (yr) {{
                yearFilter.value = yr;
            }}

            const inc = params.get('include');
            if (inc) {{
                includeTags = new Set(inc.split(','));
                includeTags.forEach(t => {{
                    const tf = document.querySelector(`.tag-filter[data-tag="${{t}}"]`);
                    if (tf) tf.classList.add('include');
                }});
            }}
            const exc = params.get('exclude');
            if (exc) {{
                excludeTags = new Set(exc.split(','));
                excludeTags.forEach(t => {{
                    const tf = document.querySelector(`.tag-filter[data-tag="${{t}}"]`);
                    if (tf) tf.classList.add('exclude');
                }});
            }}
            const selPapers = params.get('selected');
            if (selPapers) {{
                const arr = selPapers.split(',');
                if (arr.length > 0) {{
                    toggleSelectionMode();
                    onlyShowSelected = true;
                    arr.forEach(id => {{
                        const row = document.querySelector(`.paper-row[data-id="${{id}}"]`);
                        if (row) {{
                            const cb = row.querySelector('.selection-checkbox');
                            if (cb) {{
                                cb.checked = true;
                                togglePaperSelection(id, cb);
                            }}
                        }}
                    }});
                }}
            }}
            // Filter
            filterPapers();
        }}

        // Popstate
        window.addEventListener('popstate', () => {{
            searchInput.value = '';
            yearFilter.value = 'all';
            includeTags.clear();
            excludeTags.clear();
            clearSelection();
            tagFilters.forEach(tag => {{
                tag.classList.remove('include','exclude');
            }});
            onlyShowSelected = false;
            applyURLParams();
        }});

        // init
        paperCards.forEach(c => c.classList.add('visible'));
        updatePaperNumbers();
        applyURLParams();

        // Expose
        window.copyBitcoinAddress = copyBitcoinAddress;
        window.clearSearch = clearSearch;
        window.toggleSelectionMode = toggleSelectionMode;
        window.clearSelection = clearSelection;
        window.showShareModal = showShareModal;
        window.hideShareModal = hideShareModal;
        window.copyShareLink = copyShareLink;
        window.removeFromSelection = removeFromSelection;
        window.togglePaperSelection = togglePaperSelection;
        window.handleCheckboxClick = handleCheckboxClick;
        window.scrollToPaper = scrollToPaper;
    }});
    </script>
</body>
</html>"""

    with open(output_file, "w", encoding="utf-8") as fp:
        fp.write(html)


def generate_year_options(entries: List[Dict[str, Any]]) -> str:
    years = sorted({str(e.get("year", "")) for e in entries if e.get("year")}, reverse=True)
    return "\n".join(f'<option value="{y}">{y}</option>' for y in years)


def generate_tag_filters(tags: List[str]) -> str:
    filtered = [t for t in sorted(tags) if not t.startswith("Year ")]
    return "\n".join(f'<div class="tag-filter" data-tag="{t}">{t}</div>' for t in filtered)


def generate_paper_cards(entries: List[Dict[str, Any]]) -> str:
    cards = []
    for e in entries:
        # Links
        links = []
        if e.get("project_page"):
            links.append(f"""<a href="{e['project_page']}" class="paper-link" target="_blank" rel="noopener">
                             <i class="fas fa-globe"></i> Project Page</a>""")
        if e.get("paper"):
            links.append(f"""<a href="{e['paper']}" class="paper-link" target="_blank" rel="noopener">
                             <i class="fas fa-file-alt"></i> Paper</a>""")
        if e.get("code"):
            links.append(f"""<a href="{e['code']}" class="paper-link" target="_blank" rel="noopener">
                             <i class="fas fa-code"></i> Code</a>""")
        if e.get("video"):
            links.append(f"""<a href="{e['video']}" class="paper-link" target="_blank" rel="noopener">
                             <i class="fas fa-video"></i> Video</a>""")

        # Tag HTML
        display_tags = [t for t in e["tags"] if not t.startswith("Year ")]
        tags_html = "\n".join(f'<span class="paper-tag">{t}</span>' for t in display_tags)

        # Abstract
        abstract_html = (
            f"""
            <button class="abstract-toggle">Show Abstract</button>
            <div class="paper-abstract">
                {e.get('abstract', 'No abstract available.')}
            </div>
            """
            if e.get("abstract")
            else ""
        )

        # Year
        year = e.get("year", "N/A")

        # Thumbnail
        thumb_url = e.get("thumbnail", f"assets/thumbnails/{e['id']}.jpg")
        fallback_url = "https://raw.githubusercontent.com/yangcaogit/3DGS-DET/main/assets/teaser.jpg"

        # Build card
        card = f"""
        <div class="paper-row" data-id="{e['id']}"
             data-title="{e['title']}"
             data-authors="{e['authors']}"
             data-year="{year}"
             data-tags='{json.dumps(e["tags"])}'>
          <div class="paper-card">
            <input type="checkbox"
                   class="selection-checkbox"
                   onclick="handleCheckboxClick(event, '{e['id']}', this)">
            <div class="paper-number"></div>
            <div class="paper-thumbnail">
                <img data-src="{thumb_url}"
                     data-fallback="{fallback_url}"
                     alt="Paper thumbnail for {e['title']}"
                     class="lazy"
                     loading="lazy"/>
            </div>
            <div class="paper-content">
                <h2 class="paper-title">
                    {e['title']} <span class="paper-year">({year})</span>
                </h2>
                <p class="paper-authors">{e['authors']}</p>
                <div class="paper-tags">{tags_html}</div>
                <div class="paper-links">{' '.join(links)}</div>
                {abstract_html}
            </div>
          </div>
        </div>
        """
        cards.append(card)
    return "\n".join(cards)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_html.py <input_yaml> <output_html>")
        sys.exit(1)
    inp = sys.argv[1]
    out = sys.argv[2]
    try:
        with open(inp, "r", encoding="utf-8") as fp:
            entries = yaml.safe_load(fp)
        generate_html(entries, out)
        print(f"Successfully generated {out}")
    except Exception as ex:
        print(f"Error: {ex}")
        sys.exit(1)
