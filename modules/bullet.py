from constants import *
from helper.spritesheet import *


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """

    def __init__(self, sprite_sheet_data):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet(BULLET)
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)

    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3
