
const readline = require('readline');

// Cria uma interface para entrada/saída
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Gera um número aleatório entre 1 e 100
const numeroAleatorio = Math.floor(Math.random() * 100) + 1;

// Variável para armazenar o número de tentativas
let numeroTentativas = 0;

// Função para verificar se o número digitado é correto
function verificarNumero(numeroDigitado) {
    numeroTentativas++;

    if (numeroDigitado === numeroAleatorio) {
        console.log(`Parabéns! Você acertou o número em ${numeroTentativas} tentativa(s).`);
        rl.close();
    } else if (numeroDigitado < numeroAleatorio) {
        console.log('Tente um número maior.');
        fazerJogada();
    } else {
        console.log('Tente um número menor.');
        fazerJogada();
    }
}

// Função para fazer uma jogada
function fazerJogada() {
    rl.question('Digite um número: ', (numeroDigitado) => {
        verificarNumero(parseInt(numeroDigitado));
    });
}

// Inicia o jogo
fazerJogada();
