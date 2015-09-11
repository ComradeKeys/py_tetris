class Tetris:

  def main_menu(self):
    self.background.fill((15, 192, 252))
    # Display some text
    self.font            = self.font.render("py_tetris", 1, (10, 10, 10))
    self.textpos         = self.font.get_rect()
    self.textpos.centerx = self.background.get_rect().centerx
    
    while not self.done:
      for event in pygame.event.get():

        if event.type == pygame.QUIT:
          self.done = True
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
          self.done = True
        
      self.background.blit(self.font, self.textpos)
      self.screen.blit(self.background, (0, 0))

      pygame.display.flip()
      self.clock.tick(60)

  #Initialize pyGame
  def __init__(self):
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('py_tetris')
    self.screen     = pygame.display.set_mode((400, 600))
    self.clock      = pygame.time.Clock()
    self.done       = False
    self.font       = pygame.font.SysFont("Liberation Sans", 72)
    self.background = pygame.Surface(self.screen.get_size())
    self.background = self.background.convert()
    self.main_menu()

  #being nice to the operating system
  def __del__(self):
    pygame.font.quit()
    pygame.quit()

