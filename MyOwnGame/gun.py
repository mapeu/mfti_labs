class Gun:
    def __init__(self, x, y, image, damage):
        self.x = x
        self.y = y
        self.image = image
        self.damage = damage
        self.power = 1

    def ready_shoot(self, event):
        self.power += 1






