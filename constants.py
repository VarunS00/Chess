import pygame

#Size of board
WIDTH = 800
HEIGHT = 800

#Amount of rows and columns
ROWS = 8
COLS = 8

#Size of each square
SQUARE_SIZE = WIDTH // COLS

#Tile colors
LIGHT = (240, 217, 181)
DARK = (181, 136, 99)

#Highlights which squares are valid moves
HIGHLIGHT = (106, 168, 79)
#Color for selected piece
SELECTED = (246, 246, 105)

#Stores colors for easier access
WHITE = "white"
BLACK = "black"

#Frames per second
FPS = 60
#Size of piece images
ASSET_SIZE = (SQUARE_SIZE, SQUARE_SIZE)