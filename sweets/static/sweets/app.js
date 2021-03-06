function modal() {
    $("#modal-trigger").animatedModal({
        modalTarget:'js-modal',
        animatedIn:'lightSpeedIn',
        animatedOut:'bounceOutDown',
        color:'#3498db',
        // Callbacks
        beforeOpen: function() {
            console.log("The animation was called");
        },
        afterOpen: function() {
            console.log("The animation is completed");
        },
        beforeClose: function() {
            console.log("The animation was called");
        },
        afterClose: function() {
            console.log("The animation is completed");
        }
    });
}

function main() {
    $('.sweets__item').hover(function() {
        $(this).find('.sweets__item-image').css({"filter": "brightness(20%)"});
        $(this).find('.sweets__item-star').toggleClass('hide');
        $(this).find('.sweets__item-rating').toggleClass('hide');
        $(this).find('.sweets__item-expander').toggleClass('hide');
        $(this).find('.sweets__item-delete-button').toggleClass('hide');
    }, function() {
        $(this).find('.sweets__item-image').css({"filter": "brightness(100%)"});
        $(this).find('.sweets__item-star').toggleClass('hide');
        $(this).find('.sweets__item-rating').toggleClass('hide');
        $(this).find('.sweets__item-expander').toggleClass('hide');
        $(this).find('.sweets__item-delete-button').toggleClass('hide');
    });

    modal();
}

$(document).ready(main());