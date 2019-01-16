    function getText(data){
        var classifications = data.predicao;
        console.log(classifications);
        var retorno = "Esse review contém comentários ofensivos";

        if (classifications == "Bad")
            return retorno;
        else
            return "Ótimo! Esse é um review somente de produto!";
    }

    function checkReview() {
        $('#result').text('...');
        $('#error').text('');
        $('#comment-text').removeClass('error');
        $('#result-box').css('background', '#f8f8f8')
        $('#result-box').removeClass('hide');


        $.ajax({
            type: "POST",
            data: JSON.stringify({
                "comment": $('#comment-text').val()
            }),
            url: '/',
            contentType: "application/json; charset=utf-8",
            dataType: "JSON",
            processData: true,
            success: function (data) {
                result = getText(data);

                $('#result').text(result);
                $('#result-box').removeClass('hide');
                if(result.includes("Esse review contém comentários ofensivos"))
                    $('#result-box').css('background', '#ebd1d1');
                else
                    $('#result-box').css('background', '#d6f0cf');
            },
            error: function (data) {
                $('#comment-text').addClass('error');
                $('#error').text(data.responseJSON.comment.join(' / '));
                $('#result-box').addClass('hide');
            }
        });
    }