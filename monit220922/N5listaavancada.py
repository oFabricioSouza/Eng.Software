# 5. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do
# atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa
# que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe
# o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado
# o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# 6. Atleta: Rodrigo Curvêllo
# 7.
# 8. Primeiro Salto: 6.5 m
# 9. Segundo Salto: 6.1 m
# 10. Terceiro Salto: 6.2 m
# 11. Quarto Salto: 5.4 m
# 12. Quinto Salto: 5.3 m
# 13.
# 14. Resultado final:
# 15. Atleta: Rodrigo Curvêllo
# 16. Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3

nomes = []
saltos = []
name = input('Digite seu nome: ')
nomes.append(name)


if name != "":
    for i in range(1,6):
        jump = float(input('Digite a distância do salto, em ordem de 1 a 5: '))
        saltos.append(jump)
    print("\n Atleta:",name)
    # for i in range(len(saltos)):
        # print("Salto %i: %.2f" % (i+1,saltos[i]))
    print("\n Saltos: \n","Primeiro salto:", saltos[0], "\n Segundo salto:", saltos[1], "\n Terceiro salto:", saltos[2],
     "\n Quarto salto:", saltos[3], "\n Quinto salto:",saltos[4],)
    print("\n Resultado final: \n Atleta:", name, "\n Saltos:", saltos)
    media = sum(saltos)/5
    print("Media:", media)
else:
    print('PROGRAMA ENCERRADO')
    
