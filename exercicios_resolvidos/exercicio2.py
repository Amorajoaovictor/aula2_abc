nome = input("insira o seu nome ")
nota_teorica = float(input("insira nota da prova teorica "))
nota_simulacao= float(input("insira nota da simulação  "))
media= (nota_simulacao + nota_teorica)/2
if media >= 7:
    print(f"detetive {nome} passou com media {media}")
else:
    print(f"detetive {nome} reprovoua com media {media}")