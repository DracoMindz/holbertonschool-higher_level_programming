$('div#red_header').click(function (){
    if($('HEADER').hasClass('red')){
	$('HEADER').addClass('green');
	$('HEADER').removeClass('red');
	$('HEADER').css('color', '#00FF00');
    } else{
	if($('HEADER').hasClass('green')){
	    $('HEADER').addClass('red');
	    $('HEADER').removeClass('green');
	    ('HEADER').css('color', '#FF0000');
	}
    });
