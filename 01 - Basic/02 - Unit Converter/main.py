import os 
def limpar_tela(): os.system('clear' if os.name == 'posix' else 'cls')

def GerarPainel():
    limpar_tela()
    print("=== Conversor de Unidades")
    print("[1]Converter Temperatura")
    print("[2]Converter Peso")
    print("[3]Converter Tempo")

def PainelTemperatura():
    limpar_tela()
    print("[1]Graus Celsius (C) para Graus Fahrenheit (F)")
    print("[2]Graus Fahrenheit (F) para Graus Celsius (C)")

def ConverterTemperatura(conversao, temperatura):
    if conversao == 1:
        return round((temperatura*1.8)+32, 1)
    elif conversao == 2:
        return round((temperatura-32)/1.8, 1)
    
def PainelPeso():
    limpar_tela()
    print("[1] Converter Quilogramas (kg) para Gramas (g)")
    print("[2] Converter Gramas (g) para Quilogramas (kg)")

def ConvereterPeso(conversao, peso):
    if conversao == 1:
        return peso * 1000
    elif conversao == 2:
        return round(peso / 1000, 3)

def PainelTempo():
    limpar_tela()
    print("[1]Converter Horas (h) para Minutos (min)")
    print("[2]Converter Horas (h) para Segundos (s)")
    print("[3]Converter Minutos (min) para Horas (h)")
    print("[4]Converter Minutos (min) para Segundos (s)")
    print("[5]Converter Segundos (s) para Horas (h)")
    print("[6]Converter Segundos (s) para Minutos (min)")

def ConverterTempo(conversao, tempo):
    if conversao == 1:
        return tempo * 60
    elif conversao == 2: 
        return tempo * 3600
    elif conversao == 3: 
        return tempo / 60
    elif conversao == 4: 
        return tempo * 60
    elif conversao == 5:
        return tempo / 3600
    elif conversao == 6:
        return tempo / 60
    
#Programa Principal.
GerarPainel()
tipo = int(input("Qual conversão você deseja fazer: ")) 
while tipo < 1 or tipo > 3: 
    GerarPainel() 
    tipo = int(input("Opção inválida, insira um opção válida: "))

if tipo == 1:  
    PainelTemperatura() 
    conversao = int(input("Qual conversão você deseja fazer:  "))
    temperatura = float(input("Insira a temperatura a ser convertida: "))
    print(f"Temperatura convertida: {ConverterTemperatura(conversao, temperatura)}")

elif tipo == 2: 
    PainelPeso() 
    conversao = int(input("Qual conversão você deseja fazer: "))
    peso = float(input("Insira o peso que deseja converter: "))
    print(f"Peso convertido: {ConvereterPeso(conversao, peso)} ")

elif tipo == 3:
    PainelTempo() 
    conversao = int(input("Qual versão você deseja fazer: "))
    tempo = float(input("Insira o tempo que você deseja converter: "))
    print(f"Tempo convertido: {ConverterTempo(conversao, tempo)}")