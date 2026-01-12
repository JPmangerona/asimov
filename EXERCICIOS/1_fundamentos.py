#requisição de dados ao usuário
nome = input("Qual seu nome?")
idade = input("Qual sua idade?")
teste = 5

#print dos dados
print("oi, " + nome)
print("seu nome possui", len(nome), "letras, e você terá", int(idade)+5, "aqui 5 anos.")
##caso eu tivesse colocado o sinal de + ao invés de , na linha acima, o resultado seria diferente. O + faz a concatenação de strings, enquanto a , separa os argumentos da função print.
##partindo do pressuposto que não se soma int com str deveria fazer a conversão do int para str ou daria erro.

##forma mais facil de formatar string
print(f'ola {teste}!')

##forma de quebrar a linha
print("linha 1\nlinha 2")

