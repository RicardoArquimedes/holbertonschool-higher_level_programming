$.get('https://swapi-api.hbtn.io/api/films/?format=json', info => {
  info.results.forEach(movie => {
    $('#list_movies').append(`<li>${movie.title}</li>`);
  });
});