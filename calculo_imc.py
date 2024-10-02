from tkinter import messagebox  # Importa el módulo messagebox de tkinter para mostrar mensajes de error.


def calcular_imc(peso, altura):

    try:
        # Verifica si el peso o la altura son nulos (None).
        if peso is None or altura is None:
            raise ValueError("El peso y la altura son requeridos.")  # Lanza un error si faltan los valores.

        # Verifica si el peso y la altura son positivos.
        if peso <= 0 or altura <= 0:
            raise ValueError(
                "El peso y la altura deben ser valores positivos.")  # Lanza un error si los valores son negativos o cero.

        # Calcula el IMC utilizando la fórmula: peso / (altura ^ 2)
        imc = peso / (altura ** 2)

        # Retorna el valor calculado del IMC.
        return imc
    except ValueError as e:
        # Muestra un mensaje de error en una ventana emergente en caso de un ValueError.
        messagebox.showerror("Error", str(e))

        # Retorna None si ocurre un error.
        return None


def clasificar_imc(imc):
    # Clasificación del IMC basada en los rangos establecidos por la OMS.

    # Si el IMC es menor que 18.5, la clasificación es "Bajo peso".
    if imc < 18.5:
        return "Bajo peso"

    # Si el IMC está entre 18.5 y 24.9, la clasificación es "Peso normal".
    elif 18.5 <= imc < 24.9:
        return "Peso normal"

    # Si el IMC está entre 25 y 29.9, la clasificación es "Sobrepeso".
    elif 25 <= imc < 29.9:
        return "Sobrepeso"

    # Si el IMC es mayor o igual a 30, la clasificación es "Obesidad".
    else:
        return "Obesidad"
