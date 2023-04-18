import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))    #画面サイズ
    clock  = pg.time.Clock()    #タイマー設定
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")    #画像ロード
    
    kouka_img = pg.image.load("ex01/fig/3.png")

    bg_img2 = pg.transform.flip(bg_img,True,False)
    kouka_img2 = pg.transform.flip(kouka_img,True,False)
    kouka_img3 = pg.transform.rotozoom(kouka_img2,10,1.0)

    
    kouka_list = [kouka_img2,
                  kouka_img3]

    # print(f"len(kouka_list):{len(kouka_list)}")

    tmr = 0
    sc_x = 0
    count = 0
    index = 0

    while True:
        for event in pg.event.get():    #すべてのイベント
            if event.type == pg.QUIT: return #×ボタン押したら終了

        tmr += 1
        sc_x = tmr%3200

        # print(f"scx:{sc_x}")

        screen.blit(bg_img, [0-sc_x, 0]) #背景画像画面にペースト（映す
        screen.blit(bg_img2, [1600-sc_x, 0])
        screen.blit(bg_img, [3200-sc_x, 0])

        count += 1

        print(f"count:{count}")

        if count > 20:
            index += 1
            count = 0

        screen.blit(kouka_list[index%2], [300, 200]) 

        print(f"index:{index}")
        
        pg.display.update()
        clock.tick(100) #フレームレート


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()