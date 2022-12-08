frases = {
    'reiniciado': 'Jogo reiniciado (progresso do jogador apagado).',
    'saindo': 'Saindo.',
    'canal_privado': 'Não é possível reproduzir áudio em canais privados.',
    'sem_canal_de_voz': 'Por favor, esteja em um canal de voz para ter a imersão completa do jogo.',
    'erro': 'Erro.'
}

# Dicionário com as definições da máquina de estados do jogo.
# As opções dos jogadores são definidas como expressões regulares.
estados = {
    0: {
        'frases': ['Digite "iniciar" para começar o jogo.'],
        'proximos_estados': {
            '[iI]niciar?': 1
        }
    },
    1: {
        'frases': ['Bem-vindo(a) ao caixa de memórias! Um jogo sobre uma jovem que não conhece a mãe, pois foi separada dela em um campo de concentração e criada pela avó paterna, o pai morreu no campo de concentração.\nA avó morre quando Clarice, a protagonista, completa 19 anos. Então, já na maioridade, ela viaja para a Alemanha, onde reencontra a antiga casa da família, lá, o novo morador entrega a ela uma caixa que uma amiga da mãe deixou na casa após voltar do campo de concentração. Você deseja ajudá-la a descobrir os mistérios existentes na caixa?'],
        'proximos_estados': {
            '[sS]i+m': 2,
            '[nN][aã]+o': 3
        }
    },
    2: {
        'frases': ['Olá, que bom que você aceitou continuar, relembrando: temos uma caixa em mãos, e precisamos descobrir o que há dentro dela.\n Então, ao abri-la, você se depara com alguns objetos enigmáticos, o que mais te chama a atenção é uma carta, que contém uma assinatura, porém, a carta se encontra em um estado deteriorado em decorrência do tempo, então, ela está repartida em 4 pedaços. Para descobrir o conteúdo da assinatura, é necessário juntar esses pedaços de forma correta. Envie a sequência correspondente à ordem correta das partes.'],
        'proximos_estados': {
            '4[ ,]*3[ ,]*2[ ,]*1': 4,
            '.+': 5
        }
    },
    3: {
        'frases': ['Bye'],
        'proximos_estados': {
            '[rR]einicia(r)*': 1
        }
    },
    4: {
        'frases': ['Com a carta completa conseguimos descobrir o nome da mãe de Clarice, que escreve a carta contando sobre sua situação antes de ser capturada e assina como: Poliana Becker.\n Além disso, na caixa encontramos uma cruzadinha quase toda respondida que vamos tentar resolver. Tente completar a cruzadinha acima.'],
        'proximos_estados': {
            '[Hh]olocausto': 6,
            '.+': 7
        }
    }, 
    5: {
        'frases': ['Que pena! Você errou, tente novamente!'],
        'proximos_estados': {
            '.+': 5,
            '4[ ,]*3[ ,]*2[ ,]*1': 4
        }
    },
    6: {
        'frases': ['Com a cruzadinha descobrimos que a mãe de Clarice foi enviada ao campo de concentração de Auschwitz e as palavras da cruzadinha nos mostram a situação terrível que as pessoas viviam lá.\n\nAo revirar um pouco mais a caixa Clarice encontra um jornal datado do fim da guerra que traz uma notícia, que retrata um encontro de sobreviventes de Auschwitz organizado por uma mulher judia Poliana Becker (que agora sabemos que é a mãe de Clarice) que aconteceu em uma sinagoga e deve ser repetir a cada 10 anos.\nPor coincidência esse encontro deve ocorrer no dia seguinte e Clarice poderia comparecer para conhecer sua mãe, mas não sabe o nome dessa sinagoga onde acontece o encontro.\nContudo, ainda há um item na caixa que ao abrir ela descobre ser um caça-palavras e decide resolver.'],
        'proximos_estados': {
            '[Nn]ova [Ss]inagoga': 9,
            '.+' : 10
        }
    },
    7: {
        'frases': ['Você errou, tente novamente!'],
        'proximos_estados': {
            '.+': 7,
            '[Hh]olocausto': 6
        }
    },
    9: {
        'frases': ['Curiosidade historica: A Neue Synagoge ou Nova Sinagoga, localizada na Oranienburger Strasse, tem um grande significado e importância na história dos judeus em Berlim e, juntamente com o Museu Judaico e o Memorial do Holocausto, é também um dos principais marcos judaicos na cidade.\nO caça-palavras revela o nome da sinagoga e isso permite que Clarice possa ir ao evento com esperança de encontrar sua mãe, que até esse momento ela acreditava não ter sobrevivido ao holocausto. No dia seguinte ao chegar na sinagoga ela aproveita a comemoração e logo antes de desistir e ir embora é apresentada para a organizadora do evento Poliana Becker, sua mãe. Sua mãe não reconhece ela de primeira, mas ao ouvir a história abraça a filha emocionada e conta que apenas não procurou Clarice depois da guerra, pois acreditava que ela não estava viva. FIM.'],
        'proximos_estados': {
            '.+': 0
        }
    },
    10: {
        'frases': ['Você errou, tente novamente!'],
        'proximos_estados': {
            '.+': 10,
            'nova sinagoga': 9
        }
    },
}

# Dicionário com os estados correntes de cada jogador.
canais_de_voz = {}