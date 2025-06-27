
import pygame
import random

pygame.init()

# Custom IDS:
SPRITE_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 2

# Define colours:

BLUE = pygame.Color('blue')
LIGHT_BLUE = pygame.Color('lightblue')
DARK_BLUE = pygame.Color('darkblue')

# sprite colours:

YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

# Sprite class repersenting the moving object

class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, height, width):
        super().__init__()

        # Creating the sprites surface with diemesions and colour:
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

        # Set initial velocity with random direction
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):

        self.rect.move_ip(self.velocity)

        boundary_hit = False

        # Check for collision with left or right boundaries and reverse direction:
        
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = - self.velocity[0]
            boundary_hit = True
        
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = - self.velocity[1]
            boundary_hit = True

        # if a boundary was hit:
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOUR_CHANGE_EVENT))
            
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOUR_CHANGE_EVENT))

    # Method to change the sprites colour:
    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))

# Function to change the background colour:
def change_background_color():
    global bg_color 
    bg_color = random.choice([BLUE, LIGHT_BLUE, DARK_BLUE])

# Create a sprite group to hold the sprite:
all_sprites_list = pygame.sprite.Group()
# Instantiate the sprite
sp1 = Sprite(WHITE, 20, 30)
# randomly postion the sprite
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
# Add the sprite to the group:
all_sprites_list.add(sp1)

# Create a game window:
screen = pygame.display.set_mode((500, 400))
# set the window title:
pygame.display.set_caption("Boundary Sprite")
# set the initial background colour:
bg_color = BLUE
# Apply the background colour:
screen.fill(bg_color)

# Game loop control flag:
exit = False
# Create a clock to controk the frame rate:
clock = pygame.time.Clock()

# Main game loop:

while not exit:
    # Event handling loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        
        elif event.type == SPRITE_COLOUR_CHANGE_EVENT:
            sp1.change_color()

        elif event.type == BACKGROUND_COLOUR_CHANGE_EVENT:
            change_background_color()

# Update all sprites:
all_sprites_list.update()
# Fill the screen with the current background colour:
screen.fill(bg_color)
# Draw all sprites to the screen:
all_sprites_list.draw(screen)

# Refresh the display
pygame.display.flip()
# Limit the frame rate to 240 fps
clock.tick(240)

# Uninitialize all pygame modules and close the window:
pygame.quit()