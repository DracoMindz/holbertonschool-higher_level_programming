$(function () {
    $.get('https://swapi.co/api/people/5/?format=json', function (data) {
      for(let mL of data.results){
	$('UL#list_movies').append('<li></li>').text(mL.title));
    }
	 });
 });
