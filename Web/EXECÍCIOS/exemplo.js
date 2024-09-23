// Função para gerar um número aleatório entre 1 e 100
function gerarNumeroAleatorio() {
    return Math.floor(Math.random() * 100) + 1;
}

// Função para o computador adivinhar o número escolhido pelo jogador
function adivinharNumero(jogadorNumero) {
    let min = 1;
    let max = 100;
    let tentativas = 0;
    let numeroAdivinhado;

    do {
        numeroAdivinhado = Math.floor((max + min) / 2);
        tentativas++;

        if (numeroAdivinhado === jogadorNumero) {
            console.log('O computador adivinhou o número ' + jogadorNumero + ' em ' + tentativas + ' tentativas!');
            return;
        } else if (numeroAdivinhado < jogadorNumero) {
            min = numeroAdivinhado + 1;
        } else {
            max = numeroAdivinhado - 1;
        }
    } while (true);
}

// Gerar um número aleatório escolhido pelo jogador
const jogadorNumero = gerarNumeroAleatorio();

// Computador tenta adivinhar o número escolhido pelo jogador
adivinharNumero(jogadorNumero);
