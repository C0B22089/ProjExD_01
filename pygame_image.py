import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230926/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01-20230926/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img2 = pg.transform.rotozoom(kk_img,10,1.0)
    kk_imgs = [kk_img, kk_img2]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        i = 800
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img,[300, 200])
        screen.blit(kk_img2,[300, 200])
        
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()