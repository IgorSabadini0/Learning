/*
* * DESAFIO: O Carregamento do Caminhão
 * * OBJETIVO:
 * * Calcular o peso total e a quantidade de caixas válidas para transporte.
 * * REGRAS:
 * 1. O peso deve estar entre 10 e 100 (inclusive).
 * 2. Ignorar caixas com peso 0 ou fora do intervalo.
 * 3. Entrada: Lista de paletes (ex: [[20, 10], [50, 200]])
 * 4. Saída: Um array [pesoTotal, quantidadeDeCaixas]
 */

function carregarCaminhao(paletesLista) {
    let lista = paletesLista.flat();
    let listaFiltrada = [];
    let quantidadeCaixas = 0;
    let pesoTotal = 0;

    for (let peso of lista) {
        if (peso >= 10 && peso <= 100) {
            listaFiltrada.push(peso);
            pesoTotal += peso;
        }
    }

    quantidadeCaixas = listaFiltrada.length;

    return [pesoTotal, quantidadeCaixas];
}

console.log(carregarCaminhao([[20, 10], [50, 200]]));