import pygame,sys
from button import Button
from main import *

pygame.init()

class Scene():
    def scene_1():
        while True:
            First_Question_MOUSE_POS = pygame.mouse.get_pos()
            SCREEN.fill("black")
            Question_TEXT = get_font(55).render("คำถาม", True, "#d7fcd4")
            Question_RECT = Question_TEXT.get_rect(center=(SCREEN.get_width()/6,5*SCREEN.get_height()/7))
            Answer1_BUTTON = Button(image=None, pos=(SCREEN.get_width()/6,5.5*SCREEN.get_height()/6), 
                                text_input="สำรวจโต๊ะของตัวเอง", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
            Answer2_BUTTON = Button(image=None, pos=(SCREEN.get_width()/2,5.5*SCREEN.get_height()/6), 
                                text_input="สำรวจโต๊ะของเพื่อน", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
            Answer3_BUTTON = Button(image=None, pos=(5*SCREEN.get_width()/6,5.5*SCREEN.get_height()/6), 
                                text_input="ไปเรียน", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
            
            SCREEN.blit(Question_TEXT, Question_RECT)
            
            for button in [Answer1_BUTTON, Answer2_BUTTON , Answer3_BUTTON ]:
                button.changeColor(First_Question_MOUSE_POS)
                button.update(SCREEN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Answer1_BUTTON.checkForInput(First_Question_MOUSE_POS):
                        Scene.scene_2(1)
                    if Answer2_BUTTON.checkForInput(First_Question_MOUSE_POS):
                        Scene.scene_2(2)
                    if Answer3_BUTTON.checkForInput(First_Question_MOUSE_POS):
                        Scene.scene_2(2)
                        
            pygame.display.update()

    def scene_2(ans):
        while True:
            Question_MOUSE_POS = pygame.mouse.get_pos()
            SCREEN.fill("black")
            if (ans==1):
                TEXT_1=get_font(24).render("เจอไดอารี่ของเจ้าของร่าง เนื้อหาเกี่ยวกับชีวิตประจำวัน\n\t1.วันนี้วันเกิด พ่อที่ไปทำงานไกลๆ ส่งของมาให้ ชอบมากๆ เลย\n\t2.วันนี้ได้มาอยู่โรงเรียนประจำวันแรก รูมเมทมีความชอบและของหลายๆ อย่างเหมือนกัน ทำให้คุยกันถูกคอ และสนิทกันมากขึ้น"
                                           , True, "#d7fcd4")
                TEXT_1_RECT = TEXT_1.get_rect(center=(SCREEN.get_width()/2,SCREEN.get_height()/6))
                NEXT_BUTTON = Button(image=None, pos=(SCREEN.get_width()-10,3*SCREEN.get_height()-10), 
                                text_input=">", font=get_font(24), base_color="#d7fcd4", hovering_color="White")
                SCREEN.blit(TEXT_1,TEXT_1_RECT)
            elif(ans==2):
                TEXT_2=get_font(24).render("เจอกล่องที่ล็อคไว้", True, "#d7fcd4")
                TEXT_2_RECT = TEXT_2.get_rect(center=(SCREEN.get_width()/2,SCREEN.get_height()/6))
                NEXT_BUTTON = Button(image=None, pos=(SCREEN.get_width()-10,3*SCREEN.get_height()-10), 
                                text_input=">", font=get_font(24), base_color="#d7fcd4", hovering_color="White")
                SCREEN.blit(TEXT_2,TEXT_2_RECT)
                
            for button in [NEXT_BUTTON]:
                button.changeColor(Question_MOUSE_POS)
                button.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if NEXT_BUTTON.checkForInput(Question_MOUSE_POS):
                        play()

            pygame.display.update()
            
pygame.quit()
sys.exit()        


