function tagAsInput() {
    let element = document.getElementById("add_file");
    element.click()
}

function getStoredFiles(url,type){
    url = url.slice(0,-1)
    url+='?type='+type;
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url);

    xhr.setRequestHeader("Accept", "*/*");

    xhr.onreadystatechange = function () {
       if (xhr.readyState === 4) {
          let storedFiles = document.getElementById('stored_files');
           let response = JSON.parse(xhr.responseText);
           for (let i = 0;i<response['files'].length;i++) {
               storedFiles.innerHTML+=
                   '<a target="_blank" class="nav-link" href="'+response['files'][i]["destination"]+'">\n' +
                   '                      <ion-icon name="document-outline"></ion-icon>\n' +
                   response['files'][i]["name"] +
                   '                    </a>' +
                   '<a href="/store/remove_file?id=' + response["files"][i]["id"]+'"><ion-icon name="remove-circle-outline"></ion-icon></a>\n';
           }
       }};
    xhr.send()
}
