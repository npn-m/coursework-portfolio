import streamlit as st
import pandas as pd
import os

#info = pd.read_excel("C:\Users\ASUS\Desktop\python pj\info.xlsx", sheet_name=['bodyshape', 'Fashion'])
#bobyshape = info['bodyshape']
#fashion = info['Fashion']

class get_info:
    def __init__(self,feature_ans,undertone_ans):
        self.feature_ans=feature_ans
        self.undertone_ans=undertone_ans
        #self.hair_color=hair_color
        #self.eye_color=eye_color
        #self.SAS=SAS
        #self.bv=bv
    
    def get_body(self,body):
        self.body=body
    
    def get_gender(self,gender):
        self.gender=gender

class personal(get_info):
    def __init__(self,feature_ans,undertone_ans):
        get_info.__init__(feature_ans,undertone_ans)
        self.pers=''
        self.un_tone=''
        self.feature=''

    def Feature(self):
        if ("Blonde/Light Color" in get_info.feature_ans)&("Blue/Light Brown" in get_info.feature_ans):
            self.feature=='Light'
        else :
            self.feature=='Dark'
        return self.feature
        
    def Undertone(self):
        if ("Red Undertone" in get_info.undertone_ans)&("Purple/Blue" in get_info.undertone_ans):
            self.un_tone=='Cool Tone'
        elif ("Golden Undertone" in get_info.undertone_ans)&("Green/Olive Green" in get_info.undertone_ans):
            self.un_tone=='Warm Tone'
        else :
            self.un_tone=='Neutral Tone'
        return self.un_tone
    
    def pers_t(self):
        if (self.un_tone=='Cool Tone'):
            if(self.feature=='Light'):
                self.pers=='Summer'
            else:
                self.pers=='Winter'
        elif (self.un_tone=='Warm Tone'):
            if(self.feature=='Light'):
                self.pers=='Spring'
            else:
                self.pers=='Autumn'
        return self.pers
            
class cloth(personal,get_info):
    def __init__(self,gender,style,un_tone,body):
        get_info.get_body(body)
        get_info.get_gender(gender)
        personal.__init__(un_tone)
        #self.style=[fashion.loc[:, ['style']]]
        self.jewery=''

    def Jewery(self):
        if personal.un_tone=='Cool Tone':
            self.jewery==['Silver','Platinum','White Gold']
        elif personal.un_tone=='Warm Tone':
            self.jewery==['Gold','Yelllow Gold','Rose Gold']
        else :
            self.jewery==['Gold','Rose Gold','Rose Gold','Silver','Platinum']
        return self.jewery
    
class feminine(cloth):
    def __init__(self,style,jewery,body):
        cloth.__init__(style,jewery,body)
        

class masculine(cloth):
    def __init__(self,style,jewery,body):
        cloth.__init__(style,jewery,body)

class spring(personal):
    def __init__(self,pers,un_tone,feature):
        personal.__init__(pers,un_tone,feature)
        self.desc='น่ารัก ร่าเริง สดใส'
        self.best_color=['สีโทนส้ม', 'เหลือง', 'เขียว', 'พีชพาสเทล', 'พีชอมชมพู']
        self.dyeing_color=['สีน้ำตาลสว่าง ๆ อมเหลือง หรืออมส้ม']
        self.avoid_color=['สีโทนตุ่น', 'สีโทนเข้มจัด ๆ']

class summer(personal):
    def __init__(self,pers,un_tone,feature):
        personal.__init__(pers,un_tone,feature)
        self.desc='น่ารักหวาน ๆ ซอฟต์ ๆ น่าทะนุถนอม'
        self.best_color=['สีโทนเย็นพาสเทลอย่างสีชมพู', 'สีฟ้า', 'สีม่วงลาเวนเดอร์', 'สีในโทนเทาอ่อน']
        self.dyeing_color=['สีผมโทนหม่น ๆ เทาหม่น', 'เขียวหม่น', 'น้ำตาลช็อกโกแล็ต']
        self.avoid_color=['สีโทนส้ม', 'น้ำตาลโทนอุ่น', 'ส้มอิฐ', 'สีโทนจัด ๆ']

class autumn(personal):
    def __init__(self,pers,un_tone,feature):
        personal.__init__(pers,un_tone,feature)
        self.desc='ขรึม สุขุม เป็นผู้ใหญ่'
        self.best_color=['สีโทนธรรมชาติ', 'สีเหลืองมัสตาร์ด', 'สีส้มอิฐ', 'สีบรอนซ์', 'สีกากี', 'เอิร์ธโทน']
        self.dyeing_color=['สีโทนแอช','น้ำตาลเข้ม']
        self.avoid_color=['สีที่สดใส', 'สีฉูดฉาด']

class winter(personal):
    def __init__(self,pers,un_tone,feature):
        personal.__init__(pers,un_tone,feature)
        self.desc='เท่ ๆ คูล ๆ มั่นใจในตัวเอง'
        self.best_color=['สีโทนม่วงอมแดง', 'สีแดง', 'สีน้ำเงินอมม่วง', 'สีแดงเบอร์กันดี', 'สีเขียวเข้ม', 'สีขาว', 'สีดำ']
        self.dyeing_color=['สีดำสนิท', 'ดำประกายน้ำเงิน']
        self.avoid_color=['สีโทนตุ่น', 'สีโทนหม่น ๆ']

#def gender(gender):
    #if (gender=='Female'):
        #feminine()
    #else:
        #masculine()

#ans=''    
#if ans=='yes':
    #getbody
#else :
    #personal_test