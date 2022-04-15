import pygame, random                                     #mooduli pygame,random importimine

pygame.init()                                             #pygame käivitamine

# värvid
lBlue = [153, 204, 255]                                   #muutuja mille väärtus värv helesinine

# ekraani seaded
screenX = 640                                             #muutuja väärtus akna pikkus
screenY = 480                                             #muutuja väärtus akna kõrgus
screen = pygame.display.set_mode([screenX, screenY])      #soovitud suurusega akna tekitamine, mis lisatakse muutujasse.
pygame.display.set_caption("PingPong")                    #aknale nimetuse andmine
screen.fill(lBlue)                                        #ekraani tausta täitmine helesinine


pall = pygame.Rect(0, 0, 20, 20)                                         #muutja mille väärtus Rect objektina, asukoht ja objekti mõõtmed
pallImage = pygame.image.load("ball.png")                                #pildi avamine ,muutuja omistab pildi.
pallImage = pygame.transform.scale(pallImage, [pall.width, pall.height]) #pildi suuruse xy koordinaadid laius, kõrgus.


alus = pygame.Rect(0, 0, 120, 20)                                        #muutja mille väärtus Rect objektina, asukoht ja objekti mõõtmed
alusimage = pygame.image.load("pad.png")                                 #pildi avamine ,muutuja omistab pildi.
alusimage = pygame.transform.scale(alusimage, [alus.width, alus.height]) #muutuja omastab aluse suuruse xy koordinaadid laius, kõrgus.


clock = pygame.time.Clock()                                              #muutuja mis võimaldab mängu ajaga (liikumine) sidumine
posX, posY = 0, 0                                                        #positsioon mille väärtus xy koordinaatidega
posX1, posY1 = random.randint(0,screenX-pallImage.get_rect().width), 0   #positsioon mille väärtus xy koordinaatidega juhuslik asukoht kogu ekraani ulatuses 0
posX2, posY2 = random.randint(0,screenX-alusimage.get_rect().width), screenY / 1.5 #positsioon mille väärtus xy koordinaatidega , palgi y postisioon 1.5 ekraanil

speedX1, speedY1 = 3, 4         #palli kiiruse väärtused x y teljel
speedX2, speedY2 = 2, 4         #aluse kiiruse väärtused x y teljel

temp = 0                        #muutuja mille väärtus 0
skoor = 0                       #muutuja mille väärtus 0

juurdelisa, mahavota = 0, 0     #muutujad mille väärtus 0

gameover = False                    #muutuja väärtus võrdne, et vale
while not gameover:                 #kui ei ole vale.
    clock.tick(60)                  #kella seadistus 60 kaadrit sekundis
    # mängu sulgemine ristist
    event = pygame.event.poll()     #muutuja omistab väärtuse kasutades pygame moodulit
    if event.type == pygame.QUIT:   #kui event tüübi väärtuseks sulgumine(pygame.QUIT)
        break                       #aken sulgub

    screen.blit(pallImage, (posX1, posY1)) #tausta uuesti joonistamine vastavalt asetusele

    posX1 += speedX1       #postitsiooni X väärtus asetus muutub vastavalt kiirusele
    posY1 += speedY1       #postitsiooni Y väärtus asetus muutub vastavalt kiirusele

    if posX1 > screenX - pallImage.get_rect().width or posX1 < 0:  #kui X1 juhusliku objekti positsioon on suurem ekraanil objektist või väiksem kui 0 ehk kokkupõrkeni äärtest
        temp = posY1                                               #muutja väärtus posY1
        speedX1 = -speedX1
    if posY1 > screenY - pallImage.get_rect().height or posY1 < 0: #kui Y1 positsioon on suurem Y ekraanil objektist või väiksem kui 0 ehk kokkupõrkeni  äärtest
        temp = posY1                                               #muutuja väärtus palli postitsioon Y telg
        speedY1 = -speedY1                                         #kiirus väheneb, liigub teisele poole

    screen.blit(alusimage, (posX2, posY2))                         #tausta uuesti joonistamine vastavalt asetusele
    posX2 += speedX2                                               #postitsiooni X väärtus asetus muutub vastavalt kiirusele

    if posX2 > screenX - alusimage.get_rect().width or posX2 < 0:  #kui X2 juhsliku objekti positsioon on suurem ekraanil servadest või väiksem kui 0 ehk kokkupõrkeni äärtest
        speedX2 = -speedX2                                         #kiirus väheneb, liigub teisele poole

    if posY2 > screenY - alusimage.get_rect().height or posY2 < 0: #kui Y2 juhsliku objekti positsioon on suurem ekraanil servadest või väiksem kui 0 ehk kokkupõrkeni äärtest
        speedY2 = -speedY2                                         #kiirus väheneb, liigub teisele poole

    screen.blit(alusimage, (posX2, posY2))                         #tausta uuesti joonistamine vastavalt asetusele
    posX2 += speedX2                                               #postitsiooni X väärtus asetus muutub vastavalt kiirusele


    if posY1 == posY2 and temp < posY2:                                     #kui positsiooon Y1 võrdne Y2 ehk palli/aluse kokkupuutepunkt ja temp(0) väiksem Y2 positsioonist
        if posX1 >= posX2 and posX1 <= posX2 + alusimage.get_rect().width:  #kui postitsioon X1 suurem või võrdne X2 ja X1 väiksem või võrne X2 koos aluse laiusega
            speedY1 = -speedY1                                              #kiirus väheneb, liigub teisele poole
            skoor += 1                                                      #muutujale skoor lisatakse enda väärtusele +1
            juurdelisa = pygame.time.get_ticks() + 1000                     #muutja mille väärtusena kasutatakse pygame, time moodulit

    elif posY1 == posY2 and temp > posY2:                                                #muuljuhul kui positsiooon Y1 võrdne Y2 ehk palli/aluse kokkupuutepunkt ja temp(0) suurem Y2 positsioonist
        if posX1 >= posX2 and posX1 <= posX2 + alusimage.get_rect().width and skoor > 0: #kui postitsioon X1 suurem või võrdne X2 ja X1 väiksem või võrne X2 koos aluse laiusega ja skoor suurem kui 0
            skoor -= 1                                                                   #muutujale skoor vähendatakse enda väärtust -1
            mahavota = pygame.time.get_ticks() + 1000                                    #muutja mille väärtusena kasutatakse pygame, time moodulit

    font1 = pygame.font.Font(pygame.font.match_font('tahoma'), 24)                 #muutja font 1 väärtusega fondi suurus, kirjastiil
    font2 = pygame.font.Font(pygame.font.match_font('arial'), 40)                  #muutja font 2 väärtusega fondi suurus, kirjastiil
    punktisumma = font1.render("Punkte: " + str(skoor), True, [255, 255, 255])     #muutuja mille väärtus sõnena valge värvusega
    screen.blit(punktisumma, [screenX - 630, screenY - 470])                       #punktisumma fondi asukoht x y koordinaatidega ekraanil

    juurde = font2.render("+1", True, [0, 255, 0])                     #muutuja mille värvus rohelise värvusega sõnena +1
    maha = font2.render("-1", True, [255, 102, 102])                       #muutuja mille värvus punanese värvusega sõnena -1

    if pygame.time.get_ticks() < juurdelisa:                           #kui aja mooduli väärtus väiksem juurdelisa väärtusest

        screen.blit(juurde, [screenX / 2.3, screenY / 3])        #teksti ekraanile joonistamine/värskendamine x y koordinaatidega ekraani suurusest jagatis võimalikult keskkkohta

    if pygame.time.get_ticks() < mahavota:                             #kui aja mooduli väärtus väiksem mahavõta väärtusest

        screen.blit(maha, [screenX / 2.3, screenY / 3])          #tekst ekraanile joonistamine/värskendamine x y koordinaatidega ekraani suurusest jagatis võimalikult keskkkohta





    pygame.display.flip()            #ekraani värskendamine
    screen.fill(lBlue)               #ekraani tausta uuesti täitmine helesinine



pygame.quit()                        #mängu sulgemine