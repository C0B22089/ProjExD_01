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
    bg_img2 = pg.transform.flip(bg_img, True, False)
    tmr = 0
    count = 0
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        if x >= 1600:
            if count == 1:
                count = 0
            else:
                count = 1
            x = 0
        if count == 0:
            screen.blit(bg_img,[-x,0])
            screen.blit(bg_img2,[1600-x, 0])
        else:
            screen.blit(bg_img2,[-x, 0])
            screen.blit(bg_img,[1600-x,0])
            
        s = (tmr // 75) %2
        screen.blit(kk_imgs[s],[300, 200])
        pg.display.update()
        tmr += 1  
        x += 1  
        clock.tick(500)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()