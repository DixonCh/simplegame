from constants import *
from helper.spritesheet import *


class Explode(pygame.sprite.Sprite):
    """ This class represents explode . """

    def __init__(self, sprite_sheet_data):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.explode_animation = []
        sprite_sheet = SpriteSheet(EXPLOD)

        image = sprite_sheet.get_image(0, 0, 32, 32)
        self.explode_animation.append(image)
        image = sprite_sheet.get_image(0, 32, 32, 32)
        self.explode_animation.append(image)
        image = sprite_sheet.get_image(0, 64, 32, 32)
        self.explode_animation.append(image)
        image = sprite_sheet.get_image(0, 96, 32, 32)
        self.explode_animation.append(image)

        image = sprite_sheet.get_image(32, 0, 32, 32)
        self.explode_animation.append(image)
        image = sprite_sheet.get_image(32, 32, 32, 32)
        self.explode_animation.append(image)
        image = sprite_sheet.get_image(32, 64, 32, 32)
        self.explode_animation.append(image)
        image = sprite_sheet.get_image(32, 96, 32, 32)
        self.explode_animation.append(image)

        image = sprite_sheet.get_image(64, 0, 32, 32)
        self.explode_animation.append(image)
        image = sprite_sheet.get_image(64, 32, 32, 32)
        self.explode_animation.append(image)
        image = sprite_sheet.get_image(64, 64, 32, 32)
        self.explode_animation.append(image)
        image = sprite_sheet.get_image(64, 96, 32, 32)
        self.explode_animation.append(image)

        image = sprite_sheet.get_image(96, 0, 32, 32)
        self.explode_animation.append(image)
        image = sprite_sheet.get_image(96, 32, 32, 32)
        self.explode_animation.append(image)
        image = sprite_sheet.get_image(96, 64, 32, 32)
        self.explode_animation.append(image)
        image = sprite_sheet.get_image(96, 96, 32, 32)
        self.explode_animation.append(image)

        self.image = self.explode_animation[0]

        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

    def update(self):
        """ Move animation. """
        self.rect.y -= 3

        frame = (self.rect.y // 10) % len(self.explode_animation)
        self.image = self.explode_animation[frame]