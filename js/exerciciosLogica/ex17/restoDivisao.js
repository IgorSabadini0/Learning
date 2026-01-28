// 3. O Desafio "Tech Lead" (Lógica de Algoritmo - FizzBuzz adaptado)
// Cenário: Este é um clássico de entrevistas para testar se o candidato entende o conceito de resto da divisão e precedência de condições.
// Tarefa: Escreva um programa que percorra os números de 1 a 30.
// Para números múltiplos de 3, imprima "Tech".
// Para números múltiplos de 5, imprima "Law".
// Para números que são múltiplos de 3 e 5 ao mesmo tempo, imprima "TechLaw".
// Para os outros números, imprima o próprio número.

for (let i = 1; i <= 30; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        console.log(i, 'TechLaw')
    }
    else if (i % 3 === 0) {
        console.log(i, 'Tech');
    }
    else if (i % 5 === 0) {
        console.log(i, 'Law')
    }
    else {
        console.log(i)
    }
}