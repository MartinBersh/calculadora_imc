import tkinter as tk
from tkinter import messagebox
from calculo_imc import calcular_imc, clasificar_imc


def calcular():
    try:
        peso = float(entrada_peso.get())
        altura = float(entry_altura.get())

        imc = calcular_imc(peso, altura)

        if imc is not None:
            clasificacion = clasificar_imc(imc)
            resultado_var.set(f"El IMC es: {imc:.1f}\nClasificación: {clasificacion}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")


ventana = tk.Tk()
ventana.title("Cálculo de IMC")

label_peso = tk.Label(ventana, text="Peso (kg):")
label_peso.pack(pady=5)

entrada_peso = tk.Entry(ventana)
entrada_peso.pack(pady=5)

label_altura = tk.Label(ventana, text="Altura (m):")
label_altura.pack(pady=5)

entry_altura = tk.Entry(ventana)
entry_altura.pack(pady=5)

boton_calcular = tk.Button(ventana, text="Calcular IMC", command=calcular)
boton_calcular.pack(pady=10)

resultado_var = tk.StringVar()
label_resultado = tk.Label(ventana, textvariable=resultado_var)
label_resultado.pack(pady=5)

ventana.mainloop()
