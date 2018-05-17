jQuery(function ($) {

    'use strict';

    // --------------------------------------------------------------------
    // PreLoader
    // --------------------------------------------------------------------

    (function () {
        $('#preloader').delay(200).fadeOut('slow');
    }());



    // --------------------------------------------------------------------
    // Sticky Sidebar
    // --------------------------------------------------------------------

    $('.left-col-block, .right-col-block').theiaStickySidebar();

}); // JQuery end

$('#edit_skills').on('click', function () {
    $.ajax({
        type: 'GET',
        url: '{% url 'skillsform' %}',
        },
        success: function (data, textStatus, jqXHR) {
            $('#foo_modal').find('.modal-body').html(data);
            $('#foo_modal').modal('show');
        },
    });
});