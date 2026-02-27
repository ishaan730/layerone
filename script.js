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
                entry.target.classList.add('active'); // Added for .reveal-up
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-in, .reveal-up').forEach(el => observer.observe(el));

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
    // PROJECT MODAL LOGIC
    // ============================================
    const modal = document.getElementById('projectModal');
    const modalBody = document.getElementById('modalBody');
    const modalClose = document.querySelector('.modal-close');
    const modalOverlay = document.querySelector('.modal-overlay');
    const bentoItems = document.querySelectorAll('.bento-item');

    const projectData = {
        'cars24-pattern': {
            title: 'Cars24 Pattern Library',
            subtitle: 'Design System Infrastructure for rapid scaling',
            description: 'We built a comprehensive pattern library for Cars24 that enabled product teams to launch new features 3x faster. The system focuses on production-ready components and automated documentation.',
            image: 'assets/images/work/cars24_pattern_library.png'
        },
        'cars24-tools': {
            title: 'Internal Tool Design System',
            subtitle: 'Powering 20+ internal applications',
            description: 'A specialized UI kit designed for administrative and internal operational tools. Focus on high data density, accessibility, and engineering efficiency.',
            image: 'assets/images/work/cars24_internal_tools.png'
        },
        'lego-system': {
            title: 'Lego Design System',
            subtitle: 'Global Architecture for 100+ designers',
            description: 'Strategic consulting and architecture for a global-scale design system. We defined the token logic and contribution workflows that made the system sustainable across multi-disciplinary teams.',
            image: 'assets/images/work/lego_design_system.png'
        },
        'riyadh-air': {
            title: 'Riyadh Air Base Elements',
            subtitle: 'Defining a new visual language',
            description: 'Foundational UI architecture for a next-generation airline. We built the base elements and decisions that power the entire digital ecosystem from booking to check-in.',
            image: 'assets/images/work/riyadh_air_base_elements.png'
        },
        'design-audit': {
            title: 'Design System Audit',
            subtitle: 'Diagnostics for high-growth teams',
            description: 'Detailed analysis of existing UI debt and inconsistency. We provided a roadmap for recovery and scaling that saved the team' + "'" + 's engineering capacity.',
            image: 'assets/images/work/cars24_pattern_library.png'
        },
        'token-architecture': {
            title: 'Token Logic',
            subtitle: 'Multi-brand foundations',
            description: 'Dynamic design token structures that support multi-brand and multi-platform deployments from a single source of truth.',
            image: 'assets/images/work/lego_design_system.png'
        }
    };

    function openModal(projectId) {
        const data = projectData[projectId];
        if (!data) return;

        modalBody.innerHTML = `
            <div class="case-study-hero">
                <span class="mono-label">CASE STUDY</span>
                <h2>${data.title}</h2>
                <p>${data.subtitle}</p>
            </div>
            <div class="case-study-grid">
                <div class="case-study-text">
                    <p>${data.description}</p>
                    <div class="spec-list" style="margin-top: 32px;">
                        <div class="spec-item"><strong>Objective</strong><p>Establish production-ready infrastructure.</p></div>
                        <div class="spec-item" style="margin-top: 16px;"><strong>Outcome</strong><p>Reduction in design debt by 40%.</p></div>
                    </div>
                </div>
                <div class="case-study-visuals">
                    <img src="${data.image}" class="case-study-image" alt="${data.title}">
                </div>
            </div>
        `;

        modal.classList.add('active');
        document.body.style.overflow = 'hidden'; // Prevent background scroll
    }

    function closeModal() {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    }

    bentoItems.forEach(item => {
        item.addEventListener('click', () => {
            const projectId = item.getAttribute('data-project');
            openModal(projectId);
        });
    });

    if (modalClose) modalClose.addEventListener('click', closeModal);
    if (modalOverlay) modalOverlay.addEventListener('click', closeModal);

    // Close on ESC
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeModal();
        }
    });
});
