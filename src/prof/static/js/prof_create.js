var tl = gsap.timeline()
tl.from('.create',{
    y:30,
    opacity:0,
    delay:0.4,
    duration:0.8,
    ease:'bounce.out(3)'
})
tl.from('.heading',{
    y:50,
    duration:0.6,
    opacity:0,
})
tl.from('form label',{
    y:50,
    duration:1,
    opacity:0,
})
tl.from('form input',{
    x:30,
    opacity:0
})
tl.from('form textarea',{
    x:30,
    opacity:0,
})

