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
            contentHtml: `
            <div class="case-study-hero">
                <span class="mono-label">CASE STUDY</span>
                <h2>CARS24</h2>
                <p>Product Design Language &amp; Pattern Library</p>
            </div>
            <div class="case-study-grid custom-layout" style="display: block;">
                <div class="case-study-text full-width" style="max-width: 800px; margin: 0 auto;">
                    <p style="margin-bottom: 32px; line-height: 1.7; font-style: italic; color: var(--text-secondary);">Accelerating large-scale product redesign through a scalable pattern library built on top of the design system.</p>

                    <h3 style="margin-top: 0; margin-bottom: 16px;">Key Facts</h3>
                    <div class="facts-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 0; margin-bottom: 40px; border: 1px solid rgba(13, 153, 255, 0.12); border-radius: 8px; overflow: hidden;">
                        <div style="padding: 20px 24px; border-right: 1px solid rgba(13, 153, 255, 0.12); border-bottom: 1px solid rgba(13, 153, 255, 0.12);"><strong style="color: #0D99FF; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.06em;">Industry</strong><br><span style="font-weight: 500; font-size: 0.95rem; margin-top: 6px; display: inline-block;">Automotive Marketplace</span></div>
                        <div style="padding: 20px 24px; border-bottom: 1px solid rgba(13, 153, 255, 0.12);"><strong style="color: #0D99FF; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.06em;">Platforms</strong><br><span style="font-weight: 500; font-size: 0.95rem; margin-top: 6px; display: inline-block;">Consumer Mobile App, Consumer Web</span></div>
                        <div style="padding: 20px 24px; border-right: 1px solid rgba(13, 153, 255, 0.12);"><strong style="color: #0D99FF; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.06em;">Scope</strong><br><span style="font-weight: 500; font-size: 0.95rem; margin-top: 6px; display: inline-block;">Pattern Library, Product Design Language (PDL), Landing Page Framework, Design Guidelines</span></div>
                        <div style="padding: 20px 24px;"><strong style="color: #0D99FF; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.06em;">Impact Area</strong><br><span style="font-weight: 500; font-size: 0.95rem; margin-top: 6px; display: inline-block;">Consumer Product Redesign Initiative</span></div>
                    </div>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">Context</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">Following the rollout of the CARS24 consumer design system, the company initiated a major redesign of its consumer product ecosystem, particularly across its core mobile application and digital platform.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">With multiple teams working simultaneously on the redesign, there was a need for a faster way to design, experiment, and ship new experiences while maintaining visual consistency.</p>
                    <p style="margin-bottom: 40px; line-height: 1.7;">To support this large-scale transformation, we partnered with the team to build a pattern library and product design language on top of the existing design system.</p>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">Challenge</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">While the design system provided reusable UI components, product teams still needed a faster way to assemble complex product experiences such as landing pages, promotional flows, and content-heavy interfaces.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">Designers were spending significant time repeatedly designing similar layouts and experimenting with different structures for product pages.</p>
                    <p style="margin-bottom: 40px; line-height: 1.7;">The challenge was to create a scalable design language and pattern framework that would allow teams to rapidly build and experiment with product experiences while maintaining consistency across the platform.</p>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">Approach</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">We began by analyzing the most common layout patterns used across the platform, particularly within landing pages and marketing-driven product flows.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">Alongside internal product research, we benchmarked leading consumer applications to understand how high-performing platforms structure content, cards, layouts, and visual hierarchy.</p>
                    <p style="margin-bottom: 40px; line-height: 1.7;">Working closely with product, design, and engineering teams, we defined a Product Design Language (PDL) that established the structural rules for layouts, grid systems, cards, content hierarchy, and visual patterns. This framework ensured that designers could quickly compose new experiences using a consistent design language.</p>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">System Implementation</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">Building on top of the existing component system, we designed a structured pattern library that included reusable layouts, landing page structures, and composable UI patterns.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">The library defined how components should be combined to create complete product experiences, covering areas such as card layouts, content sections, grids, promotional modules, and structured page compositions.</p>
                    <p style="margin-bottom: 40px; line-height: 1.7;">We also created detailed design guidelines that documented best practices for designers, developers, and product teams to ensure consistent implementation.</p>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">Governance &amp; Adoption</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">To ensure adoption across the organization, the pattern library was introduced as a shared framework for building product experiences during the redesign initiative.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">Design teams were able to use the library to quickly assemble layouts and prototype new product ideas, while engineering teams benefited from clearer UI structures and repeatable implementation patterns.</p>
                    <p style="margin-bottom: 40px; line-height: 1.7;">The framework also helped align product, design, and engineering teams around a common language for building product experiences.</p>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">Impact</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">The pattern library significantly accelerated the redesign of CARS24's consumer platform while maintaining visual consistency across the product ecosystem.</p>
                    <ul style="list-style-type: none; padding: 0; display: flex; flex-direction: column; gap: 12px; margin-bottom: 24px;">
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Enabled redesign of 10+ product landing pages across services</li>
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Accelerated design iteration and experimentation across teams</li>
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Reduced design time for new page layouts and product experiences</li>
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Improved collaboration between product, design, and engineering teams</li>
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Established a shared product design language for building experiences at scale</li>
                    </ul>
                </div>
            </div>
            `
        },
        'cars24-tools': {
            contentHtml: `
            <div class="case-study-hero">
                <span class="mono-label">CASE STUDY</span>
                <h2>CARS24</h2>
                <p>Internal Tools Design System</p>
            </div>
            <div class="case-study-grid custom-layout" style="display: block;">
                <div class="case-study-text full-width" style="max-width: 800px; margin: 0 auto;">
                    <h3 style="margin-top: 0; margin-bottom: 16px;">Key Facts</h3>
                    <div class="facts-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; margin-bottom: 40px; padding: 24px; background: rgba(13, 153, 255, 0.05); border-radius: 8px; border: 1px solid rgba(13, 153, 255, 0.1);">
                        <div><strong style="color: #0D99FF; font-size: 0.8rem; text-transform: uppercase;">Industry</strong><br><span style="font-weight: 500; font-size: 0.95rem;">Automotive Marketplace</span></div>
                        <div><strong style="color: #0D99FF; font-size: 0.8rem; text-transform: uppercase;">Team</strong><br><span style="font-weight: 500; font-size: 0.95rem;">3 Designers, 2 Design Engineers</span></div>
                        <div><strong style="color: #0D99FF; font-size: 0.8rem; text-transform: uppercase;">Platforms</strong><br><span style="font-weight: 500; font-size: 0.95rem;">Internal Web Applications, Operational Tools</span></div>
                        <div><strong style="color: #0D99FF; font-size: 0.8rem; text-transform: uppercase;">Adoption</strong><br><span style="font-weight: 500; font-size: 0.95rem;">10–15 Designers, 35+ Engineers</span></div>
                        <div><strong style="color: #0D99FF; font-size: 0.8rem; text-transform: uppercase;">Timeline</strong><br><span style="font-weight: 500; font-size: 0.95rem;">6 Months Rollout</span></div>
                    </div>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">Context</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">CARS24 operates a large number of internal products that support its operations, including tools for engineering, sales operations, logistics, and marketing workflows.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">Over time, these internal tools had evolved independently, resulting in fragmented user experiences, duplicated UI patterns, and inconsistent interaction models across products.</p>
                    <p style="margin-bottom: 40px; line-height: 1.7;">As the organization began expanding into B2B products and scaling internal operations, there was a growing need for a unified design system to bring consistency and efficiency to internal product development.</p>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">Challenge</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">The internal tooling ecosystem consisted of multiple complex applications built by different teams over time.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">Designers and engineers were solving similar problems repeatedly without shared components or standardized design patterns. This created inconsistencies in user experience and increased development effort.</p>
                    <p style="margin-bottom: 40px; line-height: 1.7;">The challenge was to create a design system tailored specifically for internal tools — one capable of handling complex workflows, dense data interfaces, and operational dashboards while supporting scalability across multiple teams.</p>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">Approach</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">We began with a comprehensive discovery phase to understand the structure and complexity of CARS24's internal tooling ecosystem.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">This involved reviewing existing tools, understanding engineering workflows, and identifying the most common UI patterns across internal applications. We also worked closely with designers and engineers to understand their day-to-day challenges when building and maintaining internal tools.</p>
                    <p style="margin-bottom: 40px; line-height: 1.7;">These insights helped define the architecture and scope of the internal design system.</p>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">System Implementation</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">Based on our research, we designed a robust component library tailored for complex internal applications.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">The system included 30+ production-ready components, many of which supported advanced and data-heavy interfaces such as dashboards, tables, navigation systems, and structured workflows.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">We also established a scalable design token architecture to ensure visual consistency and support long-term scalability as new tools and products were introduced.</p>
                    <p style="margin-bottom: 40px; line-height: 1.7;">Given the complexity of the components, the system was developed in close collaboration with frontend engineers to ensure smooth implementation across internal platforms.</p>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">Governance &amp; Adoption</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">To drive adoption across teams, we introduced a structured governance and rollout strategy.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">We worked closely with developers and product teams to support migration efforts and provided dedicated guidance on how the system should be implemented across projects.</p>
                    <p style="margin-bottom: 40px; line-height: 1.7;">Internal workshops, training sessions, and documentation helped designers and engineers understand how to use the system effectively and maintain consistency across products.</p>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">Impact</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">The internal tools design system became the foundation for building and scaling operational products at CARS24.</p>
                    <ul style="list-style-type: none; padding: 0; display: flex; flex-direction: column; gap: 12px; margin-bottom: 24px;">
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Adopted by 10–15 designers across internal product teams</li>
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Used by 35+ frontend engineers building internal tools</li>
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> 30+ complex components designed for data-heavy interfaces</li>
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> 10–15 internal tools migrated to the new system</li>
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Improved consistency across operational products</li>
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Reduced development effort for new internal tools</li>
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Increased productivity for both design and engineering teams</li>
                    </ul>
                </div>
            </div>
            `
        },

        'cars24-consumer': {
            contentHtml: `
            <div class="case-study-hero">
                <span class="mono-label">CASE STUDY</span>
                <h2>CARS24</h2>
                <p>Consumer Product Design System</p>
            </div>
            <div class="case-study-grid custom-layout" style="display: block;">
                <div class="case-study-text full-width" style="max-width: 800px; margin: 0 auto;">
                    <h3 style="margin-top: 0; margin-bottom: 16px;">Key Facts</h3>
                    <div class="facts-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; margin-bottom: 40px; padding: 24px; background: rgba(13, 153, 255, 0.05); border-radius: 8px; border: 1px solid rgba(13, 153, 255, 0.1);">
                        <div><strong style="color: #0D99FF; font-size: 0.8rem; text-transform: uppercase;">Industry</strong><br><span style="font-weight: 500; font-size: 0.95rem;">Automotive Marketplace</span></div>
                        <div><strong style="color: #0D99FF; font-size: 0.8rem; text-transform: uppercase;">Team</strong><br><span style="font-weight: 500; font-size: 0.95rem;">3 Designers, 2 Design Engineers</span></div>
                        <div><strong style="color: #0D99FF; font-size: 0.8rem; text-transform: uppercase;">Platforms</strong><br><span style="font-weight: 500; font-size: 0.95rem;">Mobile, Web</span></div>
                        <div><strong style="color: #0D99FF; font-size: 0.8rem; text-transform: uppercase;">Adoption</strong><br><span style="font-weight: 500; font-size: 0.95rem;">60+ Designers, 80+ Engineers</span></div>
                        <div><strong style="color: #0D99FF; font-size: 0.8rem; text-transform: uppercase;">Timeline</strong><br><span style="font-weight: 500; font-size: 0.95rem;">2 Months Rollout</span></div>
                    </div>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">Context</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">As part of a broader brand transformation, CARS24 needed a unified design foundation to support its growing consumer product ecosystem across mobile and web.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">With multiple product teams building features simultaneously, inconsistencies in UI patterns, design decisions, and implementation approaches were beginning to slow development.</p>
                    <p style="margin-bottom: 40px; line-height: 1.7;">The goal was to establish a scalable design system that could align design and engineering teams while enabling faster and more consistent product development.</p>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">Challenge</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">Over time, different teams had created their own UI patterns and components. This resulted in fragmented interfaces and duplicated effort across design and engineering.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">Without a centralized system, maintaining consistency across products became increasingly difficult as the organization scaled.</p>
                    <p style="margin-bottom: 40px; line-height: 1.7;">The challenge was to create a design system that not only standardized UI components but also introduced a structure that teams across the company could adopt and evolve.</p>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">Approach</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">We started with a comprehensive discovery phase to understand the product ecosystem, team structures, and existing workflows.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">Through discussions with design leads, product managers, and engineers, we mapped the current UI landscape and identified the most critical inconsistencies.</p>
                    <p style="margin-bottom: 40px; line-height: 1.7;">Rather than rebuilding everything at once, we designed a flexible system architecture that could gradually replace existing patterns while allowing teams to continue shipping product improvements.</p>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">System Implementation</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">We established the foundational layer of the design system, including typography, color tokens, iconography, and layout principles.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">From there, we prioritized component development based on real product usage. High-impact components used across multiple product surfaces were developed first to enable early adoption.</p>
                    <p style="margin-bottom: 40px; line-height: 1.7;">The system was built in close collaboration with frontend engineers to ensure seamless translation from design to production.</p>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">Governance & Adoption</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">To ensure long-term sustainability, we helped establish the governance and operating model for the design system.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">This included defining ownership, contribution workflows, versioning practices, and processes for evolving the system over time.</p>
                    <p style="margin-bottom: 40px; line-height: 1.7;">We also ran internal workshops and onboarding sessions to help designers and engineers integrate the system into their workflows.</p>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">Impact</h3>
                    <ul style="list-style-type: none; padding: 0; display: flex; flex-direction: column; gap: 12px; margin-bottom: 24px;">
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Adopted by 60+ designers across product teams</li>
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Used by 80+ frontend engineers in production</li>
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Rolled out across multiple mobile and web consumer products</li>
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Migrated the core mobile application to the new system</li>
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Reduced rollout timeline from ~5 months to ~2 months</li>
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Significantly improved UI consistency and development efficiency</li>
                    </ul>
                </div>
            </div>
            `
        },

        'riyadh-air': {
            contentHtml: `
            <div class="case-study-hero">
                <span class="mono-label">CASE STUDY</span>
                <h2>Riyadh Air</h2>
                <p>Foundational Design System for a New Aviation Platform</p>
            </div>
            <div class="case-study-grid custom-layout" style="display:block;">
                <div class="case-study-text full-width" style="max-width:800px;margin:0 auto;">
                    <p style="margin-bottom:32px;line-height:1.7;font-style:italic;color:var(--text-secondary);">Building the design foundation for a next-generation airline's digital products across web and mobile.</p>
                    <h3 style="margin-top:0;margin-bottom:16px;">Key Facts</h3>
                    <div class="facts-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:16px;margin-bottom:40px;padding:24px;background:rgba(13,153,255,0.05);border-radius:8px;border:1px solid rgba(13,153,255,0.1);">
                        <div><strong style="color:#0D99FF;font-size:0.8rem;text-transform:uppercase;">Industry</strong><br><span style="font-weight:500;font-size:0.95rem;">Aviation</span></div>
                        <div><strong style="color:#0D99FF;font-size:0.8rem;text-transform:uppercase;">Platforms</strong><br><span style="font-weight:500;font-size:0.95rem;">Consumer Web, Mobile Applications</span></div>
                        <div><strong style="color:#0D99FF;font-size:0.8rem;text-transform:uppercase;">Components</strong><br><span style="font-weight:500;font-size:0.95rem;">20+ Core Components</span></div>
                        <div><strong style="color:#0D99FF;font-size:0.8rem;text-transform:uppercase;">Timeline</strong><br><span style="font-weight:500;font-size:0.95rem;">~4 Months</span></div>
                        <div><strong style="color:#0D99FF;font-size:0.8rem;text-transform:uppercase;">Focus</strong><br><span style="font-weight:500;font-size:0.95rem;">Foundational Design System, Component Library, Adoption</span></div>
                    </div>

                    <h3 style="margin-top:32px;margin-bottom:16px;">Context</h3>
                    <p style="margin-bottom:16px;line-height:1.7;">Riyadh Air is a new airline entering the global aviation market from the Middle East. As the company was building its digital products from the ground up, there was a unique opportunity to establish a strong design foundation from day one.</p>
                    <p style="margin-bottom:40px;line-height:1.7;">The goal was to create a scalable design system that could support the development of their core consumer experiences across web and mobile while enabling product teams to move quickly as the platform evolved.</p>

                    <h3 style="margin-top:32px;margin-bottom:16px;">Challenge</h3>
                    <p style="margin-bottom:16px;line-height:1.7;">Aviation platforms are inherently complex, with intricate booking flows, large data structures, and multiple operational scenarios that must work seamlessly together.</p>
                    <p style="margin-bottom:16px;line-height:1.7;">Since Riyadh Air's digital ecosystem was still being developed, the challenge was to architect a design system that could support upcoming product features while aligning with the brand identity and engineering capabilities already in place.</p>
                    <p style="margin-bottom:40px;line-height:1.7;">The system needed to be flexible enough to scale as new products and features were introduced.</p>

                    <h3 style="margin-top:32px;margin-bottom:16px;">Approach</h3>
                    <p style="margin-bottom:16px;line-height:1.7;">We began by working closely with Riyadh Air's product, design, and engineering stakeholders to understand the roadmap and upcoming product capabilities.</p>
                    <p style="margin-bottom:16px;line-height:1.7;">Alongside this, we conducted a detailed benchmark of leading aviation platforms to understand how complex airline interfaces are structured, particularly around booking flows, data presentation, and interaction patterns.</p>
                    <p style="margin-bottom:40px;line-height:1.7;">These insights helped us define the structure and scope of the design system and identify the components required to support the early product roadmap.</p>

                    <h3 style="margin-top:32px;margin-bottom:16px;">System Implementation</h3>
                    <p style="margin-bottom:16px;line-height:1.7;">We first established the foundational layer of the design system, aligning with the visual language already defined by the brand team, including typography, color tokens, and iconography.</p>
                    <p style="margin-bottom:16px;line-height:1.7;">With the foundation in place, we worked closely with the product design team to identify the most critical UI components required for the first phase of product development.</p>
                    <p style="margin-bottom:16px;line-height:1.7;">Over the course of four months, we designed and delivered 20+ core components to support the initial development of the platform's web and mobile experiences.</p>
                    <p style="margin-bottom:40px;line-height:1.7;">Components were released incrementally to allow teams to start using the system early while the library continued to evolve.</p>

                    <h3 style="margin-top:32px;margin-bottom:16px;">Governance &amp; Adoption</h3>
                    <p style="margin-bottom:16px;line-height:1.7;">Since the internal team was new to design systems, we worked closely with designers and engineers to help them understand how to adopt and scale the system effectively.</p>
                    <p style="margin-bottom:16px;line-height:1.7;">We supported the team through workshops, collaborative working sessions, and ongoing guidance on how to design new features using the system.</p>
                    <p style="margin-bottom:40px;line-height:1.7;">Instead of a single large rollout, the system was introduced in smaller iterations, allowing teams to gradually adapt their workflows and integrate the components into product development.</p>

                    <h3 style="margin-top:32px;margin-bottom:16px;">Impact</h3>
                    <ul style="list-style-type:none;padding:0;display:flex;flex-direction:column;gap:12px;margin-bottom:24px;">
                        <li style="display:flex;gap:12px;"><span style="color:#0D99FF;">&bull;</span> 20+ core components delivered for early product development</li>
                        <li style="display:flex;gap:12px;"><span style="color:#0D99FF;">&bull;</span> Supported web and mobile platform foundations</li>
                        <li style="display:flex;gap:12px;"><span style="color:#0D99FF;">&bull;</span> Reduced design and development overhead for new features</li>
                        <li style="display:flex;gap:12px;"><span style="color:#0D99FF;">&bull;</span> Improved collaboration between design and engineering teams</li>
                        <li style="display:flex;gap:12px;"><span style="color:#0D99FF;">&bull;</span> Reduced QA and review cycles through standardized UI patterns</li>
                        <li style="display:flex;gap:12px;"><span style="color:#0D99FF;">&bull;</span> Enabled teams to move faster while maintaining design consistency</li>
                    </ul>
                </div>
            </div>
            `
        },
        'design-audit': {
            contentHtml: `
            <div class="case-study-hero">
                <span class="mono-label">CASE STUDY</span>
                <h2>Global Pharmaceutical Company (USA)</h2>
                <p>Next-Generation B2B Platform Design System</p>
            </div>
            <div class="case-study-grid custom-layout" style="display:block;">
                <div class="case-study-text full-width" style="max-width:800px;margin:0 auto;">
                    <p style="margin-bottom:32px;line-height:1.7;font-style:italic;color:var(--text-secondary);">Designing the foundational design system for a large-scale B2B healthcare commerce platform.</p>
                    <h3 style="margin-top:0;margin-bottom:16px;">Key Facts</h3>
                    <div class="facts-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:0;margin-bottom:40px;border:1px solid rgba(13,153,255,0.12);border-radius:8px;overflow:hidden;">
                        <div style="padding:20px 24px;border-right:1px solid rgba(13,153,255,0.12);border-bottom:1px solid rgba(13,153,255,0.12);"><strong style="color:#0D99FF;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.06em;">Industry</strong><br><span style="font-weight:500;font-size:0.95rem;margin-top:6px;display:inline-block;">Pharmaceutical &amp; Healthcare</span></div>
                        <div style="padding:20px 24px;border-bottom:1px solid rgba(13,153,255,0.12);"><strong style="color:#0D99FF;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.06em;">Platforms</strong><br><span style="font-weight:500;font-size:0.95rem;margin-top:6px;display:inline-block;">B2B E-commerce &amp; Enterprise Web</span></div>
                        <div style="padding:20px 24px;border-right:1px solid rgba(13,153,255,0.12);"><strong style="color:#0D99FF;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.06em;">Scope</strong><br><span style="font-weight:500;font-size:0.95rem;margin-top:6px;display:inline-block;">Design System Foundation, Component Library, Tooling Migration</span></div>
                        <div style="padding:20px 24px;"><strong style="color:#0D99FF;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.06em;">Focus</strong><br><span style="font-weight:500;font-size:0.95rem;margin-top:6px;display:inline-block;">Platform Redesign Initiative</span></div>
                    </div>

                    <h3 style="margin-top:32px;margin-bottom:16px;">Context</h3>
                    <p style="margin-bottom:16px;line-height:1.7;">As part of a major digital transformation initiative, one of the largest pharmaceutical companies in the United States began redesigning its B2B e-commerce platform to support the next generation of healthcare commerce.</p>
                    <p style="margin-bottom:16px;line-height:1.7;">The initiative aimed to modernize the platform's user experience, improve operational efficiency, and establish a consistent design language across a complex ecosystem of internal and customer-facing tools.</p>
                    <p style="margin-bottom:40px;line-height:1.7;">We partnered with their product and design teams to build a scalable design system that could support the platform redesign and enable teams to build new features efficiently.</p>

                    <h3 style="margin-top:32px;margin-bottom:16px;">Challenge</h3>
                    <p style="margin-bottom:16px;line-height:1.7;">The platform was highly complex, supporting a wide range of workflows related to healthcare commerce, product management, and enterprise operations.</p>
                    <p style="margin-bottom:16px;line-height:1.7;">At the same time, the organization was undergoing a major tooling shift — migrating its design workflows from Adobe XD to Figma. This transition created an additional challenge in ensuring that teams could adopt the new tools while also aligning around a unified design system.</p>
                    <p style="margin-bottom:40px;line-height:1.7;">The goal was to establish a structured design system that could support the platform redesign while enabling smooth collaboration between designers and engineers.</p>

                    <h3 style="margin-top:32px;margin-bottom:16px;">Approach</h3>
                    <p style="margin-bottom:16px;line-height:1.7;">We began by working closely with the product, design, and engineering teams to understand the platform architecture and the evolving requirements of the new B2B ecosystem.</p>
                    <p style="margin-bottom:16px;line-height:1.7;">This included mapping key product workflows, identifying common interface patterns, and defining the structural foundations required for scalable UI development.</p>
                    <p style="margin-bottom:40px;line-height:1.7;">Alongside this, we supported the organization's transition from Adobe XD to Figma, helping teams adopt a more collaborative and system-driven design workflow.</p>

                    <h3 style="margin-top:32px;margin-bottom:16px;">System Implementation</h3>
                    <p style="margin-bottom:16px;line-height:1.7;">We built the design system from the ground up, starting with the foundational layer including typography, color tokens, layout principles, and interaction patterns.</p>
                    <p style="margin-bottom:16px;line-height:1.7;">On top of this foundation, we designed a comprehensive component and pattern library tailored for enterprise-level workflows. The system included modular components and composable patterns that allowed teams to build complex interfaces efficiently.</p>
                    <p style="margin-bottom:40px;line-height:1.7;">Throughout the process, we collaborated closely with frontend engineers to ensure that components were implemented accurately in production. We also helped establish a structured Storybook environment to support engineering teams in maintaining and scaling the component library.</p>

                    <h3 style="margin-top:32px;margin-bottom:16px;">Governance &amp; Adoption</h3>
                    <p style="margin-bottom:16px;line-height:1.7;">To ensure long-term adoption, we worked closely with internal design teams to introduce system-driven workflows.</p>
                    <p style="margin-bottom:16px;line-height:1.7;">We conducted workshops and collaborative sessions to help designers understand how to design using the new component library and how the system could support their day-to-day product work.</p>
                    <p style="margin-bottom:40px;line-height:1.7;">These efforts helped the organization transition smoothly to a design system-driven approach to product development.</p>

                    <h3 style="margin-top:32px;margin-bottom:16px;">Impact</h3>
                    <ul style="list-style-type:none;padding:0;display:flex;flex-direction:column;gap:12px;margin-bottom:24px;">
                        <li style="display:flex;gap:12px;"><span style="color:#0D99FF;">&bull;</span> Established a scalable design system foundation for the new platform</li>
                        <li style="display:flex;gap:12px;"><span style="color:#0D99FF;">&bull;</span> Enabled the organization's migration from Adobe XD to Figma</li>
                        <li style="display:flex;gap:12px;"><span style="color:#0D99FF;">&bull;</span> Introduced a composable component and pattern library for enterprise workflows</li>
                        <li style="display:flex;gap:12px;"><span style="color:#0D99FF;">&bull;</span> Improved collaboration between design and engineering teams</li>
                        <li style="display:flex;gap:12px;"><span style="color:#0D99FF;">&bull;</span> Reduced design inconsistencies across the platform</li>
                        <li style="display:flex;gap:12px;"><span style="color:#0D99FF;">&bull;</span> Accelerated product development during the platform redesign initiative</li>
                    </ul>
                </div>
            </div>
            `
        },
        'token-architecture': {
            contentHtml: `
            <div class="case-study-hero">
                <span class="mono-label">CASE STUDY</span>
                <h2>District (by Zomato)</h2>
                <p>Visual Identity System for a New Consumer App</p>
            </div>
            <div class="case-study-grid custom-layout" style="display: block;">
                <div class="case-study-text full-width" style="max-width: 800px; margin: 0 auto;">
                    <p style="margin-bottom: 32px; line-height: 1.7; font-style: italic; color: var(--text-secondary);">Designing the foundational visual language for a new entertainment and ticketing platform.</p>

                    <h3 style="margin-top: 0; margin-bottom: 16px;">Key Facts</h3>
                    <div class="facts-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 0; margin-bottom: 40px; border: 1px solid rgba(13, 153, 255, 0.12); border-radius: 8px; overflow: hidden;">
                        <div style="padding: 20px 24px; border-right: 1px solid rgba(13, 153, 255, 0.12); border-bottom: 1px solid rgba(13, 153, 255, 0.12);"><strong style="color: #0D99FF; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.06em;">Industry</strong><br><span style="font-weight: 500; font-size: 0.95rem; margin-top: 6px; display: inline-block;">Entertainment &amp; Ticketing</span></div>
                        <div style="padding: 20px 24px; border-bottom: 1px solid rgba(13, 153, 255, 0.12);"><strong style="color: #0D99FF; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.06em;">Platforms</strong><br><span style="font-weight: 500; font-size: 0.95rem; margin-top: 6px; display: inline-block;">Mobile Application</span></div>
                        <div style="padding: 20px 24px; border-right: 1px solid rgba(13, 153, 255, 0.12);"><strong style="color: #0D99FF; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.06em;">Scope</strong><br><span style="font-weight: 500; font-size: 0.95rem; margin-top: 6px; display: inline-block;">Visual Identity System, Typography System, Color System, Iconography, Visual Language Guidelines</span></div>
                        <div style="padding: 20px 24px;"><strong style="color: #0D99FF; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.06em;">Parent Brand</strong><br><span style="font-weight: 500; font-size: 0.95rem; margin-top: 6px; display: inline-block;">Zomato</span></div>
                    </div>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">Context</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">District is a consumer platform developed by Zomato that enables users to discover and book entertainment experiences such as movie tickets, events, and local gigs.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">As the product was being built from the ground up, the team needed a clear and cohesive visual language that could define the overall look and feel of the mobile application.</p>
                    <p style="margin-bottom: 40px; line-height: 1.7;">We partnered with the team to design the foundational visual identity system that would guide the interface design and help establish a consistent product experience from day one.</p>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">Challenge</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">Since the application was entirely new, there was no established visual framework to guide the design of the product interface.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">The challenge was to create a visual system that felt modern, scalable, and aligned with the broader ecosystem while also being flexible enough to support a wide range of content-heavy entertainment experiences.</p>
                    <p style="margin-bottom: 40px; line-height: 1.7;">The system needed to provide clear visual rules that designers and engineers could follow as the product continued to evolve.</p>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">Approach</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">We began by defining the core visual principles that would shape the identity of the application.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">Working closely with the product and design teams, we explored visual directions for typography, color usage, iconography, and overall interface styling. These explorations helped establish the aesthetic foundation for the platform.</p>
                    <p style="margin-bottom: 40px; line-height: 1.7;">From these explorations, we defined a cohesive visual language that could support different interface scenarios across the mobile application.</p>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">System Implementation</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">The visual identity system established the foundational design elements required to build the app's UI.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">This included defining the typography system, color system, and iconography framework, along with guidelines for layout clarity and visual hierarchy.</p>
                    <p style="margin-bottom: 16px; line-height: 1.7;">We also documented how these visual elements should be applied across the interface to ensure a consistent and recognizable product experience.</p>
                    <p style="margin-bottom: 40px; line-height: 1.7;">This visual foundation enabled the product team to design new features quickly while maintaining a cohesive look and feel across the application.</p>

                    <h3 style="margin-top: 32px; margin-bottom: 16px;">Impact</h3>
                    <p style="margin-bottom: 16px; line-height: 1.7;">The visual identity system became the foundational layer for the District mobile application and guided the early development of the platform's interface.</p>
                    <ul style="list-style-type: none; padding: 0; display: flex; flex-direction: column; gap: 12px; margin-bottom: 24px;">
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Established the core visual language for the mobile app</li>
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Designed a scalable typography and color system</li>
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Developed a cohesive iconography framework</li>
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Enabled consistent UI design across product screens</li>
                        <li style="display: flex; gap: 12px;"><span style="color: #0D99FF;">&bull;</span> Provided a strong visual foundation for the platform's launch</li>
                    </ul>
                </div>
            </div>
            `
        }
    };

    function openModal(projectId) {
        const data = projectData[projectId];
        if (!data) return;

        if (data.contentHtml) {
            modalBody.innerHTML = data.contentHtml;
        } else {
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
        }

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
