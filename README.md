Queens_Placement
This Python program solves the 8 Queens puzzle using a backtracking algorithm. The 8 Queens puzzle involves placing 8 queens on an 8x8 chessboard such that no two queens threaten each other. This means that no two queens can share the same row, column, or diagonal.

How It Works
The program uses a recursive backtracking approach to explore all possible ways to place the queens on the board. It starts by placing queens row by row and backtracks when it encounters a conflict (i.e., two queens threatening each other).

Functions:
init_board(): Initializes an 8x8 chessboard represented by a 2D list. Each cell starts with a value of 0 (no queen).
place_queen(board, a, b): Places a queen on the board at position (a, b) and marks the rows, columns, and diagonals as unsafe for further queens.
delete_queen(board, a, b): Removes a queen from position (a, b) and restores the safety of the rows, columns, and diagonals.
solution(board, a, count): Recursively tries to place queens on each row, starting from row 0. If a valid placement is found for all 8 queens, it outputs the solution.
output_position(board): Prints the positions of the queens on the board in standard chess notation (e.g., "a1, b3, c5...").
main(): Initializes the chessboard, calls the solution function, and prints the total number of valid solutions.
Usage
To run the program, simply execute the Python script. It will solve the puzzle and print all possible solutions, along with the total number of solutions.

python 8_queens.py

Example Output:

a1; b5; c8; d6; e3; f7; g2; h4
a1; b6; c8; d3; e7; f4; g2; h5
...

Total solutions: 92

License
This project is open source and available under the MIT License.
