# ==============================

# MENÚ PRINCIPAL

# ==============================

# YEFRY BERAS = 22-MISN-2-040

def menu():

    while True:

        pantalla.fill(NEGRO)

        titulo = fuente.render("PERSECUSION EN LA ARENA", True, BLANCO)


        iniciar_rect = pygame.Rect(280,230,240,50)

        volumen_rect = pygame.Rect(280,300,240,50)

        salir_rect = pygame.Rect(280,370,240,50)


        pygame.draw.rect(pantalla, VERDE, iniciar_rect)

        pygame.draw.rect(pantalla, AZUL, volumen_rect)

        pygame.draw.rect(pantalla, ROJO, salir_rect)


        pantalla.blit(titulo,(280,150))

        pantalla.blit(fuente.render("INICIAR JUEGO",True,NEGRO), iniciar_rect.move(30,10))

        pantalla.blit(fuente.render("CONFIGURACIÓN",True,NEGRO), volumen_rect.move(35,10))

        pantalla.blit(fuente.render("SALIR",True,NEGRO), salir_rect.move(70,10))


        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit(); sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:

                if iniciar_rect.collidepoint(evento.pos):
                    return

                if volumen_rect.collidepoint(evento.pos):

                    menu_volumen()

                if salir_rect.collidepoint(evento.pos):

                    pygame.quit(); sys.exit()

        pygame.display.flip()

        reloj.tick(60)

# ==============================

# MENÚ VOLUMEN

# ==============================

# YEFRY BERAS = 22-MISN-2-040

def menu_volumen():

    global volumen

    while True:

        pantalla.fill(NEGRO)

        texto = fuente.render(f"VOLUMEN: {int(volumen*100)}%", True, BLANCO)


        subir_rect = pygame.Rect(300,250,200,50)

        bajar_rect = pygame.Rect(300,320,200,50)

        volver_rect = pygame.Rect(300,390,200,50)


        pygame.draw.rect(pantalla, VERDE, subir_rect)

        pygame.draw.rect(pantalla, ROJO, bajar_rect)

        pygame.draw.rect(pantalla, AZUL, volver_rect)


        pantalla.blit(texto,(300,180))

        pantalla.blit(fuente.render("SUBIR",True,NEGRO), subir_rect.move(60,10))

        pantalla.blit(fuente.render("BAJAR",True,NEGRO), bajar_rect.move(60,10))

        pantalla.blit(fuente.render("VOLVER",True,NEGRO), volver_rect.move(50,10))


        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit(); sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:

                if subir_rect.collidepoint(evento.pos):

                    volumen = min(1.0, volumen+0.1)

                if bajar_rect.collidepoint(evento.pos):

                    volumen = max(0.0, volumen-0.1)

                if volver_rect.collidepoint(evento.pos):
                    return

                pygame.mixer.music.set_volume(volumen)

        pygame.display.flip()

        reloj.tick(60)






