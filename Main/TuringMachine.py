from automata.tm.mntm import MNTM

# Creamos la máquina de Turing del Wordle

    # FILL
def Wordle_Turing_Machine():
    wordle_tm=MNTM(
        states={'q0', '---' },
        input_symbols={},
        tape_symbols={'#'},
        n_tapes=3,
        transitions={
            # FILL
        },
        initial_state='q0',
        blank_symbol='#',
        final_states={'---'}
    )

# Creamos una función encargada de llamar Turing_Machine_Calling()

def Turing_Machine_Calling(input_str):
    """
    Previo a pasar el input por la máquina de Turing, hacemos uso de lower()
    para que todos los símbolos se encuentren en mínusculas, simplificando la
    máquina de Turing del Wordle.
    """
    lower_input_str = input_str.lower()
    wordle_tm = Wordle_Turing_Machine()

    try:
        wordle_tm_result=wordle_tm.read_input(lower_input_str)
    except:
        print('Ha ingresado un caractér invalido, intente nuevamente')

    print(lower_input_str)

    return lower_input_str