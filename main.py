from tkinter import messagebox
import tkinter.simpledialog as simpledialog
from operations import plus, subtraction, division, multiply, showArray

band = True


def getX():
    x = simpledialog.askstring("Primer valor", "Ingrese el primer número")
    return x

def getY():
    y = simpledialog.askstring("Segundo valor", "Ingrese el segundo número")
    return y

def result(number):
    messagebox.showinfo("Resultado", f"El resultado de la operación es {number}")

while band:
    var = simpledialog.askstring("Calculadora simple", "Ingrese lo que desea hacer:\n 1.Sumar \n 2.Restar \n 3.Multiplicar \n 4.Dividir \n 5.Historial \n 6.Salir")

    if int(var) == 1:
        sum_result = plus(getX(), getY())
        result(sum_result)
    elif int(var) == 2:
        sub_result = subtraction(getX(), getY())
        result(sub_result)
    elif int(var) == 3:
        mult_result = multiply(getX(), getY())
        result(mult_result)
    elif int(var) == 4:
        div_result = division(getX(), getY())
        result(div_result)
    elif int(var) == 5:
        showArray()
    elif int(var) == 6:
        band = False
    
