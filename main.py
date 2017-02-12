from modules.bullet import *
from modules.explode import *
from modules.target import *

from helper.readLevel import *
from modules.player import *
from pygame import *


class Main:

    def __init__(self, mscreen):

        self.screen = mscreen
        self.score = 0
        self.fire_sound = pygame.mixer.Sound(FIRE)
        self.explode_sound = pygame.mixer.Sound(EXPLODE)

        self.all_sprites_list = pygame.sprite.Group()
        self.block_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        self.explode_list = pygame.sprite.Group()

        self.player = ''

        level_data = ReadLevel(LEVEL1)
        self.draw_blocks = level_data.get_level_data()

        self.setup_level()

    def setup_level(self):
        for new_blocks in self.draw_blocks:
            if new_blocks[2]:
                block = Block([0, 0, 30, 30])
                block.rect.x = new_blocks[0]
                block.rect.y = new_blocks[1]
                block.init_loc[0] = new_blocks[0]
                block.init_loc[1]= new_blocks[1]

                # Add the block to the list of objects
                self.block_list.add(block)
                self.all_sprites_list.add(block)

                self.player = Player([0, 0, 75 ,73])
                self.player.rect.x = SCREEN_W - 500
                self.player.rect.y = SCREEN_H - 70
                self.all_sprites_list.add(self.player)

    def event_listener(self, restart):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            elif event.type == pygame.MOUSEBUTTONDOWN and not restart:
                self.firebullet()

            elif event.type == pygame.KEYDOWN and not restart:
                if event.key == pygame.K_SPACE:
                    self.firebullet()

                if event.key == pygame.K_ESCAPE:
                    return True
        return False

    def drawFrames(self):

        self.all_sprites_list.update()

        for explosion in self.explode_list:
            self.explode_list.remove(explosion)
            self.all_sprites_list.remove(explosion)

    def checkhits(self):

        for bullet in self.bullet_list:

            # See if it hit a block
            block_hit_list = pygame.sprite.spritecollide(bullet, self.block_list, True)

            # For each block hit, remove the bullet and add to the score
            for block in block_hit_list:
                self.bullet_list.remove(bullet)
                self.all_sprites_list.remove(bullet)
                self.score += 1

                explode_me = Explode([0, 0, 30, 30])
                explode_me.rect.x = block.rect.x
                explode_me.rect.y = block.rect.y
                self.all_sprites_list.add(explode_me)
                self.explode_list.add(explode_me)
                self.explode_sound.play()

            if bullet.rect.y < -10:
                self.bullet_list.remove(bullet)
                self.all_sprites_list.remove(bullet)

            if len(self.block_list) <= 0:
                return True

        return False

    def firebullet(self):
        if len(self.bullet_list) < 5 :
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet([0, 0, 16, 16])
            # Set the bullet so it is where the player is
            self.fire_sound.play()
            bullet.rect.x = self.player.rect.x + 30
            bullet.rect.y = self.player.rect.y
            # Add the bullet to the lists
            self.all_sprites_list.add(bullet)
            self.bullet_list.add(bullet)

            # Limit to 60 frames per second
            clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

if __name__ == '__main__':

    pygame.mixer.init()
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_W, SCREEN_H])
    background_image = pygame.image.load(BACKGROUND)
    bg_sound = pygame.mixer.Sound(BGMUSIC)
    pygame.display.set_caption(TITEL_TEXT)

    game = Main(screen)

    clock = pygame.time.Clock()

    display_instructions = True
    font = pygame.font.Font(None, 36)
    font1 = pygame.font.Font(None, 24)
    font2 = pygame.font.Font(None, 18)

    restart = False
    textscore = font.render("", True, BLACK)
    gameover = False

    while display_instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                display_instructions = False
                bg_sound.play(loops=-1)

        # Set the screen background
        game.screen.fill(BLACK)

        text = font.render(TITEL_TEXT, True, WHITE)
        screen.blit(text, [SCREEN_W / 2 - 100, SCREEN_H / 2 - 5])

        text = font1.render(INST, True, GREEN)
        screen.blit(text, [SCREEN_W / 2 - 200, SCREEN_H / 2 + 50])

        text = font2.render(PAKTC, True, RED)
        screen.blit(text, [SCREEN_W / 2 - 100, SCREEN_H / 2 + 150])

        # Limit to 60 frames per second
        clock.tick(30)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    while not gameover:
        gameover = game.event_listener(restart)
        game.drawFrames()
        restart = game.checkhits()
        screen.blit(background_image, [0, 0])
        # Draw all the spites
        game.all_sprites_list.draw(screen)
        textscore = font.render("Score: " + str(game.score), True, WHITE)
        screen.blit(textscore, [0, 0])
        pygame.display.flip()

        while restart:
            screen.fill(BLACK)
            text = font.render("YOU WIN !!!", True, WHITE)
            screen.blit(text, [SCREEN_W / 2 - 100, SCREEN_H / 2 - 5])
            text = font.render(PAKTC, True, RED)
            screen.blit(text, [SCREEN_W / 2 - 175, SCREEN_H / 2 + 50])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    restart = False
                    gameover = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    restart = False
                    game.__init__(screen)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        restart = False
                        gameover = True
                    else:
                        restart = False
                        game.__init__(screen)

            clock.tick(30)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

        clock.tick(30)

    pygame.quit()

