import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))    #画面サイズ
    clock  = pg.time.Clock()    #タイマー設定
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")    #画像ロード
    kouka_img = pg.image.load("ex01/fig/3.png")

    kouka_img = pg.transform.flip(kouka_img,True,False)

    tmr = 0

    while True:
        for event in pg.event.get():    #すべてのイベント
            if event.type == pg.QUIT: return #×ボタン押したら終了

        tmr += 1
        screen.blit(bg_img, [0, 0]) #画面にペースト（映す

        
        screen.blit(kouka_img, [400, 300]) 

        pg.display.update()
        clock.tick(100) #フレームレート


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()