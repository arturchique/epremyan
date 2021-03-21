'use strict'

$(document).ready(function(){
    $('#form').on('submit',(function(e) {
        e.preventDefault();
        var formData = new FormData($('#form')[0]);

        $.ajax({
            type:'POST',
            url: $(this).attr('action'),
            data:formData,
            cache:false,

            contentType: false,
            processData: false,
            success:function(data){
                console.log("Завершилось успешно");
                console.log(data);
                $('.message').text("Фотография успешно загружена, проверьте почту, на нее пришло оповещение")
            },
            error: function(data){
                console.log("Завершилось с ошибкой");
                console.log(data);
                $('.message').text("Ошибка. Попробуйте обновить страницу и повторить действие.")
            }
        });
    }));
});