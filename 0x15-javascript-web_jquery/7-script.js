const LinkU = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const $divchar = $('div#character');

$.ajax({
	  url: LinkU ,
	  dataType: 'json'
}).done((data) => {
	  $divchar.text(data.name);
});
