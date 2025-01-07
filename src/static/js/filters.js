function filterPapers() {
    // Show/hide non-paper elements regardless of filter state
    document.querySelectorAll('.papers-grid > *').forEach(el => {
        if (!el.classList.contains('paper-row')) {
            el.style.display = 'block'; // Always show headers, donation box, etc.
        }
    });

    if (state.onlyShowSelected) {
        // When showing only selected papers, hide all non-selected papers
        paperCards.forEach(row => {
            const id = row.getAttribute('data-id');
            row.classList.toggle('visible', state.selectedPapers.has(id));
        });
    } else {
        // Normal filtering
        const sTerm = searchInput.value.toLowerCase();
        const selYear = yearFilter.value;
        
        paperCards.forEach(row => {
            const title = row.getAttribute('data-title').toLowerCase();
            const authors = row.getAttribute('data-authors').toLowerCase();
            const year = row.getAttribute('data-year');
            const tags = JSON.parse(row.getAttribute('data-tags'));

            const matchSearch = title.includes(sTerm) || authors.includes(sTerm);
            const matchYear = (selYear === 'all') || (year === selYear);
            const matchInc = (state.includeTags.size === 0) || [...state.includeTags].every(t => tags.includes(t));
            const matchExc = (state.excludeTags.size === 0) || ![...state.excludeTags].some(t => tags.includes(t));

            const visible = matchSearch && matchYear && matchInc && matchExc;
            row.classList.toggle('visible', visible);
        });
    }
    
    updatePaperNumbers();
    lazyLoadInstance.update();
    updateURL();
}

function clearSearch() {
    searchInput.value = '';
    filterPapers();
}

function initializeFilters() {
    // Tag filter clicks
    tagFilters.forEach(tagFilter => {
        tagFilter.addEventListener('click', () => {
            const tag = tagFilter.getAttribute('data-tag');
            if (!tagFilter.classList.contains('include') && !tagFilter.classList.contains('exclude')) {
                tagFilter.classList.add('include');
                state.includeTags.add(tag);
            } else if (tagFilter.classList.contains('include')) {
                tagFilter.classList.remove('include');
                tagFilter.classList.add('exclude');
                state.includeTags.delete(tag);
                state.excludeTags.add(tag);
            } else {
                tagFilter.classList.remove('exclude');
                state.excludeTags.delete(tag);
            }
            filterPapers();
        });
    });

    // Search input
    searchInput.addEventListener('input', debounce(filterPapers, 150));
    
    // Year filter
    yearFilter.addEventListener('change', filterPapers);
}