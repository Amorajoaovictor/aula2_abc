# Problema: Boletim da Delegacia 99

## Objetivo

Crie um programa que monte o boletim de treinamento de um novo detetive da **Delegacia 99**.

O programa deve receber o **nome do detetive**, duas **notas de treinamento**, calcular a **media** e exibir se ele foi **aprovado** ou **reprovado** usando `if/else`.

---

## Historia

A Delegacia 99 esta treinando novos detetives.

Cada participante recebe duas notas:

- nota da prova teorica;
- nota da simulacao de investigacao.

Para ser aprovado no treinamento, o detetive precisa ter media maior ou igual a `7`.

Se a media for menor que `7`, ele precisa refazer o treinamento.

---
![holt](https://media.tenor.com/XnRZGt_Zx4MAAAAM/yes-raymond-holt.gif)
## Entrada

O programa deve receber:

```text
nome do detetive
nota da prova teorica
nota da simulacao de investigacao
```

---

## Processamento

O programa deve calcular a media das duas notas:

```text
media = (nota_teorica + nota_simulacao) / 2
```

Depois, deve usar `if/else` para verificar se o detetive foi aprovado.

```text
se media >= 7:
    detetive aprovado no treinamento
senão:
    detetive precisa refazer o treinamento
```

---

## Saida

O programa deve exibir:

```text
Nome do detetive
Nota da prova teorica
Nota da simulacao
Media
Situacao: Aprovado ou Reprovado
```

---

## Ferramentas que podem ser usadas

### Exibir uma mensagem no terminal

```python
print("mensagem")
```

Lembre-se: a mensagem deve ficar entre aspas.

---

### Receber uma informacao digitada pelo usuario

```python
input("mensagem")
```

Tambem e possivel guardar o valor digitado em uma variavel:

```python
nome = input("Nome do detetive: ")
```

---

### Converter texto para numero decimal

O `input()` sempre recebe texto. Para trabalhar com notas, use `float()`.

```python
nota = float(input("Digite a nota: "))
```

---

### Operacoes matematicas

```python
numero + numero
numero - numero
numero / numero
numero * numero
```

---

### Quebra de linha

```python
\n
```

---

## Exemplo de logica em pseudocodigo

```text
ler nome
ler nota_teorica
ler nota_simulacao

media = (nota_teorica + nota_simulacao) / 2

se media >= 7:
    situacao = "Aprovado no treinamento"
senão:
    situacao = "Precisa refazer o treinamento"

exibir nome
exibir nota_teorica
exibir nota_simulacao
exibir media
exibir situacao
```

---

## Exemplo em Python

```python
nome = input("Digite o nome do detetive: ")
nota_teorica = float(input("Digite a nota da prova teorica: "))
nota_simulacao = float(input("Digite a nota da simulacao de investigacao: "))

media = (nota_teorica + nota_simulacao) / 2

if media >= 7:
    situacao = "Aprovado no treinamento"
else:
    situacao = "Precisa refazer o treinamento"

print("\nBoletim da Delegacia 99")
print("Detetive:", nome)
print("Prova teorica:", nota_teorica)
print("Simulacao:", nota_simulacao)
print("Media:", media)
print("Situacao:", situacao)
```

---

## Resultado esperado

```text
Digite o nome do detetive: Jake
Digite a nota da prova teorica: 8
Digite a nota da simulacao de investigacao: 6

Boletim da Delegacia 99
Detetive: Jake
Prova teorica: 8.0
Simulacao: 6.0
Media: 7.0
Situacao: Aprovado no treinamento
```
![aprovado](https://media4.giphy.com/media/v1.Y2lkPTZjMDliOTUyNWp6a2czdDQ4cGprcHR6MW8ycXN6cXpjMHc5OXdqczdiM200cXh4bCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/KxiRwO7tqXCTDVKobo/giphy.gif)

```text
Digite o nome do detetive: Jake
Digite a nota da prova teorica: 5
Digite a nota da simulacao de investigacao: 6

Boletim da Delegacia 99
Detetive: Jake
Prova teorica: 5.0
Simulacao: 6.0
Media: 5.5
Situacao: Precisa refazer o treinamento
```

![reprovado](https://media1.giphy.com/media/xThuWmdBg5KbLYLMBy/giphy.gif)