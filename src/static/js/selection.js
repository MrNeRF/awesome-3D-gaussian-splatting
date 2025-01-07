function toggleSelectedOnly() {
    state.onlyShowSelected = !state.onlyShowSelected;
    const button = document.querySelector('.preview-header-right .control-button.show-selected');
    
    if (button) {
        button.innerHTML = state.onlyShowSelected ? 
            '<i class="fas fa-list"></i> Show All Papers' :
            '<i class="fas fa-filter"></i> Show Selected Only';
    }
    
    // Update the URL first
    const url = new URL(window.location.href);
    if (state.onlyShowSelected) {
        url.searchParams.set('show_selected', 'true');
    } else {
        url.searchParams.delete('show_selected');
    }
    window.history.replaceState({}, '', url.toString());
    
    // Then update the display
    filterPapers();
}

function toggleSelectionMode() {
    state.isSelectionMode = !state.isSelectionMode;
    document.body.classList.toggle('selection-mode', state.isSelectionMode);

    // Update toggle button icon and tooltip
    const toggleButton = document.querySelector('.selection-mode-toggle');
    if (toggleButton) {
        toggleButton.innerHTML = state.isSelectionMode ? 
            `<i class="fas fa-times"></i><span class="tooltip">Exit Selection Mode</span>` :
            `<i class="fas fa-list-check"></i><span class="tooltip">Enter Selection Mode</span>`;
    }

    // Handle visibility and selection display
    if (!state.isSelectionMode) {
        if (state.onlyShowSelected) {
            state.onlyShowSelected = false;
            const button = document.querySelector('.preview-header-right .control-button.show-selected');
            if (button) {
                button.innerHTML = '<i class="fas fa-filter"></i> Show Selected Only';
            }
            const url = new URL(window.location.href);
            url.searchParams.delete('show_selected');
            window.history.replaceState({}, '', url.toString());
        }
        filterPapers();
    }

    updateSelectionCount();
}

function clearSelection() {
    state.selectedPapers.clear();
    state.onlyShowSelected = false;
    document.querySelectorAll('.paper-card').forEach(card => {
        card.classList.remove('selected');
        const checkbox = card.querySelector('.selection-checkbox');
        if (checkbox) checkbox.checked = false;
    });
    document.getElementById('selectionPreview').innerHTML = '';
    
    // Update button state
    const button = document.querySelector('.preview-header-right .control-button.show-selected');
    if (button) {
        button.innerHTML = '<i class="fas fa-filter"></i> Show Selected Only';
    }
    
    // Update URL and display
    const url = new URL(window.location.href);
    url.searchParams.delete('show_selected');
    url.searchParams.delete('selected');
    window.history.replaceState({}, '', url.toString());
    
    updateSelectionCount();
    filterPapers();
}

function togglePaperSelection(paperId, checkbox) {
    if (!state.isSelectionMode) return;
    
    const paperCard = checkbox.closest('.paper-card');
    const paperRow = paperCard.closest('.paper-row');

    if (checkbox.checked) {
        // Add to selection
        state.selectedPapers.add(paperId);
        paperCard.classList.add('selected');

        // Create preview item
        const title = paperRow.getAttribute('data-title');
        const authors = paperRow.getAttribute('data-authors');
        const year = paperRow.getAttribute('data-year');

        const previewItem = document.createElement('div');
        previewItem.className = 'preview-item';
        previewItem.setAttribute('data-paper-id', paperId);
        previewItem.innerHTML = `
            <div class="preview-content" onclick="scrollToPaper('${paperId}')">
                <div class="preview-title">${title} (${year})</div>
                <div class="preview-authors">${authors}</div>
            </div>
            <button class="preview-remove" onclick="event.stopPropagation(); removeFromSelection('${paperId}')">
                <i class="fas fa-times"></i>
            </button>
        `;
        document.getElementById('selectionPreview').appendChild(previewItem);
    } else {
        removeFromSelection(paperId);
    }
    updateSelectionCount();
    if (state.onlyShowSelected) {
        filterPapers();
    }
    updateURL();
}

function removeFromSelection(paperId) {
    const checkbox = document.querySelector(`.paper-row[data-id="${paperId}"] .selection-checkbox`);
    if (checkbox) {
        checkbox.checked = false;
        state.selectedPapers.delete(paperId);

        const paperCard = checkbox.closest('.paper-card');
        if (paperCard) {
            paperCard.classList.remove('selected');
        }

        const previewItem = document.querySelector(`.preview-item[data-paper-id="${paperId}"]`);
        if (previewItem) {
            previewItem.remove();
        }

        updateSelectionCount();
        if (state.onlyShowSelected) {
            filterPapers();
        }
        updateURL();
    }
}

function updateSelectionCount() {
    const counter = document.querySelector('.selection-counter');
    counter.textContent = `${state.selectedPapers.size} paper${state.selectedPapers.size === 1 ? '' : 's'} selected`;
}

function handleCheckboxClick(ev, paperId, checkbox) {
    ev.stopPropagation();
    togglePaperSelection(paperId, checkbox);
}

function scrollToPaper(paperId) {
    const paperRow = document.querySelector(`.paper-row[data-id="${paperId}"]`);
    if (paperRow) {
        paperRow.scrollIntoView({ behavior: 'smooth', block: 'center' });
        
        const paperCard = paperRow.querySelector('.paper-card');
        if (paperCard) {
            paperCard.style.transition = 'background-color 0.3s ease';
            paperCard.style.backgroundColor = '#f0f9ff';
            setTimeout(() => {
                paperCard.style.backgroundColor = '';
            }, 1500);
        }
    }
}