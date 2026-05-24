# Wordle Turing Machine
This repository was made with the purpose of using a Turing Machine to model the original [Wordle](https://www.nytimes.com/games/wordle/index.html) created by Josh Wardle.
The word list the project uses was taken from the following [repository](https://github.com/lorenbrichter/Words?tab=readme-ov-file).

## How to run

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
