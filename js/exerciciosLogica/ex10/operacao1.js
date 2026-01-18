console.log(`Qual operação deseja realizar: `)
console.log(`[+] - Soma`)
console.log(`[-] - Subtraçao`)
console.log(`[*] - Multiplicação`)
console.log(`[/] - Divisão`)

function contasOperacionais(operacao, n1, n2) {

    let resultado

    if (operacao === '/' && n2 === 0) {
        throw new Error('Impossível dividir por ZERO')
    }
    else if (operacao === '+') {
        resultado = n1 + n2
    }
    else if (operacao === '-') {
        resultado = n1 - n2
    }
    else if (operacao === '*') {
        resultado = n1 * n2
    }
    else if (operacao === '/') {
        resultado = n1 / n2
    } else {
        throw new Error('Operação Inválida')
    }

    return resultado
}

contasOperacionais('/', 4, 2)