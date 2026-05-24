from automata.tm.mntm import MNTM

# Creamos la máquina de Turing del Wordle

def Wordle_Turing_Machine(wordle_input):
    """
    La máquina de Turing siempre cambiará según la cadena del Wordle,
    por ende, no es viable usar una máquina de Turing ya predefinida,
    sino una que se adapte según dicha cadena. Debido a esto, es necesario
    predefinir los alfabetos y manejar las transiciones según la
    cantidad de símbolos para cada palabra, con ayuda de for's.
    """

    if len(wordle_input)==5:
        # wordle_input se usará en forma de array y de conjunto, el array permitirá acceder a las
        # posiciones deseadas, y el conjunto evitará la repetición de símbolos.
        wordle_array = list(wordle_input.lower())
        wordle_set = set(wordle_input.lower())

        # Creación de alfabeto de símbolos y el alfabeto de las cintas
        wordle_alphabet = set('abcdefghijklmnñopqrstuvwxyz')
        tape_alphabet = set('012-#') | wordle_alphabet

        # Creación de un conjunto que contiene todos los elementos del alfabeto excepto aquellos que forman
        # la cadena del wordle
        wa_wout_input = tape_alphabet - wordle_set

        # Creación de la máquina de Turing
        try:
            wordle_tm=None
            wordle_tm = MNTM(
                states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'},
                input_symbols= wordle_alphabet,
                tape_symbols= tape_alphabet,
                n_tapes=2,
                transitions={
                    'q0':{
                        # Transición directa
                        (wordle_array[0], '#'): [('q1', (('1', 'R'), ('-', 'R')))],
                        # Transición para todos los elementos pertenecientes a wordle_set excepto el elemento x_i
                        **{(tape1_symbol, '#'): [('q1', ((tape1_symbol, 'R'), (wordle_array[0], 'R')))]
                           for tape1_symbol in (wordle_set - set(wordle_array[0]))},
                        # Transición para todos los elementos no pertenecientes a wordle_set
                        **{(tape1_symbol, '#'): [('q1', (('0', 'R'), (wordle_array[0], 'R')))]
                           for tape1_symbol in wa_wout_input}
                    },
                    'q1':{
                        (wordle_array[1], '#'): [('q2', (('1', 'R'), ('-', 'R')))],
                        **{(tape1_symbol, '#'): [('q2', ((tape1_symbol, 'R'), (wordle_array[1], 'R')))]
                           for tape1_symbol in (wordle_set - set(wordle_array[1]))},
                        **{(tape1_symbol, '#'): [('q2', (('0', 'R'), (wordle_array[1], 'R')))]
                           for tape1_symbol in wa_wout_input}
                    },
                    'q2': {
                        (wordle_array[2], '#'): [('q3', (('1', 'R'), ('-', 'R')))],
                        **{(tape1_symbol, '#'): [('q3', ((tape1_symbol, 'R'), (wordle_array[2], 'R')))]
                           for tape1_symbol in (wordle_set - set(wordle_array[2]))},
                        **{(tape1_symbol, '#'): [('q3', (('0', 'R'), (wordle_array[2], 'R')))]
                           for tape1_symbol in wa_wout_input}
                    },
                    'q3': {
                        (wordle_array[3], '#'): [('q4', (('1', 'R'), ('-', 'R')))],
                        **{(tape1_symbol, '#'): [('q4', ((tape1_symbol, 'R'), (wordle_array[3], 'R')))]
                           for tape1_symbol in (wordle_set - set(wordle_array[3]))},
                        **{(tape1_symbol, '#'): [('q4', (('0', 'R'), (wordle_array[3], 'R')))]
                           for tape1_symbol in wa_wout_input}
                    },
                    'q4': {
                        (wordle_array[4], '#'): [('q5', (('1', 'N'), ('-', 'N')))],
                        **{(tape1_symbol, '#'): [('q5', ((tape1_symbol, 'N'), (wordle_array[4], 'N')))]
                           for tape1_symbol in (wordle_set - set(wordle_array[4]))},
                        **{(tape1_symbol, '#'): [('q5', (('0', 'N'), (wordle_array[4], 'N')))]
                           for tape1_symbol in wa_wout_input}
                    },
                    'q5': {
                        # Si el símbolo de ambas cintas es blanco, es porque llegaron al inicio de la cinta
                        ('#','#'): [('q6', (('#','R'), ('#', 'R')))],
                        # Las cintas retroceden si ambas leen cualquier símbolo distinto a blanco
                        **{(tape1_symbol, tape2_symbol): [('q5', ((tape1_symbol, 'L'), (tape2_symbol, 'L')))]
                           for tape1_symbol in tape_alphabet - {'#','-'}
                           for tape2_symbol in tape_alphabet - {'#','0','1','2'}},
                        # Puede suceder el caso en el que alguna de las dos cintas llega primero al blanco (disparejos)
                        **{(tape1_symbol, '#'): [('q5', ((tape1_symbol, 'L'), ('#', 'N')))]
                           for tape1_symbol in tape_alphabet - {'#','-'}},
                        **{('#', tape2_symbol): [('q5', (('#', 'N'), (tape2_symbol, 'L')))]
                           for tape2_symbol in tape_alphabet - {'#','0','1','2'}}
                    },
                    'q6':{
                        # Si el símbolo en la primera cinta es un '0', '1' o '2', se omite
                        **{('0', tape2_symbol): [('q6', (('0', 'R'), (tape2_symbol,'N')))]
                           for tape2_symbol in tape_alphabet - {'#','0','1','2'}},
                        **{('1', tape2_symbol): [('q6', (('1', 'R'), (tape2_symbol, 'N')))]
                           for tape2_symbol in tape_alphabet - {'#','0','1','2'}},
                        **{('2', tape2_symbol): [('q6', (('2', 'R'), (tape2_symbol, 'N')))]
                           for tape2_symbol in tape_alphabet - {'#','0','1','2'}},
                        # Si el símbolo en la primera cinta es cualquier símbolo de entrada, debe revisar dicho caso
                        **{(tape1_symbol, tape2_symbol): [('q7', ((tape1_symbol, 'N'), (tape2_symbol, 'N')))]
                           for tape1_symbol in wordle_alphabet
                           for tape2_symbol in tape_alphabet - {'#','0','1','2'}},
                        # Si la primera cinta llega al blanco es porque no hay más símbolos por revisar, acepta
                        **{('#', tape2_symbol): [('q8', (('#', 'N'), (tape2_symbol, 'N')))]
                           for tape2_symbol in tape_alphabet - {'#','0','1','2'}}
                    },
                    'q7':{
                        # Si encuentra un símbolo de entrada igual en ambas cintas, se marca con un '2' en la
                        # primera cinta, y un '-' en la segunda cinta para evitar repeticiones. Vuelve a 'q5'
                        **{(tapeX_symbol, tapeX_symbol): [('q5', (('2', 'N'), ('-', 'N')))]
                           for tapeX_symbol in tape_alphabet - {'#'}},
                        # Mientras no se cumpla la condición anterior, verifique para cada símbolo en la segunda cinta
                        **{(tape1_symbol, tape2_symbol): [('q7', ((tape1_symbol, 'N'), (tape2_symbol, 'R')))]
                           for tape1_symbol in wordle_alphabet
                           for tape2_symbol in tape_alphabet - {'#','0','1','2'}
                           if tape1_symbol != tape2_symbol},
                        # Si no encontro símbolos iguales para ambas cintas, ya no quedan más símbolos por repetir,
                        # marca '0'. Vuelve a 'q5'
                        **{(tape1_symbol, '#'): [('q5', (('0','N'), ('#', 'L')))]
                           for tape1_symbol in wordle_alphabet}
                    }
                },
                initial_state='q0',
                blank_symbol='#',
                final_states={'q8'},
            )
        except Exception as e:
            print(f'Error: {e}')
            return None

        return wordle_tm

    else:
        print("La longitud de la cadena ingresada en Wordle_Turing_Machine es diferente a la requerida")

        return None


def Turing_Machine_Calling(input_str, wordle_input):
    if len(input_str) == 5:
        input_str = input_str.lower()
        wordle_tm = Wordle_Turing_Machine(wordle_input)
        
        # Leemos la configuración final de la MT
        final_config = wordle_tm.read_input(input_str).pop()
        
        # Extraemos lo que quedó escrito en la primera cinta (Tapes[0])
        # Filtramos para obtener solo los '0', '1' y '2' correspondientes a las 5 letras
        tape_result = [char for char in final_config.tapes[0].tape if char in ['0', '1', '2']]
        return tape_result
    else:
        return None
