const $listitems = $('ul.my_list');
const $toadd = $('div#add_item');

$toadd.on('click', () => {
	  $listitems.append('<li>Item</li>');
});
