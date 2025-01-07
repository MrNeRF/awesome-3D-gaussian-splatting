document.addEventListener('DOMContentLoaded', function() {
    // Initialize variables
    window.paperCards = document.querySelectorAll('.paper-row');
    window.searchInput = document.getElementById('searchInput');
    window.yearFilter = document.getElementById('yearFilter');
    window.tagFilters = document.querySelectorAll('.tag-filter');
    
    // Add toggleAbstract to window object so it's globally accessible
    window.toggleAbstract = function(button) {
        const abstract = button.nextElementSibling;
        const isShowing = abstract.classList.toggle('show');
        button.innerHTML = isShowing ? '📖 Hide Abstract' : '📖 Show Abstract';
    };

    // Initialize LazyLoad
    window.lazyLoadInstance = new LazyLoad({
        elements_selector: ".lazy",
        callback_error: (img) => {
            if (img.dataset.fallback) {
                img.src = img.dataset.fallback;
            }
        },
        callback_loaded: (img) => {
            img.classList.add('loaded');
        }
    });

    // Initialize filters
    initializeFilters();

    // Initialize paper card events
    document.querySelectorAll('.paper-card').forEach(card => {
        card.addEventListener('click', (ev) => {
            if (!state.isSelectionMode) return;
            // if click on link or abstract btn, ignore
            if (
                ev.target.classList.contains('paper-link') ||
                ev.target.closest('.paper-link') ||
                ev.target.classList.contains('abstract-toggle')
            ) {
                return;
            }
            const checkbox = card.querySelector('.selection-checkbox');
            if (checkbox && ev.target !== checkbox) {
                checkbox.checked = !checkbox.checked;
                const pid = card.parentElement.getAttribute('data-id');
                togglePaperSelection(pid, checkbox);
            }
        });
    });

    // Apply URL parameters
    applyURLParams();

    // Show initial papers
    paperCards.forEach(c => c.classList.add('visible'));
    updatePaperNumbers();

    // Expose global functions for HTML onclick handlers
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
});
