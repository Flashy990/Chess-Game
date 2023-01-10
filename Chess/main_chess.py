# Main driver file
# Responsible for handling user input
# Also responsible for displaying the current game_state object

import pygame as p
from Chess import game_engine

p.init()

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def load_images():
    pieces = ["bB", "bK", "bN", "bP", "bQ", "bR", "wB", "wK", "wN", "wP", "wQ", "wR"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

# Driver for the code
# Handles user input
# Updates the graphics

def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = game_engine.game_state()
    #print(gs.board)
    load_images()
    running = True
    # initially we don't have any square selected
    square_selected = ()
    # keeps a track of players' clicks
    player_clicks = []
    while running:
            for e in p.event.get():
                if e.type == p.QUIT:
                        running = False
                elif e.type == p.MOUSEBUTTONDOWN:
                    # variable for the location of the mouse
                    location = p.mouse.get_pos()
                    column = location[0]//SQ_SIZE
                    row = location[1]//SQ_SIZE

                    # to deselect if the user has already selected a square
                    if square_selected == (row, column):
                        square_selected = ()
                        player_clicks = []
                    else:
                        square_selected = (row, column)
                        player_clicks.append(square_selected)

                    if len(player_clicks) == 2:
                        move = game_engine.move(player_clicks[0], player_clicks[1], gs.board)
                        print(move.get_chess_notation())
                        gs.make_move(move)

                        # resetting the user clicks
                        square_selected = ()
                        player_clicks = []

            draw_game_state(screen, gs)
            clock.tick(MAX_FPS)
            p.display.flip()

# draw the squares on the board and other graphics in the current game state
def draw_game_state(screen, gs):
    draw_squares_board(screen)
    draw_pieces(screen, gs.board)

def draw_squares_board(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[((row + column) % 2)]
            p.draw.rect(screen, color, p.Rect(column * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, board):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(column * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))



if __name__ == "__main__":
    main()