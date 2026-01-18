// A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
// um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
// quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
// sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

function calcularTotalAluguelCarro(km_percorrido, dias_alugado) {
    const VALOR_DIA = 90
    const VALOR_KM = 0.2
    
    if (km_percorrido < 0 || dias_alugado < 0) {
        console.log(`Valores menores que 0 são inválidos`)
        return null
    }

    let total_km = VALOR_KM * km_percorrido
    let total_dia = VALOR_DIA * dias_alugado

    let total_aluguel = total_dia + total_km

    console.log(total_aluguel.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' }))

    return total_aluguel
}

calcularTotalAluguelCarro(250, 0)