import pygame as pg
def win():
    win_ceck=[]
    for side in "xo":
        for row in field:
            if row.count(side)==3:
                row = field.index(row)
                win_ceck = ((0,row),(1,row),(2,row))
                if side == "o":
                    pg.display.set_caption("победили нолики")

                else:
                    pg.display.set_caption("победили крестики")

        for column in range(3):
            if field[0][column] == field[1][column] == field[2][column] == side:
                win_ceck = ((column, 0), (column, 1), (column, 2))
                if side == "o":
                    pg.display.set_caption("победили нолики")

                else:
                    pg.display.set_caption("победили крестики")
        if field[0][0] == field[1][1] == field[2][2] == side:
            win_ceck = ((0,0),(1,1),(2,2))
            if side == "o":
                pg.display.set_caption("победили нолики")

            else:
                pg.display.set_caption("победили крестики")
        if field[2][0] == field[1][1] == field[0][2] == side:
            win_ceck = ((2,0),(1,1),(0,2))
            if side == "o":
                pg.display.set_caption("победили нолики")

            else:
                pg.display.set_caption("победили крестики")
    return win_ceck

def draw(victory):
    screen.fill(color=(138, 138, 138))
    pg.draw.line(screen,(89,89,89), (200,0),(200,600), width=5)
    pg.draw.line(screen, (89, 89, 89), (400, 0), (400, 600), width=5)
    pg.draw.line(screen, (89, 89, 89), (0, 200), (600, 200), width=5)
    pg.draw.line(screen, (89, 89, 89), (0, 400), (600, 400), width=5)
    for j,i in victory:
        pg.draw.rect(screen,"grey", (j*200,i*200, 200, 200))
    for x in range (3):
        for y in range(3):
            if field[y][x] == "x":
                pg.draw.line(screen,(255,0,0),(x*200,y*200),(x*200+200,y*200+200),width=6)
                pg.draw.line(screen, (255, 0, 0), (x * 200 + 200, y * 200), (x * 200, y * 200 + 200),width=6)
            elif field[y][x] == "o":
                pg.draw.circle(screen, (0,0,255),(x*200+100,y*200+100),100,width= 6)
    pg.display.flip()



pg.init()
field = [[None,None,None],[None,None,None],[None,None,None]]
HEIGHT = 600
WIDTH = 600

screen = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
while True:

    events = pg.event.get()
    victory = win()
    draw(victory)
    for event in events:
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                x,y= pg.mouse.get_pos()
                if x < 200:
                    x = 0
                elif x < 400:
                    x = 1
                else: x = 2
                if y < 200:
                    y = 0
                elif y < 400:
                    y = 1
                else:
                    y = 2
                if field[y][x] == None:
                    field [y][x] = "x"
                    pg.display.flip()


