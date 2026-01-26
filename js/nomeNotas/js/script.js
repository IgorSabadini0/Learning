function media() {
    let nome = document.getElementById('nome').value;

    let n1 = parseFloat(document.getElementById('n1').value);

    let n2 = parseFloat(document.getElementById('n2').value);

    let media = (n1 + n2) / 2;

    if (n2 > 10 || n1 > 10 || n1 < 0 || n2 < 0) {
        alert("Insira um valor correto");
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