const $entete = $('header');
const $divRed = $('div#red_header');

$divRed.on('click', function () {
	  $entete.css('color', '#FF0000');
});
