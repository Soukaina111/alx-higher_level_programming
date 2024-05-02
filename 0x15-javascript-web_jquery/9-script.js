$(document).ready(function () {
	  const First = 'https://fourtonfish.com/hellosalut/?lang=fr';
	  const $greeting = $('div#hello');

	  function greeting () {
		      return $.get({
			            url: First,
			            dataType: 'json'
			          });
		    }

	  greeting().then((ans) => {
		      $greeting.text(ans.hello);
		    });
});
