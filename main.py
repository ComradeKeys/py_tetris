import pygame
from pygame.locals import *

def main():

  #Initialize pyGame
  pygame.init()
  pygame.font.init()
  screen  = pygame.display.set_mode((400, 600))
  clock   = pygame.time.Clock()
  done    = False
  pygame.display.set_caption('py_tetris')
  font = pygame.font.SysFont("Liberation Sans", 72)

  # Fill background
  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill((15, 192, 252))
    
  # Display some text
  font = font.render("py_tetris", 1, (10, 10, 10))
  textpos = font.get_rect()
  textpos.centerx = background.get_rect().centerx

  while not done:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        done = True
      background.blit(font, textpos)
      screen.blit(background, (0, 0))
ppppp
    pygame.display.flip()
    clock.tick(60)

if __name__ == '__main__': main()

#being nice to the operating system
pygame.font.quit()
pygame.quit()
