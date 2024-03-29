from tkinter import *
from tkinter import ttk

# Crear las funciones de la calculadora

def ingresar_valores(tecla):
    if tecla >= "0" and tecla <= "9" or tecla == ")" or tecla == "(" or tecla == ".":
        entrada_02.set(entrada_02.get() + str(tecla))

    if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
        if tecla == "*":
            entrada_01.set(entrada_02.get() + "*")
        elif tecla == "/":
            entrada_01.set(entrada_02.get() + "/")
        elif tecla == "+":
            entrada_01.set(entrada_02.get() + "+")
        elif tecla == "-":
            entrada_01.set(entrada_02.get() + "-")

        entrada_02.set("")

    if tecla == "=":
        entrada_01.set(entrada_01.get() + entrada_02.get())
        resultado = eval(entrada_01.get())

        entrada_02.set(resultado)

def ingresar_valores_teclado(event):
    tecla = event.char
    if tecla >= "0" and tecla <= "9" or tecla == ")" or tecla == "(" or tecla == ".":
        entrada_02.set(entrada_02.get() + str(tecla))

    if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
        if tecla == "*":
            entrada_01.set(entrada_02.get() + "*")
        elif tecla == "/":
            entrada_01.set(entrada_02.get() + "/")
        elif tecla == "+":
            entrada_01.set(entrada_02.get() + "+")
        elif tecla == "-":
            entrada_01.set(entrada_02.get() + "-")

        entrada_02.set("")

    if tecla == "=" or tecla == "\r":
        entrada_01.set(entrada_01.get() + entrada_02.get())
        resultado = eval(entrada_01.get())

        entrada_02.set(resultado)

def borrar(event):
    inicio = 0
    final = len(entrada_02.get())
    entrada_02.set(entrada_02.get()[inicio:final-1])

def borrar_todo(event):
    entrada_01.set("")
    entrada_02.set("")


# Crear la ventana de la calculadora

root = Tk()
root.title("Reto de calculadora - The Bridge")
root.geometry("+500+80") # Posicion de la ventana
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Agregar los estilos

estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure('mainframe.TFrame')

mainframe = ttk.Frame(root, style="mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky=(W, E, N, S))
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)


# Crear las variables de entrada

estilos_label_01 = ttk.Style()
estilos_label_01.configure('Label_01.TLabel', font=("Arial 15"), ANCHOR="e")

entrada_01 = StringVar()
Label_entrada_01 = ttk.Label(mainframe, textvariable=entrada_01, style="Label_01.TLabel")
Label_entrada_01.grid(column=0, row=0, columnspan=4, sticky=(W, N, E, S))

estilos_label_02 = ttk.Style()
estilos_label_02.configure('Label_02.TLabel', font=("Arial 30"), ANCHOR="e")


entrada_02 = StringVar()
label_entrada_02 = ttk.Label(mainframe, textvariable=entrada_02, style="Label_02.TLabel")
label_entrada_02.grid(column=0, row=1, columnspan=4, sticky=(W, N, E, S))

# Crear los botones

# estilos de los botones	

estilos_numeros = ttk.Style()
estilos_numeros.configure('Butones_numeros.TButton', font=("Arial 22"), width=5, background="#fff", relif="flat")
estilos_numeros.map('Butones_numeros.TButton', foreground=[('active', "#6c72ff")], background=[('active', "#fff")])

estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure('Botones_borrar.TButton', font=("Arial 22"), width=5, background="#676767", relif="flat", foreground="#fff")
estilos_botones_borrar.map('Botones_borrar.TButton', foreground=[('active', "#00ff19")], background=[('active', "#fff")])


estilos_botones_default = ttk.Style()
estilos_botones_default.configure('Botones_default.TButton', font=("Arial 22"), width=5, background="#676767", relif="flat", foreground="#fff")
estilos_botones_default.map('Botones_default.TButton', foreground=[('active', "#f06c6c")], background=[('active', "#fff")])

button_00 = ttk.Button(mainframe, text="0", style="Butones_numeros.TButton", command=lambda: ingresar_valores("0"))
button_01 = ttk.Button(mainframe, text="1", style="Butones_numeros.TButton", command=lambda: ingresar_valores("1"))
button_02 = ttk.Button(mainframe, text="2", style="Butones_numeros.TButton", command=lambda: ingresar_valores("2"))
button_03 = ttk.Button(mainframe, text="3", style="Butones_numeros.TButton", command=lambda: ingresar_valores("3"))
button_04 = ttk.Button(mainframe, text="4", style="Butones_numeros.TButton", command=lambda: ingresar_valores("4"))
button_05 = ttk.Button(mainframe, text="5", style="Butones_numeros.TButton", command=lambda: ingresar_valores("5"))
button_06 = ttk.Button(mainframe, text="6", style="Butones_numeros.TButton", command=lambda: ingresar_valores("6"))
button_07 = ttk.Button(mainframe, text="7", style="Butones_numeros.TButton", command=lambda: ingresar_valores("7"))
button_08 = ttk.Button(mainframe, text="8", style="Butones_numeros.TButton", command=lambda: ingresar_valores("8"))
button_09 = ttk.Button(mainframe, text="9", style="Butones_numeros.TButton", command=lambda: ingresar_valores("9"))

button_borrar = ttk.Button(mainframe, text=chr(9003), style="Botones_borrar.TButton", command=lambda: borrar())
button_borrar_todo = ttk.Button(mainframe, text="C", style="Botones_borrar.TButton", command=lambda: borrar_todo())
Button_parentesis_01 = ttk.Button(mainframe, text="(", style='Botones_default.TButton', command=lambda: ingresar_valores("("))
Button_parentesis_02 = ttk.Button(mainframe, text=")", style='Botones_default.TButton', command=lambda: ingresar_valores(")"))
Button_punto = ttk.Button(mainframe, text=".", style='Botones_default.TButton', command=lambda: ingresar_valores("."))

button_division = ttk.Button(mainframe, text=chr(247), style='Botones_default.TButton', command=lambda: ingresar_valores("/"))
button_multiplicacion = ttk.Button(mainframe, text="*", style='Botones_default.TButton', command=lambda: ingresar_valores("*"))
button_resta = ttk.Button(mainframe, text="-", style='Botones_default.TButton', command=lambda: ingresar_valores("-"))
button_suma = ttk.Button(mainframe, text="+", style='Botones_default.TButton', command=lambda: ingresar_valores("+"))

button_igual = ttk.Button(mainframe, text="=", style='Botones_default.TButton', command=lambda: ingresar_valores("="))
# button_raiz_cuadrada = ttk.Button(mainframe, text="√", style='Botones_default.TButton')

# Imprimir los botones en la pantalla

Button_parentesis_01.grid(column=0, row=2, sticky=(W, E, N, S))
Button_parentesis_02.grid(column=1, row=2, sticky=(W, E, N, S))
button_borrar_todo.grid(column=2, row=2, sticky=(W, E, N, S))
button_borrar.grid(column=3, row=2, sticky=(W, E, N, S))

button_07.grid(column=0, row=3, sticky=(W, E, N, S))
button_08.grid(column=1, row=3, sticky=(W, E, N, S))
button_09.grid(column=2, row=3, sticky=(W, E, N, S))
button_division.grid(column=3, row=3, sticky=(W, E, N, S))

button_04.grid(column=0, row=4, sticky=(W, E, N, S))
button_05.grid(column=1, row=4, sticky=(W, E, N, S))
button_06.grid(column=2, row=4, sticky=(W, E, N, S))
button_multiplicacion.grid(column=3, row=4, sticky=(W, E, N, S))

button_01.grid(column=0, row=5, sticky=(W, E, N, S))
button_02.grid(column=1, row=5, sticky=(W, E, N, S))
button_03.grid(column=2, row=5, sticky=(W, E, N, S))
button_resta.grid(column=3, row=5, sticky=(W, E, N, S))

button_00.grid(column=0, row=6, sticky=(W, E, N, S)) # (columnspan=2, sticky="nsew")
Button_punto.grid(column=1, row=6, sticky=(W, E, N, S))
button_igual.grid(column=2, row=6, sticky=(W, E, N, S))
button_suma.grid(column=3, row=6, sticky=(W, E, N, S))


for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=0, pady=0)


root.bind("<Key>", ingresar_valores_teclado)
root.bind("<BackSpace>", borrar)
root.bind("<Delete>", borrar_todo)
root.mainloop()



























# Vamos a realizar el reto de la calculadora, en donde vamos a realizar las operaciones basicas de una calculadora, suma, resta, multiplicacion y division.



# Para ello vamos a necesitar los siguientes pasos:

# declarar las funciones de suma, resta, multiplicacion y division

# # sumar dos numeros
# def suma(a, b):
#     return a + b

# # restar dos numeros
# def resta(a, b):
#     return a - b

# # multiplicar dos numeros
# def multiplicacion(a, b):
#     return a * b

# # dividir dos numeros
# def division(a, b):
#     return a / b

# # declarar los imputs de los numeros y la operacion a realizar
# num1 = int(input("Ingresa el primer numero: "))
# operacion = input("Ingresa la operacion a realizar (suma, resta, multiplicacion, division): ")
# num2 = int(input("Ingresa el segundo numero: "))


# # realizar la operacion

# # switch case

# match operacion:
#     case "+":
#         print(suma(num1, num2))
#     case "-":
#         print(resta(num1, num2))
#     case "*":
#         print(multiplicacion(num1, num2))
#     case "":
#         print(division(num1, num2))
#     case _:
#         print("Operacion no valida")

