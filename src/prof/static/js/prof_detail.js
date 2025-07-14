const container = document.querySelector('.main2')
var tl = gsap.timeline()

tl.from('.profile h1',{
    y:10,
    opacity:0,
    stagger:0.7,
    duration:1,
    delay:0.5,
})
tl.from('.btn div',{
    y:10,
    opacity:0,
    stagger:0.5,
    duration:1,
    
})
tl.from('.main',{
    opacity:0,
})
tl.from('.main h2',{
    opacity:0,
})
tl.to('.main h2',{
    scale:1.5,
    yoyo:true,
    duration:0.67,
    repeat:1,
})
tl.from(container,{
    opacity:0
})
tl.to(container,{
    scrollLeft:container.scrollWidth-container.clientWidth, // it is the maximum scrollable distance
    duration:10,
    ease:"none",
    repeat:-1,
    yoyo:true,

})