import math

def evaluar(expresion):
    try:
        return str(eval(expresion))
    except:
        return "Error"


def traducir_input(texto, valor):
    if valor == "√":
        return texto + "math.sqrt("
    elif valor == "sin":
        return texto + "math.sin("
    elif valor == "cos":
        return texto + "math.cos("
    elif valor == "tan":
        return texto + "math.tan("
    elif valor == "log":
        return texto + "math.log10("
    elif valor == "^":
        return texto + "**"
    else:
        return texto + valor
