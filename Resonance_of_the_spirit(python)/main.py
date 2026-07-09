import pygame,sys
from button import Button
import os
from pygame.sprite import Sprite, Group

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)  # เปลี่ยนให้เป็นเต็มหน้าจอ
WIDTH, HEIGHT = SCREEN.get_size()
pygame.display.set_caption("เกมสืบสวนสอบสวน")
point = [0,0,0]
click = 0
i = 0

def blit_char(surface,image,height,x):
    img_name="Characters\%s" %image
    img=pygame.image.load(img_name)
    img = pygame.transform.scale(img, (img.get_width()*40/100,height))
    surface.blit(img, (x,0))

def blit_image(surface,image,y):
    img_name="BG project\%s" %image
    img = pygame.image.load(img_name).convert()
    img = pygame.transform.scale(img, (SCREEN.get_width(),y))
    surface.blit(img, (0,0))
    return img.get_height()

def blit_text_scene(surface,text,pos,size,color):
    text=pygame.font.Font('THSarabunNew.ttf',size).render(text, True,color)
    text_RECT = text.get_rect(center=(pos))
    surface.blit(text, text_RECT)
        
def blit_button(surface,mouse,text,pos,size,color):
    button=Button(image=None, pos=pos,text_input=text, font=pygame.font.Font('THSarabunNew.ttf',size)
                  , base_color=color, hovering_color="White")
    button.changeColor(mouse)
    button.update(surface)
    return button.checkForInput(mouse)

def blit_text(surface, text, pos, size, color):
    font=pygame.font.Font('THSarabunNew.ttf',size)
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y = y + word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y = y + word_height  # Start on new row.

def main_menu():
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        blit_text_scene(SCREEN, "หน้าหลัก", (SCREEN.get_width()/2, SCREEN.get_height()/6), (100), "#b68f40")
        
        PLAY_BUTTON = blit_button(SCREEN, MENU_MOUSE_POS, "เริ่มเกม", (SCREEN.get_width()/2, 3*SCREEN.get_height()/6), (75), "#d7fcd4")
        QUIT_BUTTON = blit_button(SCREEN, MENU_MOUSE_POS, "ออกจากเกม", (SCREEN.get_width()/2, 4*SCREEN.get_height()/6), (75), "#d7fcd4")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON:
                    scene_1_0()
                if QUIT_BUTTON:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # กด ESC ออกจากเกม
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
            

def scene_1_0():
    global click
    click = 0
    while True:
        scene_1_0_MOUSE_POS = pygame.mouse.get_pos()
        story=["คุณลืมตาตื่นขึ้นมาในสถานที่แปลกตา สถานที่นี้ดูเหมือนจะเป็นห้องนอนของคนสองคน ดูจากการที่มีอุปกรณ์หลายอยย่างที่เหมือนกัน บางทีคนที่อาศัยอยู่ในห้องนี้คงเป็นฝาแฝดกัน",
               "เมื่อมองสำรวจจนพอใจแล้ว คุณจึงเริ่มสำรวจตัวเองบ้าง ตัวคุณดูจะแปลกไปจากปกติ ทั้งมุมมองความสูง และชุดที่คุณใส่ก็เป็นชุดนักเรียน ซึ่งแตกต่างจากชุดล่าสุดที่คุณใส่",
               "อยู่ดีๆ ก็มีหน้าต่างแปลกๆ โผล่ขึ้นมากลางอากาศ คุณตกใจกับสิ่งแปลกๆ ที่เห็น",
               "เมื่อคุณตั้งสติกับสิ่งที่เกิดขึ้นได้ คุณจึงอ่านสิ่งที่ปรากฎบนหน้าต่างนั้น",
               "","เมื่อคุณอ่านจบก็มีคนวิ่งเข้ามาในห้อง",
               "คุณจึงมองไปที่คนคนนั้น ปรากฎเป็นร่างของเด็กผู้หญิงคนนึง",
               "เด็กผู้หญิงคนนั้นใส่ชุดนักเรียนที่ดูจะยับนิดหน่อย",
               "แต่เมื่อเด็กผู้หญิงคนนั้นเข้ามาใกล้คุณมากยิ่งขึ้น คุณก็เห็นหน้าต่างแปลกๆ นั่นปรากฎขึ้นมาอีกครั้ง",
               "","ยังไม่ทันที่คุณจะอ่านเนื้อหาบนหน้าต่างอย่างละเอียด เด็กผู้หญิงคนนั้นก็พูดขึ้นมา",
               "'เดี๋ยวฉันรีบไปก่อนนะ พอดีมีนัดกับเพื่อนในห้องตอนเช้า'",
               "เมื่อเด็กผู้หญิงเอ่ยจบก็รีบวิ่งออกจากห้องไป พร้อมทั้งการหายไปหน้าต่างแปลกๆ",
               "คุณตกใจกับสถานะการณ์ที่พึ่งเกิดขึ้น แต่สิ่งที่พึ่งเห็นจากหน้าต่างแปลกๆ ก็ทำให้คุณรู้ตัวผู้ที่เสียชีวิตแล้ว และรู้ว่าที่นี่คือโรงเรียนประจำ พวกคุณเป็นรูมเมทกัน",
               "คุณจึงพยายามคิดวิธีสืบหาสาเหตุที่เด็กผู้หญิงคนนั้นจะเสียชีวิต"] 
        img=["(2.1) BG หอพัก.png","BG system1.png","BG system2.png"]
        SCREEN.fill("black")
        if (click==4):
            blit_image(SCREEN,img[1],SCREEN.get_height())
        elif (click==9):
            blit_image(SCREEN,img[2],SCREEN.get_height())
        else :
            blit_image(SCREEN,img[0],SCREEN.get_height()-145)
            if(click>4)and(click<=11):
                blit_char(SCREEN,"เหยื่อ.png",(SCREEN.get_height()-145),(300))
        blit_text(SCREEN, story[click], (100,SCREEN.get_height()-120), (40), color="#d7fcd4" )
        NEXT_BUTTON = blit_button(SCREEN, scene_1_0_MOUSE_POS, ">", (SCREEN.get_width()-75, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                    if NEXT_BUTTON or event.key==pygame.K_RETURN:
                        click=click+1
                        if (click<15):
                            os.system('cls')
                        elif(click==15):
                            scene_1()

        pygame.display.update()   


def scene_1():
    while True:
        scene_1_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        blit_image(SCREEN,"(2.1) BG หอพัก.png",SCREEN.get_height()-145)
        blit_text_scene(SCREEN, "คุณจะทำอะไรต่อไป", (SCREEN.get_width()/6, 6*SCREEN.get_height()/7), (55), "#d7fcd4")
        Answer1_BUTTON = blit_button(SCREEN, scene_1_MOUSE_POS, "สำรวจโต๊ะของตัวเอง"
                                     , (SCREEN.get_width()/6,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        Answer2_BUTTON = blit_button(SCREEN, scene_1_MOUSE_POS, "สำรวจโต๊ะของเพื่อน"
                                     , (SCREEN.get_width()/2,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        Answer3_BUTTON = blit_button(SCREEN, scene_1_MOUSE_POS, "ไปเรียน"
                                     , (5*SCREEN.get_width()/6, 5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Answer1_BUTTON:
                    result_1(1)
                if Answer2_BUTTON:
                    result_1(2)
                if Answer3_BUTTON:
                    result_1(3)   

        pygame.display.update()


def result_1(ans):
    global click
    click = 0
    while True:
        result_1_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        if (ans==1):
            story=["คุณตัดสินใจสำรวจโต๊ะของคุณ",
                    "คุณค้นหาสิ่งที่อยู่บนโต๊ะ"]
            SCREEN.fill("black")
            blit_image(SCREEN,"โต๊ะเรา.png",SCREEN.get_height()-145)
            blit_text(SCREEN, story[click], (100,SCREEN.get_height()-120), (40), color="#d7fcd4" )
            NEXT_BUTTON = blit_button(SCREEN, result_1_MOUSE_POS, ">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                        if NEXT_BUTTON or event.key==pygame.K_RETURN:
                            click=click+1
                            if (click<2):
                                os.system('cls')
                            elif(click==2):
                                evidence1(0)
            
        elif(ans==2):
            story=["คุณตัดสินใจสำรวจโต๊ะของเพื่อน",
                    "คุณค้นหาสิ่งที่อยู่บนโต๊ะ"] 
            SCREEN.fill("black")
            blit_image(SCREEN,"โต๊ะเพื่อน.png",SCREEN.get_height()-145)
            blit_text(SCREEN, story[click], (100,SCREEN.get_height()-120), (40), color="#d7fcd4" )
            NEXT_BUTTON = blit_button(SCREEN, result_1_MOUSE_POS, ">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                        if NEXT_BUTTON or event.key==pygame.K_RETURN:
                            click=click+1
                            if (click<2):
                                os.system('cls')
                            elif(click==2):
                                evidence1(1)
        elif(ans==3):
            story=["คุณตัดสินใจไปเรียน",
                    "เมื่อคุณตัดสินใจได้จึงรีบหยิบกระเป๋านักเรียนของคุณ และเดินตามหาห้องเรียนของตัวเองตามสิ่งที่เขียนไว้ในบัตรนักเรียนของคุณ"] 
            SCREEN.fill("black")
            blit_image(SCREEN,"(2.1) BG หอพัก.png",SCREEN.get_height()-145)
            blit_text(SCREEN, story[click], (100,SCREEN.get_height()-120), (40), color="#d7fcd4" )
            NEXT_BUTTON = blit_button(SCREEN, result_1_MOUSE_POS, ">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                        if NEXT_BUTTON or event.key==pygame.K_RETURN:
                            click=click+1
                            if (click<2):
                                os.system('cls')
                            elif(click==2):
                                scene_2_0()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                if NEXT_BUTTON or event.key==pygame.K_RETURN:
                    scene_1()

        pygame.display.update()

def evidence1(ans):
    evi=["คุณพบไดอารี่ของเจ้าของร่าง เนื้อหาเกี่ยวกับชีวิตประจำวัน",
         "คุณพบกล่องที่ล็อคไว้ ซึ่งที่แม่กุญแจนั้นดูจะสามารถปลดล็อคได้หากหารหัสเลข 4 ตัวมาใส่ได้"]
    img=["สำรวจไดอารี่.png","สำรวจกล่อง.png"]
    while True:
        evidence_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        if (ans==0):
            blit_image(SCREEN,img[ans],SCREEN.get_height()-145)
            blit_text_scene(SCREEN,evi[ans],(SCREEN.get_width()/2, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            NEXT_BUTTON = blit_button(SCREEN, evidence_MOUSE_POS, ">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            point[0] = point[0] + 1
        elif(ans==1):
            blit_image(SCREEN,img[ans],SCREEN.get_height()-145)
            blit_text_scene(SCREEN,evi[ans],(SCREEN.get_width()/2, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            NEXT_BUTTON = blit_button(SCREEN, evidence_MOUSE_POS,">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            point[0] = point[0] + 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                if NEXT_BUTTON or event.key==pygame.K_RETURN:
                    scene_1()

        pygame.display.update()

def scene_2_0():
    global click
    click=0
    while True:
        scene_2_0_MOUSE_POS = pygame.mouse.get_pos()
        story=["เมื่อคุณพบห้องเรียนแล้วจึงพบว่าอาจารย์มาถึง และเตรียมจะเริ่มสอนแล้ว",
                "คุณกวาดตามองหาโต๊ะที่ว่างอยู่ เมื่อพบโต๊ะที่เป็นโต๊ะเดียวที่เหลืออยู่ คุณจึงรีบเข้าไปนั่งที่โต๊ะนั้นที่คาดว่าจะเป็นโต๊ะเรียนของเจ้าของร่าง",
                "เมื่อคุณนั่งแล้วจึงกวาดสายตามองไปรอบๆ ห้องเรียน พยายามหาเด็กผู้หญิงที่คุณพบในห้องนอน แต่คุณก็ต้องผิดหวัง เมื่อไม่พบเด็กผู้หญิงคนนั้น คุณจึงถอนสายตากลับมามองไปที่อาจารย์หน้าห้องเรียน",
                "หน้าต่างแปลกๆ นั่นปรากฎขึ้นอีกครั้ง ครั้งนี้เป็นข้อมูลของอาจารย์ที่อยู่หน้าห้อง",
                "","จากนั้นไม่นานอาจารย์ที่อยู่หน้าห้องก็เริ่มสอนบทเรียน จากที่คุณฟังก็ได้พบว่าอาจารย์คนนี้สอนวิชาคณิตศาสตร์ ซึ่งกำลังสอนวิธีการหาคำตอบจากสามเหลี่ยมแปลกๆ ตรงหน้า",
                "เมื่อได้ยินดังนั้นคุณจึงหยิบหนังสือที่อยู่ในกระเป๋าของคุณขึ้นมา เพื่อเปิดอ่านตามบทเรียนให้ดูไม่มีพิรุธ แต่ที่ปกหนังสือเรียนนั้นมีชื่อของเพื่อนรูมเมทของคุณอยู่ ทำให้คุณคิดว่าคงจะหยิบสลับกันมา",
                "ระหว่างที่คุณเปิดหาเนื้อหาที่ตรงกัน คุณก็เห็นเลขแปลกๆ เขียนอยู่ในหน้าหนังสือ เลขนั้นคือ 2511 แต่คุณก็ไม่ได้สนใจกับเลขนั้นมากนัก จึงเปิดหนังสือไปจนพบเนื้อหาที่อาจารย์กำลังพูดอยู่",
                "อัมพร : เลขที่อยู่ตรงกลางสามเหลี่ยมได้มาจากการนำเลขที่อยู่บริเวณมุมของสามเหลี่ยมทั้งสามเลขมาคิด โดยใช้เครื่องหมายทางคณิตศาสตร์ต่างๆ",
                "ตัวอย่าง",
                "เฉลยวิธีคิด",
                "เมื่ออาจารย์อธิบายเสร็จก็ได้ทำการกวาดสายตามองรอบๆ ห้อง",
                "อัมพร : เธอลองมาตอบโจทย์ข้อนี้",
                "อาจารย์ชี้นิ้วมาที่คุณ เพื่อให้คุณตอบคำถาม",
                "คุณตกใจเล็กน้อยแต่ไม่แสดงอาการแปลกๆ ออกไป และลุกขึ้นเดินไปที่หน้าห้องเพื่อตอบคำถาม"] 
        img=["(5) BG ห้องเรียน.png","BG system3.png","หนังสือเรียน.png","ตัวอย่าง.png","ตัวอย่าง+เฉลย.png","โจทย์1.png"]
        SCREEN.fill("black")
        if(click==4):
            blit_image(SCREEN,img[1],SCREEN.get_height())
        elif(click==7):
            blit_image(SCREEN,img[2],SCREEN.get_height()-145)
        elif(click>7)and(click<=9):
            blit_image(SCREEN,img[3],SCREEN.get_height()-145)
            blit_char(SCREEN,"ครูคณิต.png",(SCREEN.get_height()-145),(450))
        elif(click>9)and(click<=11):
            blit_image(SCREEN,img[4],SCREEN.get_height()-145)
            blit_char(SCREEN,"ครูคณิต.png",(SCREEN.get_height()-145),(450))
        elif(click>11):
            blit_image(SCREEN,img[5],SCREEN.get_height()-145)
            blit_char(SCREEN,"ครูคณิต.png",(SCREEN.get_height()-145),(450))
        else:
            blit_image(SCREEN,img[0],SCREEN.get_height()-145)
        blit_text(SCREEN, story[click], (100,SCREEN.get_height()-120), (40), color="#d7fcd4" )
        NEXT_BUTTON = blit_button(SCREEN, scene_2_0_MOUSE_POS, ">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                    if NEXT_BUTTON or event.key==pygame.K_RETURN:
                        click=click+1
                        if (click<15):
                            os.system('cls')
                        elif(click==15):
                            scene_2_1()

        pygame.display.update()   

def scene_2_1():
    while True:
        scene_2_1_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        blit_image(SCREEN,"โจทย์1.png",SCREEN.get_height()-145)
        blit_text_scene(SCREEN, "คำตอบของคำถามข้อที่ 1 คืออะไร",(SCREEN.get_width()/2, 5*SCREEN.get_height()/7), (55), "#d7fcd4")
        Answer1_BUTTON = blit_button(SCREEN, scene_2_1_MOUSE_POS, "15", (SCREEN.get_width()/5,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        Answer2_BUTTON = blit_button(SCREEN, scene_2_1_MOUSE_POS, "3", (2*SCREEN.get_width()/5,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        Answer3_BUTTON = blit_button(SCREEN, scene_2_1_MOUSE_POS, "9", (3*SCREEN.get_width()/5,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        Answer4_BUTTON = blit_button(SCREEN, scene_2_1_MOUSE_POS, "11", (4*SCREEN.get_width()/5,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Answer1_BUTTON:
                    result_2(1)
                if Answer2_BUTTON:
                    result_2(1)
                if Answer3_BUTTON:
                    result_2(1)
                if Answer4_BUTTON:
                    result_2(2)

        pygame.display.update()

def scene_2_2():
    while True:
        scene_2_2_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        blit_image(SCREEN,"โจทย์2.png",SCREEN.get_height()-145)
        blit_text_scene(SCREEN, "คำตอบของคำถามข้อที่ 2 คืออะไร",(SCREEN.get_width()/2, 5*SCREEN.get_height()/7), (55), "#d7fcd4")
        Answer1_BUTTON = blit_button(SCREEN, scene_2_2_MOUSE_POS, "8", (SCREEN.get_width()/5,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        Answer2_BUTTON = blit_button(SCREEN, scene_2_2_MOUSE_POS, "11", (2*SCREEN.get_width()/5,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        Answer3_BUTTON = blit_button(SCREEN, scene_2_2_MOUSE_POS, "7", (3*SCREEN.get_width()/5,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        Answer4_BUTTON = blit_button(SCREEN, scene_2_2_MOUSE_POS, "4", (4*SCREEN.get_width()/5,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Answer1_BUTTON:
                    result_2(1)
                if Answer2_BUTTON:
                    result_2(1)
                if Answer3_BUTTON:
                    result_2(2)
                if Answer4_BUTTON:
                    result_2(1)

        pygame.display.update()

def result_2(ans):
    global i
    i=i+1
    while True:
        result_2_MOUSE_POS = pygame.mouse.get_pos()
        img=["โจทย์1+เฉลย.png","โจทย์2+เฉลย.png"]
        SCREEN.fill("black")
        if (ans==1):
            if(i==1):
                blit_image(SCREEN,img[0],SCREEN.get_height()-145)
            else:
                blit_image(SCREEN,img[1],SCREEN.get_height()-145)
            blit_text_scene(SCREEN, "คุณตอบผิด อาจารย์ที่อยู่ตรงหน้าคุณขมวดคิ้วเล็กน้อย"
                            ,(SCREEN.get_width()/2, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            NEXT_BUTTON = blit_button(SCREEN, result_2_MOUSE_POS,">", (SCREEN.get_width()-100,5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
        elif(ans==2):
            if(i==1):
                blit_image(SCREEN,img[0],SCREEN.get_height()-145)
            else:
                blit_image(SCREEN,img[1],SCREEN.get_height()-145)
            blit_text_scene(SCREEN, "คุณตอบถูก อาจารย์ที่อยู่ตรงหน้าคุณอมยิ้มเล็กน้อย"
                            ,(SCREEN.get_width()/2, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            NEXT_BUTTON = blit_button(SCREEN, result_2_MOUSE_POS, ">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            point[1] = point[1] + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                if NEXT_BUTTON or event.key==pygame.K_RETURN:
                    if(i == 1):
                        scene_2_2()
                    else:
                        scene_3_0()

        pygame.display.update()

def scene_3_0():
    global click
    click=0
    while True:
        scene_3_0_MOUSE_POS = pygame.mouse.get_pos()
        story=["เมื่อตอบคำถามของอาจารย์จบคุณก็ได้ยินเสียงกริ่งเลิกเรียน เมื่ออาจารย์ได้ยินเสียงนั้นจึงเก็บของ และออกจากห้องเรียนไป",
                "คุณเห็นดังนั้นจึงเก็บของ และออกจากห้องเรียนเช่นกัน เพื่อกลับมาที่ห้องนอนของคุณ",
                "คุณเดินกลับมาที่ห้องนอน และเตรียมของเพื่อไปอาบน้ำ",
                "เมื่อคุณอาบน้ำเสร็จจึงเดินกลับห้องนอน และระหว่างทางเดินคุณก็ได้พบกับร่างๆ นึง ที่กำลังจะเดินสวนทางกับคุณ",
                "เมื่อร่างนั้นเข้ามาใกล้ก็ทำให้คุณเห็นว่าร่างนั้นดูจะไม่เหมือนมนุษย์ มีผิวที่ซีดขาว และมีเลือดเปื้อนที่ตัว",
                "ร่างนั้นเข้ามาใกล้เรื่อยๆ จนห่างจากคุณประมาณหนึ่งช่วงแขน คุณก็รู้สึกคุ้นๆ ตากับร่างนี้ชอบกล",
                "นึกเรื่องนี้ได้ไม่นาน คุณก็นึกออก ว่าร่างตรงหน้านี้คือใคร",
                "ร่างตรงหน้านี้ คือ เพื่อนรูทเมทของคุณนั่นเอง"] 
        img=["(5) BG ห้องเรียน.png","(8) BG ทางไปหอพัก.png","(2.1) BG หอพัก.png",""]
        SCREEN.fill("black")
        if(click==0):
            blit_image(SCREEN,img[click],SCREEN.get_height()-145)
        elif(click==1):
            blit_image(SCREEN,img[click],SCREEN.get_height()-145)
        elif(click==2):
            blit_image(SCREEN,img[click],SCREEN.get_height()-145)

        blit_text(SCREEN, story[click], (100,600), (40), color="#d7fcd4" )
        NEXT_BUTTON = blit_button(SCREEN, scene_3_0_MOUSE_POS, ">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                    if NEXT_BUTTON or event.key==pygame.K_RETURN:
                        click=click+1
                        if (click<8):
                            os.system('cls')
                        elif(click==8):
                            scene_3()

        pygame.display.update()   

def scene_3():
    while True:
        scene_3_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        blit_text_scene(SCREEN, "คุณจะทำอะไรต่อไป", (SCREEN.get_width()/6, 5*SCREEN.get_height()/7), (55), "#d7fcd4")
        Answer1_BUTTON = blit_button(SCREEN, scene_3_MOUSE_POS, "คุณทำตัวปกติ ", (SCREEN.get_width()/6,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        Answer2_BUTTON = blit_button(SCREEN, scene_3_MOUSE_POS, "คุณตกใจรีบวิ่งกลับห้องโดยไม่ทักทายเพื่อนของคุณ", (SCREEN.get_width()/2,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        Answer3_BUTTON = blit_button(SCREEN, scene_3_MOUSE_POS, "คุณกรี๊ดออกมาแล้วรีบวิ่งเข้าห้อง", (5*SCREEN.get_width()/6, 5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Answer1_BUTTON:
                    result_3(1)
                if Answer2_BUTTON:
                    result_3(2)
                if Answer3_BUTTON:
                    result_3(3)   

        pygame.display.update()

def result_3(ans):
    global click
    click = 0
    while True:
        result_3_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        if (ans==1):
            story=["ธิญา : จะไปไหน",
                    "คุณถามเพื่อนไปโดยพยายามทำให้น้ำเสียงปกติที่สุด",
                    "ญาตา : ไปอาบน้ำ",
                    "เมื่อเอ่ยจบเพื่อนของคุณก็เดินหนีออกไป คุณจึงรีบเดินกลับห้องกัน"]
            SCREEN.fill("black")
            blit_image(SCREEN,"โต๊ะเรา.png",SCREEN.get_height()-145)
            blit_text(SCREEN, story[click], (100,SCREEN.get_height()-120), (40), color="#d7fcd4" )
            NEXT_BUTTON = blit_button(SCREEN, result_3_MOUSE_POS, ">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            point[2] = point[2] + 1

        elif(ans==2):
            blit_text_scene(SCREEN, "เพื่อนของคุณมึนงงกับสิ่งที่คุณทำ", (SCREEN.get_width()/2, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            NEXT_BUTTON = blit_button(SCREEN, result_3_MOUSE_POS,">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")

        elif(ans==3):
            blit_text_scene(SCREEN, "เพื่อนของคุณตกใจ และไม่พอใจกับสิ่งที่คุณทำ"
                            ,(SCREEN.get_width()/2, 5*SCREEN.get_height()/6), (40), "#d7fcd4")
            NEXT_BUTTON = blit_button(SCREEN, result_3_MOUSE_POS, ">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            point[2] = point[2] - 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                if NEXT_BUTTON or event.key==pygame.K_RETURN:
                    if(ans==1):
                        click=click+1
                        if (click<4):
                            os.system('cls')
                        elif(click==4):
                            scene_4_0
                    else:
                        scene_4_0()

        pygame.display.update()

def scene_4_0():
    global click
    click=0
    while True:
        scene_4_0_MOUSE_POS = pygame.mouse.get_pos()
        story=["เมื่อคุณมาถึงห้องแล้วจึงรีบปิด และล็อคประตู ก่อนจะพยายามสงบสติอารมณ์ของตัวเองจากสิ่งที่พึ่งพบเห็น และหวังว่าเพื่อนของคุณจะยังไม่กลับมาที่ห้องด้วยสภาพนั้นเร็วๆ นี้",
                "เวลาผ่านไปซักพักคุณจึงเริ่มสงบลง และเริ่มคิดเกี่ยวกับสิ่งที่พบเห็น",
                "ธิญา : ‘เด็กผู้หญิงคนนั้นโผล่มาแบบน่ากลัวเลย ลักษณะของเธอที่เห็นบางทีอาจจะเหมือนกับตอนที่เธอเสียชีวิต’",
                "ธิญา : ‘เอาเป็นว่าคืนนี้นอนพักผ่อน เพื่อเก็บแรงไว้หาหลักฐานในวันพรุ่งนี้ดีกว่า’",
                "เมื่อคุณคิดได้ดังนั้นจึงล้มตัวลงพยายามนอนให้หลับ ถึงแม้ตอนหลับตาจะนึกถึงภาพที่พึ่งเห็นไปก็ตาม",
                "เวลาผ่านไปพักใหญ่คุณถึงได้หลับลง",
                "เวลาล่วงเลยผ่านไปจนเช้า",
                "คุณลืมตาตื่นขึ้นมาในตอนเช้า ถึงแม้ว่าคุณจะนอนไปไม่นาน แต่ก็ถือว่าไม่แย่สำหรับวันแรกที่อยู่ในสถานที่แปลกๆ นี้",
                "คุณลุกขึ้นมานั่งคิดว่าจะทำอะไรต่อไปหลังจากนี้ และนึกทบทวนสิ่งที่เจอมาเมื่อวาน ทำให้คุณนึกถึงเลขที่คุณพบในหนังสือเรียนที่คุณหยิบสลับกับเพื่อนรูมเมท และกล่องที่ล็อคไว้บนโต๊ะเพื่อนคนนั้น",
                "เมื่อคุณนำสองสิ่งนี้มารวมกัน คุณจึงคิดว่ารหัสนั้นอาจจะเป็นเลขที่คุณพบก็ได้ คุณจึงเดินไปที่โต๊ะของเพื่อนเพื่อลองใส่รหัสนั้นลงไป"] 
                
        SCREEN.fill("black")
        if(click<=4)and(click==8):
            blit_image(SCREEN,"(2.1) BG หอพัก.png",SCREEN.get_height()-145) 
        elif(click<8):
            blit_image(SCREEN,"โต๊ะเพื่อน.png",SCREEN.get_height()-145)
        blit_text(SCREEN, story[click], (100,600), (40), color="#d7fcd4" )
        NEXT_BUTTON = blit_button(SCREEN, scene_4_0_MOUSE_POS, ">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                    if NEXT_BUTTON or event.key==pygame.K_RETURN:
                        click=click+1
                        if (click<10):
                            os.system('cls')
                        elif(click==10):
                            scene_4()

        pygame.display.update()   

def scene_4():
    while True:
        scene_4_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        blit_image(SCREEN,"สำรวจกล่อง.png",SCREEN.get_height()-145)
        blit_text_scene(SCREEN, "รหัสเลขที่คุณพบคืออะไร", (SCREEN.get_width()/6, 5*SCREEN.get_height()/7), (55), "#d7fcd4")
        Answer1_BUTTON = blit_button(SCREEN, scene_4_MOUSE_POS, "1511", (SCREEN.get_width()/5,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        Answer2_BUTTON = blit_button(SCREEN, scene_4_MOUSE_POS, "2511", (2*SCREEN.get_width()/5,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        Answer3_BUTTON = blit_button(SCREEN, scene_4_MOUSE_POS, "1512", (3*SCREEN.get_width()/5,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        Answer4_BUTTON = blit_button(SCREEN, scene_4_MOUSE_POS, "2512", (4*SCREEN.get_width()/5,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Answer1_BUTTON:
                    result_4(1)
                if Answer2_BUTTON:
                    result_4(2) 
                if Answer3_BUTTON:
                    result_4(1) 
                if Answer4_BUTTON:
                    result_4(1) 

        pygame.display.update()

def result_4(ans):
    global click
    click = 0
    while True:
        result_4_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        if (ans==1):
            blit_text_scene(SCREEN, "เพื่อนของคุณมึนงงกับสิ่งที่คุณทำ", (SCREEN.get_width()/2, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            NEXT_BUTTON = blit_button(SCREEN, result_4_MOUSE_POS, ">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            
        elif(ans==2):
            scene_5_0()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                if NEXT_BUTTON or event.key==pygame.K_RETURN:
                    scene_4()

        pygame.display.update()

def scene_5_0():
    global click
    click=0
    while True:
        scene_5_0_MOUSE_POS = pygame.mouse.get_pos()
        story=["คุณใส่รหัสนั้นไปทำให้กล่องใบนั้นสามาถเปิดได้",
                "ในกล่องใบนั้นมีสำเนาเอกสารสำคัญต่างๆ ของเพื่อนคุณ เช่น สำเนาใบเกิด และสำเนาทะเบียนบ้าน",
                "คุณลองอ่านเอกสารต่างๆ แต่ก็ไม่พบเบาะแสใดๆ เพิ่มเติม คุณจึงคิดว่าควรจะไปสำรวจรอบๆ โรงเรียน"] 
        SCREEN.fill("black")
        
        blit_text(SCREEN, story[click], (100,600), (40), color="#d7fcd4" )
        NEXT_BUTTON = blit_button(SCREEN, scene_5_0_MOUSE_POS, ">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                    if NEXT_BUTTON or event.key==pygame.K_RETURN:
                        click=click+1
                        if (click<3):
                            os.system('cls')
                        elif(click==3):
                            scene_5()

        pygame.display.update()   

def scene_5():
    while True:
        scene_5_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        blit_text_scene(SCREEN, "คุณจะไปสำรวจที่ไหนก่อน", (SCREEN.get_width()/6, 5*SCREEN.get_height()/7), (55), "#d7fcd4")
        Answer1_BUTTON = blit_button(SCREEN, scene_5_MOUSE_POS, "ห้องพยาบาล", (SCREEN.get_width()/6,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        Answer2_BUTTON = blit_button(SCREEN, scene_5_MOUSE_POS, "โรงอาหาร", (SCREEN.get_width()/2,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Answer1_BUTTON:
                    result_5(1)
                if Answer2_BUTTON:
                    result_5(2)

        pygame.display.update()

def result_5(ans):
    global click
    click = 0
    while True:
        result_5_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        story=["เมื่อตัดสินใจว่าจะไปที่ไหนได้แล้วคุณจึงเดอนตามหาสถานที่นั้น",
                "โดยระหว่างทางคุณก็ได้ยินเสียงคนที่ทะเลาะกันเสียงดัง ตอนแรกคุณก็ไม่สนใจที่จะฟัง แต่ดันได้ยินชื่อที่คุ้นหูเข้า ชื่อนั้น คือ ชื่อของเพื่อนรูมเมทของคุณ",
                "??? : ปล่อยมือญาตา ก็เคยบอกเธอแล้วว่าถ้าเธอไม่ดูแลตัวเอง ไม่กินยาคุม แล้วเกิดท้องขึ้นมาฉันจะไม่รับผิดชอบ และเราจะต้องเลิกกัน",
                "เสียงเด็กผู้ชายที่เลยวัยแตกหนุ่มไปแล้วพูดออกมา",
                "ญาตา : ทำไมถึงทำกับฉันแบบนี้ เราก็รักกัน ไม่เคยมีเรื่องทะเลาะกันมาตลอด แต่ทำไมนายถึงพูดแบบนั้นออกมา เราไม่รักกันตอนไหน",
                "เสียงของเด็กผู้หญิงที่คุ้นหูพูดออกมา",
                "??? : ก็ไม่เคยรักมาตลอดนะญาตา สิ่งที่ทำกับเธอมาตลอดก็แค่สนุกเฉยๆ อีกอย่างฉันก็ทำแบบนี้กับเด็กผู้หญิงทุกคนนะ ไม่เห็นมีใครมาโวยวายแบบนี้เลย",
                "เมื่อได้ยินบทสนทนานี้คุณจึงพยายามฟังต่อเพื่อเก็บข้อมูลไว้หาสาเหตุที่ทำให้รูมเมทของคุณเสียชีวิต",
                "หลังจากที่เด็กผู้ชายพูดแบบนั้นออกมาก็ไม่ได้ยินเสียตอบกลับจากเด็กผู้หญิง แต่กลับได้ยินเสียงร้องไห้ของเธอแทน",
                "??? : พวกเธอทะเลาะอะไรกัน",
                "เสียงของคนที่คาดว่าเป็นอาจารย์ดังขึ้นหลังจากนั้นไม่นาน คุณจึงรีบเดินหนีออกจากที่นั่น เพราะไม่อยากให้ใครมาพบคุณ",
                "คุณตัดสินใจเดินทางไปที่สถานที่ที่คุณตัดสินใจไว้ต่อ"] 
        if (ans==1):
            SCREEN.fill("black")
            blit_image(SCREEN,"(8) BG ทางไปหอพัก.png",SCREEN.get_height()-145)
            blit_text(SCREEN, story[click], (100,SCREEN.get_height()-120), (40), color="#d7fcd4" )
            NEXT_BUTTON = blit_button(SCREEN, result_5_MOUSE_POS, ">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                        if NEXT_BUTTON or event.key==pygame.K_RETURN:
                            click=click+1
                            if (click<12):
                                os.system('cls')
                            elif(click==12):
                                scene_5_1()
    
        elif(ans==2):
            SCREEN.fill("black")
            blit_image(SCREEN,"(8) BG ทางไปหอพัก.png",SCREEN.get_height()-145)
            blit_text(SCREEN, story[click], (100,SCREEN.get_height()-120), (40), color="#d7fcd4" )
            NEXT_BUTTON = blit_button(SCREEN, result_5_MOUSE_POS, ">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                        if NEXT_BUTTON or event.key==pygame.K_RETURN:
                            click=click+1
                            if (click<2):
                                os.system('cls')
                            elif(click==2):
                                evidence2(0)
                                scene_5_1()

            pygame.display.update()

def scene_5_1():
    while True:
        scene_5_1_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        blit_text_scene(SCREEN, "คุณจะสำรวจที่ใดก่อน", (SCREEN.get_width()/6, 5*SCREEN.get_height()/7), (55), "#d7fcd4")
        Answer1_BUTTON = blit_button(SCREEN, scene_5_1_MOUSE_POS, "สำรวจโต๊ะของอาจารย์ประจำห้องพยาบาล", (SCREEN.get_width()/6,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        Answer2_BUTTON = blit_button(SCREEN, scene_5_1_MOUSE_POS, "สำรวจชั้นวางยาในห้องพยาบาล", (SCREEN.get_width()/2,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Answer1_BUTTON:
                    result_5_1(1)
                if Answer2_BUTTON:
                    result_5_1(2)

        pygame.display.update()

def result_5_1(ans):
    global click
    click = 0
    while True:
        result_5_1_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        story=["เมื่อคุณมาถึงห้องพยาบาลแล้วจึงลองเข้าไปสำรวจในห้อง",
                "แต่เมื่อสำรวจแล้วคุณก็ไม่พบใครในห้อง คุณจึงคิดจะเดินสำรวจห้อง"]
        img=["(1) BG ห้องพยาบาล",""]
        blit_text(SCREEN, story[click], (100,600), (40), color="#d7fcd4" )
        blit_image(SCREEN,img[click],SCREEN.get_height()-145)
        if click<2 :
            click=0
            if  (ans==1):
                choice1=["คุณตัดสินใจสำรวจโต๊ะของอาจารย์ประจำห้องพยาบาล","คุณหาสิ่งที่อยู่บนโต๊ะ"] 
                blit_image(SCREEN,img[click],SCREEN.get_height()-145)
                blit_text(SCREEN, choice1[click], (100,600), (40), color="#d7fcd4" )
                NEXT_BUTTON = blit_button(SCREEN, result_5_1_MOUSE_POS, ">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                            if NEXT_BUTTON or event.key==pygame.K_RETURN:
                                click=click+1
                                if (click<2):
                                    os.system('cls')
                                elif(click==2):
                                    evidence2(0)
                
            elif(ans==2):
                choice2=["คุณตัดสินใจสำรวจชั้นวางยาในห้องพยาบาล","คุณมองดูชั้งที่วางยาต่างๆ ไว้มากมาย"] 
                blit_image(SCREEN,img[click],SCREEN.get_height()-145)
                blit_text(SCREEN, choice2[click], (100,600), (40), color="#d7fcd4" )
                NEXT_BUTTON = blit_button(SCREEN, result_5_1_MOUSE_POS, ">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
                    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                            if NEXT_BUTTON or event.key==pygame.K_RETURN:
                                click=click+1
                                if (click<2):
                                    os.system('cls')
                                elif(click==2):
                                    evidence2(1)

        pygame.display.update()

def evidence2(ans):
    evi=["คุณพบประวัติการเข้าห้องพยาบาลของเทอมนี้",
         "คุณพบยาแปลกๆ ที่ไม่ได้เขียนรายละเอียดไว้"]
    img=["(1) BG ห้องพยาบาล.png",""]
    while True:
        evidence_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        if (ans==0):
            blit_image(SCREEN,img[ans],SCREEN.get_height()-145)
            blit_text_scene(SCREEN,evi[ans],(SCREEN.get_width()/2, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            NEXT_BUTTON = blit_button(SCREEN, evidence_MOUSE_POS, ">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            point[0] = point[0] + 1
        elif(ans==1):
            blit_image(SCREEN,img[ans],SCREEN.get_height()-145)
            blit_text_scene(SCREEN,evi[ans],(SCREEN.get_width()/2, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            NEXT_BUTTON = blit_button(SCREEN, evidence_MOUSE_POS,">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            point[0] = point[0] + 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                if NEXT_BUTTON or event.key==pygame.K_RETURN:
                    scene_5()

        pygame.display.update()

def scene_5_2():
    global click
    click=0
    while True:
        scene_4_0_MOUSE_POS = pygame.mouse.get_pos()
        story=["เมื่อคุณสำรวจเสร็จได้ไม่นานประตูก็ถูกเปิดออกโดยใครบางคน และคนคนนั้นก็เข้ามาในห้อง",
                "ระหว่างนั้นหน้าต่างแปลกๆ ก็ปรากฎขึ้นอีกครั้ง ครั้งนี้เป็นข้อมูลของคนที่พึ่งเข้ามา",
                "ระบบ",
                "พงษ์นรินทร์ : ป่วยหรือบาดเจ็บอะไรมา มาตรวจกันก่อน เผื่อมีอะไรร้ายแรง",
                "อาจารย์ห้องพยาบาลพูดขึ้นขณะมองสำรวจตัวคุณไปด้วย",
                "ธิญา : พอดีรู้สึกไม่ค่อยสบายค่ะ เลยจะมาขอยาพาราไว้กินค่ะ",
                "คุณที่ไม่ได้เป็นอะไรแต่ดันมาที่ห้องพยาบาลจึงพยายามหาข้อแก้ตัว",
                "ธิญา : พอดีหนูเห็นชื่อเพื่อนรูมเมทของหนูในใบประวัติการเข้าห้องพยาบาลค่ะ ที่ชื่อญาตา เธอมาที่ห้องพยาบาลบ่อยหรือคะ",
                "พงษ์นรินทร์ : ญาตาสินะ เธอมาติดต่อขอยาโรคประจำตัวทุกเดือน และมาตรวจสุขภาพที่นี่เป็นประจำ เธอเป็นรูมเมทกันสินะ",
                "ธิญา : ใช่ค่ะ พวกหนูเป็นรูมเมทกันแล้วเห็นเธอมาบ่อยเลยสงสัยค่ะ",
                "พงษ์นรินทร์ : อืม เรื่องราวเป็นแบบนี้เองสินะ เห็นเธอเป็นรูมเมทกัน งั้นฝากยาโรคประจำตัวนี้ไปให้ญาตาทีนะ",
                "อาจารย์ห้องพยาบาลพูดพร้อมยื่นยาที่บอกมาให้คุณ",
                "ธิญา : ได้ค่ะ เดี๋ยวหนูจะเอาไปให้เธอเองค่ะ",
                "คุณยื่นมือไปรับยาที่ว่ามาเก็บไว้",
                "พงษ์นรินทร์ : ขอบใจที่เป็นธุระให้นะ",
                "ธิญา : ไม่เป็นไรค่ะ ไหนๆ ก็อยู่ห้องนอนเดียวกันแล้ว งั้นหนูขอตัวก่อนนะคะ",
                "อาจารย์พยักหน้าตอบรับคุณ",
                "เมื่อเห็นดังนั้นคุณจึงเดินออกมาจากห้องพยาบาล"] 
        SCREEN.fill("black")
        blit_image(SCREEN,"(1) BG ห้องพยาบาล",SCREEN.get_height()-145)
        blit_text(SCREEN, story[click], (100,600), (40), color="#d7fcd4" )
        NEXT_BUTTON = blit_button(SCREEN, scene_4_0_MOUSE_POS, ">", (SCREEN.get_width()-100, 5.5*SCREEN.get_height()/6), (40), "#d7fcd4")
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                    if NEXT_BUTTON or event.key==pygame.K_RETURN:
                        click=click+1
                        if (click<18):
                            os.system('cls')
                        elif(click==18):
                            scene_4()

        pygame.display.update()  

def scene_5_3():
    while True:
        scene_5_1_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        blit_text_scene(SCREEN, "คุณจะไปที่ไหนต่อ", (SCREEN.get_width()/6, 5*SCREEN.get_height()/7), (55), "#d7fcd4")
        Answer1_BUTTON = blit_button(SCREEN, scene_5_1_MOUSE_POS, "โรงอาหาร", (SCREEN.get_width()/6,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        Answer2_BUTTON = blit_button(SCREEN, scene_5_1_MOUSE_POS, "กลับไปเก็บของเตรียมกลับบ้าน", (SCREEN.get_width()/2,5.5*SCREEN.get_height()/6), (30), "#d7fcd4")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Answer1_BUTTON:
                    result_5_3(1)
                if Answer2_BUTTON:
                    result_5_3(2)

        pygame.display.update()

def result_5_3(ans):
    global click
    click = 0
    while True:
        result_5_2_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        #if (ans==1):
            ##story
            
        #elif(ans==2):
            ##story

        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #pygame.quit()
                #sys.exit()
            #if event.type == pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
                #if NEXT_BUTTON or event.key==pygame.K_RETURN:

        pygame.display.update()

main_menu()

pygame.quit()
sys.exit()