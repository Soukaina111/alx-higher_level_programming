const $entete = $('header');
const $divRed  = $('DIV#toggle_header');

$divRed.on('click', () => {
	  const nowc = $entete.attr('class');

	  if (nowc === 'green') {
		      $entete.toggleClass(`${nowc} red`);
		    }

	  if (nowc === 'red') {
		      $entete.toggleClass(`${nowc} green`);
		    }
});
