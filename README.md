# Tic Tac Toe - Python & Pygame

Este es un juego de **Tic Tac Toe** desarrollado en **Python** usando **Pygame** para la interfaz gráfica y una IA que utiliza el algoritmo **Minimax**. El juego permite que un jugador humano compita contra la IA, que toma decisiones óptimas basadas en este algoritmo.

## Características

- **Pygame**: Se usa para la interfaz gráfica, permitiendo al jugador interactuar con el tablero.
- **Minimax Algorithm**: Implementa una IA que busca la mejor jugada posible, garantizando un juego competitivo.
- Opciones para jugar como X o O.
- Detección automática de ganador o empate.

## Requisitos

- Python 3.x
- Pygame: Puedes instalarlo usando `pip install pygame`.

## Archivos del proyecto

- `runner.py`: Este archivo contiene el código para inicializar y correr el juego con una interfaz gráfica usando Pygame.
- `tictactoe.py`: Contiene la lógica del juego, incluyendo el algoritmo **Minimax**, la representación del tablero y la detección de ganadores.

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu-usuario/tictactoe.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd tictactoe
    ```

3. Instala las dependencias necesarias (Pygame):

    ```bash
    pip install pygame
    ```

## Ejecución

1. Ejecuta el juego usando el siguiente comando:

    ```bash
    python3 runner.py
    ```

2. Aparecerá una ventana con el tablero de Tic Tac Toe. Elige si quieres jugar como "X" o "O" haciendo clic en los botones correspondientes.

3. Juega contra la IA, que utilizará el algoritmo **Minimax** para decidir sus movimientos. El tablero se actualiza visualmente en cada turno.

## Cómo funciona

### Lógica del Juego

- El tablero es una matriz de 3x3.
- Las funciones en `tictactoe.py` incluyen:
  - **`initial_state()`**: Genera el estado inicial del tablero.
  - **`player(board)`**: Retorna qué jugador tiene el turno.
  - **`actions(board)`**: Retorna todas las acciones posibles que se pueden tomar en el tablero.
  - **`result(board, action)`**: Retorna el nuevo tablero después de que se ha hecho una acción.
  - **`winner(board)`**: Determina si un jugador ha ganado.
  - **`terminal(board)`**: Verifica si el juego ha terminado.
  - **`utility(board)`**: Retorna el resultado del juego (+1 si X gana, -1 si O gana, 0 si es empate).
  - **`minimax(board)`**: Aplica el algoritmo minimax para determinar la mejor jugada.

### IA Minimax

La IA utiliza el algoritmo **Minimax** para evaluar todas las posibles jugadas y seleccionar la que minimiza las pérdidas (en el caso de O) o maximiza las ganancias (en el caso de X). Esto garantiza que la IA siempre tomará la mejor decisión posible en cada turno.

## Controles

- Usa el mouse para seleccionar en el tablero dónde quieres colocar tu marca (X u O).
- Elige tu equipo (X u O) antes de comenzar.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea una nueva rama con tu mejora (`git checkout -b feature/nueva-mejora`).
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva mejora'`).
4. Haz push a la rama (`git push origin feature/nueva-mejora`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Revisa el archivo `LICENSE` para más detalles.

