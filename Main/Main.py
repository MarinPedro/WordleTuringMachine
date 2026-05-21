from TuringMachine import Turing_Machine_Calling
import random
from Words import words

def main():
    palabra_secreta = random.choice(words)
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
