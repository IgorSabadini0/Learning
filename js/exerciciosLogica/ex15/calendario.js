// Cenário: O escritório de advocacia onde você trabalha quer automatizar a triagem de processos baseada na urgência.
// Tarefa: Escreva uma função que receba o número de dias que um processo está parado e retorne a categoria dele:
// Menos de 5 dias: "Regular"
// De 5 a 10 dias: "Atenção"
// Mais de 10 dias: "Urgente"
// Se o número for negativo: Deve retornar "Entrada Inválida".

const categoria_processos = (dias) => {
    if (dias < 0) {
        return 'Entrada Inválida';
    }
    else if (dias < 5) {
        return 'Regular';
    }
    else if (dias >= 5 && dias <= 10) {
        return 'Atenção';
    }
    else if (dias > 10) {
        return 'Urgente';
    }
}