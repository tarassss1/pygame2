import pygame # підключаємо бібліотеку pygame
pygame.init() # "запускаємо"

window = pygame.display.set_mode((1200,500)) # створення головного вікна
RED  = (255,0,0) # встановлення червоного кольору
game = True # змінна для контролю стану гри

player = pygame.Rect(100, 100, 50, 50) # створення об'єкта "Прямокутник"

while game: # цикл працюватиме поки game = True

    for e in pygame.event.get(): # перебір всіх подій
        if e.type == pygame.QUIT: # якщо подія "вихід", то гра завершується
            game = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= 10
    if keys[pygame.K_s]:
        player.y += 10  
    if keys[pygame.K_d]:
        player.x += 10
    if keys[pygame.K_w]:
        player.y -= 10  


    window.fill(RED) # заповнення кольором
    pygame.draw.rect(window, (0,0,255), player) # відображення персонажа
    pygame.time.Clock().tick(60) # встановлення частоти кадрів
    pygame.display.update() # оновлення вікна
