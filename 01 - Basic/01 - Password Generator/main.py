import random #Importando a bilbioteca random para deixar a senha aleatória.
import string #Importando a bilbioteca string para facilitar a seleção dos caracteres.
import os #Importando a biblioteca os para limpar o terminal e deixar o código mais limpo.

def GerarSenha(tamanho, tipo):
    match tipo:
        case 1:
            caracteres = string.ascii_letters + string.digits + string.punctuation #Adicionando todas as letras do alfabeto maiúsculas e minúsculas, digitos de 0 a 9 e caracteres especiais na variável caracteres. Não utilizei string.printable pois são considerados espaços em branco.
            senha = "".join(random.choices(caracteres, k = tamanho)) #A função de random me retorna uma lista, e eu adiciono essa lista com o separador vazio "" a variável "senha" utilizando o ".join()".
            return senha
        case 2:
            caracteres = string.ascii_letters + string.digits #Adicionando apenas letras e números a senha que será gerada.
            senha = "".join(random.choices(caracteres, k = tamanho)) #A função de random me retorna uma lista, e eu adiciono essa lista com o separador vazio "" a variável "senha" utilizando o ".join()".
            return senha
        case 3:
            caracteres = string.ascii_letters #Adicionando apenas letras a senha.
            senha = "".join(random.choices(caracteres, k = tamanho)) #A função de random me retorna uma lista, e eu adiciono essa lista com o separador vazio "" a variável "senha" utilizando o ".join()"
            return senha
        case 4:
            caracteres = string.digits #Adicionando apenas números a senha.
            senha = "".join(random.choices(caracteres, k = tamanho)) #A função de random me retorna uma lista, e eu adiciono essa lista com o separador vazio "" a variável "senha" utilizando o ".join()".
            return senha
        
def GerarPainel():
    os.system("cls") #Comando que vai limpar o terminal a cada vez que a função de GerarPainel for chamada, deixando o terminal limpo.
    print("=== Gerador de Senhas ===")
    print("[1]Completa")
    print("[2]Letras e números sem caracteres especiais")
    print("[3]Apenas letras")   
    print("[4]Apenas números")

#Programa Principal
GerarPainel()
tipo = int(input("Qual tipo de senha você deseja: ")) #O usuário escolhe qual tipo de senha melhor lhe agrada.

while tipo < 1 or tipo > 4:
    GerarPainel()
    tipo = int(input("Opção inválida, insira um opção válida: "))

tamanho = int(input("Escolha o tamanho da senha: "))
print(f"Senha gerada: {GerarSenha(tamanho, tipo)}")