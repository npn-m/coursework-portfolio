TEXT2 = get_font(40).render(story[0], False, "#d7fcd4")
        TEXT2_RECT = TEXT2.get_rect(center=(SCREEN.get_width()/6,5*SCREEN.get_height()/7))
        TEXT3 = get_font(40).render(story[0], False, "#d7fcd4")
        TEXT3_RECT = TEXT3.get_rect(center=(SCREEN.get_width()/6,5*SCREEN.get_height()/7))
        TEXT4 = get_font(40).render(story[0], False, "#d7fcd4")
        TEXT4_RECT = TEXT4.get_rect(center=(SCREEN.get_width()/6,5*SCREEN.get_height()/7))

if NEXT_BUTTON.checkForInput(scene_0_MOUSE_POS):
                        TEXT2 = get_font(40).render(story[0], False, "#d7fcd4")
                        TEXT3 = get_font(40).render(story[0], True, "#d7fcd4")
                        TEXT3_RECT = TEXT3.get_rect(center=(SCREEN.get_width()/2,5.5*SCREEN.get_height()/6))
                        SCREEN.blit(TEXT3, TEXT3_RECT)
                        if NEXT_BUTTON.checkForInput(scene_0_MOUSE_POS):
                            TEXT3 = get_font(40).render(story[0], False, "#d7fcd4")
                            TEXT4 = get_font(40).render(story[0], True, "#d7fcd4")
                            TEXT4_RECT = TEXT4.get_rect(center=(SCREEN.get_width()/2,5.5*SCREEN.get_height()/6))
                            SCREEN.blit(TEXT4, TEXT4_RECT)
                            if NEXT_BUTTON.checkForInput(scene_0_MOUSE_POS):
                                scene_1()
        pygame.display.update()

for j in str(value):
    
    # Here I check if my target is met (if I clicked a button)

    if event.type == mousepress and event.button == leftclick:
        pygame.draw.rect(clicker, "black", pygame.Rect(650, 120, 350, 100))
        break
    
    # I then update the blit and font or text or whatever

    font = pygame.font.SysFont("Times New Roman", 35)
    numberdisplay = font.render('upgrade: ' + j, True, 'pink')
    clicker.blit(display,(650 - display.get_width() // 2, 150 - display.get_height() // 2))

    import os
os.system('cls')
print('Hello Devdit');