// O Desafio do Desenvolvedor Júnior (Manipulação de Arrays/Listas)
// Cenário: Você está organizando uma lista de IDs de clientes, mas alguns IDs acabaram saindo duplicados no banco de dados.

// Tarefa: Crie uma função que receba uma lista de números e retorne uma nova lista apenas com os números únicos, sem repetições.

// Exemplo de entrada: [10, 22, 10, 3, 5, 22, 11]

// Saída esperada: [10, 22, 3, 5, 11]

// Dica de entrevista: Tente resolver isso de duas formas: uma usando um laço de repetição (for) e outra usando uma estrutura de dados específica que não aceita duplicatas (como o Set no JS ou Python).

const numeros_sem_duplicatas = (lista) => [...new Set(lista)]

console.log(numeros_sem_duplicatas([10, 22, 10, 3, 5, 22, 11]))