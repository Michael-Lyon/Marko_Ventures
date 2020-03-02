
// var Nav = document.querySelector(".navigation");
var back = document.querySelector(".background");
var checkBox = document.getElementById("#check");

document.querySelector('.check').addEventListener('click',()=>{
    back.classList.toggle('in');
});

document.querySelector('.background__link').addEventListener('click',()=>{
    back.classList.toggle('in');
    console.log('yam');
    
});







