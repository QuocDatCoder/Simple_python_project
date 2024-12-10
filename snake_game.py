import pygame as pg
import random

pg.init()

# Khởi tạo cửa sổ
screen = pg.display.set_mode((400, 400))  # set width cua screen
pg.display.set_caption('Snake Game')  # set tieu de cho trang 

# Tạo rắn
score = highscore = 0
snake_part = 20
x_pos = y_pos = 200  # Vị trí ban đầu của rắn
x_change = y_change = 0  # Di chuyển của rắn
snake_body = []
snake_length = 1

# Tạo thức ăn
food_x = random.randint(0, 19) * snake_part
food_y = random.randint(0, 19) * snake_part

# Tốc độ rắn
clock = pg.time.Clock()
speed = 10  # Điều chỉnh tốc độ rắn

# Hàm kiểm tra va chạm
def check_col():
    global gameplay
    # Kiểm tra va chạm biên và va chạm với thân rắn
    if x_pos < 0 or x_pos > 400 or y_pos < 0 or y_pos > 400 or (x_pos, y_pos) in snake_body[:-1]:
        gameplay = False  # Kết thúc trò chơi
        return False
    return True

# Hàm hiển thị điểm số
def score_view():
    font = pg.font.SysFont('Arial', 36)
    if gameplay:
        score_txt = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_txt, (0, 0))
        hscore_txt = font.render(f'Highscore: {highscore}', True, (255, 255, 255))
        screen.blit(hscore_txt, (200, 0))
    else:
        note_txt = font.render(f'Press space to play again', True, (255, 255, 255))
        screen.blit(note_txt, (30, 60))

# Vòng lặp trò chơi
gameplay = True
while True:  # Vòng lặp chính không bao giờ thoát cho đến khi người chơi thoát ứng dụng
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

        # Di chuyển rắn
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x_change = -snake_part
                y_change = 0
            elif event.key == pg.K_RIGHT:
                x_change = snake_part
                y_change = 0
            elif event.key == pg.K_UP:
                x_change = 0
                y_change = -snake_part
            elif event.key == pg.K_DOWN:
                x_change = 0
                y_change = snake_part
            elif event.key == pg.K_SPACE and not gameplay:  # Khi nhấn SPACE sau khi trò chơi kết thúc
                # Reset lại trò chơi
                score = 0
                x_pos = y_pos = 200  # Vị trí ban đầu của rắn
                x_change = y_change = 0  # Di chuyển của rắn
                snake_body = []
                snake_length = 1
                gameplay = True  # Tiếp tục trò chơi

    # Vẽ màn hình
    screen.fill((0, 0, 0))
    score_view()  # Gọi hàm hiển thị điểm số

    if gameplay:
        # Cập nhật vị trí rắn
        x_pos += x_change
        y_pos += y_change

        # Kiểm tra va chạm
        gameplay = check_col()

        # Thêm phần thân rắn
        snake_body.append((x_pos, y_pos))

        # Xóa phần đuôi khi rắn dài ra
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Kiểm tra ăn thức ăn
        if x_pos == food_x and y_pos == food_y:
            snake_length += 1
            score += 1  # Tăng điểm số khi ăn thức ăn
            if score > highscore:
                highscore = score  # Cập nhật điểm cao nhất
            food_x = random.randint(0, 19) * snake_part
            food_y = random.randint(0, 19) * snake_part

        # Vẽ phần thân rắn
        for x, y in snake_body:
            pg.draw.rect(screen, (255, 255, 255), (x, y, snake_part, snake_part))  # Dùng x, y từ snake_body

        # Vẽ phần đầu rắn nếu không có va chạm
        if gameplay:
            pg.draw.rect(screen, (255, 255, 255), (x_pos, y_pos, snake_part, snake_part))
        else:
            # Nếu va chạm, vẽ đầu rắn màu đỏ
            pg.draw.rect(screen, (255, 0, 0), (x_pos, y_pos, snake_part, snake_part))
            if x_pos >= 400:
                pg.draw.rect(screen, (255, 0, 0), (380, y_pos, snake_part, snake_part))
            elif x_pos < 0:
                pg.draw.rect(screen, (255, 0, 0), (0, y_pos, snake_part, snake_part))
            if y_pos >= 400:
                pg.draw.rect(screen, (255, 0, 0), (x_pos, 380, snake_part, snake_part))
            elif y_pos < 0:
                pg.draw.rect(screen, (255, 0, 0), (x_pos, 0, snake_part, snake_part))

        # Vẽ thức ăn
        pg.draw.rect(screen, (255, 0, 0), (food_x, food_y, snake_part, snake_part))

        # Cập nhật màn hình
        pg.display.update()
        
        # Cập nhật tốc độ
        clock.tick(speed)
    else:
        # Khi trò chơi kết thúc, hiển thị thông báo và chờ người chơi nhấn SPACE để chơi lại       
        pg.display.update()  # Cập nhật màn hình để hiển thị thông báo
