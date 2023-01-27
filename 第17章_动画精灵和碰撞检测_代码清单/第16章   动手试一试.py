import pygame,sys,random
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
for i in range(100):
    width = random.randint(0,250)
    height = random.randint(0,100)
    top = random.randint(0,400)
    left = random.randint(0,500)
    pygame.draw.rect(screen,[0,0,0],[left,top,width,height],1)
    pygame.display.flip()
    pygame.time.delay(30)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()


import pygame,sys
pygame.init()
screen = pygame.display.set_mode((640,480))
screen.fill((250,120,0))
pygame.draw.arc(screen,(255,255,0),pygame.rect.Rect(43,368,277,235),-6.25,0,15)
pygame.draw.rect(screen,(255,0,0),pygame.rect.Rect(334,191,190,290))
pygame.draw.line(screen,(0,255,0),(268,259),(438,84),25)
pygame.draw.line(screen,(0,255,0),(578,259),(438,84),25)
pygame.draw.circle(screen,(0,0,0),(452,409),11,2)
pygame.draw.polygon(screen,(0,0,255),[(39,39),(44,136),(59,136),(60,102),(92,102),(94,131),(107,141),(111,50),(97,50),(93,86),(60,82),
                                      (58,38)],5)
pygame.draw.rect(screen,(0,0,255),pygame.rect.Rect(143,90,23,63),5)
pygame.draw.circle(screen,(0,0,255),(153,60),15,5)
clock = pygame.time.Clock()
pygame.display.flip()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
pygame.quit()

