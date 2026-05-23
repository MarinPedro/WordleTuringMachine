import tkinter as tk
from tkinter import font, messagebox  #font nos permite elegir el tipo de letra y messagebox nos permite mostrar mensajes a través de una ventana emergente
import random  #para escoger la palabra secreta de forma aleatoria
import os
from TuringMachine import Turing_Machine_Calling
class WordleGUI:
    def __init__(self, root):   #root es la ventana de Tkinter
        self.root = root
        self.root.title("Wordle TM")
        self.root.configure(bg="#FFFFFF") # la ventana tiene fondo blanco
        self.root.resizable(True, True) # le indica al gestor de ventanas que SÍ se puede redimensionar en ancho y en alto
        self.root.state('zoomed') #para que la ventana esté maximizada desde el principio
        self.cargar_palabras()
        self.palabra_secreta = random.choice(self.palabras).lower()  #elige la palabra al azar y la convierte en minúsculas
        self.fila_actual = 0
        self.col_actual = 0
        self.casillas = []
        #creamos un contenedor invisible que agrupa a todos los elementos visuales del juego
        self.botones_teclado = {}
        self.contenedor_principal = tk.Frame(self.root, bg="#FFFFFF")
        self.contenedor_principal.pack(expand=True) #se expande el marco y queda centrado
        self.configurar_interfaz()  #este metodo dibujará los titulos, la cadricula, etc.
        self.root.bind("<Key>", self.teclado_fisico) #vincula el teclado físico
    def configurar_interfaz(self):
        fuente_titulo = font.Font(family="Georgia", size=26, weight="bold")
        lbl_titulo = tk.Label(
            self.contenedor_principal,
            text="LA PALABRA DEL DÍA",
            font=fuente_titulo,
            bg="#FFFFFF",
            fg="#111111"
        )
        lbl_titulo.pack(pady=(15, 20))  #añade 15 pixeles de espacio libre arriba del título y 20 abajo
        #cuadrícula de juego (6x5)
        frame_grid = tk.Frame(self.contenedor_principal, bg="#FFFFFF")  #creamos un subcontenedor para los cuadros del juego
        frame_grid.pack(pady=10) # está separado de lo demás por 10 píxeles arriba y abajo
        for r in range(6):
            fila_casillas = []
            for c in range(5):
                frame_borde = tk.Frame(frame_grid, bg="#D3D6DA", width=62, height=62)
                frame_borde.grid(row=r, column=c, padx=5, pady=5)
                frame_borde.pack_propagate(False) #evita que el cuadro cambie de tamaño
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
        #etiqueta para el contador de intentos
        self.lbl_intentos = tk.Label(
            self.contenedor_principal,
            text="Intento: 1 / 6",
            font=("Helvetica", 16, "bold"),
            bg="#FFFFFF",
            fg="#555555"
        )
        self.lbl_intentos.pack(pady=(30, 10))
        self.crear_teclado_virtual()
    def crear_teclado_virtual(self):
        frame_teclado = tk.Frame(self.contenedor_principal, bg="#FFFFFF")
        frame_teclado.pack(pady=10)

        filas_letras = [
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L", "Ñ"],
            ["ENTER", "Z", "X", "C", "V", "B", "N", "M", "BORRAR"]
        ]

        fuente_teclado = font.Font(family="Helvetica Neue", size=12, weight="bold")

        for fila in filas_letras:
            fila_frame = tk.Frame(frame_teclado, bg="#FFFFFF")
            fila_frame.pack(pady=3)

            for letra in fila:
                ancho_boton = 6 if letra in ["ENTER", "BORRAR"] else 3

                def crear_comando(l=letra):
                    return lambda: self.teclado_virtual_click(l)

                btn = tk.Button(
                    fila_frame,
                    text=letra,
                    font=fuente_teclado,
                    bg="#D3D6DA",
                    fg="#000000",
                    width=ancho_boton,
                    height=2,
                    relief="flat",  #estilo plano, sin bordes 3D
                    command=crear_comando()
                )
                btn.pack(side=tk.LEFT, padx=3)

                letra_limpia = letra.strip().upper()
                if letra_limpia not in ["ENTER", "BORRAR"]:
                    self.botones_teclado[letra_limpia] = btn
    def teclado_virtual_click(self, letra):
        if letra == "BORRAR":
            self.borrar_letra()
        elif letra == "ENTER":
            self.evaluar_palabra()
        else:
            self.escribir_letra(letra)
    def actualizar_borde_morado(self):
        #bordes por defecto (gris claro o gris oscuro si tiene letra)
        for r in range(6):
            for c in range(5):
                if self.casillas[r][c][1].cget("bg") == "#FFFFFF":
                    if self.casillas[r][c][1].cget("text") != "":
                        self.casillas[r][c][0].configure(bg="#878A8C")
                    else:
                        self.casillas[r][c][0].configure(bg="#D3D6DA")
        #aplicar borde morado exclusivamente a la celda actual que está vacía
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
            return  #espera a que la palabra esté completa
        palabra_ingresada = "".join(
            self.casillas[self.fila_actual][c][1].cget("text") for c in range(5)
        ).lower()
        #llamamos a la MT
        resultado_mt = Turing_Machine_Calling(palabra_ingresada, self.palabra_secreta)
        if not resultado_mt or len(resultado_mt) < 5:
            messagebox.showwarning("Error", "No retornó una configuración válida.")
            return
        COLOR_VERDE = "#6AAA64"
        COLOR_AMARILLO = "#C9B458"
        COLOR_GRIS = "#787C7E"

        #diccionario temporal para calcular el mejor estado de cada letra en ESTE intento
        estados_letras_intento = {}

        #pintar la cuadricula
        for c in range(5):
            frame_borde, lbl_letra = self.casillas[self.fila_actual][c]
            letra_pulsada = palabra_ingresada[c].upper()
            estado = resultado_mt[c]

            if estado == '1':
                color_final = COLOR_VERDE
            elif estado == '2':
                color_final = COLOR_AMARILLO
            else:
                color_final = COLOR_GRIS

            frame_borde.configure(bg=color_final)
            lbl_letra.configure(bg=color_final, fg="#FFFFFF")

            #guardamos el estado con mayor prioridad para el teclado
            #verde (1) > amarillo (2) > gris (cualquier otro)
            if letra_pulsada not in estados_letras_intento:
                estados_letras_intento[letra_pulsada] = estado
            else:
                estado_anterior = estados_letras_intento[letra_pulsada]
                if estado == '1' or (estado == '2' and estado_anterior != '1'):
                    estados_letras_intento[letra_pulsada] = estado

        #actualiza los botones del teclado segun lo anterior
        for letra_pulsada, estado in estados_letras_intento.items():
            if letra_pulsada in self.botones_teclado:
                btn = self.botones_teclado[letra_pulsada]
                color_actual_btn = btn.cget("bg")
                #si el botón es verde en el teclado general, nada lo puede cambiar
                if color_actual_btn == COLOR_VERDE:
                    continue
                if estado == '1':
                    btn.configure(bg=COLOR_VERDE, fg="#FFFFFF")
                elif estado == '2':
                    btn.configure(bg=COLOR_AMARILLO, fg="#FFFFFF")
                else:
                    #solo se vuelve gris si no era ya amarillo
                    if color_actual_btn != COLOR_AMARILLO:
                        btn.configure(bg=COLOR_GRIS, fg="#FFFFFF")
        #validamos el intento
        if palabra_ingresada == self.palabra_secreta:
            self.root.unbind("<Key>")
            if messagebox.askyesno("¡Adiviniste!", f"La palabra era {self.palabra_secreta.upper()}\n¿Quieres jugar de nuevo?"):
                self.reiniciar_juego()
        elif self.fila_actual == 5:
            self.root.unbind("<Key>")
            if messagebox.askyesno("Fin del juego", f"Se agotaron los intentos. La palabra era: {self.palabra_secreta.upper()}\n¿Quieres jugar de nuevo?"):
                self.reiniciar_juego()
        else:
            #para pasar al siguiente intento
            self.fila_actual += 1
            self.col_actual = 0
            self.actualizar_borde_morado()
            #actualizamos el contador de intentos
            self.lbl_intentos.configure(text=f"Intento: {self.fila_actual + 1} / 6")
    def cargar_palabras(self):
        ruta = os.path.join(os.path.dirname(__file__), "..", "Words.txt")
        with open(ruta, "r") as f:
            self.palabras = [line.strip() for line in f if line.strip()]
    def reiniciar_juego(self):
        self.palabra_secreta = random.choice(self.palabras).lower()
        self.fila_actual = 0
        self.col_actual = 0
        for r in range(6):
            for c in range(5):
                frame_borde, lbl_letra = self.casillas[r][c]
                lbl_letra.configure(text="", bg="#FFFFFF", fg="#000000")
                frame_borde.configure(bg="#D3D6DA")

        for btn in self.botones_teclado.values():
            btn.configure(bg="#D3D6DA", fg="#000000")

        self.lbl_intentos.configure(text="Intento: 1 / 6")
        self.actualizar_borde_morado()
        self.root.bind("<Key>", self.teclado_fisico)

if __name__ == "__main__":
    root = tk.Tk()
    app = WordleGUI(root)
    root.mainloop()
