{*+**********************************************************************************
* The contents of this file are subject to the vtiger CRM Public License Version 1.1
* ("License"); You may not use this file except in compliance with the License
* The Original Code is: vtiger CRM Open Source
* The Initial Developer of the Original Code is vtiger.
* Portions created by vtiger are Copyright (C) vtiger.
* All Rights Reserved.
************************************************************************************}
{* modules/Users/views/Login.php *}
{strip}
<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/gh/kenwheeler/slick@1.8.0/slick/slick.css"/>
<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/gh/kenwheeler/slick@1.8.0/slick/slick-theme.css"/>
<style>
   .slick-prev{
   color:#0097CE;
   }
   .slick-next{
   color:#0097CE;
   }
   .slick-prev:hover {
   background-color: transparent;
   color: black;
   }
   .slick-next:hover {
   background-color: transparent;
   color: black;
   }
   body {
   margin: 0;
   font-family: Arial;
   font-size: 17px;
   }
   #myVideo {
   position: fixed;
   right: 0;
   bottom: 0;
   min-width: 100%;
   min-height: 100%;
   }
   hr {
   margin-top: 15px;
   background-color: #7C7C7C;
   height: 2px;
   border-width: 0;
   }
   h3, h4 {
   margin-top: 0px;
   }
   hgroup {
   text-align:center;
   margin-top: 4em;
   }
   input {
   font-size: 16px;
   padding: 10px 10px 10px 0px;
   -webkit-appearance: none;
   display: block;
   color: #636363;
   width: 100%;
   border: none;
   border-radius: 0;
   border-bottom: 1px solid #757575;
   }
   input:focus {
   outline: none;
   }
   label {
   font-size: 16px;
   font-weight: normal;
   position: absolute;
   pointer-events: none;
   left: 0px;
   top: 10px;
   transition: all 0.2s ease;
   }
   input:focus ~ label, input.used ~ label {
   top: -20px;
   transform: scale(.75);
   left: -12px;
   font-size: 18px;
   }
   input:focus ~ .bar:before, input:focus ~ .bar:after {
   width: 50%;
   }
   #page {
   padding-top: 6%;
   }
   .widgetHeight {
   height: 410px;
   margin-top: 20px !important;
   }
   .loginDiv {
   width: 380px;
   margin: 0 auto;
   border-radius: 4px;
   box-shadow: 0 0 50px gray;
   background-color: #FFFFFF;
   }
   .separatorDiv {
   background-color: #7C7C7C;
   width: 5px;
   height: 460px;
   margin-left: 20px;
   }
   .user-logo {
   height: 110px;
   margin: 0 auto;
   padding-top: 40px;
   padding-bottom: 20px;
   }
   .blockLink {
   border: 1px solid #303030;
   padding: 3px 5px;
   }
   .group {
   position: relative;
   margin: 20px 20px 40px;
   }
   .failureMessage {
   color: red;
   display: block;
   text-align: center;
   padding: 0px 0px 10px;
   }
   .successMessage {
   color: green;
   display: block;
   text-align: center;
   padding: 0px 0px 10px;
   }
   .inActiveImgDiv {
   padding: 5px;
   text-align: center;
   margin: 30px 0px;
   }
   .app-footer p {
   margin-top: 0px;
   }
   .footer {
   background-color: transparent;
   height:26px;
   }
   .bar {
   position: relative;
   display: block;
   width: 100%;
   }
   .bar:before, .bar:after {
   content: '';
   width: 0;
   bottom: 1px;
   position: absolute;
   height: 1px;
   background: #0097CE;
   transition: all 0.2s ease;
   box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
   }
   .bar:before {
   left: 50%;
   }
   .bar:after {
   right: 50%;
   }
   .button {
   position: relative;
   display: inline-block;
   padding: 9px;
   margin: .3em 0 1em 0;
   width: 100%;
   vertical-align: middle;
   color: #fff;
   font-size: 16px;
   line-height: 20px;
   -webkit-font-smoothing: antialiased;
   text-align: center;
   letter-spacing: 1px;
   background: transparent;
   border: 0;
   cursor: pointer;
   transition: all 0.15s ease;
   }
   .button:focus {
   outline: 0;
   }
   .buttonBlue {
   background-image: linear-gradient(to bottom, #0097CE 0px, #0097CE 100%)
   }
   .buttonBlue:hover {
   background-image: linear-gradient(to bottom, #0097CE 0px, #0097CE 100%)
   background-color: #0097CE;
   box-shadow: 0px 15px 20px rgba(0,151,206, 0.4);
   color: #fff;
   transform: translateY(-7px);
   }
   .slick-prev:before, .slick-next:before {
   color: black !important;
   }
   .ripples {
   position: absolute;
   top: 0
   left: 0;
   width: 100%;
   height: 100%;
   overflow: hidden;
   background: transparent;
   }
   .overlay {
   position: relative;
   font-family: Arial;
   align: center;
   }
   .text-block {
   margin: auto;
   width: 100%
   position: absolute;
   background-color: black;
   color: white;
   padding-left: 20px;
   padding-right: 20px;
   opacity: 0.5;
   }
   .slideshow-img {
   width: 100%;
   height: 100%;
   }
   //Animations
   @keyframes inputHighlighter {
   from {
   background: #4a89dc;
   }
   to 	{
   width: 0;
   background: transparent;
   }
   }
   @keyframes ripples {
   0% {
   opacity: 0;
   }
   25% {
   opacity: 1;
   }
   100% {
   width: 200%;
   padding-bottom: 200%;
   opacity: 0;
   }
   }
</style>
<style>
   /* The Modal (background) */
   .modalDialog {
     position: fixed;
     font-family: Arial, Helvetica, sans-serif;
     top: 0;
     right: 0;
     bottom: 0;
     left: 0;
     background: rgba(0, 0, 0, 0.8);
     z-index: 99999;
     opacity:0;
     -webkit-transition: opacity 400ms ease-in;
     -moz-transition: opacity 400ms ease-in;
     transition: opacity 400ms ease-in;
     pointer-events: none;
 }
 .modalDialog:target {
     opacity:1;
     pointer-events: auto;
 }
 .modalDialog > div {
     width: 50%;
     position: relative;
     margin: 10% auto;
     padding: 5px 20px 13px 20px;
     border-radius: 10px;
     background: #fff;
     background: -moz-linear-gradient(#fff, #999);
     background: -webkit-linear-gradient(#fff, #999);
     background: -o-linear-gradient(#fff, #999);
 }
 .close {
     background: #606061;
     color: #FFFFFF;
     line-height: 25px;
     position: absolute;
     right: -12px;
     text-align: center;
     top: -10px;
     width: 24px;
     text-decoration: none;
     font-weight: bold;
     -webkit-border-radius: 12px;
     -moz-border-radius: 12px;
     border-radius: 12px;
     -moz-box-shadow: 1px 1px 3px #000;
     -webkit-box-shadow: 1px 1px 3px #000;
     box-shadow: 1px 1px 3px #000;
 }
 .close:hover {
     background: #00d9ff;
 }
</style>
<body>
   <video autoplay muted loop id="myVideo">
      <source src="layouts/v7/resources/marketing/videograss.mp4" type="video/mp4">
   </video>
   <span class="app-nav"></span>
   <div class="col-lg-12 col-md-12 col-sm-10 col-xs-10" style="background-color: transparent;">
      <div class="col-lg-4 col-md-5 col-sm-8 col-xs-8" style="background-color: transparent;">
         <div class="loginDiv widgetHeight">
            <img class="img-responsive user-logo" src="layouts/v7/resources/Images/logo.png">
            <div>
               <span class="{if !$ERROR}hide{/if} failureMessage" id="validationMessage">{$MESSAGE}</span>
               <span class="{if !$MAIL_STATUS}hide{/if} successMessage">{$MESSAGE}</span>
            </div>
            <div id="loginFormDiv">
               <form class="form-horizontal" method="POST" action="index.php">
                  <input type="hidden" name="module" value="Users"/>
                  <input type="hidden" name="action" value="Login"/>
                  <div class="group">
                     <input id="username" type="text" name="username" placeholder="Username">
                     <span class="bar"></span>
                     <label>Username</label>
                  </div>
                  <div class="group">
                     <input id="password" type="password" name="password" placeholder="Password">
                     <span class="bar"></span>
                     <label>Password</label>
                  </div>
                  <div class="group">
                    <p style="font-size: 10px">By signing in you agree to our <u><a style="color: blue" href="#openTC">Terms and Conditions</a></u></p>
                     <button type="submit" class="button buttonBlue" style="color: #FFFFFF">Sign in</button><br>
                     <a style="color: blue; font-size: 12px" href="#openModal">Forgot Password?</a>
                  </div>
               </form>
            </div>
         </div>
      </div>
      <div class="col-lg-2 col-md-1">
        <div id="openTC" class="modalDialog">
          <div>	<a href="#close" title="Close" class="close">X</a>
            <iframe class="iframe" width="100%" height="500px" src="layouts/v7/modules/Users/tnc.html"></iframe>
          </div>
        </div>
        <div id="openModal" class="modalDialog">
          <div>	<a href="#close" title="Close" class="close">X</a>
            <iframe class="iframe" width="100%" height="500px" src="https://ompw.omnisrv.com/pm/"></iframe>
          </div>
        </div>
      </div>







      <!-- **************************** MARKETING **************************** -->
      <!-- **************************** MARKETING **************************** -->
      <!-- **************************** MARKETING **************************** -->
      <!-- **************************** MARKETING **************************** -->
      <!-- **************************** MARKETING **************************** -->
      <!-- **************************** MARKETING **************************** -->
      <!-- **************************** MARKETING **************************** -->
      <!-- **************************** MARKETING **************************** -->

      <div class="col-lg-4 col-md-4" style="display: inline-block; padding: 50px 0px 0px 0px">
         <div class="adCarousel">
            <div class="overlay">
               <img class="slideshow-img" src="layouts/v7/resources/marketing/img1.jpg">
               <div class="text-block lazyload">
                  <h3> Omniscient CRM Rocks! </h3>
                  <p> Don't believe me? Try it out :) </p>
               </div>
            </div>
            <div class="overlay">
               <img class="slideshow-img" data-lazy="layouts/v7/resources/marketing/img2.jpg">
               <div class="text-block lazyload">
                  <h3> This is the second slide </h3>
                  <p> This is some texty</p>
               </div>
            </div>
            <div class="overlay">
               <img class="slideshow-img" data-lazy="layouts/v7/resources/marketing/img3.jpg">
               <div class="text-block lazyload" >
                  <h3> 3</h3>
                  <p> This is some normal text. </p>
               </div>
            </div>
            <div class="overlay">
               <img class="slideshow-img" data-lazy="layouts/v7/resources/marketing/img4.jpg">
               <div class="text-block lazyload">
                  <h3> Heading </h3>
                  <p> This is some normal text. </p>
               </div>
            </div>
            <div class="overlay">

               <img class="slideshow-img" data-lazy="layouts/v7/resources/marketing/img5.jpg">
               <div class="text-block lazyload">
                  <h3> Heading </h3>
                  <p> This is some normal text. </p>
               </div>
            </div>
         </div>
      </div>
   </div>
   <!-- **************************** MARKETING **************************** -->
   <!-- **************************** MARKETING **************************** -->
   <!-- **************************** MARKETING **************************** -->
   <!-- **************************** MARKETING **************************** -->
   <!-- **************************** MARKETING **************************** -->
   <!-- **************************** MARKETING **************************** -->
   <!-- **************************** MARKETING **************************** -->
   <!-- **************************** MARKETING **************************** -->
   <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.min.js"></script>
   <script>
      jQuery(document).ready(function () {
      	var validationMessage = jQuery('#validationMessage');
      	var loginFormDiv = jQuery('#loginFormDiv');
      	loginFormDiv.find('#password').focus();
      	loginFormDiv.find('button').on('click', function () {
      		var username = loginFormDiv.find('#username').val();
      		var password = jQuery('#password').val();
      		var result = true;
      		var errorMessage = '';
      		if (username === '') {
      			errorMessage = 'Please enter valid username';
      			result = false;
      		} else if (password === '') {
      			errorMessage = 'Please enter valid password';
      			result = false;
      		}
      		if (errorMessage) {
      			validationMessage.removeClass('hide').text(errorMessage);
      		}
      		return result;
      	});
      	jQuery('input').blur(function (e) {
      		var currentElement = jQuery(e.currentTarget);
      		if (currentElement.val()) {
      			currentElement.addClass('used');
      		} else {
      			currentElement.removeClass('used');
      		}
      	});
      	var ripples = jQuery('.ripples');
      	ripples.on('click.Ripples', function (e) {
      		jQuery(e.currentTarget).addClass('is-active');
      	});
      	ripples.on('animationend webkitAnimationEnd mozAnimationEnd oanimationend MSAnimationEnd', function (e) {
      		jQuery(e.currentTarget).removeClass('is-active');
      	});
      	loginFormDiv.find('#username').focus();
      	var slider = jQuery('.bxslider').bxSlider({
      		auto: true,
      		pause: 4000,
      		nextText: "",
      		prevText: "",
      		autoHover: true
      	});
      	jQuery('.bx-prev, .bx-next, .bx-pager-item').live('click',function(){ slider.startAuto(); });
      	jQuery('.bx-wrapper .bx-viewport').css('background-color', 'transparent');
      	jQuery('.bx-wrapper .bxslider li').css('text-align', 'left');
      	jQuery('.bx-wrapper .bx-pager').css('bottom', '-15px');
      	var params = {
      		theme		: 'dark-thick',
      		setHeight	: '100%',
      		advanced	:	{
      							autoExpandHorizontalScroll:true,
      							setTop: 0
      						}
      	};
      	jQuery('.scrollContainer').mCustomScrollbar(params);
       $(".adCarousel").slick({
         slidesToShow: 1,
         slidesToScroll: 1,
         dots: true,
         arrows: true,
         autoplay: true,
         autoplaySpeed: 3000,
         infinite: true,
         adaptiveHeight: true,
         adaptiveWidth: true,
         lazyLoad: 'progressive'
       });
      });
   </script>
   </div>
</body>
{/strip}
