// A senha é representada por um número binário de 10 dígitos formado pelo dígito predominante de cada coluna. Caso a coluna tenha a mesma quantidade de dígitos 0 e 1, deve se considerar o número 1.

// Exemplo: A primeira coluna da lista tem como dígito predominante o número 1, sendo assim, o primeiro dígito - dos 10 - da senha é 1.

// 0110100000
// 1001011111
// 1110001010
// 0111010101
// 0011100110
// 1010011001
// 1101100100
// 1011010100
// 1001100111
// 1000011000

// Desenvolva um algoritmo que receba um array de valores binários (como o exemplo acima) e retorne a representação decimal da senha.

let lista_binario = [
    "0110100000",
    "1001011111",
    "1110001010",
    "0111010101",
    "0011100110",
    "1010011001",
    "1101100100",
    "1011010100",
    "1001100111",
    "1000011000"
]

let digito_coluna;

function senhaBinarioParaDecimal() {
    for (let i = 0; i < lista_binario[0].length; i++) { // Percorre as colunas do array
        let qtd1 = 0;
        let qtd0 = 0;
        for (let j = 0; j < lista_binario.length; j++) { // Percorre os digitos de cada item do array
            digito_coluna = lista_binario[j][i]
            console.log(`${j + 1}º Digito Coluna ${i + 1}: ${digito_coluna}`)
        }
    }
}

senhaBinarioParaDecimal()