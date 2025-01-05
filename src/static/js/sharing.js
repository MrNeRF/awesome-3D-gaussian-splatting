function showShareModal() {
    if (state.selectedPapers.size === 0) {
        alert('Please select at least one paper to share.');
        return;
    }
    const shareUrl = new URL(window.location.href);
    shareUrl.searchParams.set('selected', Array.from(state.selectedPapers).join(','));
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
    
    // Search
    const searchTerm = params.get('search');
    if (searchTerm) {
        searchInput.value = searchTerm;
    }
    
    // Year
    const yr = params.get('year');
    if (yr) {
        yearFilter.value = yr;
    }

    // Tags
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

    // Selection
    const selPapers = params.get('selected');
    if (selPapers) {
        const arr = selPapers.split(',');
        if (arr.length > 0) {
            toggleSelectionMode();
            state.onlyShowSelected = true;
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
        }
    }
    
    filterPapers();
}