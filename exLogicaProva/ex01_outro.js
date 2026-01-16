// Você e seu time estão desenvolvendo um sistema de indicações de pontos de recarga para carros elétricos próximos da localização atual do veículo.
// No modo de direção “viagem”, a regra é:
// O veículo está na posição 0 (início da rota).
// Você recebe uma lista de pontos de recarga, onde cada ponto é representado pela distância (em km) a partir do início (ex.: 12 significa “a 12 km do ponto atual”).
// O carro tem autonomia atual de A km (distância máxima que consegue percorrer).
// A funcionalidade deve indicar o ponto de recarga mais distante possível que ainda seja alcançável (distância <= A).
// Se não existir nenhum ponto alcançável, retorne -1.
// Se houver mais de um ponto na mesma distância, tanto faz (retorna aquela distância mesmo).
// }


function viagem(pontos_recarga, autonomia) {
    let ponto_alcancavel = -1;

    for (let ponto_recarga of pontos_recarga) {
        if (ponto_recarga <= autonomia && ponto_recarga > ponto_alcancavel) { //para verificar qual a maior distancia.
            ponto_alcancavel = ponto_recarga;
        }
    }
    console.log(`O ponto de recarga mais distante possível de ser alcançado é ${ponto_alcancavel} Km`);
}

viagem([40, 22, 53, 68, 135], 95);