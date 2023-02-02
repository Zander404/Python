# nome = input("Digite seu nome: ")

# import math

# word = "level"
# website = "https://google.com"

# # if word == word[::-1]:
# #     print(f"Sua palavra é um palidromo!")
# #     print(word)
# #     print(word[::-1])
    
# # else:
# #     print(f"Tá errado")
# #     print(word)
# #     print(word[::-1])

# website = website[8:-4]
# print(website)


# if len(word) == 5 and website == "google":
#     print("Caraca eihhh!")


# import time

# for seconds in range(10,-1,-1):
#     print(seconds)
#     if seconds == 0:
#         print("Happy New Year")
#     time.sleep(1)


# rows = int(input("Quantidades de linhas: "))
# columns = int(input("Quantidade de colunas: "))
# symbol = input("Digite um simbolo: ")


# for  i in range(columns):
#     for j in range(rows):
#         print(symbol, end="")
#     print("")


# for i in range(1,10):
#     if i == 4:
#         pass
#     else:
#         print(i)


# food = ["pao","queijo","tomate","alface","hamburguer"]
# food.append("Picles")
# food.insert(0,"Batata")
# food.pop()
# food.remove("tomate")
# food.reverse()
# food.sort()

# for i in food:
#     print(i)

# print(food[2])


# # SETS

# talher = {"garfo", "faca", "colher","Prato"}
# mesa = {"Prato", "Sorrocaba", "faca"}
# # talher.add("guardanapo")
# # talher.remove("garfo")
# # talher.clear()
# # talher.update(mesa)
# mesa_de_jantar = talher.union(mesa)


# # for i in mesa_de_jantar:
# #     print(i)

# # print(mesa.difference(talher))
# print(talher.intersection(mesa))

# def hello():
#     print("Caca")

# hello()


# def multiply(num1, num2):
#     return num1*num2


# print(multiply(8,5))


# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
    
#     return sum 


    
# sum = add(12,55,12)
# print(sum)

# def key(**kwargs):
#     print(f"Hello {kwargs['first']}, {kwargs['second']}")



# key(second="Carlos", first="Fedido")

try:
    num_1 = int(input("Digite um numero: "))
    num_2 = int(input("Digite outro numero: "))
    div = num_1/num_2
    print(f"O resultado foi: {div}")
except ZeroDivisionError as e:
    print(f"Vc fez merda, {e}")


