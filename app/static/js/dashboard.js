const listado = document.querySelector("ul");

async function insertNote(){
    
    let id= Math.random().toString(36).substring(5);

    const nota = document.createElement("li");
    nota.id = "n"+id;
    nota.innerHTML = "<a href='#'><h2>Title #1</h2><p>Text Content #1</p></a>";
    nota.addEventListener("click", ()=>{removeNote(nota.id)});
    listado.appendChild(nota);
    return ;
}

async function removeNote(id){
    
    const child = document.querySelector("#"+id);

    child.remove();

    return ;
}
