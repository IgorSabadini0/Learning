/**
 * Exercício 2: Números Primos
*! O objetivo:
** Crie uma função chamada verificarPrimo(n).
** Ela deve retornar true se o número for primo e false se não for.
*? Regra: Números primos são divisíveis apenas por 1 e por eles mesmos (e devem ser maiores que 1).
*todo Desafio adicional: Se o número não for primo, faça a função retornar qual é o próximo número primo depois dele.
 */

const verificarPrimo = (n) => {
    if (n <= 1) {
        return false
    }
    for (let i = 2; i < n; i++) {
        if (n % i === 0) {
            return false
        }
    }
    return true
}

console.log(verificarPrimo(6))