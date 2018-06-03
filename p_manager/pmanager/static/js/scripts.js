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
        url: 'pmanager/skillsform',
        dataType: 'json',
        beforeSend: function () {
            $("#modal-book").modal("show");
        },
        success: function (data) {
            $("#modal-book .modal-content").html(data.html_form);
        },
    });
});

$('#add_exp').on('click', function () {
    $.ajax({
        type: 'GET',
        url: 'pmanager/experienceform',
        dataType: 'json',
        beforeSend: function () {
            $("#modal_exp").modal("show");
        },
        success: function (data) {
            $("#modal_exp .modal-content").html(data.html_form);
        },
    });
});
$('.edit_exp').on('click', function () {
    console.log($('.edit_exp').attr('id'))
    $.ajax({
        type: 'POST',
        url: 'pmanager/experienceform',
        data:{id:$('.edit_exp').attr('id')}
    });
    $.ajax({
        type: 'GET',
        url: 'pmanager/experienceform',
        dataType: 'json',
        beforeSend: function () {
            $("#modal_exp").modal("show");
        },
        success: function (data) {
            $("#modal_exp .modal-content").html(data.html_form);
        },
    });
});