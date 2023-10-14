from tkinter import *
import random
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Navyas Game-Rock,Paper,Scissor')
root.config(bg ='lightpink')
Label(root, text = 'Rock, Paper ,Scissor' , font='arial 25 bold', bg = 'lightpink').pack()
user_take = StringVar()
Label(root, text = 'Lets start :Rock, Paper ,Scissor' , font='arial 18 bold', bg = 'white').place(x = 20,y=70)
Entry(root, font = 'arial 15 bold', textvariable = user_take , bg = 'antiquewhite2').place(x=90 , y = 130)
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissor'
    Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie,you both selected same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose,computer selected paper')
    elif user_pick == 'rock' and comp_pick == 'scissor':
        Result.set('you win,computer selected scissors')
    elif user_pick == 'paper' and comp_pick == 'scissor':
        Result.set('you loose,computer selected scissor')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,computer selected rock')
    elif user_pick == 'scissor' and comp_pick == 'rock':
        Result.set('you loose,computer selected rock')
    elif user_pick == 'scissor' and comp_pick == 'paper':
        Result.set('you win ,computer selected paper')
    else:
        Result.set('invalid: select anyone from -- rock, paper, scissor')
def Reset():
    Result.set("") 
    user_take.set("")
def Exit():
    root.destroy()
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2',width = 50,).place(x=30, y = 250)

Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=190)

Button(root, font = 'arial 13 bold', text = 'PLAYAGAIN'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=70,y=310)

Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=310)
root.mainloop()