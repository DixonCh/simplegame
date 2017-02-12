from constants import *
from helper.spritesheet import *


class Block(pygame.sprite.Sprite):
    """ This class represents the block. """

    def __init__(self, sprite_sheet_data):

        pygame.sprite.Sprite.__init__(self)
        self.rect_change_x = 2
        sprite_sheet = SpriteSheet(TARGET)
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()
        self.init_loc = [0,0]

    def update(self):
        """ Update the target's position. """

        if self.rect.x > self.init_loc[0] + 100 or self.rect.x < self.init_loc[0] - 5:
            self.rect_change_x = self.rect_change_x * -1

        self.rect.x += self.rect_change_x
