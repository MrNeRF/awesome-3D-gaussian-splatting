// Navigation controls
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

function scrollToBottom() {
    window.scrollTo({
        top: document.documentElement.scrollHeight,
        behavior: 'smooth'
    });
}

// Update scroll progress
function updateScrollProgress() {
    const winScroll = document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = Math.round((winScroll / height) * 100);
    document.querySelector('.scroll-progress').textContent = `${scrolled}%`;
}

// Filter status functionality
function updateFilterStatus() {
    const visiblePapers = document.querySelectorAll('.paper-row.visible').length;
    const totalPapers = document.querySelectorAll('.paper-row').length;
    
    document.getElementById('visibleCount').textContent = visiblePapers;
    document.getElementById('totalCount').textContent = totalPapers;

    const searchTerm = document.getElementById('searchInput').value;
    const yearFilter = document.getElementById('yearFilter').value;
    const activeTags = Array.from(document.querySelectorAll('.tag-filter'))
        .filter(tag => tag.classList.contains('include') || tag.classList.contains('exclude'))
        .map(tag => ({
            text: tag.getAttribute('data-tag'),
            type: tag.classList.contains('include') ? 'include' : 'exclude'
        }));

    const filterStatusEl = document.querySelector('.filter-status');
    const activeFiltersEl = document.getElementById('activeFilters');
    activeFiltersEl.innerHTML = '';

    // Create filter tags
    if (searchTerm) {
        activeFiltersEl.appendChild(createFilterTag('search', `Search: ${searchTerm}`, () => {
            document.getElementById('searchInput').value = '';
            filterPapers();
        }));
    }

    if (yearFilter !== 'all') {
        activeFiltersEl.appendChild(createFilterTag('year', `Year: ${yearFilter}`, () => {
            document.getElementById('yearFilter').value = 'all';
            filterPapers();
        }));
    }

    activeTags.forEach(tag => {
        activeFiltersEl.appendChild(createFilterTag('tag', 
            `${tag.text} (${tag.type})`,
            () => document.querySelector(`.tag-filter[data-tag="${tag.text}"]`).click()
        ));
    });

    // Show/hide filter status bar
    filterStatusEl.classList.toggle('active', 
        searchTerm || yearFilter !== 'all' || activeTags.length > 0);
}

function createFilterTag(type, text, onRemove) {
    const tag = document.createElement('span');
    tag.className = `filter-tag ${type}`;
    tag.innerHTML = `
        ${text}
        <button onclick="event.stopPropagation();" aria-label="Remove filter">
            <i class="fas fa-times"></i>
        </button>
    `;
    tag.querySelector('button').addEventListener('click', onRemove);
    return tag;
}

function clearAllFilters() {
    document.getElementById('searchInput').value = '';
    document.getElementById('yearFilter').value = 'all';
    
    document.querySelectorAll('.tag-filter').forEach(tag => {
        if (tag.classList.contains('include') || tag.classList.contains('exclude')) {
            tag.click();
        }
    });
    
    filterPapers();
}

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    // Set initial paper counts
    updateFilterStatus();
    
    // Add scroll listener
    window.addEventListener('scroll', updateScrollProgress);
    
    // Override the existing filterPapers function to update filter status
    const originalFilterPapers = window.filterPapers;
    window.filterPapers = function() {
        originalFilterPapers();
        updateFilterStatus();
    };
});