import random

import pygame

import blockduko

# create a window
pygame.init()
screen = pygame.display.set_mode((360, 600))
pygame.display.set_caption("Blockduko")


button_size = (150, 50)
move_button_origin = (screen.get_width()/2-button_size[0]/2, screen.get_height()-button_size[1]-50)
queue_origin = (screen.get_width()/2-button_size[0]/2, screen.get_height()-button_size[1]-200)

board = [[False for _ in range(9)] for __ in range(9)]
blockduko.print_board(board)
queue = blockduko.get_queue()

# main loop
running = True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # button click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if move_button_origin[0] <= event.pos[0] <= move_button_origin[0]+button_size[0] and move_button_origin[1] <= event.pos[1] <= move_button_origin[1]+button_size[1]:
                board = blockduko.make_ai_move(board, queue)
                if len(queue) == 0:
                    queue = blockduko.get_queue()
                # blockduko.printBoard(board)

    # game logic
    # drawing code
    screen.fill((255, 255, 255))

    # draw a suduko board
    # the board is a 9x9 grid
    # each square is a 3x3 grid

    square_size = 25
    board_origin = (screen.get_width()/2-(square_size*4.5), 100)

    for x in range(9):
        for y in range(9):
            pygame.draw.rect(screen, (40, 40, 40), (board_origin[0]+square_size*x, board_origin[1]+square_size*y, square_size+1, square_size+1), 1)
            if board[x][y]:
                pygame.draw.rect(screen, (52, 186, 235), (board_origin[0]+square_size*x+1, board_origin[1]+square_size*y+1, square_size-1, square_size-1), 0)

    # draw the queue
    # print("---")
    for ox in range(len(queue)):
        piece = queue[ox]
        piece_size = min(300/len(queue), 100)
        padding = 60/(len(queue)+1)
        # print()
        # blockduko.print_board(piece)
        for x in range(len(piece)):
            piece_square_size = min(piece_size/max(len(piece), len(piece[0])), 30)
            for y in range(len(piece[0])):
                if piece[x][y]:
                    pygame.draw.rect(screen, (52, 186, 235), ((padding)*(ox+1)+(piece_size)*ox+piece_square_size*x, queue_origin[1]+piece_square_size*y, piece_square_size, piece_square_size), 0)
                    pygame.draw.rect(screen, (0, 0, 0), ((padding)*(ox+1)+(piece_size)*ox+piece_square_size*x, queue_origin[1]+piece_square_size*y, piece_square_size+1, piece_square_size+1), 1)
                    

    # draw a button
    button = pygame.Rect(move_button_origin, button_size)
    button_text = "Make move"
    pygame.draw.rect(screen, (52, 186, 235), button)
    font = pygame.font.Font(None, 36)
    screen.blit(font.render(button_text, True, (255, 255, 255)), (move_button_origin[0]+button_size[0]/2-font.size(button_text)[0]/2, move_button_origin[1]+button_size[1]/2-font.size(button_text)[1]/2))

    pygame.display.flip()
