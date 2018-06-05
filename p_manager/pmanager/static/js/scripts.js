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

//------- Experiencia---------------

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
    $.ajax({
        type: 'GET',
        url: 'pmanager/experienceform',
        dataType: 'json',
        data:{id:$(this).attr('id')},
        beforeSend: function () {
            $("#modal_exp").modal("show");
        },
        success: function (data) {
            $("#modal_exp .modal-content").html(data.html_form);
        },
    });
});

$('.delete_exp').on('click', function () {
    console.log($(this).attr('id'))
    $.ajax({
        type: 'DELETE',
        url: 'pmanager/experienceform',
        dataType: 'json',
        data:{'id':$(this).attr('id')},
    });
    window.location.reload(true);
});

//------- Educação---------------

$('#add_ed').on('click', function () {
    $.ajax({
        type: 'GET',
        url: 'pmanager/educationform',
        dataType: 'json',
        beforeSend: function () {
            $("#modal_ed").modal("show");
        },
        success: function (data) {
            $("#modal_ed .modal-content").html(data.html_form);
        },
    });
});
$('.edit_ed').on('click', function () {
    $.ajax({
        type: 'GET',
        url: 'pmanager/educationform',
        dataType: 'json',
        data:{id:$(this).attr('id')},
        beforeSend: function () {
            $("#modal_ed").modal("show");
        },
        success: function (data) {
            $("#modal_ed .modal-content").html(data.html_form);
        },
    });
});

$('.delete_ed').on('click', function () {
    $.ajax({
        type: 'DELETE',
        url: 'pmanager/educationform',
        dataType: 'json',
        data:{'id':$(this).attr('id')},
    });
    window.location.reload(true);
});

//------- Contato---------------

$('#add_ct').on('click', function () {
    $.ajax({
        type: 'GET',
        url: 'pmanager/contatoform',
        dataType: 'json',
        beforeSend: function () {
            $("#modal_ct").modal("show");
        },
        success: function (data) {
            $("#modal_ct .modal-content").html(data.html_form);
        },
    });
});
$('.edit_ct').on('click', function () {
    $.ajax({
        type: 'GET',
        url: 'pmanager/contatoform',
        dataType: 'json',
        data:{id:$(this).attr('id')},
        beforeSend: function () {
            $("#modal_ct").modal("show");
        },
        success: function (data) {
            $("#modal_ct .modal-content").html(data.html_form);
        },
    });
});

$('.delete_ct').on('click', function () {
    $.ajax({
        type: 'DELETE',
        url: 'pmanager/contatoform',
        dataType: 'json',
        data:{'id':$(this).attr('id')},
    });
    window.location.reload(true);
});