/* ============================================================
   main.js
   Handles: terminal typewriter, smooth nav, contact form AJAX
   ============================================================ */

'use strict';

/* ── Terminal Typewriter ────────────────────────────────────── */
(function initTerminal() {
  function typeText(el, text, delay, callback) {
    if (!el) return;
    let i = 0;
    const interval = setInterval(() => {
      el.textContent += text[i];
      i++;
      if (i >= text.length) {
        clearInterval(interval);
        if (callback) setTimeout(callback, 300);
      }
    }, delay);
  }

  function showLine(id) {
    const el = document.getElementById(id);
    if (el) el.style.display = 'block';
    return el;
  }

  const t1 = document.getElementById('t1');
  if (!t1) return;  // terminal not on this page

  setTimeout(() => {
    typeText(t1, 'cat profile.txt', 40, () => {
      showLine('t2');
      const lines = ['t3', 't4', 't5', 't6', 't7', 't8'];
      lines.forEach((id, i) => setTimeout(() => showLine(id), (i + 1) * 200));
      setTimeout(() => showLine('t9'), 1800);
    });
  }, 600);
})();


/* ── Smooth Scroll Nav ──────────────────────────────────────── */
(function initNav() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  // Highlight active nav link on scroll
  const sections  = document.querySelectorAll('section[id]');
  const navLinks  = document.querySelectorAll('.nav-links a');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        navLinks.forEach(link => {
          link.style.color = link.getAttribute('href') === '#' + entry.target.id
            ? 'var(--accent)' : '';
        });
      }
    });
  }, { threshold: 0.4 });

  sections.forEach(s => observer.observe(s));
})();


/* ── Contact Form (AJAX) ────────────────────────────────────── */
(function initContactForm() {
  const form = document.getElementById('contactForm');
  if (!form) return;

  const submitBtn  = form.querySelector('.btn-submit');
  const alertBox   = document.getElementById('formAlert');

  function showAlert(message, type) {
    alertBox.textContent  = message;
    alertBox.className    = 'alert alert-' + type;
    alertBox.style.display = 'block';
    alertBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  function hideAlert() {
    alertBox.style.display = 'none';
  }

  function setLoading(loading) {
    submitBtn.disabled    = loading;
    submitBtn.textContent = loading ? 'TRANSMITTING...' : 'SEND MESSAGE';
  }

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    hideAlert();
    setLoading(true);

    const formData = new FormData(form);

    try {
      const response = await fetch(form.action || window.location.href, {
        method:  'POST',
        headers: { 'X-Requested-With': 'XMLHttpRequest' },
        body:    formData,
      });

      const data = await response.json();

      if (response.ok && data.status === 'ok') {
        showAlert('✓ Message transmitted successfully. I will get back to you soon.', 'success');
        form.reset();
      } else {
        // Show field-level errors
        const errors = data.errors || {};
        const messages = Object.values(errors).flat().join(' | ');
        showAlert('✗ ' + (messages || 'Something went wrong. Please try again.'), 'error');
      }
    } catch (err) {
      // Fallback: regular form submit
      form.submit();
    } finally {
      setLoading(false);
    }
  });
})();


/* ── Nav background on scroll ──────────────────────────────── */
(function initNavScroll() {
  const nav = document.querySelector('nav');
  if (!nav) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 60) {
      nav.style.background = 'rgba(2,11,15,0.98)';
      nav.style.boxShadow  = '0 1px 20px rgba(0,0,0,0.5)';
    } else {
      nav.style.background = 'rgba(2,11,15,0.9)';
      nav.style.boxShadow  = 'none';
    }
  });
})();
