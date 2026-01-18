let valor_primeiro_dia = Number(1);
let valor_ultimo_dia = Number(365);
let dias = Number(365);

let total = ((valor_primeiro_dia + valor_ultimo_dia) * dias)  / 2

console.log(`O valor final é de ${total.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})}`);