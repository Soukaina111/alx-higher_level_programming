$(document).ready(function() {
	  $('input#btn_translate').on('click', function() {
		      translateHello();
		    });

	  $('input#language_code').on('keydown', function(event) {
		      if (event.keyCode === 13) {
			            translateHello();
			          }
		    });

	  function translateHello() {
		      const languageCode = $('input#language_code').val();
		      const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;

		      $.ajax({
			            url: apiUrl,
			            dataType: 'json'
			          }).done(function(data) {
					        $('div#hello').text(data.hello);
					      });
		    }
});
