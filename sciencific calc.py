import tkinter as tk
import math

SC = tk.Tk()
SC.title("SCİENCİFİC CALCULATOR")
SC.minsize(400,600)
SC.maxsize(400,600)

def ONE():
     CALCULATOR_AREA["text"] += "1"
    
def TWO():
    CALCULATOR_AREA["text"] += "2"

def THREE():
    CALCULATOR_AREA["text"] += "3"

def FOUR():
    CALCULATOR_AREA["text"] += "4"

def FİVE():
    CALCULATOR_AREA["text"] += "5"

def SİX():
    CALCULATOR_AREA["text"] += "6"

def SEVEN():
    CALCULATOR_AREA["text"] += "7"

def EİGHT():
    CALCULATOR_AREA["text"] += "8"

def NİNE():
    CALCULATOR_AREA["text"] += "9"

def ZERO():
    CALCULATOR_AREA["text"] += "0"

def MİNUS():
    CALCULATOR_AREA["text"] += "-"

def PLUS():
    CALCULATOR_AREA["text"] += "+"

def MULTİPLY():
    CALCULATOR_AREA["text"] += "*"

def DİVİDE():
    CALCULATOR_AREA["text"] += "/"

def CLEAR():
    CALCULATOR_AREA["text"] = ""

def EQUALS():
    data = CALCULATOR_AREA["text"]
    resoult = str(eval(data))
    CALCULATOR_AREA["text"] = str(resoult)

def P1():
    CALCULATOR_AREA["text"] += "("

def P2():
    CALCULATOR_AREA["text"] += ")"

def Pİ():
    CALCULATOR_AREA["text"] += "3.142857142857143"

def FACTORİAL():
    data = CALCULATOR_AREA["text"]
    data2 = int(data)
    resoult = math.factorial(data2)
    CALCULATOR_AREA["text"] = str(resoult)

def SQUARE():
     CALCULATOR_AREA["text"] += "**"

def SİN():
     data = CALCULATOR_AREA["text"]
     data2 = int(data)
     resoult = math.sin(data2)
     CALCULATOR_AREA["text"] = str(resoult)

def COS():
     data = CALCULATOR_AREA["text"]
     data2 = int(data)
     resoult = math.cos(data2)
     CALCULATOR_AREA["text"] = str(resoult)

def TAN():
     data = CALCULATOR_AREA["text"]
     data2 = int(data)
     resoult = math.tan(data2)
     CALCULATOR_AREA["text"] = str(resoult)

def COT():
     data = CALCULATOR_AREA["text"]
     data2 = int(data)
     val1 = math.cos(data2)
     val2 = math.sin(data2)
     resoult = (val1/val2)
     CALCULATOR_AREA["text"] = str(resoult)

def NL():
     data = CALCULATOR_AREA["text"]
     data2 = int(data)
     resoult = math.log(data2)
     CALCULATOR_AREA["text"] = str(resoult)

def MS():
     SC.minsize(500,600)
     SC.maxsize(500,600)
     CALCULATOR_AREA.place(width = 500,height = 100,x = 0,y = 0)
     LS_BUTTON.place(width = 20,height = 20,x = 480,y = 0)
     MS_BUTTON.place(width = 20,height = 20,x = 380,y = 1000)
     MİNUS_BUTTON.place(width = 100,height = 75,x = 400,y = 200)
     PLUS_BUTTON.place(width = 100,height = 75,x = 400,y = 275)
     MULTİPLY_BUTTON.place(width = 100,height = 75,x = 400,y = 350)
     DİVİDE_BUTTON.place(width = 100,height = 75,x = 400,y = 425)
     CLEAR_BUTTON.place(width = 100,height = 100,x = 400,y = 100)
     EQUALS_BUTTON.place(width = 200,height = 100,x = 300,y = 500)
     SİN_BUTTON.place(width = 100,height = 100,x = 300,y = 100)
     COS_BUTTON.place(width = 100,height = 100,x = 300,y = 200)
     TAN_BUTTON.place(width = 100,height = 100,x = 300,y = 300)
     COT_BUTTON.place(width = 100,height = 100,x = 300,y = 400)
     NL_BUTTON.place(width = 100,height = 100,x = 200,y = 500)
     
def LS():
     SC.minsize(400,600)
     SC.maxsize(400,600)
     CALCULATOR_AREA.place(width = 400,height = 100,x = 0,y = 0)
     LS_BUTTON.place(width = 20,height = 20,x = 380,y = 1000)
     MS_BUTTON.place(width = 20,height = 20,x = 380,y = 0)
     MİNUS_BUTTON.place(width = 100,height = 75,x = 300,y = 200)
     PLUS_BUTTON.place(width = 100,height = 75,x = 300,y = 275)
     MULTİPLY_BUTTON.place(width = 100,height = 75,x = 300,y = 350)
     DİVİDE_BUTTON.place(width = 100,height = 75,x = 300,y = 425)
     CLEAR_BUTTON.place(width = 100,height = 100,x = 300,y = 100)
     EQUALS_BUTTON.place(width = 200,height = 100,x = 200,y = 500)
     SİN_BUTTON.place(width = 100,height = 100,x = 1000,y = 1000)
     COS_BUTTON.place(width = 100,height = 100,x = 1000,y = 1000)
     TAN_BUTTON.place(width = 100,height = 100,x = 1000,y = 1000)
     COT_BUTTON.place(width = 100,height = 100,x = 1000,y = 1000)
     NL_BUTTON.place(width = 20,height = 20,x = 1000,y = 1000)


CALCULATOR_AREA = tk.Label(SC,fg = "black",bg = "white",font = "Arial 20")
CALCULATOR_AREA.place(width = 400,height = 100,x = 0,y = 0)

MİNUS_BUTTON = tk.Button(SC,text = "-",fg = "black",bg = "lime",font = "Arial 70",command = MİNUS)
MİNUS_BUTTON.place(width = 100,height = 75,x = 300,y = 200)

PLUS_BUTTON = tk.Button(SC,text = "+",fg = "black",bg = "lime",font = "Arial 50",command = PLUS)
PLUS_BUTTON.place(width = 100,height = 75,x = 300,y = 275)

MULTİPLY_BUTTON = tk.Button(SC,text = "X",fg = "black",bg = "lime",font = "Arial 40",command = MULTİPLY)
MULTİPLY_BUTTON.place(width = 100,height = 75,x = 300,y = 350)

DİVİDE_BUTTON = tk.Button(SC,text = "÷",fg = "black",bg = "lime",font = "Arial 50",command = DİVİDE)
DİVİDE_BUTTON.place(width = 100,height = 75,x = 300,y = 425)

CLEAR_BUTTON = tk.Button(SC,text = "C",fg = "red",bg = "orange",font = "Arial 40",command = CLEAR)
CLEAR_BUTTON.place(width = 100,height = 100,x = 300,y = 100)

EQUALS_BUTTON = tk.Button(SC,text = "=",fg = "red",bg = "orange",font = "Arial 50",command = EQUALS)
EQUALS_BUTTON.place(width = 200,height = 100,x = 200,y = 500)

P1_BUTTON = tk.Button(SC,text = "(",fg = "lime",bg = "black",font = "Arial 50",command = P1)
P1_BUTTON.place(width = 50,height = 100,x = 0,y = 100)

P2_BUTTON = tk.Button(SC,text = ")",fg = "lime",bg = "black",font = "Arial 50",command = P2)
P2_BUTTON.place(width = 50,height = 100,x = 50,y = 100)

FACTORİAL_BUTTON = tk.Button(SC,text = "n!",fg = "lime",bg = "black",font = "Arial 50",command = FACTORİAL)
FACTORİAL_BUTTON.place(width = 100,height = 100,x = 200,y = 100)

SQUARE_BUTTON = tk.Button(SC,text = "xⁿ",fg = "lime",bg = "black",font = "Arial 50",command = SQUARE)
SQUARE_BUTTON.place(width = 100,height = 100,x = 100,y = 100)

NL_BUTTON = tk.Button(SC,text = "Ln",fg = "lime",bg = "black",font = "Arial 50",command = NL)
NL_BUTTON.place(width = 100,height = 100,x = 1000,y = 1000)

MS_BUTTON = tk.Button(SC,text = "+",fg = "black",bg = "white",font = "Arial 10",command = MS)
MS_BUTTON.place(width = 20,height = 20,x = 380,y = 0)

LS_BUTTON = tk.Button(SC,text = "-",fg = "black",bg = "white",font = "Arial 10",command = LS)
LS_BUTTON.place(width = 20,height = 20,x = 380,y = 1000)

SİN_BUTTON = tk.Button(SC,text = "Sin°",fg = "lime",bg = "black",font = "Arial 37",command = SİN)
SİN_BUTTON.place(width = 100,height = 100,x = 1000,y = 1000)

COS_BUTTON = tk.Button(SC,text = "Cos°",fg = "lime",bg = "black",font = "Arial 34",command = COS)
COS_BUTTON.place(width = 100,height = 100,x = 1000,y = 1000)

TAN_BUTTON = tk.Button(SC,text = "Tan°",fg = "lime",bg = "black",font = "Arial 35",command = TAN)
TAN_BUTTON.place(width = 100,height = 100,x = 1000,y = 1000)

COT_BUTTON = tk.Button(SC,text = "Cot°",fg = "lime",bg = "black",font = "Arial 37",command = COT)
COT_BUTTON.place(width = 100,height = 100,x = 1000,y = 1000)

BUTTON_Pİ = tk.Button(SC,text = "π",fg = "lime",bg = "black",font = "Arial 60",command = Pİ)
BUTTON_Pİ.place(width = 100,height = 100,x = 100,y = 500)

BUTTON_1 = tk.Button(SC,text = "1",fg = "lime",bg = "black",font = "Arial 30",command = ONE)
BUTTON_1.place(width = 100,height = 100,x = 0,y = 200)

BUTTON_2 = tk.Button(SC,text = "2",fg = "lime",bg = "black",font = "Arial 30",command = TWO)
BUTTON_2.place(width = 100,height = 100,x = 100,y = 200)

BUTTON_3 = tk.Button(SC,text = "3",fg = "lime",bg = "black",font = "Arial 30",command = THREE)
BUTTON_3.place(width = 100,height = 100,x = 200,y = 200)

BUTTON_4 = tk.Button(SC,text = "4",fg = "lime",bg = "black",font = "Arial 30",command = FOUR)
BUTTON_4.place(width = 100,height = 100,x = 0,y = 300)

BUTTON_5 = tk.Button(SC,text = "5",fg = "lime",bg = "black",font = "Arial 30",command = FİVE)
BUTTON_5.place(width = 100,height = 100,x = 100,y = 300)

BUTTON_6 = tk.Button(SC,text = "6",fg = "lime",bg = "black",font = "Arial 30",command = SİX)
BUTTON_6.place(width = 100,height = 100,x = 200,y = 300)

BUTTON_7 = tk.Button(SC,text = "7",fg = "lime",bg = "black",font = "Arial 30",command = SEVEN)
BUTTON_7.place(width = 100,height = 100,x = 0,y = 400)

BUTTON_8 = tk.Button(SC,text = "8",fg = "lime",bg = "black",font = "Arial 30",command = EİGHT)
BUTTON_8.place(width = 100,height = 100,x = 100,y = 400)

BUTTON_9 = tk.Button(SC,text = "9",fg = "lime",bg = "black",font = "Arial 30",command = NİNE)
BUTTON_9.place(width = 100,height = 100,x = 200,y = 400)

BUTTON_0 = tk.Button(SC,text = "0",fg = "lime",bg = "black",font = "Arial 30",command = ZERO)
BUTTON_0.place(width = 100,height = 100,x = 0,y = 500)

SC.mainloop()
