import tkinter as tk
from tkinter import font, messagebox
import random
import os
from TuringMachine import Turing_Machine_Calling
class WordleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle TM")
        self.root.configure(bg="#FFFFFF") # fondo blanco
        self.root.resizable(True, True)
        self.root.state('zoomed') # para que la ventana se abra maximizada
        self.cargar_palabras()
        self.palabra_objetivo = random.choice(self.palabras).lower()
        self.fila_actual = 0
        self.col_actual = 0
        self.casillas = []
        # Centrar el contenedor principal
        self.contenedor_principal = tk.Frame(self.root, bg="#FFFFFF")
        self.contenedor_principal.pack(expand=True)
        self.configurar_interfaz()
        self.root.bind("<Key>", self.teclado_fisico)
    def configurar_interfaz(self):
        fuente_titulo = font.Font(family="Georgia", size=26, weight="bold")
        lbl_titulo = tk.Label(
            self.contenedor_principal, 
            text="LA PALABRA DEL DÍA", 
            font=fuente_titulo, 
            bg="#FFFFFF", 
            fg="#111111"
        )
        lbl_titulo.pack(pady=(15, 20))
        # Cuadrícula de juego (6x5)
        frame_grid = tk.Frame(self.contenedor_principal, bg="#FFFFFF")
        frame_grid.pack(pady=10)
        for r in range(6):
            fila_casillas = []
            for c in range(5):
                frame_borde = tk.Frame(frame_grid, bg="#D3D6DA", width=62, height=62)
                frame_borde.grid(row=r, column=c, padx=5, pady=5)
                frame_borde.pack_propagate(False)
                lbl_letra = tk.Label(
                    frame_borde, 
                    text="", 
                    font=("Helvetica Neue", 24, "bold"), 
                    bg="#FFFFFF", 
                    fg="#000000"
                )
                lbl_letra.pack(fill=tk.BOTH, expand=True, padx=2, pady=2) 
                fila_casillas.append((frame_borde, lbl_letra))
            self.casillas.append(fila_casillas)
        self.actualizar_borde_morado()
        # Etiqueta para el contador de intentos, va debajo de la cuadrícula
        self.lbl_intentos = tk.Label(
            self.contenedor_principal,
            text="Intento: 1 / 6",
            font=("Helvetica", 16, "bold"),
            bg="#FFFFFF",
            fg="#555555"
        )
        self.lbl_intentos.pack(pady=(30, 10))
    def actualizar_borde_morado(self):
        # Manejo de bordes por defecto (gris claro o gris oscuro si tiene letra)
        for r in range(6):
            for c in range(5):
                if self.casillas[r][c][1].cget("bg") == "#FFFFFF":
                    if self.casillas[r][c][1].cget("text") != "":
                        self.casillas[r][c][0].configure(bg="#878A8C")
                    else:
                        self.casillas[r][c][0].configure(bg="#D3D6DA")
        # Aplicar borde morado exclusivamente a la celda vacía actual enfocada
        if self.fila_actual < 6 and self.col_actual < 5:
            self.casillas[self.fila_actual][self.col_actual][0].configure(bg="#800080")
    def teclado_fisico(self, event):
        char = event.char.upper()
        keysym = event.keysym
        if keysym == "BackSpace":
            self.borrar_letra()
        elif keysym == "Return":
            self.evaluar_palabra()
        elif char.isalpha() or char == 'Ñ':
            self.escribir_letra(char)
    def escribir_letra(self, char):
        if self.col_actual < 5 and self.fila_actual < 6:
            _, lbl = self.casillas[self.fila_actual][self.col_actual]
            lbl.configure(text=char)
            self.col_actual += 1
            self.actualizar_borde_morado()
    def borrar_letra(self):
        if self.col_actual > 0:
            self.col_actual -= 1
            _, lbl = self.casillas[self.fila_actual][self.col_actual]
            lbl.configure(text="")
            self.actualizar_borde_morado()
    def evaluar_palabra(self):
        if self.col_actual < 5:
            return  # Esperar a que la palabra de 5 letras esté completa
        palabra_ingresada = "".join(
            self.casillas[self.fila_actual][c][1].cget("text") for c in range(5)
        ).lower()
        # Llamar a la MT
        resultado_mt = Turing_Machine_Calling(palabra_ingresada, self.palabra_objetivo)
        if not resultado_mt or len(resultado_mt) < 5:
            messagebox.showwarning("Error", "La simulación del autómata no retornó una configuración válida.")
            return
        COLOR_VERDE = "#6AAA64"
        COLOR_AMARILLO = "#C9B458"
        COLOR_GRIS = "#787C7E"
        # Pintar las casillas según el vector resultante de la MT
        for c in range(5):
            frame_borde, lbl_letra = self.casillas[self.fila_actual][c]
            estado = resultado_mt[c]
            if estado == '1':
                color_final = COLOR_VERDE
            elif estado == '2':
                color_final = COLOR_AMARILLO
            else:
                color_final = COLOR_GRIS
            frame_borde.configure(bg=color_final)
            lbl_letra.configure(bg=color_final, fg="#FFFFFF")
        # Validar el intento
        if palabra_ingresada == self.palabra_objetivo:
            self.root.unbind("<Key>")
            if messagebox.askyesno("¡Ganaste!", f"¡Adivinaste! La palabra era {self.palabra_objetivo.upper()}\n¿Quieres jugar de nuevo?"):
                self.reiniciar_juego()
        elif self.fila_actual == 5:
            self.root.unbind("<Key>")
            if messagebox.askyesno("Fin del juego", f"Se agotaron los intentos. La palabra era: {self.palabra_objetivo.upper()}\n¿Quieres jugar de nuevo?"):
                self.reiniciar_juego()
        else:
            # Pasar al siguiente intento
            self.fila_actual += 1
            self.col_actual = 0
            self.actualizar_borde_morado()
            # Actualizar el contador dinámico de intentos
            self.lbl_intentos.configure(text=f"Intento: {self.fila_actual + 1} / 6")

    def cargar_palabras(self):
        ruta = os.path.join(os.path.dirname(__file__), "Words.txt")
        with open(ruta, "r") as f:
            self.palabras = [line.strip() for line in f if line.strip()]

    def reiniciar_juego(self):
        self.palabra_objetivo = random.choice(self.palabras).lower()
        self.fila_actual = 0
        self.col_actual = 0
        for r in range(6):
            for c in range(5):
                frame_borde, lbl_letra = self.casillas[r][c]
                lbl_letra.configure(text="", bg="#FFFFFF", fg="#000000")
                frame_borde.configure(bg="#D3D6DA")
        self.lbl_intentos.configure(text="Intento: 1 / 6")
        self.actualizar_borde_morado()
        self.root.bind("<Key>", self.teclado_fisico)

if __name__ == "__main__":
    root = tk.Tk()
    app = WordleGUI(root)
    root.mainloop()
