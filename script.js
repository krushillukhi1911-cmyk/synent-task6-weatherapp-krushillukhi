document.addEventListener('DOMContentLoaded', () => {
    // Dark mode toggle
    const themeToggleBtn = document.getElementById('theme-toggle');
    if (themeToggleBtn) {
        const currentTheme = localStorage.getItem('theme') || 'light';
        document.documentElement.setAttribute('data-theme', currentTheme);
        updateThemeIcon(currentTheme);

        themeToggleBtn.addEventListener('click', () => {
            let theme = document.documentElement.getAttribute('data-theme');
            let newTheme = theme === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
        });
    }

    // Loading overlay for forms
    const forms = document.querySelectorAll('form');
    const loadingOverlay = document.getElementById('loading-overlay');
    
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            if (form.checkValidity()) {
                if (loadingOverlay) loadingOverlay.classList.add('active');
            }
        });
    });

    // Form validation
    const searchForm = document.getElementById('search-form');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            const input = this.querySelector('input[name="city"]');
            if (!input.value.trim()) {
                e.preventDefault();
                input.classList.add('is-invalid');
            } else {
                input.classList.remove('is-invalid');
            }
        });
    }
});

function updateThemeIcon(theme) {
    const icon = document.querySelector('#theme-toggle i');
    if(icon) {
        if (theme === 'dark') {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        } else {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
        }
    }
}
