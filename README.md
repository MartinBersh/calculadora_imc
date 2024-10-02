# Cálculo de Índice de Masa Corporal (IMC)

Este proyecto es una aplicación en Python que permite calcular el Índice de Masa Corporal (IMC) de una persona, clasificar el resultado en categorías como "Bajo peso", "Peso normal", "Sobrepeso" o "Obesidad".
## Descripción

El IMC es una medida estándar utilizada para identificar el estado de peso de una persona en función de su peso y altura. Este proyecto consta de dos funciones principales:

- `calcular_imc(peso, altura)`: Calcula el IMC a partir del peso y la altura. Maneja errores si los valores no son válidos.
- `clasificar_imc(imc)`: Clasifica el IMC calculado en una categoría (Bajo peso, Peso normal, Sobrepeso, Obesidad).

### Validaciones
- El peso y la altura deben ser valores positivos.
- Si faltan valores o son negativos, se mostrará un mensaje de error al usuario.

### Pruebas unitarias
Se incluyen varias pruebas para verificar el correcto funcionamiento de las funciones, utilizando el módulo `unittest` y `unittest.mock` para simular los errores.
