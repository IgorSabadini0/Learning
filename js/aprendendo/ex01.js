// Você está desenvolvendo um sistema para um e-commerce que precisa selecionar automaticamente um pedido para envio promocional.

// A regra de negócio é a seguinte:

// Você recebe uma lista de valores de pedidos (em reais).

// O setor financeiro define um limite máximo de orçamento para a promoção.

// O sistema deve escolher o pedido de maior valor possível, desde que não ultrapasse o limite.

// Se nenhum pedido estiver dentro do limite, o sistema deve retornar -1.

function e_commerce(pedidos, limite_orcamento) {
    let limite = -1

    for (let pedido of pedidos) {
        if (pedido < limite_orcamento && pedido > limite) {
            limite = pedido
        }
    }
    console.log(limite)
}

e_commerce([50, 43, 25, 76, 83], 60)