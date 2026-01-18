function contasOperacionais(operacao, n1, n2) {
    console.log(`Qual operação deseja realizar: `)
    console.log(`[+] - Soma`)
    console.log(`[-] - Subtraçao`)
    console.log(`[*] - Multiplicação`)
    console.log(`[/] - Divisão`)

    if (operacao === '*') {
        console.log(`${n1} * ${n2} = ${n1 * n2}`)
    } else if (operacao === '+') {
        console.log(`${n1} + ${n2} = ${n1 + n2}`)
    } else if (operacao === '-') {
        console.log(`${n1} - ${n2} = ${n1 - n2}`)
    } else if (operacao === '/') {
        if (n2 === 0) {
            console.log(`A divisão por ZERO é impossível`)
        } else {
            console.log(`${n1} / ${n2} = ${n1 / n2}`)
        }
    } else {
        console.log(`Operação INVÁLIDA`)
    }
}

contas('/', 8, 0)