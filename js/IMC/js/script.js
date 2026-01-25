function imc() {
    let peso = prompt('Qual seu peso');
    let altura = prompt('Qual sua altura em CM');
    let imc = peso / ((altura / 100) ** 2);
    document.getElementById('imc').innerText = 'Seu IMC é: ' + imc;

    if (imc < 18.5) {
        document.getElementById('classificar').innerText = 'Sua classificação é: Abaixo do peso';
    }

    else if (imc >= 18.5 && imc <= 24.99) {

        // PARA REALIZAR DUAS COMPARAÇÕES, USAMOS "E" (&&) EM JS.

        document.getElementById('classificar').innerText = 'Sua classificação é: Normal';
    }

    else if (imc >= 25 && imc <= 29.99) {
        document.getElementById('classificar').innerText = 'Sua classificação é: Sobrepeso';
    }

    else {
        document.getElementById('classificar').innerText = 'Sua classificação é: Obesidade'
    }
}