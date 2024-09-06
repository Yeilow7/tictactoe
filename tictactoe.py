"""
Tic Tac Toe Player
"""
# Importar librerias nescesarias
import math
import copy

X = "X"
O = "O"
EMPTY = None


# Inicializar la tablar por defecto
def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_cont = 0
    o_cont = 0  # contar cuantas jugadas lleva cada jugador
    for i in board:
        for j in i:
            if j == X:
                x_cont += 1
            if j == O:
                o_cont += 1
    # Asignar a que jugador le toca
    if x_cont > o_cont:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_s = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action_s.add((i, j))
    # retorna todos los movimientos posibles en el tablero
    return action_s


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid Action!")
    # Crear copia profunda
    board_copy = copy.deepcopy(board)

    board_copy[action[0]][action[1]] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win = utility(board)
    # darle un valor a la victoria en cada caso (X, O)
    if win == 1:
        return X
    elif win == -1:
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Verificar si hay algun ganador
    if winner(board) is not None:
        return True
    # Comprobar si hay algun lugar sin marcar
    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Comprobar si hay algun ganador en lines
    # row
    for row in board:
        if row.count(X) == 3:
            return 1
        elif row.count(O) == 3:
            return -1
    # Comprobar si hay algun ganador en columnas
    # columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            if board[0][i] == X:
                return 1
            elif board[0][i] == O:
                return -1

    # Comprobar si hay algun ganador en diagonales
    # diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        if board[0][0] == X:
            return 1
        elif board[0][0] == O:
            return -1
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        if board[0][2] == X:
            return 1
        elif board[0][2] == O:
            return -1

    # Si no sucede ninguno de los anteriores es empate
    return 0


# Buscar el movimiento con el valor minimo posible
def minvalue(board):
    if terminal(board):
        return utility(board)
    t = math.inf
    for action in actions(board):
        t = min(t, maxvalue(result(board, action)))
    return t


# Buscar el movimiento con el valor maximo posible
def maxvalue(board):
    if terminal(board):
        return utility(board)
    t = -math.inf
    for action in actions(board):
        t = max(t, minvalue(result(board, action)))
    return t


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Comprobar si el juego termino
    if terminal(board):
        return None

    if player(board) == X:
        t = -math.inf

        for action in actions(board):
            min_result = minvalue(result(board, action))
            if min_result > t:
                t = min_result
                best_action = action

    else:
        t = math.inf
        best_action = None
        for action in actions(board):
            max_result = maxvalue(result(board, action))
            if max_result < t:
                t = max_result
                best_action = action

    # retornar la mejor accion dependiendo el jugador
    return best_action