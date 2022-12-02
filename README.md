# An Intelligent Othello Player
Repo for Aritfical Intelligence assigment at University

## About
Our Assignment was to program an "Intelligent Othello player"
This intelligent agent was created using **Minimax** algorithm with **Alpha Beta Pruning** to increase efficiency.
The game of Othello was also implemented by myself, agruably harder than programming the AI.

Currently, the agent is not very intelligent. It can play the game. However, it is not difficult to beat.
By tuning the heuristic function used in minimax the preformance of the agent can be increased. 

## How to play
The game is ran through the controller.py file in the command line:
```
python3 controller.py
```
You will be prompted with two options to play the game:
* Playing against the AI
* Playing against another human (or yourself)

If you select to play against the AI you will be asked to set the search depth for Minimax. A depth of 4 is recommended, anything higher and you will be waiting a significant amount of time for a response from the AI. 
Then pick the color you would like to play as.

While playing against the AI, if you would like to turn of Alpha Beta pruning. Wait for your turn and type:
```
settings
```


### Controller.py
This file houses the logic of the game as well as the AI.

### Othello.py 
Logic for the game of Othello.
