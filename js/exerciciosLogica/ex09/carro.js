// A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
// um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
// quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
// sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

const input = require('prompt-sync')(); //Necessário ter a biblioteca prompt-sync (npm install prompt-sync) dentro do projeto.

let km_percorridos = input("Digite a distancia em KM percorridos: ");
let dias_alugados = input("Digite a quantidade de dias alugados: "); 
const VALOR_DIA = Number(90);
const VALOR_KM = Number(0.2);
let preco_km = km_percorridos * VALOR_KM;
let preco_dia = dias_alugados * VALOR_DIA;

let total = preco_dia + preco_km;
console.log(`O valor total foi de ${total.toFixed(2).replace('.',',')}`);