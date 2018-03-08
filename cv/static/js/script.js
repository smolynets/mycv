function initLangSelector() {
    $('button.initLangSelector').click(function(event){
        var lan = $(this).val();
        $.cookie('django_language', lan, {'path': '/', 'expires': 365});
        location.reload(true);
        return true;
     });
    }


$(document).ready(function(){

    initLangSelector()


 
    function showingMenu(){
        $('.menu-items').toggleClass('hidden');
    }

    $('.menu-container').mouseover(function(){
        showingMenu();
    })

    $('.menu-container').mouseout(function(){
        showingMenu();
    })




    function biggerArrow_left(){
        $('.arrow_left').show().animate( {
        	fontSize:"70px"
        	} , 200 );
    }

    function lessArrow_left(){
        $('.arrow_left').show().animate( {
        	fontSize:"40px"
        	} , 200 );
    }


    $('.arrow_left').mouseover(function(){
        biggerArrow_left();
    })

    $('.arrow_left').mouseout(function(){
        lessArrow_left();
    })




    function biggerArrow_right(){
        $('.arrow_right').show().animate( {
        	fontSize:"70px"
        	} , 200 );
    }

    function lessArrow_right(){
        $('.arrow_right').show().animate( {
        	fontSize:"40px"
        	} , 200 );
    }


    $('.arrow_right').mouseover(function(){
        biggerArrow_right();
    })

    $('.arrow_right').mouseout(function(){
        lessArrow_right();
    })

    function initLangSelector() {
    $('button.initLangSelector').click(function(event){
        var lan = $(this).val();
        $.cookie('django_language', lan, {'path': '/', 'expires': 365});
        location.reload(true);
        return true;
     });
    }


});