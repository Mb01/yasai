//Created on Dec 2, 2012
//author: mark

//included in head of mainpage.html




$(document).ready(function(){
		$('.title').hide()
		$('.search').hide();
		$('form').hide();
		$('.title').show('slow');
		$('.search').show('slow');
		
		
		$('.itemName').hide();
		$('.itemPrice').hide();
		$('.storeName').hide();
	
	$(".search").click(function(){
		$('form').hide('slow');
		$('.itemName').hide();
		$('.itemPrice').hide();
		$('.storeName').hide();
		toShow = $('input[name=searchBar]').val();
		$toShow = $('span:contains('+toShow+')').parentsUntil('.results').children();
		$toShow.show('slow');
	});
	
	$('.input').click(function(){
		$('form').show('slow');
	});
	
});

