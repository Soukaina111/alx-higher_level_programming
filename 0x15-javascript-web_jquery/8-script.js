const LinkSer = 'https://swapi-api.hbtn.io/api/films/?format=json';
const $datamovie = $('UL#list_movies');

$.ajax({
	  url: LinkSer,
	  dataType: 'json'
}).done((data) => {
	  const series = data.results;

	  for (let i = 0; i < series.length; ++i) {
		      const titleser = series[i].title;
		      const objecc = `<li>${titleser}`;
		      $datamovie.append(objecc );
		    }
});
