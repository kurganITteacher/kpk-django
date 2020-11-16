window.onload = function () {
    console.log("DOM loaded");
    $('.basket li a').on('click', function (event) {
        event.preventDefault();
        // console.log(event.target.href);
        $.ajax({
            url: event.target.href,
            success: function (data) {
                // console.log('response', data);
                $('.basket-item-' + data.course_basket_id).remove();
            }
        })
    })
}