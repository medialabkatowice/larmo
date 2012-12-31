;(function ($) {
    $(document).ready(function () {
        $('body').imagesLoaded(function () {
            $('.main').each(function () {
                var main_h = $(this).outerHeight();
                $(this).next().outerHeight(main_h);
            });
        })
    });
//        var loaded_counter = 0;
//        var img_len = $('img').length;
//
//        $('img').load(adjust_background);
//
//        function adjust_background() {
//            loaded_counter += 1; 
//
//            if(loaded_counter === img_len) {
//                $('.main').each(function () {
//                    var main_h = $(this).outerHeight();
//                    $(this).next().outerHeight(main_h);
//                });
//            }
//        }
//    });
})(jQuery);
