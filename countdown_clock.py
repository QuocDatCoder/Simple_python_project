import pygame
import time
import math

pygame.init()

# Khởi tạo cửa sổ
screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()

# Biến thời gian
total_secs = 0
seconds = 0
minutes = 0

r_sec = 90  # Radius for second hand
r_min = 90  # Radius for minute hand

# Màu sắc
GREY = (150, 150, 150)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED= (255,0,0)

# Khởi tạo font
font = pygame.font.SysFont('Arial', 30)

# Tạo văn bản
text1 = font.render("+", True, BLACK)
text2 = font.render("-", True, BLACK)
text3 = font.render("START", True, BLACK)
text4 = font.render("RESET", True, BLACK)
text5 = font.render(":", True, BLACK)

# Vòng lặp chính
running = True
start = False  # Set the initial state of the timer to "not started"

while running:
    clock.tick(60)  # Run the clock at 60 FPS
    screen.fill(GREY)  # Làm sạch màn hình

    # Lấy vị trí chuột
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Vẽ các nút
    pygame.draw.rect(screen, WHITE, (100, 50, 50, 50))  # +60
    pygame.draw.rect(screen, WHITE, (100, 200, 50, 50))  # -60
    pygame.draw.rect(screen, WHITE, (200, 50, 50, 50))  # +1
    pygame.draw.rect(screen, WHITE, (200, 200, 50, 50))  # -1
    pygame.draw.rect(screen, WHITE, (300, 50, 150, 50))  # START
    pygame.draw.rect(screen, WHITE, (300, 150, 150, 50))  # RESET

    # Vẽ các văn bản
    screen.blit(text1, (120, 50))
    screen.blit(text1, (220, 50))
    screen.blit(text2, (120, 210))
    screen.blit(text2, (220, 210))
    screen.blit(text3, (330, 60))
    screen.blit(text4, (330, 160))

    # Vẽ đường tròn
    pygame.draw.circle(screen, BLACK, (250, 400), 100)  # Đường tròn ngoài
    pygame.draw.circle(screen, WHITE, (250, 400), 95)  # Đường tròn bên trong
    pygame.draw.circle(screen, BLACK, (250, 400), 0)  # Đường tròn bên trong

    # Tính toán góc cho phút và giây
    a_sec = (seconds * 6) * math.pi / 180
    a_min = (minutes * 6) * math.pi / 180

    # Vẽ kim giây
    sec_x = 250 + r_sec * math.sin(a_sec)
    sec_y = 400 - r_sec * math.cos(a_sec)
    pygame.draw.line(screen, BLACK, (250, 400), (sec_x, sec_y))

    # Vẽ kim phút
    min_x = 250 + r_min * math.sin(a_min)
    min_y = 400 - r_min * math.cos(a_min)
    pygame.draw.line(screen, BLACK, (250, 400), (min_x, min_y))

    # Cập nhật phút và giây
    minutes = total_secs // 60
    if( minutes >60):
        total_secs=seconds
    seconds = total_secs % 60

    # Tạo lại các văn bản phút và giây
    min_text = font.render(str(minutes), True, BLACK)
    sec_text = font.render(str(seconds), True, BLACK)

    # Vẽ các văn bản phút, giây và dấu ":"
    screen.blit(min_text, (150, 150))
    screen.blit(text5, (170, 150))  # Dấu ":"
    screen.blit(sec_text, (200, 150))

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Nút chuột trái
                # Kiểm tra nếu chuột nhấn vào các nút
                if (100 < mouse_x < 150) and (50 < mouse_y < 100):  # +60
                    total_secs += 60
                if (200 < mouse_x < 250) and (50 < mouse_y < 100):  # +1
                    total_secs += 1
                if (100 < mouse_x < 150) and (200 < mouse_y < 250):  # -60
                    total_secs -= 60
                if (200 < mouse_x < 250) and (200 < mouse_y < 250):  # -1
                    total_secs -= 1
                if (300 < mouse_x < 450) and (150 < mouse_y < 200):  # RESET
                    total_secs = 0
                    start = False  # Pause when reset
                if (300 < mouse_x < 450) and (50 < mouse_y < 100):  # START
                    start = not start  # Toggle start/pause
        
                    print(start)

    # Decrement total_secs if the timer is running
    if start==True:
        if total_secs > 0:
            total_secs -= 1
            minutes = total_secs // 60
            seconds = total_secs % 60
        time.sleep(1)

    pygame.display.flip()  # Cập nhật màn hình

pygame.quit()
