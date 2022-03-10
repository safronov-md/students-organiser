function tagAsInput(element_id) {
    let element = document.getElementById(element_id);
    element.click()
}

function setActive(page){
    let elements = document.getElementsByClassName('nav-item');
    for(let i = 0; i<elements.length; i++){
        elements[i].classList.remove('active');
    }
    let menuEl = document.getElementById(page);
    menuEl.classList.add('active');
}

function editIssue(id){
    let desc = document.getElementById('desc_'+id+'_edit'); // TextArea of description
    desc.removeAttribute('hidden');
    document.getElementById('desc_'+id+'_text').setAttribute('hidden', 'true'); // Text of description
    document.getElementById('form_'+id+'_edit').setAttribute('hidden', 'true')
    document.getElementById('form_'+id+'_save').removeAttribute('hidden');
    document.getElementById('date_'+id+'_text').setAttribute('hidden', 'true')
    document.getElementById('date_'+id+'_edit').removeAttribute('hidden');
}

var csrfcookie = function() {
    var cookieValue = null,
        name = 'csrftoken';
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};
function saveIssue(i_id, link){
    let desc = document.getElementById('desc_'+i_id+'_edit'); // TextArea of description
    desc.setAttribute('hidden', 'true');
    document.getElementById('desc_'+i_id+'_text').removeAttribute('hidden');
    document.getElementById('desc_'+i_id+'_text').innerHTML=desc.value;
    document.getElementById('form_'+i_id+'_save').setAttribute('hidden', 'true');
    document.getElementById('form_'+i_id+'_edit').removeAttribute('hidden');
    document.getElementById('date_'+i_id+'_edit').setAttribute('hidden', 'true');
    document.getElementById('date_'+i_id+'_text').removeAttribute('hidden');
    let request = new XMLHttpRequest();
    request.open('POST', link, true);
    request.setRequestHeader('Content-Type', 'application/json');
    request.setRequestHeader('X-CSRFToken', csrfcookie());
    request.send(JSON.stringify({
        id: i_id,
        desc: desc.value,
        deadline: document.getElementById('date_'+i_id+'_edit').value
    }));
    request.onreadystatechange = function () {
        try {
            let data = JSON.parse(request.responseText);
            document.getElementById('date_' + i_id + '_text').innerHTML = data['date'];
        }catch{
            document.getElementById('date_' + i_id + '_text').innerHTML = 'None'
        }
    }
}

function changeStatus(event, link){
    status_id = event.target.id.replace('status_','');
    link+='?id='+status_id+'&status='+event.target.checked;
    const xhr = new XMLHttpRequest();
    xhr.open("GET", link);

    xhr.setRequestHeader("Accept", "*/*");
    xhr.send()
}
function editSchedule(){
    let elements = document.getElementsByClassName('meet_link');
    for(let i = 0; i<elements.length; i++){
        elements[i].removeAttribute('hidden');
    }
    let editButton = document.getElementById('editButton');
    editButton.setAttribute('onclick', 'closeEdit();');
    editButton.innerHTML = "<span class='text'>Close</span>";
}

function closeEdit(){
    let elements = document.getElementsByClassName('meet_link');
    for(let i = 0; i<elements.length; i++){
        elements[i].setAttribute('hidden', 'true');
    }
    let closeButton = document.getElementById('editButton');
    closeButton.setAttribute('onclick', 'editSchedule();');
    closeButton.innerHTML = "<span class='text'>Edit</span>";
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
