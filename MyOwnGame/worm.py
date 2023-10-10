import pygame.event

from gun import *
class Worm:
    def __init__(self, x, y, image, side):
        self.x = x
        self.y = y
        self.image = image
        self.hearts = 10
        self.side = side
        self.start_pos = (self.x, self.y)

        if side == "left":
            self.gun = Gun(self.x + 20, self.y, 'pistol.bmp', 1, side)
        else:
            self.gun = Gun(self.x - 20, self.y, 'pistol.bmp', 1, side)

    def move(self, event):
        if event.key == pygame.K_a:
            if self.x >= 0:
                self.x -= 2
                self.gun.x -= 2
            if self.side == "right" and self.x <= 600:
                self.x = self.start_pos[0]
                self.gun.x = self.start_pos[0] - 20
        elif event.key == pygame.K_d:
            if self.x <= 800:
                self.x += 2
                self.gun.x += 2
            if self.side == "left" and self.x >= 200:
                self.x = self.start_pos[0]
                self.gun.x = self.start_pos[0] + 20

    def draw(self, screen):
        worm = pygame.image.load(self.image)
        worm = pygame.transform.scale(worm, (40, 40))

        if self.side == "left":
            worm = pygame.transform.flip(worm, True, False)

        worm_rect = worm.get_rect(center = (self.x, self.y))
        screen.blit(worm, worm_rect)
        self.gun.draw(screen)

    def hit(self, obj):
        distance = math.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2)

        if distance <= 8:
            self.hearts -= 1
            obj.destroy()
