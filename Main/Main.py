from TuringMachine import Turing_Machine_Calling
import random
import os

def main():
    ruta = os.path.join(os.path.dirname(_file_), "..", "Words.txt")
    with open(ruta, "r") as f:
        palabras = [line.strip() for line in f if line.strip()]
    palabra_secreta = random.choice(palabras)
    intentos = 6
    for i in range(intentos):
        palabra = input(f"Intento {i+1}/{intentos} - Ingresa una palabra de 5 letras: ")
        if len(palabra) != 5:
            print("La palabra debe tener 5 letras")
            continue
        resultado = Turing_Machine_Calling(palabra, palabra_secreta)
        if resultado is None:
            print("Error en la simulación")
            continue
        resultado_str = "".join(resultado)
        print(f"Resultado: {resultado_str}")
        if resultado_str == "11111":
            print("Ganaste!")
            return
    print(f"Perdiste! La palabra era: {palabra_secreta}")

if __name__ == "__main__":
    main()
