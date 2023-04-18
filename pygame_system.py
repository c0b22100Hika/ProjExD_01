import pygame as pg
import sys

def main():
    pg.display.set_caption("はじめてのPygame")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    fonto  = pg.font.Font(None, 80)
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        tmr += 1
        txt = fonto.render(str(tmr), True, (255, 0, 0))
        screen.fill((255, 255, 255))
        screen.blit(txt, [400, 300])
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()