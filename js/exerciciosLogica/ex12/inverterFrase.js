//* 1. Inversão de Sentenças (Médio)
//todo: Crie uma função que receba uma string contendo várias palavras e retorne a mesma string, mas com a ordem das palavras invertida, mantendo os espaços originais. Não vale usar o método .reverse() diretamente no array de palavras.
//? Entrada: "O céu é azul"
//? Saída: "azul é céu O"

function inverter(palavras) {
    const palavrasString = palavras.split(' ') //? Dentro das aspas vai um ESPAÇO para indicar que as palavras do array serão separadas por um espaço.

    const quantidadePalavras = palavrasString.length;
    let palavrasInvertidas = [];
    for (let i = quantidadePalavras - 1; i >= 0; i--) {
        palavrasInvertidas.push(palavrasString[i]);
    }
    return palavrasInvertidas;
}
console.log(inverter('o ceu é azul'));