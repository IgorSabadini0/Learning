function media() {
    let nome = document.getElementById('nome').value;

    let n1 = Number(document.getElementById('n1').value);

    let n2 = Number(document.getElementById('n2').value);

    let media = (n1 + n2) / 2;

    if (n2 > 10 || n1 > 10) {
        alert("Insira um valor menor que 10");
    } else {
        document.getElementById('media').innerText = media;
        document.getElementById('nomeLocal').innerText = nome;
        if (media >= 6) {
            document.getElementById('media').style.color = 'green';
        } else {
            document.getElementById('media').style.color = 'red';
        }
    }
}