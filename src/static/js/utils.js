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
    document.querySelectorAll('.paper-row.visible').forEach(row => {
        const numElem = row.querySelector('.paper-number');
        numElem.textContent = num++;
    });
}