(() => {
  const current = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('[data-nav]').forEach(link => {
    const href = link.getAttribute('href');
    if ((current === '' && href === 'index.html') || href === current) {
      link.setAttribute('aria-current', 'page');
    }
  });

  const toggle = document.querySelector('[data-menu-toggle]');
  const menu = document.querySelector('[data-menu]');
  if (toggle && menu) {
    toggle.addEventListener('click', () => {
      const isOpen = menu.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(isOpen));
    });
  }

  const revealEls = document.querySelectorAll('.lh-reveal');
  if (revealEls.length && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('is-visible'); io.unobserve(e.target); } });
    }, { threshold: 0.1 });
    revealEls.forEach(el => io.observe(el));
  } else {
    revealEls.forEach(el => el.classList.add('is-visible'));
  }

  const filterButtons = document.querySelectorAll('[data-filter]');
  const cards = document.querySelectorAll('[data-categories]');
  filterButtons.forEach(button => {
    button.addEventListener('click', () => {
      const filter = button.dataset.filter;
      filterButtons.forEach(btn => btn.classList.remove('is-active'));
      button.classList.add('is-active');
      cards.forEach(card => {
        const categories = card.dataset.categories.toLowerCase();
        const show = filter === 'all' || categories.includes(filter);
        card.hidden = !show;
      });
    });
  });
})();
