# Sudoku-Solver
## What is Sudoku?
Sudoku is a numeric logics game.
The goal of the game is to fill a 9x9 matrix according to the following rules:
    Each cell can only be filled with numbers from 1-9;
    In each row and collumn, each number can only appear once;
    In each 3x3 block, all numbers from 1-9 must appear.

There are a lot of techniques to solving this game. In this project we will use the backtracking technique.

## What is backtracking?
Backtracking is a problem-solving algorithmic technique that involves finding a solution incrementally by trying different options and undoing them if they lead to a dead end. It is commonly used in situations where you need to explore multiple possibilities to solve a problem, like searching for a path in a maze or solving puzzles like Sudoku. When a dead end is reached, the algorithm backtracks to the previous decision point and explores a different path until a solution is found or all possibilities have been exhausted. [1]

#TODO: 
    Create a function that checks after assigning the current index the grid becomes unsafe or not. Keep Hashmap for a row, column and boxes. If any number has a frequency greater than 1 in the hashMap return false else return true; hashMap can be avoided by using loops.
    Create a recursive function that takes a grid.
    Check for any unassigned location. 
        If present then assigns a number from 1 to 9.
        Check if assigning the number to current index makes the grid unsafe or not. 
        If safe then recursively call the function for all safe cases from 0 to 9.
        If any recursive call returns true, end the loop and return true. If no recursive call returns true then return false.
    If there is no unassigned location then return true.

[1]https://www.geeksforgeeks.org/sudoku-backtracking-7/

[2]https://www.codingdrills.com/tutorial/introduction-to-backtracking-algorithms/sudoku-solver

[3]https://en.wikipedia.org/wiki/Sudoku_solving_algorithms
