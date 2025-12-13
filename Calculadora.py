import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import *


ventana=tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x500")
ventana.config(bg="steelblue")
ventana.resizable(False,False)

#pantalla
pantalla=tk.Entry(ventana, width=60)
pantalla.pack(pady=20, ipady=10)
pantalla.config(state="disabled")  

frame1 = tk.Frame(ventana, bg="steelblue", bd=5, relief="ridge")
frame1.pack(fill="both", expand=True)

#botones
boton7=tk.Button(frame1, bg="white", text="7", width=9, height=3)
boton7.grid(row=1, column=0, padx=10, pady=5)

boton8=tk.Button(frame1, text="8", bg="white", width=9, height=3)
boton8.grid(row=1, column=1, padx=10, pady=5)

boton9=tk.Button(frame1, text="9", bg="white", width=9, height=3)
boton9.grid(row=1, column=2, padx=10, pady=5)

boton_division=tk.Button(frame1, text="/", bg="white", width=9, height=3)
boton_division.grid(row=1, column=3, padx=10, pady=5)

boton4=tk.Button(frame1, bg="white", text="4", width=9, height=3)
boton4.grid(row=2, column=0, padx=10, pady=5)

boton5=tk.Button(frame1, bg="white", text="5", width=9, height=3)
boton5.grid(row=2, column=1, padx=10, pady=5)

boton6=tk.Button(frame1, bg="white", text="6", width=9, height=3)
boton6.grid(row=2, column=2, padx=10, pady=5)

boton_producto=tk.Button(frame1, bg="white", text="*", width=9, height=3)
boton_producto.grid(row=2, column=3, padx=10, pady=5)

boton1=tk.Button(frame1, bg="white", text="1", width=9, height=3)
boton1.grid(row=3, column=0, padx=10, pady=5)

boton2=tk.Button(frame1, bg="white", text="2", width=9, height=3)
boton2.grid(row=3, column=1, padx=10, pady=5)

boton3=tk.Button(frame1, bg="white", text="3", width=9, height=3)
boton3.grid(row=3, column=2, padx=10, pady=5)

boton_resta=tk.Button(frame1, bg="white", text="-", width=9, height=3)
boton_resta.grid(row=3, column=3, padx=10, pady=5)

boton_punto=tk.Button(frame1, text=".", width=9 ,height=3)
boton_punto.grid(row=4, column=0, padx=10, pady=5)

boton0=tk.Button(frame1, bg="white", text="0", width=9, height=3)
boton0.grid(row=4, column=1, padx=10, pady=5)

boton_igual=tk.Button(frame1, bg="white", text="=", width=9, height=3)
boton_igual.grid(row=4, column=2, padx=10, pady=5)

boton_suma=tk.Button(frame1, bg="white", text="+", width=9, height=3)
boton_suma.grid(row=4, column=3, padx=10, pady=5)

frame2 = tk.Frame(frame1, bg="lightblue", bd=5, relief="ridge")
frame2.grid(row=5, column=0, columnspan=4, pady=10)

boton_borrar=tk.Button(frame2, text="Borrar", bg="white")
boton_borrar.grid(row=5, column=0, padx=10, pady=5)


def bloquear_input(event):
    return "break"
pantalla.bind("<Key>", bloquear_input)



def insertar(valor):
    pantalla.config(state="normal")
    pantalla.insert("end", valor)
    pantalla.config(state="disabled")


def click_7(event):
    print("Boton 7 presionado")
    insertar("7")
boton7.bind("<Button-1>", click_7)

def click_8(event):
    print("Boton 8 presionado")
    insertar("8")
boton8.bind("<Button-1>", click_8)

def click_9(event):
    print("Boton 9 presionado")
    insertar("9")
boton9.bind("<Button-1>", click_9)

def click_6(event):
    print("Boton 6 presionado")
    insertar("6")
boton6.bind("<Button-1>", click_6)

def click_5(event):
    print("Boton 5 presionado")
    insertar("5")
boton5.bind("<Button-1>", click_5)

def click_4(event):
    print("Boton 4 presionado")
    insertar("4")
boton4.bind("<Button-1>", click_4)

def click_3(event):
    print("Boton 3 presionado")
    insertar("3")
boton3.bind("<Button-1>", click_3)

def click_2(event):
    print("Boton 2 presionado")
    insertar("2")
boton2.bind("<Button-1>", click_2)

def click_1(event):
    print("Boton 1 presionado")
    insertar("1")
boton1.bind("<Button-1>", click_1)

def click_0(event):
    print("Boton 0 presionado")
    insertar("0")
boton0.bind("<Button-1>", click_0)

# === Funciones para el teclado ===
def key_0(event):
    if event.char == "0":
        print("USTED PRESIONO LA TECLA '0'")
        insertar("0")
ventana.bind("<KeyPress-0>", key_0)

def key_1(event):
    if event.char == "1":
        print("USTED PRESIONO LA TECLA '1'")
        insertar("1")
ventana.bind("<KeyPress-1>", key_1)

def key_2(event):
    if event.char == "2":
        print("USTED PRESIONO LA TECLA '2'")
        insertar("2")
ventana.bind("<KeyPress-2>", key_2)

def key_3(event):
    if event.char == "3":
        print("USTED PRESIONO LA TECLA '3'")
        insertar("3")
ventana.bind("<KeyPress-3>", key_3)

def key_4(event):
    if event.char == "4":
        print("USTED PRESIONO LA TECLA '4'")
        insertar("4")
ventana.bind("<KeyPress-4>", key_4)

def key_5(event):
    if event.char == "5":
        print("USTED PRESIONO LA TECLA '5'")
        insertar("5")
ventana.bind("<KeyPress-5>", key_5)

def key_6(event):
    if event.char == "6":
        print("USTED PRESIONO LA TECLA '6'")
        insertar("6")
ventana.bind("<KeyPress-6>", key_6)

def key_7(event):
    if event.char == "7":
        print("USTED PRESIONO LA TECLA '7'")
        insertar("7")
ventana.bind("<KeyPress-7>", key_7)

def key_8(event):
    if event.char == "8":
        print("USTED PRESIONO LA TECLA '8'")
        insertar("8")
ventana.bind("<KeyPress-8>", key_8)

def key_9(event):
    if event.char == "9":
        print("USTED PRESIONO LA TECLA '9'")
        insertar("9")
ventana.bind("<KeyPress-9>", key_9)

def salir_programa(event):
    ventana.destroy()
    print("Saliendo del programa...")
ventana.bind("<Escape>", salir_programa)

def borrar_datos():
    pantalla.config(state="normal") 
    pantalla.delete(0,tk.END)
    pantalla.config(state="disabled")
    print("Borrando datos...")
boton_borrar.config(command=borrar_datos)

def click_suma(event):
    print(f'Operacion : (+)')
    pantalla.config(state="normal")
    pantalla.insert("end", "+")
boton_suma.bind("<Button-1>", click_suma)

def click_resta(event):
    print(f'Operacion : (-)')
    pantalla.config(state="normal")
    pantalla.insert("end", "-")
boton_resta.bind("<Button-1>", click_resta)

def click_producto(event):
    print(f'Operacion : (*)')
    pantalla.config(state="normal")
    pantalla.insert("end", "*")
boton_producto.bind("<Button-1>", click_producto)

def click_division(event):
    print(f'Operacion : (/)')
    pantalla.config(state="normal")
    pantalla.insert("end", "/")
boton_division.bind("<Button-1>", click_division)



def key_suma(event):
    if event.char == "+":
        print("Operación: (+)")
        pantalla.config(state="normal")
        pantalla.insert("end", "+")
        pantalla.config(state="disabled")
ventana.bind("<KeyPress-+>", key_suma)

def key_resta(event):
    if event.char == "-":
        print("Operación: (-)")
        pantalla.config(state="normal")
        pantalla.insert("end", "-")
        pantalla.config(state="disabled")
ventana.bind("<KeyPress-->", key_resta)

def key_producto(event):
    if event.char == "*":
        print("Operación: (*)")
        pantalla.config(state="normal")
        pantalla.insert("end", "*")
        pantalla.config(state="disabled")
ventana.bind("<KeyPress-*>", key_producto)

def key_division(event):
    if event.char == "/":
        print("Operación: (/)")
        pantalla.config(state="normal")
        pantalla.insert("end", "/")
        pantalla.config(state="disabled")
ventana.bind("<KeyPress-/>", key_division)


def calcular_resultado():
    pantalla.config(state="normal")
    expresion = pantalla.get()  
    try:
        resultado = eval(expresion)  
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        messagebox.showwarning("Error", "No se puede dividir entre 0.")
    except Exception as e:
        messagebox.showerror("Error", "Operación no válida")
        print(f"Error: {e}")
    pantalla.config(state="disabled")

boton_igual.config(command=calcular_resultado)



def key_resultado(event):
    if event.char=="Return":
        pantalla.config(state="normal")
    expresion=pantalla.get()
    try:
        resultado=eval(expresion)
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
        print(f'El resultado es {resultado}')
    except ZeroDivisionError:
        messagebox.showwarning("Error", "No se puede dividir entre 0 ")
    except Exception as e:
        messagebox.showerror("Error", "Operación no válida")
        print(f"Error: {e}")
    pantalla.config(state="disabled")
ventana.bind("<Return>", key_resultado)


ventana.mainloop()
