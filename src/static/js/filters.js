function filterPapers() {
    if (state.onlyShowSelected) {
        paperCards.forEach(row => {
            const id = row.getAttribute('data-id');
            row.classList.toggle('visible', state.selectedPapers.has(id));
        });
        updatePaperNumbers();
        lazyLoadInstance.update();
        updateURL();
        return;
    }

    // Normal filter
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
    updatePaperNumbers();
    lazyLoadInstance.update();
    updateURL();
}

function clearSearch() {
    searchInput.value = '';
    filterPapers();
    updateURL();
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
            updateURL();
        });
    });

    // Search input
    searchInput.addEventListener('input', debounce(filterPapers, 150));
    
    // Year filter
    yearFilter.addEventListener('change', filterPapers);
}