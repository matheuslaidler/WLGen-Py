# WLGen-Py
### Gerador de Wordlist

Este é um script Python para gerar uma wordlist (lista de palavras) personalizada. Ele permite que você insira várias palavras e gera várias variações dessas palavras, substituindo certos caracteres e adicionando sequências numéricas. Cada palavra é única e não se mistura com alguma outra digitada, assim você pode criar uma wordlist com combinações de diversas palavras em um só arquivo.

Para ficar mais claro, veja como funciona abaixo.

## Como funciona

Resumidamente, neste script a criação da lista de palavras se dá ao reescrever as palavras de diversas formas diferentes, utilizando caracteres especiais e/ou números nos lugares de letras parecidas, além de poder utilizar sequências numéricas também para incrementar.

O script usa a função `maketrans` do Python para criar várias tabelas, os quais cada uma 'mapeia' um conjunto de caracteres para outro conjunto. Por exemplo, a primeira tabela mapeia 'aioO' para '@100' - ou seja, colocando 'a' para ser substituído por '@', 'i' por '1' e por aí vai -, assim o script usa essas 'tabelas' para substituir caracteres nas palavras de entrada e gerar variações da palavra digitada.

Na prática, o que estamos fazendo é criando variações de escrita da(s) palavra(s) fornecida(s) pelo usuário, substituindo letras por caracteres especiais parecidas, como por exemplo trocar um `S` da palavra fornecida por um `$`, ou um `A` por `@` - ou um `4` -, e por aí vai. Até aqui teremos uma lista que pega qualquer palavra digitada e a deixa de várias formas diferentes, porém ainda temos mais opções de combinações para ser feito de forma a incrementar a lista.

Podemos adicionar, por exemplo, essas variações de palavras geradas seguidas de um ano específico - ou um ano específico seguido dessas palavras. Assim, estamos gerando novas combinações que agora também usam sequências númericas para complementar a lista de senhas. Para utilizar esta função, é necessário utilizar o Modo Simples ao escolher a sequência numéria padrão. Até aqui, temos palavras geradas de diversas formas de escrita e as mesmas seguidas de sequência numéria. 

Existe também a ideia de criar uma wordlist que utilize números aleatórios ao invés do padrão digitado, também vindo antes ou depois de cada palavra, caso não saiba que sequência digitar. Poderá ser feito assim utilizando o Modo Avançado do script. Neste caso, não importa se você digitou ou não algo nas sequências, pois neste os números serão aleatórios e serão testados mais de uma sequência numérica. 
Até aqui, podemos ver que temos algumas opções interessantes para criação de uma lista de senhas, podendo utilizar as variações e sequências numéricas.

## Modo de uso

Podemos ver, então, que as opções interessantes se baseiam em criar uma lista de variações de palavras, com ou sem sequências numéricas padronizados ou randomizados. Para isso, temos a opção dos 'modos de uso'.

No modo simples, o script utiliza a sequência numérica para incrementar a wordlist - que pode ter sido digitada ou não -, colocando-a antes ou depois da variação de caractere.

No modo avançado, o script gera números aleatórios as variação de palavra gerada, em vez de usar a sequência numérica fixa - que pode ter sido digitada ou não.

É importante dizer que o arquivo `wordlist.txt` já gerado será sobrescrito ao reusar o script com o mesmo na pasta. O recomendado é renomear o nome da lista que desejar manter ou fazer um backup.

## Como usar o script

1. Execute o script Python (pode ser usado via IDLE ou terminal, por exemplo).
2. Quando solicitado, digite uma palavra e pressione Enter. Você pode digitar quantas palavras quiser. Quando terminar, pressione Enter novamente sem digitar mais nada.
3. Digite uma sequência numérica quando solicitado, ou deixe em branco para não usar uma sequência numérica padronizada *(principalmente caso queira o aleatório do avançado)*.
4. Escolha o modo de execução: '1' para Modo Simples ou '2' para Modo Avançado.
5. O script irá gerar a wordlist e salvar em um arquivo chamado 'wordlist.txt'.

## Exemplo

Vamos supor que você insira a palavra 'senha' e escolha o Modo Avançado. O script irá gerar variações como '$3nh4', 'senha1234', '1234senha', 'senha@5678', '5678@senha' e assim por diante.
Neste mesmo cenário tendo escolhido o Modo Simples e com o padrão numérico de `2001`, o script irá gerar variações como '$3nh4', 'senha2001','senha@2001', '2001@Senha', e assim por diante.

## Nota

Este script foi escrito para Python 3. Certifique-se de ter Python 3 instalado em seu sistema antes de executar o script.
