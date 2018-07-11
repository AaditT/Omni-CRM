{*+**********************************************************************************
* The contents of this file are subject to the vtiger CRM Public License Version 1.1
* ("License"); You may not use this file except in compliance with the License
* The Original Code is: vtiger CRM Open Source
* The Initial Developer of the Original Code is vtiger.
* Portions created by vtiger are Copyright (C) vtiger.
* All Rights Reserved.
************************************************************************************}

<!--Contributed in a major way ;) by Aadit Trivedi, Rishi Balakrishnan, and Ajosh Antony -->

{* modules/Users/views/Login.php *}
{strip}
<style>
   body {
   background: url(layouts/v7/resources/Images/login-background.jpg);
   background-position: center;
   background-size: cover;
   width: 100%;
   height: 96%;
   background-repeat: no-repeat;
	 background-color: transparent;
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
   background: #35aa47;
   transition: all 0.2s ease;
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
   background-image: linear-gradient(to bottom, #35aa47 0px, #35aa47 100%)
   }
   .ripples {
   position: absolute;
   top: 0;
   left: 0;
   width: 100%;
   height: 100%;
   overflow: hidden;
   background: transparent;
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
<!-- <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/2.0.2/anime.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script> -->
<span class="app-nav"></span>
<div class="col-lg-12 col-md-12">
   <!--<div class=”col-lg-4 col-lg-offset-4″>-->
   <div class="col-lg-4 col-md-5">
      <div class="loginDiv widgetHeight">
         <img class="img-responsive user-logo" src="layouts/v7/skins/images/Vtiger.png">
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
                  <button type="submit" class="button buttonBlue">Sign in</button><br>
                  <a class="forgotPasswordLink" style="color: #15c;">Forgot password?</a>
               </div>
            </form>
         </div>
         <div id="forgotPasswordDiv" class="hide">
            <form class="form-horizontal" action="forgotPassword.php" method="POST">
               <div class="group">
                  <input id="fusername" type="text" name="username" placeholder="Username" >
                  <span class="bar"></span>
                  <label>Username</label>
               </div>
               <div class="group">
                  <input id="email" type="email" name="emailId" placeholder="Email" >
                  <span class="bar"></span>
                  <label>Email</label>
               </div>
               <div class="group">
                  <button type="submit" class="button buttonBlue forgot-submit-btn">Submit</button><br>
                  <span>Please enter details and submit<a class="forgotPasswordLink pull-right" style="color: #15c;">Back</a></span>
               </div>
            </form>
         </div>
      </div>
   </div>
   <div class="col-lg-2 col-md-1"></div>



























   <!-- **************************** MARKETING **************************** -->
   <!-- **************************** MARKETING **************************** -->
   <!-- **************************** MARKETING **************************** -->
   <!-- **************************** MARKETING **************************** -->
   <!-- **************************** MARKETING **************************** -->
   <!-- **************************** MARKETING **************************** -->
   <!-- **************************** MARKETING **************************** -->
   <!-- **************************** MARKETING **************************** -->
   <div class="col-lg-6 col-md-5" style="background-color: transparent;">
      <div style="background-color: transparent;">
         <div style="background-color: transparent;">
            <script src="https://www.w3schools.com/lib/w3.js"></script>
						<div class="container" style="width: 100%; height: 80%; background-color: transparent;">
               <div id="myCarousel" class="carousel slide" data-ride="carousel" style="background-color: transparent;">
                  <!-- Indicators -->
                  <ol class="carousel-indicators">
                     <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
                     <li data-target="#myCarousel" data-slide-to="1"></li>
                     <li data-target="#myCarousel" data-slide-to="2"></li>
										 <li data-target="#myCarousel" data-slide-to="3"></li>
										 <li data-target="#myCarousel" data-slide-to="4"></li>
                  </ol>
                  <div class="carousel-inner" align="center" style="background-color: transparent;">
                     <div class="item active">
                        <img src="layouts/v7/resources/marketing/img1.jpg" alt="Los Angeles">
                        <div class="carousel-caption">
													 <!-- HEADER FOR FIRST SLIDE -->
                           <h3>Los Angeles</h3>
													 <!--TEXT FOR FIRST SLIDE -->
                           <p>LA is always so much fun!</p>
                        </div>
                     </div>
                     <div class="item">
                        <img src="layouts/v7/resources/marketing/img2.jpg" alt="Chicago">
                        <div class="carousel-caption">
													<!-- HEADER FOR SECOND SLIDE -->
                           <h3>Chicago</h3>
													 <!-- TEXT FOR SECOND SLIDE-->
                           <p>Thank you, Chicago!</p>
                        </div>
                     </div>
                     <div class="item">
                        <img src="layouts/v7/resources/marketing/img3.jpg" alt="New York">
                        <div class="carousel-caption">
													<!-- HEADER FOR THIRD SLIDE -->
                           <h3>New York</h3>
													 <!-- TEXT FOR THIRD SLIDE -->
													 <p> NEW YORK </p>
                        </div>
                     </div>
										 <div class="item">
                        <img src="layouts/v7/resources/marketing/img4.jpg" alt="Chicago">
                        <div class="carousel-caption">
													<!-- HEADER FOR FOURTH IMAGE -->
                           <h3>Chicago</h3>
													 <!-- TEXT FOR FOURTH IMAGE -->
                           <p>Thank you, Chicago!</p>
                        </div>
                     </div>
										 <div class="item">
                        <img src="layouts/v7/resources/marketing/img5.jpg" alt="Chicago">
                        <div class="carousel-caption">
													<!-- HEADER FOR FIFTH IMAGE -->
                           <h3>Chicago</h3>
													 <!-- TEXT FOR FIFTH IMAGE -->
                           <p>Thank you, Chicago!</p>
                        </div>
                     </div>
                  </div>
                  <!-- Left and right controls -->
                  <a class="left carousel-control" href="#myCarousel" data-slide="prev">
                  <span class="glyphicon glyphicon-chevron-left"></span>
                  <span class="sr-only">Previous</span>
                  </a>
                  <a class="right carousel-control" href="#myCarousel" data-slide="next">
                  <span class="glyphicon glyphicon-chevron-right"></span>
                  <span class="sr-only">Next</span>
                  </a>
               </div>
            </div>
            <script>
               w3.slideshow(".nature", 2000);
            </script>
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






















<!--
   <div class="col-lg-5 newsDiv">
     <div class="marketingDiv widgetHeight">
       {if $JSON_DATA}
         {assign var=COUNTER value=0}
         {foreach key=BLOCK_NAME item=BLOCKS_DATA from=$JSON_DATA}
           {if $BLOCKS_DATA}
             <div>
               {assign var=COUNTER value=$COUNTER+1}
               <h4  >{$BLOCKS_DATA[0].heading}</h4>
               {foreach item=BLOCK_DATA from=$BLOCKS_DATA}
                 <div class="row">
                   {if $BLOCK_DATA.image}
                     <div class="col-lg-4" style="min-height: 100px;"><img src="{$BLOCK_DATA.image}" style="width: 100%;height: 100%;margin-top: 10px;"/></div>
                     <div class="col-lg-8">
                   {else}
                     <div class="col-lg-12">
                   {/if}
                     <div title="{$BLOCK_DATA.summary}">
                       <h3  ><b>{$BLOCK_DATA.displayTitle}</b></h3>
                       <p  >{$BLOCK_DATA.displaySummary}</p><br><br>
                     </div>
                     <a href="{$BLOCK_DATA.url}" target="_blank"><u  >{$BLOCK_DATA.urlalt}</u></a>
                   {if $BLOCK_DATA.image}
                     </div>
                   {else}
                     </div>
                   {/if}
                 </div>
               {/foreach}
             </div>
             {if $COUNTER neq $DATA_COUNT}
               <hr>
             {/if}
           {/if}
         {/foreach}
       {else}
         <div class="inActiveImgDiv">
           <div>
             <h4>Get more out of Vtiger with extensions from</h4>
             <h4>Vtiger Marketplace</h4>
           </div>
           <a href="https://marketplace.vtiger.com/app/listings" target="_blank" style="margin-right: 25px;"><img src="layouts/v7/resources/Images/extensionstore.png" style="width: 85%; height: 100%; margin-top: 25px;"/></a>
         </div>
       {/if}
       </div>
     </div>
   -->
</div>
<script>
   jQuery(document).ready(function () {
   	var validationMessage = jQuery('#validationMessage');
   	var forgotPasswordDiv = jQuery('#forgotPasswordDiv');

   	var loginFormDiv = jQuery('#loginFormDiv');
   	loginFormDiv.find('#password').focus();

   	loginFormDiv.find('a').click(function () {
   		loginFormDiv.toggleClass('hide');
   		forgotPasswordDiv.toggleClass('hide');
   		validationMessage.addClass('hide');
   	});

   	forgotPasswordDiv.find('a').click(function () {
   		loginFormDiv.toggleClass('hide');
   		forgotPasswordDiv.toggleClass('hide');
   		validationMessage.addClass('hide');
   	});

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

   	forgotPasswordDiv.find('button').on('click', function () {
   		var username = jQuery('#forgotPasswordDiv #fusername').val();
   		var email = jQuery('#email').val();

   		var email1 = email.replace(/^\s+/, '').replace(/\s+$/, '');
   		var emailFilter = /^[^@]+@[^@.]+\.[^@]*\w\w$/;
   		var illegalChars = /[\(\)\<\>\,\;\:\\\"\[\]]/;

   		var result = true;
   		var errorMessage = '';
   		if (username === '') {
   			errorMessage = 'Please enter valid username';
   			result = false;
   		} else if (!emailFilter.test(email1) || email == '') {
   			errorMessage = 'Please enter valid email address';
   			result = false;
   		} else if (email.match(illegalChars)) {
   			errorMessage = 'The email address contains illegal characters.';
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
   });
</script>
</div>
<div>

{/strip}



<!-- INSTRUCTIONS FOR CHANGING THE HEADERS AND DESCRIPTION TEXT ASSOSCIATED WITH EACH IMAGE

To change the text and the headers assosciated with each image:
	For the first image, the header is on line 309 and the description text is on line 311
	For the second image, the header is on line 318 and the description text is on line 320
	For the third image, the header is on line 327 and the description text is on line 329
	For the fourth image, the header is on line 336 and the description text is on line 338
	For the fifth image, the header is on line 345 and the description text is on line 347
-->
