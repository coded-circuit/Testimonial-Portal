
var tl = gsap.timeline()

tl.from('.heading',{
    y:10,
    delay:0.4,
    duration:0.8,
    opacity:0
})
tl.from('.card',{
    // delay:0.4,
    duration:1,
    stagger:1,
    y:50,
    ease:'back.out(4)',
    opacity:0,
})
// document.querySelectorAll(".edit").forEach((btn) => {
//     btn.addEventListener("click", function (e) {
//         e.preventDefault(); // stop immediate navigation
        
//         const url = this.dataset.href;
        
//         // Play reverse animation
//         tl.reverse();
        
//        // Fallback: navigate after timeline duration (adjust as needed)
//     setTimeout(() => {
//       window.location.href = url;
//     }, tl.duration() * 1000); // Convert timeline duration to ms
//     });
// });
