from datetime import date

today_list = str(date.today()).split("-")

if today_list[1][0]=='0':
    today_list[1]=today_list[1][1]

today_date = today_list[1]+"/"+today_list[2]




class PTT_data():
    
    def __init__(self):
        board = ""
        title = ""
        author = ""
        date = ""
        url=""
        push =""

    def _Get_all(self):

        text = ""   
        text="=---------------------------="+"\n"+("Board name: "+self.board)+"\n"\
            +("Title: "+self.title)+"\n"\
            +("Author: "+self.author)+"\n"\
            +("Date: "+self.date)+"\n"\
            +("Url: "+self.url)+"\n"\
            +("Popularity: ")

        if self.push == "":
                text+=('None')
        elif self.push[0] == 'X':
                text+= ('Bad')
        elif self.push == '爆':
                text+=('Very good')
        else:
                text+=(self.push)

        text+="\n=---------------------------=\n"
        return text
    

    def _Get_push(self,Goods):
            text= ""

            if Goods > 99:
                if self.push == '爆':
                   text = self._Get_all()
        
            elif Goods <= -1:

                if (self.push != "") and (self.push[0] == 'X'):
                    text = self._Get_all()

            else:
                if  ((self.push != "") and (self.push[0] != 'X') ):
                    if ((self.push == '爆') or (int(self.push) >= Goods)) :
                        text=self._Get_all()
            return text

    def Get(self,Goods=0,today=1):
       
        if today==1:
            if self.date == today_date:
                 return self._Get_push(Goods)

        
        else:
            return self._Get_push(Goods)






