const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

//Alerts fadeout
setTimeout(function() {
  $('#message').fadeOut('slow');
}, 3000);