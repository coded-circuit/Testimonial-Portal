const dot = document.querySelector('.cursor-dot');
  const trail = document.querySelector('.cursor-trail');

  window.addEventListener('mousemove', (e) => {
    gsap.to(dot, {
      x: e.clientX,
      y: e.clientY,
      duration: 0.1
    });

    gsap.to(trail, {
      x: e.clientX,
      y: e.clientY,
      duration: 0.4,
      ease: 'power2.out'
    });
  });