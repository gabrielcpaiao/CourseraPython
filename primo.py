#Primeiro pegar o dividendo e dividir por todos os divisores até o dividendo, se um der resto == 0 decrementa o dividendo
#dividendo ira diminuir
#divisor aumentando
#for divisor in range(2, dividendo):
#if dividendo % divisor == 0:
#dividendo -= 1

#dividendo = int(input("Digite um numero: "))
def maior_primo(dividendo):
  divisor = 2
  while dividendo != divisor:
    if dividendo % divisor == 0:
      dividendo -= 1
      divisor = 2
    elif dividendo % divisor != 0:
      divisor += 1

  return dividendo

print(maior_primo(25))