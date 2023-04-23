from pygame import *
window = display.set_mode((700,500))
display.set_caption("Шутер")
background = transform.scale(image.load('background.jpg'), (700,500))
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.diration = 'left'

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

racket1 = Player('racket.png', 10, 200, 30, 100, 10)
racket2 = Player('racket.png', 660, 200, 30, 100, 10)
ball = GameSprite('tenis_ball.png',325, 200, 50, 50, 7)

game = True
while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False

    racket1.reset()
    racket2.reset()
    ball.reset()
    racket1.update_L()
    racket2.update_R()
            
    display.update()
    clock.tick(60)
