# Problema: Permissao para Torneio Ninja

## Objetivo

Crie um programa que leia o nome e a idade de um personagem de anime e informe se ele pode participar do **Torneio Ninja** usando `if/else`.

Para participar, o personagem precisa ter **18 anos ou mais**.

---

## Historia

A vila esta organizando um grande torneio entre ninjas.

Antes da inscricao, o sistema precisa verificar a idade de cada participante.

Se o personagem tiver 18 anos ou mais, ele entra no torneio.

Se tiver menos de 18 anos, ele ainda precisa treinar mais um pouco antes de competir.

---

## Entrada

O programa deve receber:

```text
nome do personagem
idade
```

---

## Processamento

O programa deve verificar se a idade e maior ou igual a 18.

```text
se idade >= 18:
    personagem pode participar do torneio
senão:
    personagem precisa continuar treinando
```

---

## Saida

O programa deve exibir:

```text
Nome do personagem
Idade
Resultado da inscricao
```

---

## Ferramentas que podem ser usadas

### Exibir uma mensagem no terminal

```python
print("mensagem")
```

---

### Receber uma informacao digitada pelo usuario

```python
input("mensagem")
```

Tambem e possivel guardar o valor digitado em uma variavel:

```python
nome = input("Digite o nome do personagem: ")
```

---

### Converter texto para numero inteiro

O `input()` sempre recebe texto. Para trabalhar com idade, use `int()`.

```python
idade = int(input("Digite a idade: "))
```

---

### Comparacao

```python
idade >= 18
```

Essa comparacao verifica se a idade e maior ou igual a 18.

---

## Exemplo de logica em pseudocodigo

```text
ler nome
ler idade

se idade >= 18:
    resultado = "Pode participar do Torneio Ninja"
senão:
    resultado = "Precisa continuar treinando"

exibir nome
exibir idade
exibir resultado
```

---

## Exemplo em Python

```python
nome = input("Digite o nome do personagem: ")
idade = int(input("Digite a idade do personagem: "))

if idade >= 18:
    resultado = "Pode participar do Torneio Ninja"
else:
    resultado = "Precisa continuar treinando"

print("\nInscricao no Torneio Ninja")
print("Personagem:", nome)
print("Idade:", idade)
print("Resultado:", resultado)
```

---

## Resultado esperado

```text
Digite o nome do personagem: Akira
Digite a idade do personagem: 16

Inscricao no Torneio Ninja
Personagem: Akira
Idade: 16
Resultado: Precisa continuar treinando
```
