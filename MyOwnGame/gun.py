import math
from bullet import *
class Gun:
    def __init__(self, x, y, image, damage, side):
        """

        :param x: координата x центра
        :param y: координата y центра
        :param image: изображение оружия
        :param damage: сколько урона оно наносит
        :param side: с какой мы стороны
        mouse - для хранения положения мыши
        power - для обработки задерживания клавиши и тогда оружие стреляет с большей начальной скоросью
        """
        self.x = x
        self.y = y
        self.image = image
        self.damage = damage
        self.power = 1
        self.mouse = [400, 400]
        self.side = side

    def ready_shoot(self, event):
        self.power += 1

    def aim(self, event):
        if event:
            self.mouse = event.pos

    def draw(self, screen):
        angle = math.atan((self.mouse[1]-self.y) / (self.mouse[0]-self.x))

        if self.side == "right":
            angle *= -1

        pistol = pygame.image.load(self.image)
        pistol = pygame.transform.scale(pistol, (10 * self.power, 10 * self.power))
        pistol = pygame.transform.rotozoom(pistol, math.degrees(-angle), 1)

        if self.side == "right":
            pistol = pygame.transform.flip(pistol, True, False)

        pistol_rect = pistol.get_rect(center = (self.x, self.y))
        screen.blit(pistol, pistol_rect)

    def shoot(self, event):
        angle = math.atan((event.pos[1]-self.y) / (event.pos[0]-self.x))
        self.power = 1

        if self.side == "right":
            angle *= -1

        return Bullet(self.x, self.y, self.power, angle, self.side)







