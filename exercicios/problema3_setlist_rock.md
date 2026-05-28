# Problema: Setlist de Rock com For Loop

## Objetivo

Crie um programa que monte e exiba o setlist de uma banda de rock usando `for`.

A ideia e simular uma apresentacao inspirada na energia de bandas como **System of a Down**: som pesado, musicas rapidas e ordem de show bem definida.

![chop-suey](https://media.tenor.com/RcWFW0PJS4sAAAAM/wake-up-system-of-a-down.gif)
---

## Historia

Vai acontecer um festival de rock.

Antes do show comecar, o tecnico precisa imprimir a ordem das musicas que serao tocadas por banda.

Para nao escrever varios `print()` repetidos, o programa deve guardar as musicas em uma lista e usar um `for` para exibir cada uma.

---

## Entrada

Neste exercicio, o programa pode usar uma lista pronta com nomes ficticios (ou não)  de musicas 

```text
lista de musicas da banda
```

Exemplo:

```python
musicas = [
    "Grito da Cidade",
    "Caos no Palco",
    "Radio Quebrado",
    "Revolta"
]
```

---

## Processamento

O programa deve passar por cada musica da lista usando `for`.

```text
para cada musica na lista:
    exibir musica
```

Tambem deve mostrar a posicao da musica no show.

```text
1 - Grito da Cidade
2 - Caos no Palco
3 - Radio Quebrado
4 - Revolta
```

---

## Saida

O programa deve exibir:

```text
Nome da banda
Setlist do show
Numero e nome de cada musica
Mensagem final
```

---

## Ferramentas que podem ser usadas

### Criar uma lista

```python
musicas = ["Musica 1", "Musica 2", "Musica 3"]
```

---

### Usar `for`

```python
for musica in musicas:
    print(musica)
```

O `for` repete um bloco de codigo para cada item da lista.

---

### Usar `range()`

```python
for numero in range(1, 5):
    print(numero)
```

O `range()` ajuda a criar uma sequencia de numeros.

---

### Acessar item da lista pelo indice

```python
musicas[0]
```

O primeiro item da lista fica na posicao `0`.

---

## Exemplo de logica em pseudocodigo

```text
criar nome da banda
criar lista de musicas

exibir nome da banda
exibir "Setlist do show"

para indice de 0 ate tamanho da lista:
    numero = indice + 1
    musica = musicas[indice]
    exibir numero e musica

exibir mensagem final
```

---

## Exemplo em Python

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

print("\nShow encerrado com guitarra pesada e bateria acelerada.")
```

---

## Resultado esperado

```text
Banda: System Cover Down

Setlist do show
1 - Grito da Cidade
2 - Caos no Palco
3 - Radio Quebrado
4 - Revolta no Amplificador

Show encerrado com guitarra pesada e bateria acelerada.
```

---

## Desafio extra

Depois que o exemplo funcionar, adicione mais musicas na lista e veja se o `for` mostra tudo automaticamente.


![rock](https://i.makeagif.com/media/2-11-2016/ohzHG8.gif)