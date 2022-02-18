function tagAsInput() {
    let element = document.getElementById("add_file");
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

function editDescription(d_id,link){
    let desc = document.getElementById(d_id+'h');
    desc.removeAttribute('hidden');
    document.getElementById(d_id).setAttribute('hidden', 'true');
    document.getElementById(d_id+'a').innerHTML = 'Save';
    document.getElementById(d_id+'a').setAttribute('onclick', "closeEditDesc('"+d_id+"','"+link+"');");
}
function closeEditDesc(d_id, link){
    let desc = document.getElementById(d_id+'h');
    desc.setAttribute('hidden', 'true');
    document.getElementById(d_id).removeAttribute('hidden');
    document.getElementById(d_id).innerHTML=desc.value;
    document.getElementById(d_id+'a').setAttribute('onclick', "editDescription('"+d_id+"','"+link+"');");
    document.getElementById(d_id+'a').innerHTML='Edit';
    link+='?id='+d_id+'&desc='+desc.value;
    const xhr = new XMLHttpRequest();
    xhr.open("GET", link);

    xhr.setRequestHeader("Accept", "*/*");
    xhr.send();
}

function changeStatus(event, link){
    link+='?id='+event.target.id+'&status='+event.target.checked;
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
    editButton.innerHTML = 'Close';
}

function closeEdit(){
    let elements = document.getElementsByClassName('meet_link');
    for(let i = 0; i<elements.length; i++){
        elements[i].setAttribute('hidden', 'true');
    }
    let closeButton = document.getElementById('editButton');
    closeButton.setAttribute('onclick', 'editSchedule();');
    closeButton.innerHTML = 'Edit';
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
