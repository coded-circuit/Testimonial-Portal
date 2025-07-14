var tl = gsap.timeline()
tl.from('.card',{
    y:10,
    duration:1,
    delay:0.5,
    opacity:0,
    stagger:0.8,
    ease:'back.out(4)'
})

