import pygame

GRAVITY = .3 # Задание гравитации (падения палки с ускорением 0.3)

class Stick(pygame.sprite.Sprite): # Класс с подклассом pygame.sprite.Sprite

    def __init__(self, pos, screen):
        super().__init__() # Вызов конструктора подкласс
        self.screen = screen
        self.image = pygame.image.load('stick.png').convert_alpha()  # Загрузка изображения палки
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 0.2), int(self.image.get_height() * 0.2)))  # Уменьшение размера изображения до 20%
        self.rect = self.image.get_rect(center=pos) # Прямоугольник, содерж. изображение
        self.pos_y = pos[1] # Изначальная позиция по ОУ
        self.speed_y = 0 # Нач. скорость по ОУ

    def update(self): # Метод с обновлением позиций
        self.speed_y += GRAVITY
        self.pos_y += self.speed_y
        self.rect.y = self.pos_y

        if self.pos_y > self.screen.get_height():
            self.kill() # Удаление палки, к-ая вышла за пределы окна

def run_game():
    pygame.init()
    screen_width = 1200
    screen_height = 680
    screen = pygame.display.set_mode((screen_width, screen_height))  # Создание окна с размером
    clock = pygame.time.Clock()  # Управление частотой кадров
    running = True  # Флаг старта
    sticks = pygame.sprite.Group(Stick((600, 0), screen))  # Группа палок

    def add_stick():
        sticks.add(Stick((600, 0), screen))

    # Создается панели инструментов в окне Pygame
    toolbar_color = (250, 250, 250)
    toolbar_height = 25
    toolbar_font = pygame.font.SysFont('Arial', 14)
    btn_width = 80
    btn_height = 25
    btn_padding = 5
    btn_color = (250, 250, 250)
    btn_text_color = (50, 50, 50)
  btn_file = pygame.Rect(btn_padding, 0, btn_width, btn_height)
    btn_save = pygame.Rect(btn_padding + btn_width, 0, btn_width, btn_height)
    btn_open = pygame.Rect(btn_padding + btn_width * 2, 0, btn_width, btn_height)
    btn_help = pygame.Rect(btn_padding + btn_width * 3, 0, btn_width, btn_height)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btn_file.collidepoint(event.pos):
                    print("Нажата кнопка Файл")
                elif btn_save.collidepoint(event.pos):
                    print("Нажата кнопка Сохранить")
                elif btn_open.collidepoint(event.pos):
                    print("Нажата кнопка Открыть")
                elif btn_help.collidepoint(event.pos):
                    print("Обращайтесь к разработчику!")
                else:
                    sticks.add(Stick(event.pos, screen))

        sticks.update()
        pygame.display.set_caption('Падение палки')  # Задание заголовка окна
        programIcon = pygame.image.load('stick.png')
        pygame.display.set_icon(programIcon)  # Задание иконки окна
        screen.fill((146, 168, 145))  # Заливка цветом окна
        sticks.draw(screen)  # Отрисовка палок на окне

        # Рисуется панель инструментов
        pygame.draw.rect(screen, toolbar_color, (0, 0, screen_width, toolbar_height))
        pygame.draw.rect(screen, btn_color, btn_file)
        pygame.draw.rect(screen, btn_color, btn_save)
        pygame.draw.rect(screen, btn_color, btn_open)
        pygame.draw.rect(screen, btn_color, btn_help)

        # Наносится текст на кнопки
        file_text = toolbar_font.render("Файл", True, btn_text_color)
        save_text = toolbar_font.render("Сохранить", True, btn_text_color)
        open_text = toolbar_font.render("Открыть", True, btn_text_color)
        help_text = toolbar_font.render("Помощь", True, btn_text_color)
        screen.blit(file_text, (btn_padding * 4, btn_padding * 2))
        screen.blit(save_text, (btn_padding * 3 + btn_width, btn_padding * 2))
        screen.blit(open_text, (btn_padding * 6 + btn_width * 2, btn_padding * 2))
        screen.blit(help_text, (btn_padding * 20 + btn_width * 2, btn_padding * 2))

        pygame.display.flip()  # Обновление экрана
        clock.tick(60)  # 60 кадров

run_game()  # Запуск
pygame.quit()  # Выход
