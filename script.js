document.addEventListener('DOMContentLoaded', () => {
    // Fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

    // Accordion functionality
    const accordions = document.querySelectorAll('.accordion-trigger');

    accordions.forEach(acc => {
        acc.addEventListener('click', function () {
            const item = this.parentElement;
            const isActive = item.classList.contains('active');

            // Close all others (optional - can serve as exclusive or inclusive)
            // document.querySelectorAll('.accordion-item').forEach(i => i.classList.remove('active'));

            if (!isActive) {
                item.classList.add('active');
            } else {
                item.classList.remove('active');
            }
        });
    });
    // Custom Cursor Logic
    const cursor = document.getElementById('cursor');
    const cursorTag = document.querySelector('.cursor-tag');

    if (cursor && window.matchMedia("(min-width: 769px)").matches) {
        document.addEventListener('mousemove', (e) => {
            requestAnimationFrame(() => {
                const x = e.clientX;
                const y = e.clientY;
                cursor.style.transform = `translate3d(${x}px, ${y}px, 0)`;
            });
        });

        // Interaction states
        document.addEventListener('mousedown', () => {
            if (cursorTag) cursorTag.style.transform = 'scale(0.9)';
        });

        document.addEventListener('mouseup', () => {
            if (cursorTag) cursorTag.style.transform = 'scale(1)';
        });
    }

    // Theme Switcher Logic
    const themeBtns = document.querySelectorAll('.theme-btn');
    const html = document.documentElement;

    // Load saved theme
    const savedTheme = localStorage.getItem('theme') || 'light';
    html.setAttribute('data-theme', savedTheme);
    setActiveBtn(savedTheme);

    themeBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const theme = btn.getAttribute('data-theme');
            html.setAttribute('data-theme', theme);
            localStorage.setItem('theme', theme);
            setActiveBtn(theme);
        });
    });

    function setActiveBtn(theme) {
        themeBtns.forEach(b => b.classList.remove('active'));
        const activeBtn = document.querySelector(`.theme-btn[data-theme="${theme}"]`);
        if (activeBtn) activeBtn.classList.add('active');
    }
});
