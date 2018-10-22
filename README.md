# Python Terminal Mario

## Introduction

A game similar to popular game Mario

This game has been written using _almost_ Vanilla Python. Important to note that the game has been tested on **ONLY** Linux-based OSs, and _may not_ work on Windows.

## Structure

The application demonstrates inheritance, encapsulation, polymorphism and abstraction.
- Each player/enemy is a derived class of the `Character` class.
- The `board` has its own class and and captures all objects placed on it.

## Features and Gameplay

- Life 1 means small mario, 2 means grown-up mario, 3 means having firing ability.
- Jumps have gravity like effect.
- Collect '$' powerup to increase life.
- Jump on enemies or fire towards them to kill them.
- Collect '0' to get additional points.
- Jumping inside pits will lead to losing a chance.
- Getting hit by enemies or by boss fire will lead to losing a life.
- On losing a chance you will respawn at start will life 1.
- Jump on spring for higher jumps.
- To play level 1 or 2, enter 1 or 2 respectively in difficulty and then enter 2.
- Make your own level using level generator. Instructions are given on executing level generator.
- To play your own level enter difficulty, then enter 1, then choose file name of saved level

## Running the program

- Go into the respective directory (python3 required)
- To play the game
	- `./game.py`
- To start level generator
	- `python3 levelGenerator.py`

## Controls

- Controls follow traditional classic titles (W,S,A,D)
- To fire `f`
- To quit, press `q`

## File Structure

.
 * [game.py](./game.py)
 * [input.py](./input.py)
 * [characters.py](./characters.py)
 * [ascii.py](./ascii.py)
 * [board.py](./board.py)
 * [missiles.py](./missiles.py)
 * [levelGenerator.py](./levelGenerator.py)
 * [README.md](./README.md)
