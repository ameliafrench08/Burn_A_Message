import pygame


pygame.init()
pygame.font.init()
start_font = pygame.font.SysFont('Zapfino', 20)
pygame.display.set_caption("Burn This Message")

# set up variables for the display
SCREEN_HEIGHT = 455
SCREEN_WIDTH = 750
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pregame = True
r = 100
g = 0
b = 0
start_button = "Start"

start_button_display = start_font.render(start_button, True, (106, 4, 15))

# c = Cochonnet(375, 175)
# nl = NewLife(125, 375)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
# -------- Main Program Loop -----------
while run:

    keys = pygame.key.get_pressed()  # checking pressed keys

    # --- Main event loop
    for event in pygame.event.get():  # User did something

        if pregame:
            if event.type == pygame.MOUSEBUTTONUP:
                pregame = False
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((0, 0, 0))
    if not pregame:
        y = 0
    if pregame:
        screen.fill((244, 140, 6))
        screen.blit(start_button_display, (100, 100))

    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
