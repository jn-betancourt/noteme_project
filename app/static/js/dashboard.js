const body = document.querySelector(".hero-body");


async function insertNote(){

    var centeredDivAncestor = document.createElement('div');
    centeredDivAncestor.className = "container has-text-centered";
    centeredDivAncestor.id = "container";
    body.insertAdjacentElement("afterbegin", centeredDivAncestor);

    var centeredDiv = document.createElement('div');
    centeredDiv.className = "column is-4 is-offset-4";
    centeredDivAncestor.insertAdjacentElement("afterbegin", centeredDiv);


    var html = document.createElement("div");
    html.className = "hero is-info box";
    html.innerHTML = "<form method='POST'><label for='title'>Title<br></label><input type='text' name='title'><br><label for='description'>Description</label><br><input type='text' id='description' name='description'><br><br><input type='submit' value='Save'></form>";
    centeredDiv.insertAdjacentElement("afterbegin", html);

    return;
}