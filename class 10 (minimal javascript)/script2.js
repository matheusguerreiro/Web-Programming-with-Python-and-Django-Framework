function mensagem() {
    alert("Aqui está a sua Mensagem!");
}

function perguntar() {
    var nome;
    nome = prompt("Qual é o seu Nome? ");
    alert("Olá, " + nome);
}

function mudartexto() {
    var h1 = document.getElementsByTagName("h1");
    if (h1[0].innerText == "O Mínimo de JavaScript") {
        h1[0].innerText = "Eu preciso Saber!";
    } else {
        h1[0].innerText = "O Mínimo de JavaScript";
    }
}

function incrementar() {
    var p1 = document.getElementById("p1");
    p1.innerText = parseInt(p1.innerText) + 1;
}