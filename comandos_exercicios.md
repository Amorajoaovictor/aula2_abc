# Comandos dos exercicios

Este arquivo resume os comandos usados nos exercicios da aula e explica para que cada um serve.

## Como executar um arquivo Python

Entre na pasta do projeto:

```powershell
cd aula2_abc
```

Execute um arquivo Python:

```powershell
python nome_do_arquivo.py
```

Exemplo:

```powershell
python teste.py
```

Se o comando `python` nao funcionar, tente:

```powershell
py nome_do_arquivo.py
```

## Comandos basicos usados nos exercicios

### `print()`

Mostra uma mensagem no terminal.

```python
print("Ola, mundo!")
```

Tambem pode mostrar o valor de uma variavel:

```python
nome = "Jake"
print(nome)
```

### `input()`

Recebe uma informacao digitada pela pessoa usuaria.

```python
nome = input("Digite seu nome: ")
```

O valor digitado sempre entra como texto.

### `int()`

Converte texto para numero inteiro.

```python
idade = int(input("Digite sua idade: "))
```

Use quando o valor nao precisa de casas decimais.

### `float()`

Converte texto para numero decimal.

```python
nota = float(input("Digite a nota: "))
```

Use para notas, medias, dinheiro ou qualquer numero com virgula/ponto.

### Variaveis

Guardam valores para usar depois no programa.

```python
nome = "Amy"
idade = 18
media = 7.5
```

### Operadores matematicos

Fazem calculos.

```python
soma = 8 + 6
subtracao = 8 - 6
multiplicacao = 8 * 6
divisao = 8 / 2
```

### Comparacao

Compara valores e retorna verdadeiro ou falso.

```python
idade >= 18
media < 7
```

Principais comparadores:

```python
==  # igual
!=  # diferente
>   # maior que
<   # menor que
>=  # maior ou igual
<=  # menor ou igual
```

### `if` e `else`

Servem para criar decisoes no programa.

```python
if idade >= 18:
    print("Pode participar")
else:
    print("Nao pode participar")
```

O bloco dentro do `if` roda quando a condicao e verdadeira.
O bloco dentro do `else` roda quando a condicao e falsa.

### `\n`

Cria uma quebra de linha dentro do texto.

```python
print("\nResultado final")
```

## Exercicio 1: Boletim da Delegacia 99

Comandos principais:

```python
nome = input("Digite o nome do detetive: ")
nota_teorica = float(input("Digite a nota da prova teorica: "))
nota_simulacao = float(input("Digite a nota da simulacao: "))

media = (nota_teorica + nota_simulacao) / 2

if media >= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print("Detetive:", nome)
print("Media:", media)
print("Situacao:", situacao)
```

Explicacao:

- `input()` pega o nome e as notas.
- `float()` transforma as notas em numeros decimais.
- `media = (...) / 2` calcula a media das duas notas.
- `if media >= 7` verifica se a media e suficiente para aprovar.
- `else` define o resultado quando a media for menor que `7`.
- `print()` mostra o boletim no terminal.

## Exercicio 2: Permissao para Torneio Ninja

Comandos principais:

```python
nome = input("Digite o nome do personagem: ")
idade = int(input("Digite a idade do personagem: "))

if idade >= 18:
    resultado = "Pode participar do Torneio Ninja"
else:
    resultado = "Precisa continuar treinando"

print("Personagem:", nome)
print("Idade:", idade)
print("Resultado:", resultado)
```

Explicacao:

- `input()` recebe o nome e a idade.
- `int()` transforma a idade em numero inteiro.
- `if idade >= 18` verifica se o personagem tem idade minima.
- `else` guarda a mensagem para quem ainda nao pode participar.
- `print()` exibe o resultado da inscricao.

## Exercicio 3: Setlist de Rock com `for`

Comandos principais:

```python
banda = "System Cover Down"

musicas = [
    "Grito da Cidade",
    "Caos no Palco",
    "Radio Quebrado",
    "Revolta"
]

print("Banda:", banda)
print("\nSetlist do show")

for indice in range(len(musicas)):
    numero = indice + 1
    musica = musicas[indice]
    print(numero, "-", musica)
```

Explicacao:

- `banda` guarda o nome da banda.
- `musicas` e uma lista com varias musicas.
- `len(musicas)` conta quantos itens existem na lista.
- `range(len(musicas))` cria uma sequencia de indices.
- `for` repete o bloco para cada indice da lista.
- `indice + 1` transforma a contagem de `0, 1, 2...` para `1, 2, 3...`.
- `musicas[indice]` acessa a musica que esta naquela posicao.
- `print()` mostra o numero e o nome da musica.

## Forma mais simples do `for`

Quando nao precisa mostrar o numero da musica, da para usar:

```python
for musica in musicas:
    print(musica)
```

Esse formato passa diretamente por cada item da lista.

## Forma com numero usando `enumerate()`

Outra forma de mostrar numero e musica:

```python
for numero, musica in enumerate(musicas, start=1):
    print(numero, "-", musica)
```

Explicacao:

- `enumerate()` percorre a lista e tambem gera um numero.
- `start=1` faz a contagem comecar em `1`.
- `numero` guarda a posicao exibida.
- `musica` guarda o nome da musica atual.

## Erros comuns

### Esquecer de converter numero

Errado:

```python
idade = input("Digite a idade: ")
if idade >= 18:
    print("Pode participar")
```

Certo:

```python
idade = int(input("Digite a idade: "))
if idade >= 18:
    print("Pode participar")
```

### Esquecer os dois pontos no `if`, `else` ou `for`

Errado:

```python
if media >= 7
    print("Aprovado")
```

Certo:

```python
if media >= 7:
    print("Aprovado")
```

### Esquecer a indentacao

Errado:

```python
for musica in musicas:
print(musica)
```

Certo:

```python
for musica in musicas:
    print(musica)
```

Em Python, os espacos no comeco da linha mostram quais comandos pertencem ao bloco.
