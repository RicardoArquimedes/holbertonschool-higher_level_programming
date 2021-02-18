$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', info => {
  $('#character').text(info.name);
});