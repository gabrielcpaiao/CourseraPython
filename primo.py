dividendo = int(input("Digite um numero: "))
#Primeiro pegar o dividendo e dividir por todos os divisores até o dividendo, se um der resto == 0 decrementa o dividendo
#dividendo ira diminuir
#divisor aumentando

def maior_primo(dividendo):
    divisor = 2
    while True:
      if dividendo % divisor == 0:
         dividendo -= 1
      elif dividendo % divisor != 0:
        divisor += 1
      
    
    for divisor in range(2, dividendo):
      if dividendo % divisor == 0:
        dividendo -= 1