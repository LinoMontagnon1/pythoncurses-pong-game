import curses
# import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    w = stdscr.subwin(sh, sw, 0, 0)

    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    w = stdscr.subwin(sh, sw, 0, 0)

    paddle1_x = sh // 2
    paddle1_y = 3
    paddle2_x = sh // 2
    paddle2_y = sw - 4
    ball_x = sh // 2
    ball_y = sw // 2

    direction_x = -1
    direction_y = -1

    # speed = 1
    # speed_increase_interval = 0.1 
    # last_speed_increase_time = time.time()


    while True:
        w.clear()
        w.border(0)
        for i in range(paddle1_x - 2, paddle1_x + 3):
            w.addstr(i, paddle1_y, "|")
        for i in range(paddle2_x - 2, paddle2_x + 3):
            w.addstr(i, paddle2_y, "|")
        w.addstr(ball_x, ball_y, "o")

        ball_x += direction_x
        ball_y += direction_y

        if (ball_y == paddle1_y + 1 and paddle1_x - 2 <= ball_x <= paddle1_x + 3) or (ball_y == paddle2_y - 1 and paddle2_x - 2 <= ball_x <= paddle2_x + 3):
            direction_y *= -1
            # speed += 1


        key = w.getch()
        if key == ord('w') and paddle1_x > 3:
            paddle1_x -= 2
        elif key == ord('s') and paddle1_x < sh - 4:
            paddle1_x += 2
        elif key == curses.KEY_UP and paddle2_x > 3:
            paddle2_x -= 2
        elif key == curses.KEY_DOWN and paddle2_x < sh - 4:
            paddle2_x += 2

        if ball_y == sw - 1:
            w.addstr(sh // 2, sw // 2 - 10, "W e S ganhou!")
            w.refresh()
            curses.napms(2000)
            break
        elif ball_y == 0:
            w.addstr(sh // 2, sw // 2 - 10, "Setinhas ganhou!")
            w.refresh()
            curses.napms(2000)
            break

        # current_time = time.time()
        # if current_time - last_speed_increase_time >= speed_increase_interval:
        #     speed += 1000
        #     last_speed_increase_time = current_time

        if ball_x == sh - 1 or ball_x == 0:
            direction_x *= -1

if __name__ == "__main__":
    curses.wrapper(main)
