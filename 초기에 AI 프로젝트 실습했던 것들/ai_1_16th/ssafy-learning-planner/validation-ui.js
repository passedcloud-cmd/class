// validation-ui.js - wire validation to UI with minimal DOM assumptions
(function () {
  if (typeof window === 'undefined') return;
  function showErrors(errors) {
    // Try to find an error container; fallback to alert
    const container = document.querySelector('#errors') || document.querySelector('.errors');
    if (!container) {
      const msgs = Object.values(errors).join('\n');
      if (msgs) alert(msgs);
      return;
    }
    container.innerHTML = '';
    Object.values(errors).forEach(msg => {
      const li = document.createElement('div');
      li.textContent = msg;
      li.className = 'error-item';
      container.appendChild(li);
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    if (!form) return;
    form.addEventListener('submit', (e) => {
      if (!window.__validation || !window.__validation.validateForm) return;
      const title = form.querySelector('[name="title"]') ? form.querySelector('[name="title"]').value : '';
      const date = form.querySelector('[name="date"]') ? form.querySelector('[name="date"]').value : '';
      const time = form.querySelector('[name="time"]') ? form.querySelector('[name="time"]').value : '';
      const duration = form.querySelector('[name="duration"]') ? form.querySelector('[name="duration"]').value : undefined;
      const errors = window.__validation.validateForm({ title, date, time, duration });
      if (Object.keys(errors).length > 0) {
        e.preventDefault();
        showErrors(errors);
      }
    });
  });
})();
