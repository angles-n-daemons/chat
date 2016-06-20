$(function() {
  setupPopups();

  $('form[name=loginForm]').submit(function(e) {
    e.preventDefault()
    submitForm(this, 'login');
  });
  $('form[name=signupForm]').submit(function(e) {
    e.preventDefault();
    submitForm(this, 'signup');
  });
});

function setupPopups() {
  var popupOpts = {
    'horizontal': 'center',
    'vertical': 'center',
    'opacity': 1,
    'transition': '0.3s',
    'scrolllock': true,
    'type': 'overlay',
    'color': '#C08ED1',
    'escape': true,
    'closeelement': '#close-btn'
  };
  $('#login-form').popup($.extend(popupOpts, {'openelement': '#login-btn'}));
  $('#signup-form').popup($.extend(popupOpts, {'openelement': '#signup-btn'}));
}

function submitForm(form, type) {

  $.ajax({
    url: 'api/' + type,
    type: 'POST',
    data: $(form).serialize()
  }).success(function(){

  }).fail(function(){

  });
};