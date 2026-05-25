# Wordle Turing Machine

🇺🇸 [English](#seccion-english) | 🇪🇸 [Español](#seccion-espanol)

---

<a name="seccion-english"></a>
## English

This repository was made with the purpose of using a Turing Machine to model the original [Wordle](https://www.nytimes.com/games/wordle/index.html) created by Josh Wardle.
The word list the project uses was taken from the following [repository](https://github.com/lorenbrichter/Words?tab=readme-ov-file).

### How to run

If you want to run the repository, first, clone the repository:

```bash
git clone https://github.com/MarinPedro/WordleTuringMachine.git
```

Then check for the dependencies required to run the project.

### Installing dependencies
This project uses automata-lib for modeling the Turing Machine, so it is required to install its dependencies in order to test it; you can download them with the following command:

```bash
pip install automata-lib
```

The project also uses tkinter for GUI elements. For Windows users, tkinter is usually included within Python, however, in Linux distros and MacOS systems, this is not always the case.

### How to check and download tkinter dependencies

- In order to check if your system has installed the tkinter dependencies, run the following command:
  
  ```bash
  python3 -m tkinter
  ```
  
  This will check for the tkinter dependencies, if they are installed properly, you are good to go. If not, you can download them with the following commands, depending of what system you are using:

  - Linux (Debian/Ubuntu/Linux Mint):
    
    ```bash
    sudo apt install python3-tk
    ```
  - Linux (Fedora):
    
    ```bash
    sudo dnf install python3-tkinter
    ```
  - Linux (Arch):
    
    ```bash
    sudo pacman -S tk
    ```
  - MacOS (homebrew installation):
    
    ```bash
    brew install python-tk
    ```
  - MacOS (python.org installation): tkinter is included, no command needed

Once you have downloaded the tkinter and automata-lib dependencies, run the following commands:

```bash
cd WordleTuringMachine
python3 Main/Main.py
```

And you are ready to go, have fun testing!

---

<a name="seccion-espanol"></a>
## Español

Este repositorio fue creado con el propósito de usar una Máquina de Turing para modelar el [Wordle](https://www.nytimes.com/games/wordle/index.html) original creado por Josh Wardle.
La lista de palabras que usa el proyecto fueron tomadas del siguiente [repositorio](https://github.com/lorenbrichter/Words?tab=readme-ov-file).

### Cómo ejecutar
Para ejecutar el repositorio, primero clónalo:

```bash
git clone https://github.com/MarinPedro/WordleTuringMachine.git
```

Luego verifica las dependencias necesarias para ejecutar el proyecto.

### Instalación de dependencias

Este proyecto usa automata-lib para modelar la Máquina de Turing, por lo que es necesario instalar sus dependencias; puedes descargarlas con el siguiente comando:

```bash
pip install automata-lib
```

El proyecto también usa tkinter para los elementos de la interfaz gráfica. Para usuarios de Windows, tkinter generalmente viene incluido con Python, sin embargo, en distribuciones de Linux y MacOS no siempre es el caso.

### Cómo verificar e instalar las dependencias de tkinter

- Para verificar si tu sistema tiene instaladas las dependencias de tkinter, ejecuta el siguiente comando:
  
```bash
python3 -m tkinter
```
  
  Esto verificará las dependencias de tkinter. Si están instaladas correctamente, puedes directamente ejecutar el projecto. Si no, puedes descargarlas con los siguientes comandos según tu sistema:
  - Linux (Debian/Ubuntu/Linux Mint):
    
  ```bash
  sudo apt install python3-tk
  ```
  - Linux (Fedora):
    
  ```bash
  sudo dnf install python3-tkinter
  ```
  - Linux (Arch):
    
  ```bash
  sudo pacman -S tk
  ```
  - MacOS (instalación con Homebrew):
    
  ```bash
  brew install python-tk
  ```
  - MacOS (instalación desde python.org): tkinter viene incluido, no se necesita ningún comando
    
Una vez descargadas las dependencias de tkinter y automata-lib, ejecuta los siguientes comandos:

```bash
cd WordleTuringMachine
python3 Main/Main.py
```

¡Y listo, diviertete probando!
