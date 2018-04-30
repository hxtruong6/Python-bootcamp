# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 23:50:41 2018

@author: HXT
"""
# Decription: Create a Tic Tac Toe game.
from IPython.display import clear_output

## Create a board to show info in game
def display_board(board):
    clear_output()
    print("   |   |   ")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("   |   |   ")
    
## Get input 'X' or 'O' from player
def player_input():
    player = input("Please pick a marker 'X' or 'O': ")
    while True :
        if (player == 'X' or player == 'O' ):
            return player
        else: 
            player = input("Input wrong! Please pick a marker 'X' or 'O' again: ")

## Function that takes in the board list object
def place_marker(board, marker, position):
    board[position] = marker


## Check if 'X' or 'O' win
def win_check(board, mark):
    posCheck = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    for pos in posCheck:
        if (False not in list(map(lambda index: board[index] == mark, pos))):
            return True
    return False

## Check a space on the board is freely available
def space_check(board, position):
    return board[position] == ' '

## Check if the board is full
def full_board_check(board):
    return not (' ' in board[1:])

## Function to ask a player's position
def player_choice(board):
    player = input("Please choose a number(1-9): ")
    while True:       
        if (player in '123456789'):
            player = int(player)
            if (player in range(1,10)): 
                if (space_check(board, player)):
                    break
                else:
                    player = input("Choose another position! Please choose a number(1-9): ")
            else:
                player = input("Out of range 1 to 9! Please choose a number(1-9): ")
        else:
            player = input("Input inavailable! Please choose a number(1-9): ")

    return player

## Function if player wanna replay
def replay():
    player = input("Do you want to play agian ('Yes' or 'No')? ")
    while True:
        if (player.lower() in ["yes", "no"]):
            return player.lower() == "yes"
        else:
            player = input("Input invailable! Do you want to play agian ('Yes' or 'No')? ")

## Main
print('Welcome to Tic Tac Toe!')
while True:
    # Set the game up here
    board = ['#',' ', ' ' , ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    #board = ['#',' ','O','X','O','X','O','X','O','X']
    turn = player_input()
    display_board(board)
    
    while True:
        pos = player_choice(board)
        place_marker(board, turn, pos)
        display_board(board)
        
        if (win_check(board, turn)):
            print(f"Player {turn} won!")
            break
        elif (full_board_check(board)):
            print("Full board!")
            break
        if (turn == 'X'):
            print("Turn player 'O': ")
            turn = 'O'
        else: 
            print("Turn player 'X': ")
            turn = 'X'
        
    if not replay():
        break
    else:
        print("New round!")

    