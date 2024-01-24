# WLGen-Py
### Gerador de Wordlist

Este é um script Python para gerar uma wordlist (lista de palavras) personalizada. Ele permite que você insira várias palavras e gera várias variações dessas palavras, substituindo certos caracteres e adicionando sequências numéricas. Cada palavra é única e não se mistura com alguma outra digitada, assim você pode criar uma wordlist com combinações de diversas palavras em um só arquivo.

Para ficar mais claro, veja como funciona abaixo.

## Como funciona

O script usa a função `maketrans` da classe `str` do Python para criar várias tabelas de tradução. Cada tabela mapeia um conjunto de caracteres para outro conjunto. Por exemplo, a primeira tabela mapeia 'aioO' para '@100'. O script então usa essas tabelas para substituir caracteres nas palavras de entrada e gerar variações.

Na prática, o que estamos fazendo é criando variações da palavra fornecida. Como substituindo letras por caracteres especiais parecidas, como por exemplo trocar um `S` da palavra fornecida por um `$`, ou um `A` por `@` ou um `4`, e por aí vai.

Até aqui teremos uma lista que pega qualquer palavra digitada e a deixa de várias formas diferentes, mas podemos escolher mais coisa para ser feito.

Podemos colocar, por exemplo, um ano que virá após as palavras geradas também. Isto é, estamos gerando novas combinações que agora usam números (Obs: É necessário utilizar o Modo Simples ao escolher uma sequência numéria, por exemplo, para colocar um ano específico). 

Até aqui, temos palavras geradas de diversas formas de escrita e as mesmas seguidas de sequência numéria. 

Agora, caso a ideia seja criar uma wordlist que utilize essas palavras geradas com números aleatórios antes ou depois de cada palavra, podemos fazer assim também.

Por isso temos a opção dos modos de uso.

No modo simples, o script utiliza a sequência numérica para incrementar a wordlist - que pode ter sido digitada ou não -, colocando-a sempre após a variação da palavra.

No modo avançado, o script gera números aleatórios para cada variação de palavra, em vez de usar a sequência numérica fixa - que pode ter sido digitada ou não.

## Como usar

1. Execute o script Python.
2. Quando solicitado, digite uma palavra e pressione Enter. Você pode digitar quantas palavras quiser. Quando terminar, pressione Enter.
3. Digite uma sequência numérica quando solicitado, ou deixe em branco para não usar uma sequência numérica *(principalmente caso queira o aleatório do avançado)*.
4. Escolha o modo de execução: '1' para Modo Simples ou '2' para Modo Avançado.
5. O script irá gerar a wordlist e salvar em um arquivo chamado 'wordlist.txt'.

## Exemplo

Vamos supor que você insira a palavra 'senha' e escolha o Modo Avançado. O script irá gerar variações como 'senha1234', '1234senha', 'senha@5678', '5678@senha', e assim por diante.

## Nota

Este script foi escrito para Python 3. Certifique-se de ter Python 3 instalado em seu sistema antes de executar o script.

