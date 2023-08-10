#Primeiro pegar o dividendo e dividir por todos os divisores até o dividendo, se um der resto == 0 decrementa o dividendo
#dividendo ira diminuir
#divisor aumentando
#for divisor in range(2, dividendo):
#if dividendo % divisor == 0:
#dividendo -= 1
#ler -> https://rpm.org.br/cdrpm/19/4.htm#:~:text=2%2C%203%2C%205%2C%207%2C%2011%2C%2013%2C,%2C%20337%2C%20347%2C%20349%2C

dividendo = int(input(""))

def maior_primo(dividendo):
  divisor = 2
  while dividendo != divisor:
    if dividendo % divisor == 0:
      dividendo -= 1
      divisor = 2
    elif dividendo % divisor != 0:
      divisor += 1

  return dividendo

print(maior_primo(dividendo))