// 01. Você e seu time estão desenvolvendo um sistema de indicações de postos de gasolina que ficam próximos da localização atual do veículo. No modo de direção “viagem”, a funcionalidade a ser desenvolvida é de indicar ao condutor o posto mais distante possível dentro do limite atual de combustível. E caso não exista posto de gasolina, retornar -1;

function viagem(consumo, combustivel, postos) {
  let distanciaPossivel = consumo * combustivel;
  let postoMaisDistante = -1;

  for (let posto of postos) {
    if (posto <= distanciaPossivel && posto > postoMaisDistante) {
      postoMaisDistante = posto;
    };
  };

  return console.log(postoMaisDistante);
};

viagem(2, 60, [12, 80, 50, 10]);