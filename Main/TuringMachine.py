from automata.tm.mntm import MNTM

# Creamos la máquina de Turing del Wordle

def Wordle_Turing_Machine(wordle_input):
    """
    La máquina de Turing siempre cambiará según la palabra del Wordle,
    por ende, no es viable usar una máquina de Turing ya predefinida,
    sino una que se adapte según la palabra del Wordle.
    """

    # Convertimos el wordle_input en un array donde cada elemento representará cada símbolo.
    wordle_input = wordle_input.lower()
    wordle_array = list(wordle_input)

    #La maquina de Turing no puede determinar que símbolos contiene wordle_array, deben especificarse, previo a su implementación
    wordle_alphabet = set('abcdefghijklmnñopqrstuvwxyz')
    wordle_alphabet |= set(wordle_array)

    tape_alphabet = set('012-#')
    tape_alphabet |= set(wordle_alphabet.copy())

    not_wordle_alphabet = wordle_alphabet - set(wordle_array)

    """
    Revisar como realizar las transiciones mediante uso de fors 
    """

    wordle_tm=MNTM(
        states={'q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11'},
        input_symbols=wordle_alphabet,
        tape_symbols=tape_alphabet,
        n_tapes=3,
        transitions={

        },
        initial_state='q0',
        blank_symbol='#',
        final_states={'---'}
    )

    return wordle_tm

# Creamos una función encargada de llamar Wordle_Turing_Machine() con nuestra palabra a descifrar

def Turing_Machine_Calling(input_str, wordle_input):
    """
    Previo a pasar el input por la máquina de Turing, hacemos uso de lower()
    para que todos los símbolos se encuentren en mínusculas, simplificando la
    máquina de Turing del Wordle.
    """
    input_str = input_str.lower()
    wordle_tm = Wordle_Turing_Machine(wordle_input)

    try:
        wordle_tm_result=wordle_tm.read_input(input_str)
    except:
        print('Ha ingresado un caractér invalido, intente nuevamente')

    print(input_str)

    return input_str