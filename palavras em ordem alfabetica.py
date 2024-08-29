
#entrada de dados
my_str = str(input("escreva a frase: "))

# identifica as palavras
words = [word.lower() for word in my_str.split()]

# lista
words.sort()

# saida de dados

print("a ordem de palavras é:")
for word in words:
   print(word)
