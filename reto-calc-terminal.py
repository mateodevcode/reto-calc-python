import colorama
from colorama import Fore, Back, Style
import os
import time

# Configurar colorama para sistemas Windows
if os.name == 'nt':
    colorama.init()

# Función para limpiar la pantalla
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para imprimir la calculadora
def print_calculator(result):
    clear_screen()
    print(Fore.GREEN + "****************** Reto de Calculadora - The Bridge ******************")
    print("Introduce 'help' para ver las instrucciones")
    print("Introduce la operación a calcular o 'q' para salir:")
    print("Resultado: ", result)

# Función para realizar cálculos
def calculate(expression):
    try:
        result = eval(expression)
        return result
    except:
        return "Error"

# Función principal
def main():
    result = 0
    while True:
        print_calculator(result)
        expression = input("> ")
        if expression.lower() == 'help':
            print("Cargando instrucciones...")
            time.sleep(3)
            clear_screen()
            print("****************** Reto de Calculadora - The Bridge ******************")
            print("Instrucciones:")
            time.sleep(1)
            print("Introduce una operación matemática y pulsa Enter para ver el resultado.")
            time.sleep(2)
            print("Operadores válidos: +, -, *, /")
            time.sleep(1.5)
            print("Introduce 'q' para salir.")
            time.sleep(1.5)
            input("Pulsa Enter para continuar...")
        if expression.lower() == 'q':
            break
        result = calculate(expression)

if __name__ == "__main__":
    main()