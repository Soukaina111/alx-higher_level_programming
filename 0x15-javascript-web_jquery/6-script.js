const $entete = $('header');
const $toupdate = $('div#update_header');

$toupdate.on('click', () => {
	  $entete .text('New Header!!!');
});
