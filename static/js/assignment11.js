
function getUsers(){
    var id_userInput = document.getElementById('id').value;
    fetch(`https://reqres.in/api/users/${id_userInput}`).then
    (
        response => response.json()
    ).then
    (
        response_obj => put_users_html(response_obj.data)
    ).catch
    (
        err=>console.log(err)
    )
}

function put_users_html(response_obj_data) {
    console.log(response_obj_data);
    const curr_main = document.querySelector("main");
      while (curr_main.firstChild) {
        curr_main.removeChild(curr_main.lastChild);}
    const section = document.createElement('section');
            section.innerHTML = `
        <img src="${response_obj_data.avatar}" alt="Profile Picture"/>
        <div>
               <span>${response_obj_data.first_name} ${response_obj_data.last_name}</span>
               <br>
               <a href="mailto:${response_obj_data.email}"> Send Email</a>
        </div>
        `;
            curr_main.appendChild(section);
}



