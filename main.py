from field import *
from constants import *
from hero import*
from platforms import*

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill([55, 255, 255])
all_sprites = pygame.sprite.Group()
hero = Hero(HERO_X, HERO_Y)


num_field = NumberField(NUMBER_OF_HORIZONTAL_BLOCKS, NUMBER_OF_VERTICAL_BLOCKS,
                        NUMBER_OF_OBSTACLES, OBSTACLES_LENGTH_MAXIMUM)
num_field.create_vertical_borders()
num_field.create_horizontal_borders()
num_field.create_obstacles()

create_platforms(num_field.blocks)

all_sprites.add(hero)
for obj in platforms:
    all_sprites.add(obj)


field = Field(screen, num_field)  

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    screen.fill([55, 255, 255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        else:
            hero.event_checking(event)
    all_sprites.update(platforms, screen)
    pygame.display.update()

pygame.quit()


