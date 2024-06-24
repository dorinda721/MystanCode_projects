"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

打磚塊遊戲的動作設定
球會反彈及消滅磚塊
並只有三次機會或消滅完所有磚塊及終止遊戲
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    # Add the animation loop here!
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    remaining = graphics.total_bricks

    while lives > 0 and remaining > 0:  # 生命值不為0，還有剩餘方塊，遊戲皆可繼續
        pause(FRAME_RATE)
        if graphics.clicked:  # 當clicked是True，開始遊戲即關閉開關
            vx = graphics.get_dx()
            vy = graphics.get_dy()
            graphics.ball.move(vx, vy)
            # 設定x的反彈
            if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
                graphics.set_dx()
            # 設定y的反彈
            if graphics.ball.y <= 0:
                graphics.set_dy()
            # 設定減少一命的條件
            if graphics.ball.y > graphics.window.height:
                lives -= 1
                graphics.window.add(graphics.ball, graphics.original_x, graphics.original_y)
                graphics.clicked = False  # 失敗時，才可打開開關
            else:
                hit_once = False
                # 球的四個點
                for i in range(0, graphics.ball.width+1, graphics.ball.width):
                    vy = graphics.get_dy()
                    for j in range(0, graphics.ball.height+1, graphics.ball.height):
                        ball_point = graphics.window.get_object_at(graphics.ball.x+i, graphics.ball.y+j)
                        # 判定球是否有撞擊及下一步動作
                        if ball_point is not None:
                            if ball_point is graphics.paddle:
                                if vy > 0:  # 確保只在向下移動時反彈
                                    graphics.set_dy()
                            else:
                                if not hit_once:  # 設定一次只消掉一個磚塊
                                    hit_once = True
                                    graphics.set_dy()
                                    graphics.window.remove(ball_point)
                                    remaining -= 1


if __name__ == '__main__':
    main()
