$('#pagination').pagination({
        dataSource: [1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14,15,16,17],
        callback: function(data, pagination) {
            // template method of yourself
            var dataHtml = '<ul>';

            $.each(data, function (index, item) {
                dataHtml += '<li>' + item.number + '</li>';
            });

            dataHtml += '</ul>';

            $("#container").html(dataHtml);
        }
    })