const slow = [];
let x = 1;
for (let i = 1; i <= 5; i++) {
    slow.push(document.querySelector(".product-header__slider--"+[i]));
    
}

window.addEventListener('scroll',()=>{
    let scrolled = window.pageYOffset;
    
    slow.forEach(s => {
        s.style.backgroundPositionY = scrolled * 0.7 +'px' ;
    });
  
});


