  gsap.to("#img", {
    // x: 20,
    // y: 10,
    rotate:3,
    duration: 0.8,
    // delay:1,
    repeat: -1,
    yoyo: true,
    ease: "power1.inOut"
  });

  var tl = gsap.timeline()

  tl.from(".right h1",{
    opacity:0,
    y:10,
    duration:1,
    delay:1,
  })
  tl.from(".right div",{
    opacity:0,
    y:10,
    duration:1,
    // delay:1,
  })
  tl.from('input,button',{
    opacity:0,
  })
  tl.from('input,button',{
    // rotate:3,
    scale:1.1,
    delay:0.5,
    duration: 1,
    // delay:1,
    repeat: -1,
    yoyo: true,
    ease: "power1.inOut",
    
  })
