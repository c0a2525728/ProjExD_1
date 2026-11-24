import os
import sys

import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    bg_img = pg.image.load("fig/pg_bg.jpg")  # 練習1：背景画像の読み込み
    bg_img2 = pg.transform.flip(bg_img, True, False)  # 練習8：背景画像の左右反転
    kk_img = pg.image.load("fig/3.png")  # 練習3：こうかとん画像の読み込み
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()  # 練習10-1：こうかとんRectの取得
    kk_rct.center = (300, 200)  # 練習10-2：こうかとん初期座標の設定

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_lst = pg.key.get_pressed()  # 練習10-3：全キー状態の取得

        # 演習1：背景と同じ速さで毎フレーム左に1ピクセル流れる。
        dx = -1
        dy = 0
        if key_lst[pg.K_UP]:
            dy -= 1
        if key_lst[pg.K_DOWN]:
            dy += 1
        if key_lst[pg.K_LEFT]:
            dx -= 1
        if key_lst[pg.K_RIGHT]:
            dx += 2  # -1 + 2 = +1 で右に進む。

        # 演習2：横と縦の移動量をまとめて反映する。
        kk_rct.move_ip((dx, dy))

        x = tmr % 3200  # 練習5：背景の横座標に使う変数／練習9：ループ
        screen.blit(bg_img, (-x, 0))  # 練習2：背景画像の描画
        screen.blit(bg_img2, (-x + 1600, 0))  # 練習7・8：2枚目の背景に反転画像を使う
        screen.blit(bg_img, (-x + 3200, 0))  # 練習9：3枚目の背景を描画する
        screen.blit(kk_img, kk_rct)  # 練習10-5：移動後の座標でこうかとんを描画する
        pg.display.update()
        tmr += 1
        clock.tick(200)  # 練習6：FPSの変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
