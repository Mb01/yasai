//Created on Dec 2, 2012
//author: mark

//included in head of mainpage.html


$(document).ready(function(){
	$('.itemName').hide();
	$('.itemPrice').hide();
	$(".search").click(function(){
		toShow = $('input[name=searchBar]').val();
		$('.' + toShow).show();
	});
});