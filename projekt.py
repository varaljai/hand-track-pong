import pygame, sys
from paddle import Paddle
from labda import Labda
import gyak 
pygame.init()

fekete = (0,0,0)
feher = (255,255,255)

meret = (700,500)
ablak = pygame.display.set_mode(meret)

paddleA = Paddle(feher, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(feher, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

labda = Labda(feher,10,10)
labda.rect.x = 345
labda.rect.y = 195

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(labda)

ora = pygame.time.Clock()

pont = 0
pont2 = 0

gyak.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.set_caption("Játék")
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)
        
    paddleB.rect.y = gyak.update()
    
    all_sprites_list.update()
    
    if labda.rect.x>=690:
        labda.velocity[0] = -labda.velocity[0]
        pont += 1
        labda.rect.x = 345
        labda.rect.y = 195
        if pont == 10:
            labda.velocity = 0
            print("A nyertes: 1. Játékos")
            sys.exit()
    if labda.rect.x<=0:
        labda.velocity[0] = -labda.velocity[0]
        pont2 += 1
        labda.rect.x = 345
        labda.rect.y = 195
        if pont2 == 10:
            labda.velocity = 0
            print("A nyertes: 2. Játékos")
            sys.exit()
    if labda.rect.y>490:
        labda.velocity[1] = -labda.velocity[1]
    if labda.rect.y<0:
        labda.velocity[1] = -labda.velocity[1] 

    if pygame.sprite.collide_mask(labda, paddleA) or pygame.sprite.collide_mask(labda, paddleB):
      labda.bounce()

        
    ablak.fill(fekete)

    pygame.draw.line(ablak, feher, [349,0], [349,500], 5)

    font = pygame.font.Font(None, 74)
    text = font.render(str(pont), 1, feher)
    ablak.blit(text, (250,10))
    text = font.render(str(pont2), 1, feher)
    ablak.blit(text, (420,10))

    all_sprites_list.draw(ablak)
    
    
    pygame.display.flip()
    
    ora.tick(60)
    
pygame.quit()