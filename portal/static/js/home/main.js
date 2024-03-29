/*==================== MENU SHOW Y HIDDEN ====================*/
const navMenu=document.getElementById('nav-menu'),
      navToggle=document.getElementById('nav-toggle'),
      navClose=document.getElementById('nav-close');

/*===== MENU SHOW =====*/
/* Validate if constant exists */
if(navToggle){
    navToggle.addEventListener('click',() =>{
        navMenu.classList.add('show-menu')
    }
    )
}
/*===== MENU HIDDEN =====*/
/* Validate if constant exists */
if(navClose){
    navClose.addEventListener('click',() =>{
        navMenu.classList.remove('show-menu');
    })
}

/*==================== REMOVE MENU MOBILE ====================*/
const navLink = document.querySelectorAll('.nav__link')

function linkAction(){
    const navMenu = document.getElementById('nav-menu')
    // When we click on each nav__link, we remove the show-menu class
    navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

/*==================== SERVICES MODAL ====================*/
const modalViews=document.querySelectorAll('.services__modal'),
      modalBtns=document.querySelectorAll('.services__button'),
      modalCloses=document.querySelectorAll('.services__modal-close')

let modal=function(modalClick){
    modalViews[modalClick].classList.add('active-modal')
}

modalBtns.forEach((modalBtn,i) =>{
    modalBtn.addEventListener('click',() =>{
        modal(i)
    })
})

modalCloses.forEach((modalClose)=>{
    modalClose.addEventListener('click',() =>{
        modalViews.forEach((modalView) =>{
            modalView.classList.remove('active-modal')
        })
    })
})


/*==================== SCROLL SECTIONS ACTIVE LINK ====================*/
const sections = document.querySelectorAll('section[id]')

function scrollActive(){
    const scrollY = window.pageYOffset

    sections.forEach(current =>{
        const sectionHeight = current.offsetHeight
        const sectionTop = current.offsetTop - 50;
        sectionId = current.getAttribute('id')

        if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight){
            document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.add('active-link')
        }else{
            document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.remove('active-link')
        }
    })
}
window.addEventListener('scroll', scrollActive)

/*==================== CHANGE BACKGROUND HEADER ====================*/ 
function scrollHeader(){
    const nav = document.getElementById('header')
    // When the scroll is greater than 200 viewport height, add the scroll-header class to the header tag
    if(this.scrollY >= 80) nav.classList.add('scroll-header'); else nav.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)
/*==================== SHOW SCROLL UP ====================*/ 
function scrollUp(){
    const scrollUp = document.getElementById('scroll-up');
    // When the scroll is higher than 560 viewport height, add the show-scroll class to the a tag with the scroll-top class
    if(this.scrollY >= 560) scrollUp.classList.add('show-scroll'); else scrollUp.classList.remove('show-scroll')
}
window.addEventListener('scroll', scrollUp)


/*==================== DARK LIGHT THEME ====================*/ 
const themeButton = document.getElementById('theme-button1')
const darkTheme = 'dark-theme'
const iconTheme = 'uil-sun'

// Previously selected topic (if user selected)
const selectedTheme = localStorage.getItem('selected-theme')
const selectedIcon = localStorage.getItem('selected-icon')

// We obtain the current theme that the interface has by validating the dark-theme class
const getCurrentTheme = () => document.body.classList.contains(darkTheme) ? 'dark' : 'light'
const getCurrentIcon = () => themeButton.classList.contains(iconTheme) ? 'uil-moon' : 'uil-sun'

// We validate if the user previously chose a topic
if (selectedTheme) {
  // If the validation is fulfilled, we ask what the issue was to know if we activated or deactivated the dark
  document.body.classList[selectedTheme === 'dark' ? 'add' : 'remove'](darkTheme)
  themeButton.classList[selectedIcon === 'uil-moon' ? 'add' : 'remove'](iconTheme)
}

// Activate / deactivate the theme manually with the button
themeButton.addEventListener('click', () => {
    // Add or remove the dark / icon theme
    document.body.classList.toggle(darkTheme)
    themeButton.classList.toggle(iconTheme)
    // We save the theme and the current icon that the user chose
    localStorage.setItem('selected-theme', getCurrentTheme())
    localStorage.setItem('selected-icon', getCurrentIcon())
})


function myFunction12() {
    var x = document.getElementById("fuel_type").value;
    var y = document.getElementById("quantity_quote").value;
    if(x==="Gasoline"){
        document.getElementById("Gallon_price").innerHTML = "5.006";
        document.getElementById("Gallon_price1").innerHTML = "5.006";
        document.getElementById("Gallon_price2").innerHTML=y
        let x1 = "5.006";
        let y1 = y;
        let fin_=x1 * y1;
        document.getElementById("Gallon_price3").innerHTML=fin_
        var numVal2 = Number(14) / 100;
        let totalValue = fin_ - (fin_ * numVal2)
        let final_grocess=Number(fin_)-Number(totalValue)
        let hhhhh=final_grocess+fin_
        document.getElementById("grand_total").innerHTML = hhhhh;
        document.getElementById("Total_Amount_Due").innerHTML = hhhhh;
    }
    else if(x==="Diesel"){
        document.getElementById("Gallon_price").innerHTML = "5.718";
        document.getElementById("Gallon_price1").innerHTML = "5.718";
        document.getElementById("Gallon_price2").innerHTML=y
        let x1 = "5.718";
        let y1 = y;
        let fin_=x1 * y1;
        document.getElementById("Gallon_price3").innerHTML=fin_
        var numVal2 = Number(14) / 100;
        let totalValue = fin_ - (fin_ * numVal2)
        let final_grocess=Number(fin_)-Number(totalValue)
        let hhhhh=final_grocess+fin_
        document.getElementById("grand_total").innerHTML = hhhhh;
        document.getElementById("Total_Amount_Due").innerHTML = hhhhh;
    }
    else if(x==="None"){
        document.getElementById("Gallon_price").innerHTML = "0";
        document.getElementById("Gallon_price1").innerHTML = "0";
        document.getElementById("Gallon_price2").innerHTML=y
        let x1 = "0";
        let y1 = y;
        let fin_=x1 * y1;
        document.getElementById("Gallon_price3").innerHTML=fin_
        var numVal2 = Number(14) / 100;
        let totalValue = fin_ - (fin_ * numVal2)
        let final_grocess=Number(fin_)-Number(totalValue)
        let hhhhh=final_grocess+fin_
        document.getElementById("grand_total").innerHTML = hhhhh;
        document.getElementById("Total_Amount_Due").innerHTML = hhhhh;
    }
  }

function checking(){
  var quantity_quote = document.getElementById("quantity_quote").value;
  var bdate=document.getElementById("bdate").value
  if(quantity_quote!='' && bdate!=''){
   document.getElementById("Get_Quote_id").disabled = false;
  }
  else{
   document.getElementById("order_fuel_id").disabled = true;
   document.getElementById("Get_Quote_id").disabled = true;
  }
}

function Get_Quote(){
    var quantity_quote = document.getElementById("quantity_quote").value;
    var state_code=document.getElementById("state-code").value
    var UID = document.getElementById("user_id").value
    details_={"quantity_quote":quantity_quote,"state_code":state_code,'user_uid':UID}
    $.ajax({
            url: '/fuel_quote/Get_Quote',
            data: JSON.stringify(details_),
            type: 'POST',
            contentType: "application/json",
            dataType: 'json',
            success: function (data2)
            {
              document.getElementById("Margin_price").innerHTML = data2['margin_'];
              document.getElementById("grand_total").innerHTML = data2['Suggested_Price'];
              document.getElementById("Total_Amount_Due").innerHTML = data2['Total_Amount_Due'];
              document.getElementById("order_fuel_id").disabled = false;
              document.getElementById("Get_Quote_id").disabled = true;``
            },
            error: function(data2)
            {
              document.getElementById("order_fuel_id").disabled = true;
              document.getElementById("Get_Quote_id").disabled = true;
                console.log(data2);
            }
    });
}





