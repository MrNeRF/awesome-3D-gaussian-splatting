function showShareModal() {
    if (state.selectedPapers.size === 0) {
        alert('Please select at least one paper to share.');
        return;
    }
    const shareUrl = new URL(window.location.href);
    shareUrl.searchParams.set('selected', Array.from(state.selectedPapers).join(','));
    if (state.onlyShowSelected) {
        shareUrl.searchParams.set('show_selected', 'true');
    } else {
        shareUrl.searchParams.delete('show_selected');
    }
    document.getElementById('shareUrl').value = shareUrl.toString();
    document.getElementById('shareModal').classList.add('show');
}

function hideShareModal() {
    document.getElementById('shareModal').classList.remove('show');
}

async function copyShareLink() {
    const shareUrl = document.getElementById('shareUrl');
    try {
        await navigator.clipboard.writeText(shareUrl.value);
        const copyButton = document.querySelector('.share-url-container .control-button');
        const origText = copyButton.innerHTML;
        copyButton.innerHTML = '<i class="fas fa-check"></i> Copied!';
        setTimeout(() => {
            copyButton.innerHTML = origText;
        }, 2000);
    } catch(e) {
        alert('Failed to copy link. Please copy manually.');
    }
}

function copyBitcoinAddress() {
    const address = document.querySelector('.bitcoin-address').textContent;
    navigator.clipboard.writeText(address).then(() => {
        const button = document.querySelector('.copy-button');
        const originalText = button.innerHTML;
        button.innerHTML = '<i class="fas fa-check"></i> Copied!';
        setTimeout(() => {
            button.innerHTML = originalText;
        }, 2000);
    });
}

function applyURLParams() {
    const params = new URLSearchParams(window.location.search);
    
    // First, check if we have selected papers
    const selPapers = params.get('selected');
    if (selPapers) {
        const arr = selPapers.split(',');
        if (arr.length > 0) {
            // Enter selection mode
            if (!state.isSelectionMode) {
                toggleSelectionMode();
            }
            
            // Select the papers first
            arr.forEach(id => {
                const row = document.querySelector(`.paper-row[data-id="${id}"]`);
                if (row) {
                    const cb = row.querySelector('.selection-checkbox');
                    if (cb) {
                        cb.checked = true;
                        togglePaperSelection(id, cb);
                    }
                }
            });
            
            // Then check if we should show only selected papers
            const showSelected = params.get('show_selected');
            if (showSelected === 'true') {
                state.onlyShowSelected = true;
                const button = document.querySelector('.preview-header-right .control-button.show-selected');
                if (button) {
                    button.innerHTML = '<i class="fas fa-list"></i> Show All Papers';
                }
                filterPapers(); // Apply the filter to show only selected papers
            }
        }
    }
    
    // Handle other filters
    const searchTerm = params.get('search');
    if (searchTerm) {
        searchInput.value = searchTerm;
    }
    
    const yr = params.get('year');
    if (yr) {
        yearFilter.value = yr;
    }

    const inc = params.get('include');
    if (inc) {
        state.includeTags = new Set(inc.split(','));
        state.includeTags.forEach(t => {
            const tf = document.querySelector(`.tag-filter[data-tag="${t}"]`);
            if (tf) tf.classList.add('include');
        });
    }
    
    const exc = params.get('exclude');
    if (exc) {
        state.excludeTags = new Set(exc.split(','));
        state.excludeTags.forEach(t => {
            const tf = document.querySelector(`.tag-filter[data-tag="${t}"]`);
            if (tf) tf.classList.add('exclude');
        });
    }
    
    // Final filter application
    filterPapers();
}