from tkinter import messagebox

class History:
    def __init__(self, name, result):
        self.name = name
        self.result = result

array = []

def plus(x, y):
    var = float(x) + float(y)
    history = History('Suma', var)
    array.append(history)
    return var

def subtraction(x, y):
    sub = float(x) - float(y)
    history = History('Resta', sub)
    array.append(history)
    return sub

def division(x, y):
    div = float(x) / float(y)
    history = History('División', div)
    array.append(history)
    return div

def multiply(x, y):
    mult = float(x) * float(y)
    history = History('Multiplicación', mult)
    array.append(history)
    return mult

def showArray():
    array_str = ""
    for item in array:
        array_str += f"Nombre: {item.name}, Resultado: {item.result}\n"
        
    messagebox.showinfo("Historial de calculos", array_str)
