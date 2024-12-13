# Queens_Placement

This Python script solves the N-Queens problem, which is a classic problem in computer science and mathematics. The objective of the problem is to place N queens on an N×N chessboard such that no two queens attack each other.

## How it Works

The script defines the following functions:

1. `init_board()`: Initializes an 8x8 chessboard with all cells set to 0.
2. `place_queen(board, a, b)`: Places a queen on the chessboard at position (a, b) and updates the board to reflect the queen's attacks.
3. `delete_queen(board, a, b)`: Removes a queen from the chessboard at position (a, b) and updates the board accordingly.
4. `solution(board, a, count)`: Recursively tries to place queens on the chessboard, starting from the row specified by `a`. The `count` parameter keeps track of the number of valid solutions found.
5. `output_position(board)`: Prints the positions of the queens on the chessboard in the format "a1; b3; c5; ..."
6. `main()`: The main function that initializes the chessboard, calls the `solution()` function, and prints the total number of solutions found.

The `solution()` function uses a backtracking algorithm to explore all possible placements of queens on the chessboard. It places a queen in the current row (specified by `a`) and recursively calls itself to place queens in the remaining rows. If a valid solution is found (i.e., all 8 queens are placed without any conflicts), the function outputs the positions of the queens and increments the `count` variable.

## Usage

To run the script, simply execute the `main()` function. The output will display the total number of valid solutions found, as well as the positions of the queens for each solution.

```python
if __name__ == '__main__':
    main()
```

This script is a classic example of a backtracking algorithm and demonstrates how to solve the N-Queens problem in Python.
