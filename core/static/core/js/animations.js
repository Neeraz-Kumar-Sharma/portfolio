/* ============================================================
   animations.js
   Handles: custom cursor, floating particles, stat counters,
            skill bar reveal, scroll-triggered fade-ins
   ============================================================ */

'use strict';

/* ── Custom Cursor ─────────────────────────────────────────── */
(function initCursor() {
  const cursor = document.getElementById('cursor');
  const ring   = document.getElementById('cursorRing');
  if (!cursor || !ring) return;

  let mx = 0, my = 0, rx = 0, ry = 0;

  document.addEventListener('mousemove', (e) => {
    mx = e.clientX;
    my = e.clientY;
    cursor.style.left = mx - 6 + 'px';
    cursor.style.top  = my - 6 + 'px';
  });

  (function animateRing() {
    rx += (mx - rx) * 0.12;
    ry += (my - ry) * 0.12;
    ring.style.left = rx - 18 + 'px';
    ring.style.top  = ry - 18 + 'px';
    requestAnimationFrame(animateRing);
  })();

  // Scale on hover over interactive elements
  const hoverTargets = document.querySelectorAll(
    'a, button, .project-card, .skill-card, .contact-item, .btn-primary, .btn-secondary'
  );
  hoverTargets.forEach(el => {
    el.addEventListener('mouseenter', () => {
      ring.style.transform  = 'scale(2)';
      ring.style.opacity    = '0.3';
      cursor.style.transform = 'scale(0.5)';
    });
    el.addEventListener('mouseleave', () => {
      ring.style.transform  = 'scale(1)';
      ring.style.opacity    = '0.6';
      cursor.style.transform = 'scale(1)';
    });
  });
})();


/* ── Floating Particles ────────────────────────────────────── */
(function initParticles() {
  const container = document.getElementById('particles');
  if (!container) return;

  for (let i = 0; i < 25; i++) {
    const p = document.createElement('div');
    p.className = 'particle';
    p.style.left              = Math.random() * 100 + 'vw';
    p.style.animationDuration = (10 + Math.random() * 14) + 's';
    p.style.animationDelay    = (Math.random() * 14) + 's';
    container.appendChild(p);
  }
})();


/* ── Stat Counters ─────────────────────────────────────────── */
(function initCounters() {
  const counters = document.querySelectorAll('.stat-number');
  if (!counters.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;

      const el     = entry.target;
      const target = parseInt(el.dataset.target, 10);
      const suffix = el.dataset.suffix || '';
      let current  = 0;
      const step   = target / 60;

      const interval = setInterval(() => {
        current += step;
        if (current >= target) {
          current = target;
          clearInterval(interval);
        }
        el.textContent = Math.floor(current) + suffix;
      }, 16);

      observer.unobserve(el);
    });
  }, { threshold: 0.5 });

  counters.forEach(c => observer.observe(c));
})();


/* ── Skill Bar Reveal ───────────────────────────────────────── */
(function initSkillBars() {
  const bars = document.querySelectorAll('.skill-fill');
  if (!bars.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });

  bars.forEach(bar => observer.observe(bar));
})();


/* ── Fade-in on scroll ─────────────────────────────────────── */
(function initFadeIn() {
  const elements = document.querySelectorAll('.project-card, .skill-card, .contact-item');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity   = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  elements.forEach((el, i) => {
    el.style.opacity   = '0';
    el.style.transform = 'translateY(24px)';
    el.style.transition = `opacity 0.5s ${i * 0.05}s ease, transform 0.5s ${i * 0.05}s ease`;
    observer.observe(el);
  });
})();
