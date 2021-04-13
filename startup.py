# Callan Murphy
# 26/07/20
# Startup File
from functions import *
from vars import *

pygame.init()
clock = pygame.time.Clock()

# screen properties
pygame.display.set_caption('Darkness')
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# user sprite
player = Mob("Player", 100, 45, 100, "img/front.png", WIDTH // 2, HEIGHT // 2)

# other object creation
walls = create("wall", WALLS)
coins = create("coin", COINS)
for x in coins:
    for y in walls:
        if x.collided(y):
            x.new_pos()
skeletons = create("skele", SKELETONS)
things = []
things.extend(walls)
things.extend(coins)
mobs = skeletons
things.extend(mobs)
fix_spawns(things + [player])

# text
gold_total = GOLD
font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 150)
health_text = font.render('Health', True, (255, 255, 255))
game_over_text = font.render('GAME OVER', True, (255, 255, 255))
gold = pygame.image.load("img/coin.png")
health_text_rect = health_text.get_rect()
gold_rect = gold.get_rect()
game_over_rect = game_over_text.get_rect()
gold_total_text = font.render(str(gold_total), True, (255, 255, 255))
gold_total_text_rect = gold_total_text.get_rect()
gold_total_text_rect.x = 60
gold_total_text_rect.y = 73
health_text_rect.x = 20
health_text_rect.y = 20
gold_rect.x = 20
gold_rect.y = 75
game_over_rect.center = (WIDTH // 2, HEIGHT // 2)

# health
healths = [5]
healths.append(Thing("img/Health0.gif", 200, 20))
healths.append(Thing("img/Health1.gif", 200, 20))
healths.append(Thing("img/Health2.gif", 200, 20))
healths.append(Thing("img/Health3.gif", 200, 20))
healths.append(Thing("img/Health4.gif", 200, 20))
healths.append(Thing("img/Health5.gif", 200, 20))
for x in healths:
    if x != 5:
        x.rect.x = 140
        x.rect.y = 26
current_health = healths[-1]
