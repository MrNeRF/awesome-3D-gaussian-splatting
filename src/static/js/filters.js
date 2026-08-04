function filterPapers() {
    // Show/hide non-paper elements regardless of filter state
    document.querySelectorAll('.papers-grid > *').forEach(el => {
        if (!el.classList.contains('paper-row')) {
            el.style.display = 'block'; // Always show headers, donation box, etc.
        }
    });

    const papers = window.paperIndex || buildPaperIndex();

    if (state.onlyShowSelected) {
        // When showing only selected papers, hide all non-selected papers
        papers.forEach(p => {
            p.row.classList.toggle('hidden', !state.selectedPapers.has(p.id));
        });
    } else {
        // Normal filtering
        const sTerm = searchInput.value.toLowerCase();
        const selYear = yearFilter.value;
        const inc = Array.from(state.includeTags);
        const exc = Array.from(state.excludeTags);

        papers.forEach(p => {
            const matchSearch = p.title.includes(sTerm) || p.authors.includes(sTerm);
            const matchYear = (selYear === 'all') || (p.year === selYear);
            const matchInc = (inc.length === 0) || inc.every(t => p.tags.includes(t));
            const matchExc = (exc.length === 0) || !exc.some(t => p.tags.includes(t));

            const visible = matchSearch && matchYear && matchInc && matchExc;
            p.row.classList.toggle('hidden', !visible);
        });
    }

    updatePaperNumbers();
    updateURL();
}

function clearSearch() {
    searchInput.value = '';
    filterPapers();
}

function initializeFilters() {
    // Tag filter clicks cycle through: not filtered -> include -> exclude -> not filtered
    tagFilters.forEach(tagFilter => {
        tagFilter.addEventListener('click', () => {
            const tag = tagFilter.getAttribute('data-tag');
            const current = tagStateOf(tagFilter);

            if (current === 'none') {
                state.includeTags.add(tag);
                setTagState(tagFilter, 'include');
            } else if (current === 'include') {
                state.includeTags.delete(tag);
                state.excludeTags.add(tag);
                setTagState(tagFilter, 'exclude');
            } else {
                state.excludeTags.delete(tag);
                setTagState(tagFilter, 'none');
            }
            filterPapers();
        });
    });

    // Search input
    searchInput.addEventListener('input', debounce(filterPapers, 150));

    // Year filter
    yearFilter.addEventListener('change', filterPapers);
}
