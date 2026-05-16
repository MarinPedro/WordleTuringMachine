from automata.tm.mntm import MNTM

# Creamos la máquina de Turing del Wordle

def Wordle_Turing_Machine(wordle_input):
    """
    La máquina de Turing siempre cambiará según la palabra del Wordle,
    por ende, no es viable usar una máquina de Turing ya predefinida,
    sino una que se adapte según la palabra del Wordle. Debido a esto,
    es necesario definir los alfabetos y transiciones previo a la creación
    de la máquina de Turing.
    """

    if len(wordle_input)==5:
        # Convertimos el wordle_input en un array donde cada elemento representará cada símbolo.
        wordle_input = wordle_input.lower()
        wordle_array = list(wordle_input)

        # Creamos los alfabetos
        wordle_alphabet = set('abcdefghijklmnñopqrstuvwxyz')
        wordle_alphabet |= set(wordle_array)

        tape_alphabet = set('012-#')
        tape_alphabet |= set(wordle_alphabet.copy())

        alphabet_wout_array = wordle_alphabet - set(wordle_array)

        # Los for's nos permitirán definir las transiciones sin importar cuál sea la palabra
        chain_length = len(wordle_array)

        for i in range(0, chain_length):
            current_state = f'q{i}'
            next_state = f'q{i + 1}'

        wordle_tm = MNTM(
            states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11'},
            input_symbols=wordle_alphabet,
            tape_symbols=tape_alphabet,
            n_tapes=2,
            transitions={
                'q0': {
                    (wordle_array[0], '#'): [('q0'), (('a', 'R'), ('#', 'R'))],
                },
            },
            initial_state='q0',
            blank_symbol='#',
            final_states={'---'}
        )

        return wordle_tm

    else:
        print("Error idk")
        return None


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