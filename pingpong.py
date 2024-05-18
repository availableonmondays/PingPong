from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, picture_name, starting_position_x, starting_position_y, x_size, y_size, speed):
        super().__init__()
        self.image = transform.scale(image.load(picture_name), (x_size, y_size))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = starting_position_x
        self.rect.y = starting_position_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_left(self):
        pass

window = display.set_mode(600, 500)


game = True
finish = False

clock = time.clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill((200, 255, 255))

    