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

    // ============================================
    // HORIZONTAL SCROLL CAROUSEL WITH INDICATOR
    // ============================================

    const panelTrack = document.getElementById('panelTrack');
    const scrollIndicator = document.getElementById('scrollIndicator');
    const scrollThumb = document.getElementById('scrollThumb');

    if (panelTrack && scrollIndicator && scrollThumb) {
        let isDragging = false;
        let startX = 0;
        let scrollLeft = 0;

        // Update scroll indicator position based on carousel scroll
        function updateScrollIndicator() {
            const scrollPercentage = panelTrack.scrollLeft / (panelTrack.scrollWidth - panelTrack.clientWidth);
            const indicatorWidth = scrollIndicator.clientWidth;
            const thumbWidth = scrollThumb.clientWidth;
            const maxThumbPosition = indicatorWidth - thumbWidth;

            scrollThumb.style.left = `${scrollPercentage * maxThumbPosition}px`;
        }

        // Sync indicator with carousel scroll
        panelTrack.addEventListener('scroll', updateScrollIndicator);

        // Drag to scroll on carousel
        panelTrack.addEventListener('mousedown', (e) => {
            isDragging = true;
            startX = e.pageX - panelTrack.offsetLeft;
            scrollLeft = panelTrack.scrollLeft;
        });

        panelTrack.addEventListener('mouseleave', () => {
            isDragging = false;
        });

        panelTrack.addEventListener('mouseup', () => {
            isDragging = false;
        });

        panelTrack.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            e.preventDefault();
            const x = e.pageX - panelTrack.offsetLeft;
            const walk = (x - startX) * 2;
            panelTrack.scrollLeft = scrollLeft - walk;
        });

        // Drag scroll indicator thumb
        let isThumbDragging = false;
        let thumbStartX = 0;

        scrollThumb.addEventListener('mousedown', (e) => {
            isThumbDragging = true;
            thumbStartX = e.clientX - scrollThumb.offsetLeft;
            e.preventDefault();
        });

        document.addEventListener('mousemove', (e) => {
            if (!isThumbDragging) return;
            e.preventDefault();

            const indicatorRect = scrollIndicator.getBoundingClientRect();
            const x = e.clientX - indicatorRect.left - thumbStartX;
            const indicatorWidth = scrollIndicator.clientWidth;
            const thumbWidth = scrollThumb.clientWidth;
            const maxThumbPosition = indicatorWidth - thumbWidth;

            const clampedX = Math.max(0, Math.min(x, maxThumbPosition));
            const scrollPercentage = clampedX / maxThumbPosition;

            panelTrack.scrollLeft = scrollPercentage * (panelTrack.scrollWidth - panelTrack.clientWidth);
        });

        document.addEventListener('mouseup', () => {
            isThumbDragging = false;
        });

        // Click on indicator track to jump
        scrollIndicator.addEventListener('click', (e) => {
            if (e.target === scrollThumb) return;

            const indicatorRect = scrollIndicator.getBoundingClientRect();
            const clickX = e.clientX - indicatorRect.left;
            const indicatorWidth = scrollIndicator.clientWidth;
            const thumbWidth = scrollThumb.clientWidth;
            const maxThumbPosition = indicatorWidth - thumbWidth;

            const scrollPercentage = (clickX - thumbWidth / 2) / maxThumbPosition;
            panelTrack.scrollLeft = scrollPercentage * (panelTrack.scrollWidth - panelTrack.clientWidth);
        });

        // Initialize indicator position
        updateScrollIndicator();

        // Update on window resize
        window.addEventListener('resize', updateScrollIndicator);
    }
});
