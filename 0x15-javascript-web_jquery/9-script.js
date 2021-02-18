$.get('https://fourtonfish.com/hellosalut/?lang=fr', info => {
  $('#hello').append(`${info.hello}`);
});