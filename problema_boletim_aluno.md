# Problema: Boletim do Aluno

## Objetivo

Crie um programa que monte o boletim de um aluno.

O programa deve receber o **nome do aluno**, duas **notas**, calcular a **média** e exibir a **situação final** usando `if/else`.

---

## Entrada

O programa deve receber:

```text
nome do aluno
nota 1
nota 2
```

---

## Processamento

O programa deve calcular a média das duas notas:

```text
media = (nota1 + nota2) / 2
```

Depois, deve usar `if/else` para verificar se o aluno passou ou reprovou.

```text
se media >= 7:
    aluno passou
senão:
    aluno reprovou
```

---

## Saída

O programa deve exibir:

```text
Nome do aluno
Nota 1
Nota 2
Média
Situação: Aprovado ou Reprovado
```

---

## Ferramentas que podem ser usadas

### Exibir uma mensagem no terminal

```python
print("mensagem")
```

Lembre-se: a mensagem deve ficar entre aspas.

---

### Receber uma informação digitada pelo usuário

```python
input("mensagem")
```

Também é possível guardar o valor digitado em uma variável:

```python
nome = input("Qual seu nome?")
```

---

### Operações matemáticas

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

## Exemplo de lógica em pseudocódigo

```text
ler nome
ler nota1
ler nota2

media = (nota1 + nota2) / 2

se media >= 7:
    situacao = "Aprovado"
senão:
    situacao = "Reprovado"

exibir nome
exibir nota1
exibir nota2
exibir media
exibir situacao
```

---

## Exemplo em Python

```python
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print("\nBoletim do Aluno")
print("Nome:", nome)
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Média:", media)
print("Situação:", situacao)
```

---

## Resultado esperado

```text
Digite o nome do aluno: João
Digite a primeira nota: 8
Digite a segunda nota: 6

Boletim do Aluno
Nome: João
Nota 1: 8.0
Nota 2: 6.0
Média: 7.0
Situação: Aprovado
```
