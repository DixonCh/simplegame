from constants import *
from helper.spritesheet import *


class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """

    def __init__(self, sprite_sheet_data):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet(TANK)
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)

    def update(self):
        """ Update the player's position. """

        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[pygame.K_RIGHT]:
            if self.rect.x < SCREEN_W - 75:
                self.rect.x = self.rect.x + 10
        elif keys[pygame.K_LEFT]:
            if self.rect.x > 0:
                self.rect.x = self.rect.x - 10
        #else:
           # pos = pygame.mouse.get_pos()
           # print pos

            #if pos[0] < SCREEN_W and pos[1] < SCREEN_W:
            #    self.rect.x = pos[0]