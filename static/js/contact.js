(function ($) {
    'use strict';

    var form = $('.contact__form'),
        message = $('.contact__msg'),
        form_data;

    // Success function
    function done_func(response) {
        message.fadeIn().removeClass('alert-danger').addClass('alert-success');
        message.text(response);
        setTimeout(function () {
            message.fadeOut();
        }, 2000);
        form.find('input:not([type="submit"]), textarea').val('');
    }

    // fail function
    function fail_func(data) {
        message.fadeIn().removeClass('alert-success').addClass('alert-danger');
        message.text(data.responseText);
        setTimeout(function () {
            message.fadeOut();
        }, 2000);
    }
    
    form.submit(function (e) {
        e.preventDefault();
        form_data = $(this).serialize();

        var csrftoken = $('[name=csrfmiddlewaretoken]').val();

        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: form_data,
            dataType: 'json',
            headers: {
                'X-CSRFToken': csrftoken
            }
        })
        .done(function (response) {
            var text = response && response.success ? response.success : response;
            done_func(text);
        })
        .fail(fail_func);
    });
    
})(jQuery);