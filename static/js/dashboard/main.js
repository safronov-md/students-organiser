$.getJSON('http://0.0.0.0:8000/init', function(data) {
    let timeSheetKeys = Object.keys(data['time_sheet']);
    //$('#table_body').append('<tr><td>HESOS</td></tr>');
    for (let i = 0; i<timeSheetKeys.length; i++){
        $('#table_body').append('<tr id="row_'+i+'"><td class="align-middle">'+timeSheetKeys[i]+'</td></tr>');
        let intervalKeys = Object.keys(data['time_sheet'][timeSheetKeys[i]])
        for (let j=0; j<intervalKeys.length; j++){
            let day = data['time_sheet'][timeSheetKeys[i]][intervalKeys[j]];
            for(let k=0;k<day.length;k++){
                console.log(day[k]);
                if(day[k]['title'] !== ""){
                    $("#row_"+i).append('' +
                        '<td><span class="badge-primary padding-5px-tb padding-15px-lr border-radius-5 margin-10px-bottom text-white font-size16  xs-font-size13">' +
                        ''+day[k]['title']+'</span>' +
                        '<div class="margin-10px-top font-size14">Door 412</div>\n' +
                        '                                                    <div class="font-size13">Marta Healy</div></td>');
                }else{
                    $("#row_"+i).append('<td class="bg-light-gray"></td>');

                }
            }
        }
    }
});