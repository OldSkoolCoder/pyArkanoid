import pygame as pg 
import random
import settings
import block
import ball
import player
#import sprites

class Game:
    def __init__(self):
        # Initialise game code
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pg.display.set_caption(settings.TITLE)
        self.clock = pg.time.Clock()
        self.running = True

        self.blockCount = 32
        self.noOfRows = 5
        self.top = 80

    def new(self):
        # Starts a new game
        self.allSprites = pg.sprite.Group()
        self.balls = pg.sprite.Group()
        self.blocks = pg.sprite.Group()

        # Add Player Sprites
        self.player = player.Player()
        self.allSprites.add(self.player)

        # Add Enemy Sprites
        self.ball = ball.Ball()
        self.allSprites.add(self.ball)
        self.balls.add(self.ball)

        # Add any other sprites
        for row in range(self.noOfRows):
            for column in range(0, self.blockCount):
                block1 = block.Block(settings.RED, column * (settings.BLOCK_WIDTH + 2) + 1, self.top)
                self.blocks.add(block1)
                self.allSprites.add(block1)

            # Move the top of the next row down
            self.top += settings.BLOCK_HEIGHT + 2

        self.run()

    def run(self):
        # Game Loop Code
        self.playing = True
        while self.playing:
            self.clock.tick(settings.FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop Update Method
        # self.allSprites.update()

        self.player.update()
        self.playing = not self.ball.update()
        self.running = self.playing

        if pg.sprite.spritecollide(self.player, self.balls, False):

            # The 'diff' lets you try to bounce the ball left or right
            # depending where on the paddle you hit it
            diff = (self.player.rect.x + self.player.width // 2) - (self.ball.rect.x + self.ball.width // 2) 

            # Set the ball's y position in case
            # we hit the ball on the edge of the paddle
            self.ball.rect.y = settings.SCREEN_HEIGHT - self.player.rect.height - self.ball.rect.height - 1
            self.ball.bounce(diff)

        # Check for collisions between the ball and the blocks
        deadblock = pg.sprite.spritecollide(self.ball, self.blocks, True)

        # If we actually hit a block, bounce the ball
        if len(deadblock) > 0 :
            self.ball.bounce(0)

            # Game ends if all the blocks are gone
            if len(self.blocks) == 0:
                self.playing = False
                self.Running = False

    def events(self):
        # Game Loop Events handler
        for event in pg.event.get():
            # check for closing the window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop draw screen
        self.screen.fill(settings.BLACK)
        self.allSprites.draw(self.screen)

        # After redrawing the screen, flip it
        pg.display.flip()

    def showStartScreen(self):
        # Show the start screen of the game
        pass

    def showGameOverScreen(self):
        # show the Game over screen
        pass

