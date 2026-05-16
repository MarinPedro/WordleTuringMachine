from automata.tm.mntm import MNTM

# Creamos la máquina de Turing del Wordle

def Wordle_Turing_Machine(wordle_input):
    """
    La máquina de Turing siempre cambiará según la cadena del Wordle,
    por ende, no es viable usar una máquina de Turing ya predefinida,
    sino una que se adapte según dicha cadena. Debido a esto,es necesario
    predefinir los alfabetos y manejar las transiciones según la
    cantidad de símbolos para cada palabra, con ayuda de for's.
    """

    if len(wordle_input)==5:
        # wordle_input se usara en forma de array y de conjunto, el array permitirá acceder a las
        # posiciones deseadas, y el conjunto evitará la repetición de símbolos.
        wordle_array = list(wordle_input.lower())
        wordle_set = set(wordle_input.lower())

        # Creación de alfabeto de símbolos y el alfabeto de las cintas
        wordle_alphabet = set('abcdefghijklmnñopqrstuvwxyz')
        tape_alphabet = set('012-#') | wordle_alphabet

        # Creación de un vector que contiene todos los elementos del alfabeto excepto aquellos que forman
        # la cadena del wordle
        wa_wout_input = list(wordle_alphabet - set(wordle_array))

        # Creación de la máquina de Turing
        wordle_tm = MNTM(
            states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
            input_symbols= wordle_alphabet,
            tape_symbols= tape_alphabet,
            n_tapes=2,
            transitions={
                'q0':{
                    # Transición directa
                    (wordle_array[0], '#'): [('q1', (('1', 'R'), ('-', 'R')))],
                    # Transición para todos los elementos pertenecientes a wordle_set excepto el elemento x_i
                    **{(current_symbol, '#'): [('q1', ((current_symbol, 'R'), (wordle_array[0], 'R')))]
                       for current_symbol in (wordle_set - set(wordle_array[0]))},
                    # Transición para todos los elementos no pertenecientes a wordle_set
                    **{(current_symbol, '#'): [('q1', (('0', 'R'), (wordle_array[0], 'R')))]
                       for current_symbol in wa_wout_input}
                },
                'q1':{
                    (wordle_array[1], '#'): [('q2', (('1', 'R'), ('-', 'R')))],
                    **{(current_symbol, '#'): [('q2', ((current_symbol, 'R'), (wordle_array[1], 'R')))]
                       for current_symbol in (wordle_set - set(wordle_array[1]))},
                    **{(current_symbol, '#'): [('q2', (('0', 'R'), (wordle_array[1], 'R')))]
                       for current_symbol in wa_wout_input}
                },
                'q2': {
                    (wordle_array[2], '#'): [('q3', (('1', 'R'), ('-', 'R')))],
                    **{(current_symbol, '#'): [('q3', ((current_symbol, 'R'), (wordle_array[2], 'R')))]
                       for current_symbol in (wordle_set - set(wordle_array[2]))},
                    **{(current_symbol, '#'): [('q3', (('0', 'R'), (wordle_array[2], 'R')))]
                       for current_symbol in wa_wout_input}
                },
                'q3': {
                    (wordle_array[3], '#'): [('q4', (('1', 'R'), ('-', 'R')))],
                    **{(current_symbol, '#'): [('q4', ((current_symbol, 'R'), (wordle_array[3], 'R')))]
                       for current_symbol in (wordle_set - set(wordle_array[3]))},
                    **{(current_symbol, '#'): [('q4', (('0', 'R'), (wordle_array[3], 'R')))]
                       for current_symbol in wa_wout_input}
                },
                'q4': {
                    (wordle_array[4], '#'): [('q5', (('1', 'R'), ('-', 'R')))],
                    **{(current_symbol, '#'): [('q5', ((current_symbol, 'R'), (wordle_array[4], 'R')))]
                       for current_symbol in (wordle_set - set(wordle_array[4]))},
                    **{(current_symbol, '#'): [('q5', (('0', 'R'), (wordle_array[4], 'R')))]
                       for current_symbol in wa_wout_input}
                },
            },
            initial_state='q0',
            blank_symbol='#',
            final_states={'q5'}
        )

        return wordle_tm

    else:
        print("La longitud de la cadena ingresada en Wordle_Turing_Machine es diferente a la requerida")

        return None


def Turing_Machine_Calling(input_str, wordle_input):

    try:
        input_str = input_str.lower()
        wordle_tm = Wordle_Turing_Machine(wordle_input)

        wordle_tm_result=wordle_tm.read_input(input_str)
        print(wordle_tm_result)

    except Exception as e:
        print(f'Error: {e}')