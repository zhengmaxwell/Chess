# Chess AI

A chess engine with an intelligent AI player. 

## Implementation
### Algorithms
The intelligent chess player predicts future moves and chooses the best available move. The predictions are calculated using a minimax algorithm and alpha-beta pruning. 
### Console Application
A quick prototype that displays the game on the Console. Written in Python for quick deployment in exchange for runtime speed. Moves are entered through the command line as a tuple. 

<p align="center">
    <img src="images/console.png" alt="Console" width="400"><br/>
    <em>Figure 1: Starting Board on Console</em>
</p>

### GUI Application
A faster version written in C#. A destop app created using a WPF is used to display the chess board. Moves are entered by clicking the desired piece and position to move to. 

Additional features not present in the console application include:
- Highlighting where AI moved
- Clicking pieces to see available moves (shown below)

<p align="center">
    <img src="images/gui.png" alt="Console" width="400"><br/>
    <em>Figure 2: In-Game on GUI</em>
</p>
