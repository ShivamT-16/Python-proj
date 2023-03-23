# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:28:54 2020

@author: Shivam Trivedi
"""


from tkinter import *
import random
import os
import tkinter.font as font
from PIL import Image, ImageTk
import time

namewin = Tk()
u_name=StringVar()
Entry(namewin,textvariable=u_name).grid(row = 0, column = 1)
na = Label(namewin, text='Enter Name: ', font = "Stencil")

name = "Unknown user"

def ent_name():
    from tkinter import messagebox
    global name
    name = u_name.get()
    messagebox.showinfo("Success", "Name Entered")

na.grid(row = 0, column = 0)

endn = Button(namewin, text = "Enter" , command = ent_name)
endn.grid(row = 1, column = 0)
cl_nam = Button(namewin, text = "Close" , command = namewin.destroy)
cl_nam.grid(row = 1, column = 1)

# The intro slide:-
introwin = Tk()
introwin.title("Home")



instr1="Welcome to 'Gamer's Getaway'! \n\n Rules of the game:- \n\n >>>\
There are three levels to the game \n\n >>> Level 1 : Guess the number \
(10 points) \n\n >>>  Level 2 : Rock,Paper,Scissors (20 points) \n\n >>> \
Level 3 : Cryptocity  (30 points) "
 
instr2 = " >>> You will get to attempt each game multiple times \n >>> More the number \
of tries you use, lesser the points \n >>> If you still dont manage to clear it , you will \
have to leave the game with 0 points . \n >>> oh and yes if you dont feel like trying out\
 a game , you can anytime decide to leave it, but as a consequence , you will record a null\
 score in that game"

instr3 = " >>> At the end of the game, a leaderboard will be shown , so that you \
know how you fared compared to your peers. \n \n Best of Luck trying to get to the top\
 !!! \n \n >>> Press continue to let the fun begin!!! "

rule1=Text(introwin, bg = 'orange')
rule2=Text(introwin, bg = 'orange')
rule3=Text(introwin, bg = 'orange') 
rule1.grid(row = 1, column = 1)
rule2.grid(row = 1, column = 2)
rule3.grid(row = 2, column = 1)
rule1.insert(END, instr1)
rule2.insert(END, instr2)
rule3.insert(END, instr3)
but1 = Button (introwin,text = "Continue",activebackground='green',bg = "yellow"\
               ,height=10,width = 20, font = 70,command=introwin.destroy)
but1.grid(row = 2, column = 2)

mainloop()


t1= time.time()


win = Tk()
win.configure(bg="blue")
win.geometry("700x700")
win.title("Number Guessing Game")

result = StringVar()
chances = IntVar()
chances1= IntVar()
choice= IntVar()
no=random.randint(1,20)
result.set("Guess a number between 1 to 20 ")
chances.set(4)
chances1.set(chances.get())
score1 = 0
score2 = 0
score3 = 0

def fun():
  global score1,no
  chances1.set(chances.get())
  if chances.get()>1:

    if choice.get() > 20 or choice.get()<0:
      result.set("You just lost 1 Chance")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
    
    elif no==choice.get():
      result.set("Congratulations YOU WON!!!")
            
      if chances.get() == 4 :
          score1 = 10
      elif chances.get() == 3:
          score1 = 6
      elif chances.get() == 2:
          score1 = 4
      
      chances.set(chances.get()-1)
      chances1.set(chances.get())
      
    elif no > choice.get():
      result.set("Your guess was too low: Guess a number higher ")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
      
    elif no < choice.get():
      result.set("Your guess was too High: Guess a number Lower ")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
  elif chances.get()==1:
      chances.set(chances.get()-1)
      chances1.set(chances.get())
      if no==choice.get():
          result.set("Congratulations YOU WON!!!")
      else:
          result.set("Game Over You Lost! "+str(no)+" is the correct answer")
          score1=2
          return

def restart():
  global no
  no=random.randint(1,20)
  result.set("Guess a number between 1 to 20 ")
  chances.set(4)
  chances1.set(chances.get())
  choice.set(0)

ent1 = Entry(win, textvariable=choice, width=3,font=('Stencil', 50))
ent1.place(relx=0.5, rely=0.3, anchor=CENTER)

ent2 = Entry(win, textvariable=result, width=50, font=('Stencil', 15), relief=GROOVE)
ent2.place(relx=0.5, rely=0.7, anchor=CENTER)

ent3 = Entry(win, text=chances1, width=2, font=('Stencil', 24), relief=GROOVE)
ent3.place(relx=0.61, rely=0.85, anchor=CENTER)

msg = Label(win, text='Guess a number between 1 to 20 ', font=("Copperplate Gothic Bold", 25), relief=GROOVE)
msg.place(relx=0.5, rely=0.09, anchor=CENTER)

msg2 = Label(win, text='Remaining Chances', font=("Copperplate Gothic Bold", 25), relief=GROOVE)
msg2.place(relx=0.3, rely=0.85, anchor=CENTER)

try_no = Button(win, width=8, text='TRY', font=('Copperplate Gothic Bold', 25), command=fun, relief=GROOVE)
try_no.place(relx=0.5, rely=0.5, anchor=CENTER)

stop = Button(win, text='Stop', width=40, command=win.destroy, bg="red", activebackground="red", relief=GROOVE)
stop.place(relx=0.25, rely=1, anchor=S)

reset = Button(win, text='Restart', width=40, command=restart, bg="red", activebackground="red", relief=GROOVE)
reset.place(relx=0.75, rely=1, anchor=S)

win.mainloop()

#LEVEL 1: END!!!!!!!

#LEVEL 2: START!!!!!!!
#ROCK PAPER SCISSOR GAME STARTS FROM HERE

player_score = 0
computer_score = 0
options = [('rock',0), ('paper',1), ('scissors',2)]
game_window = Tk()
game_window.title("Rock Paper Scissors Game")

def player_choice(player_input):
    global player_score, computer_score,score2

    computer_input = get_computer_choice()

    player_choice_label.config(text = 'Your Selected : ' + player_input[0])
    computer_choice_label.config(text = 'Computer Selected : ' + computer_input[0])

    if(player_input == computer_input):
        winner_label.config(text = "Tie")
    elif((player_input[1] - computer_input[1]) % 3 == 1):
        player_score += 1
        winner_label.config(text="You Won!!!")
        player_score_label.config(text = 'Your Score : ' + str(player_score))
    else:
        computer_score += 1
        winner_label.config(text="Computer Won!!!")
        computer_score_label.config(text='Computer Score : ' + str(computer_score))
    if player_score==10:
       winner_label.config(text="You Won the game!!!")
       score2 = 20
    elif computer_score==10:
        winner_label.config(text="Computer Won the game!!!")
#Function to Randomly Select Computer Choice
def get_computer_choice():
    return random.choice(options)



app_font = font.Font(size = 12)

#Displaying Game Title
game_title = Label(text = 'LEVEL 2: Rock Paper Scissors', font = font.Font(size = 20), fg = 'grey')
game_title.pack()

#Second Header
#Displaying Game Title
points_title = Label(text = 'Whosoever scores 10 points first WINS!!!', font = font.Font(size = 20), fg = 'orange')
points_title.pack()

#Label to dispay, who wins each time
winner_label = Label(text = "Let's Start the Game...", fg = 'green', font = font.Font(size = 13))
winner_label.pack()

input_frame = Frame(game_window)
input_frame.pack()

#Displaying player options
player_options = Label(input_frame, text = "Your Options : ", font = app_font, fg = 'grey')
player_options.grid(row = 0, column = 0)

rock_btn = Button(input_frame, text = 'Rock', width = 15, bd = 0, bg = 'pink', pady = 5, command = lambda: player_choice(options[0]))
rock_btn.grid(row = 1, column = 1)

paper_btn = Button(input_frame, text = 'Paper', width = 15, bd = 0, bg = 'silver', pady = 5, command = lambda: player_choice(options[1]))
paper_btn.grid(row = 1, column = 2)

scissors_btn = Button(input_frame, text = 'Scissors', width = 15, bd = 0, bg = 'light blue', pady = 5, command = lambda: player_choice(options[2]))
scissors_btn.grid(row = 1, column = 3)

#Displaying Score and players choice
score_label = Label(input_frame, text = 'Score : ', font = app_font, fg = 'grey')
score_label.grid(row = 2, column = 0)

player_choice_label = Label(input_frame, text = 'Your Selected : ---', font = app_font)
player_choice_label.grid(row = 3, column = 1, pady = 5)

player_score_label = Label(input_frame, text = 'Your Score : -', font = app_font)
player_score_label.grid(row = 3, column = 2, pady = 5)

computer_choice_label = Label(input_frame, text = 'Computer Selected : ---', font = app_font, fg = 'black')
computer_choice_label.grid(row = 4, column = 1, pady = 5)

computer_score_label = Label(input_frame, text = 'Computer Score : -', font = app_font, fg = 'black')
computer_score_label.grid(row = 4, column = 2, padx = (10,0), pady = 5)
    

game_window.geometry('700x300')
game_window.mainloop()

#LEVEL 2: END !!!!!!!! 

#LEVEL 3 STARTS
#GUESS THE CITY

from tkinter import *
root=Tk()

#Instructions
root.title("Level 3 : Guess the city")
root.configure(bg="blue")
Label(root,text="INSTRUCTIONS",font=('Arial Bold',16),fg='Red',bg='Yellow').grid(row=0)
Label(root,text="",bg='blue').grid(row=1)

#Instructions
l1=Label(root,text="You will be given the name of a city in an encrypted form with all the letters shuffled (for a city with 2 or more words the individual words are shuffled).",font=('Arial',11),fg='white',bg='Blue')
l1.grid(row=2,column=0)
Label(root,text="You will be provided the rotation by which the original word has been shifted. ",font=('Arial',11),fg='white',bg='Blue').grid(row=3,column=0)
Label(root,text="",bg='blue').grid(row=4)
Label(root,text="For example,if the city name is Delhi and the rotation 4,each letter will become the letter that comes 4 letters after in alphabetic order.",font=('Arial',11),fg='white',bg='Blue').grid(row=5,column=0)
Label(root,text="So, the new word would be Hiplm.",font=('Arial',11),fg='white',bg='Blue').grid(row=6,column=0)
Label(root,text="",bg='blue').grid(row=7)
Label(root,text="But then the letters will be shuffled to get a new combination of letters; for example Delhi may become Hpmil or Hlmpi.",font=('Arial',11),fg='white',bg='Blue').grid(row=8,column=0)
Label(root,text="You will get 6 attempts to guess the correct answer. If you guess correctly, you clear the round",font=('Arial',11),fg='white',bg='Blue').grid(row=9)
Label(root,text="If not, you get the number of tries left.",font=('Arial',11),fg='white',bg='Blue').grid(row=10)
Label(root,text="",bg='blue').grid(row=11)
Label(root,text="After the 3rd attempt, you get a hint:- the name of the continent in which the city lies",font=('Arial',11),fg='white',bg='Blue').grid(row=12)
Label(root,text="After another attempt,you get another hint:- you get to know the starting and ending letters of the city.",font=('Arial',11),fg='white',bg='Blue').grid(row=13)
Label(root,text="",bg='blue').grid(row=14)
Label(root,text="",bg='blue').grid(row=15)
b1=Button(root,text="Next",fg='Red',bg='Yellow',command=root.destroy)
b1.grid(row=16) 
root.mainloop()

a={1:"New Delhi",2:"Mumbai",3:"Kolkata",4:"Bengaluru",5:"Chennai",6:"Jaipur",7:"Barcelona",8:"Madrid",9:"Lisbon",10:"Frankfurt",11:"Berlin",12:"Munich",13:"Hamilton",14:"Auckland",15:"Wellington",16:"Hamburg",17:"Christchurch",18:"Hobart",19:"Adelaide",20:"Sydney",21:"Melbourne",22:"Singapore",23:"Jakarta",24:"Kuala Lampur",25:"Dubai",26:"Sharjah",27:"Rome",28:"Paris",29:"Abu Dhabi",30:"London",31:"Edinburgh",32:"Manchester",81:"Dublin",83:"Belfast",33:"Bucharest",34:"Budapest",35:"Shanghai",36:"Beijing",37:"Tokyo",38:"Cape Town",39:"Johannesburg",40:"Rio de Janeiro",41:"Brazilia",42:"Los Angeles",43:"San Francisco",44:"New York",45:"Dhaka",46:"Colombo",82:"New Jersey",47:"Albany",48:"Austin",49:"Phoenix",50:"Zurich",51:"Amsterdam",52:"Stuttgart",53:"Leipzig",54:"Chicago",55:"Winnipeg",56:"Toronto",57:"Vancouver",58:"Anchorage",59:"Honolulu",60:"Venice",61:"Vienna",62:"Prague",63:"Athens",64:"Cherapungee",65:"Stockholm",66:"Athens",67:"Warsaw",68:"Sacramento",69:"Seattle",70:"Moscow",71:"Saint Petersburg",72:"Marseilles",73:"Nairobi",74:"Cairo",75:"Port Blair",76:"Monaco",77:"Milan",78:"Ahmedabad",79:"Hyderabad",80:"Noida"}
import random
b=random.randint(1,len(a))
r=random.randint(1,25)
s=a[b]  #Actual city name
x=[]
y=[]
t=""
for i in range(65,91): 
        x.append(chr(i))
for j in range(97,123):
        y.append(chr(j))
q=[]
    #code for rotating each letter in the city name
for k in s:
        if k==" ":
            t=t+" "
            continue
        elif str(k).isupper():
            if (int(ord(k))+r<=90):
                t=t+str(chr(ord(k)+r))
            else:
                t=t+str(chr(ord(k)+r-90+65-1))
        elif str(k).islower():
            if (int(ord(k))+r<=122):
                t=t+str(chr(ord(k)+r))
            else:
                t=t+str(chr(ord(k)+r-122+97-1))
z=t     #city name with rotation
v=len(s)
    #shuffling the letters
if " " not in s:
        t=""
        while len(t)!=v:
            p=random.randint(0,len(s)-1)
            if p not in q:
                q.append(p)
                t=t+str(z[p])
            else:
                continue
else:
        sn=z.split()
        t=""
        for v1 in sn:
            v2=""
            while len(v2)!=len(v1):
                p=random.randint(0,len(v1)-1)
                if p not in q:
                    q.append(p)
                    v2=v2+str(v1[p])
            t=t+v2+" "
        t=t[0:len(t)-1]

rt=Tk()
rt.title("Please Continue ")
rt.configure(bg="red")
c=0   
Label(rt,text="The city name to be decrypted and unjumbled is :"+t.lower(),fg='blue',bg='red',font=('Times New Roman',14)).grid(row=0)
Label(rt,text="The rotation of letter is: "+str(r),bg='red',font=('Times New Roman',14),fg='blue').grid(row=1)
Label(rt,text="Guess the city!",bg='red',font=('Times New Roman',14),fg='blue').grid(row=2)
Label(rt,text="",bg='red').grid(row=3)
tv=StringVar()
def clear():
    tv.set("")
Label(rt,text="Enter your guess",bg='red',font=('Times New Roman',14),fg='blue').grid(row=4,column=0)
e1=Entry(rt,textvariable=tv)
e1.grid(row=4,column=1)
Label(rt,text="",bg='red').grid(row=5)
def fn():
    global c,a,s,b,score3
    from tkinter import messagebox
    g=tv.get()
    g=g.title()
    c=c+1
    if c not in (0,1,2,3,4,5,6):
        clear()
        messagebox.showinfo("GAME OVER","Sorry! You have exhausted all your tries.")
        return
    if g!=s:
        messagebox.showinfo("","Sorry! This is the wrong answer,You have "+str(6-c)+" tries left.")
        if len(g)!=len(t):
            messagebox.showinfo("Tip","Enter city name with same no of letters!")
        if c==6:
            clear()
            messagebox.showinfo("GAME OVER","Sorry! You have exhausted all your tries. \
                                The correct answer is "+s)
        if c==3:
            rt2=Tk()
            rt2.configure(bg="yellow")
            rt2.title("Hint 1")
            l1=Label(rt2,text="You will get a hint.",bg="yellow",font=('Arial',13))
            l1.grid(row=0,column=0)
            if b in [1,2,3,4,5,6,23,24,25,26,29,35,36,37,45,46,64,75,78,79,80]:
                Label(rt2,text=t.lower()+" lies in Asia",bg="yellow",font=('Arial',13)).grid(row=1,column=0)
            elif b in [13,14,15,17,18,19,20,21]:
                Label(rt2,text=t.lower()+" lies in Oceania",bg="yellow",font=('Arial',13)).grid(row=1,column=0)
            elif b in [38,39,73,74]:
                Label(rt2,text=t.lower()+" lies in Africa",bg="yellow",font=('Arial',13)).grid(row=1,column=0)
            elif b in [40,41,42,43,44,46,47,48,49,54,55,56,57,58,59,68,69,82]:
                Label(rt2,text=t.lower()+" lies in the Americas",font=('Arial',13),bg="yellow").grid(row=1,column=0)
            else:
                Label(rt2,text=t.lower()+" lies in Europe",bg="yellow",font=('Arial',13)).grid(row=1,column=0)
            Label(rt2,text='',bg="yellow").grid(row=2,column=0)
            Button(rt2,text="Okay",command=rt2.destroy,font=('Arial',11)).grid(row=3,column=0)
            rt2.mainloop()
        if c==4:
            rt2=Tk()
            rt2.configure(bg="yellow")
            rt2.title("Hint 2")
            Label(rt2,text="The correct order of these letters is: "+z,bg="yellow",font=('Arial',13)).grid(row=2,column=0)
            Label(rt2,text="You will get another hint: "+z+" starts with "+s[0]+" and ends with "+s[len(s)-1],bg="yellow",font=('Arial',13)).grid(row=3,column=0)
            Label(rt2,text='',bg="yellow").grid(row=4,column=0)
            Button(rt2,text="Okay",command=rt2.destroy,font=('Arial',11)).grid(row=5,column=0)
            rt2.mainloop()
        

    if g==s:
        messagebox.showinfo("Congrats","Your Answer is correct!You may proceed further.")
        clear()
        if c == 1:
            score3 = 30
        elif c ==2:
            score3 = 28
        elif c ==3:
            score3 = 26
        elif c ==4:
            score3 = 24
        elif c ==5:
            score3 = 22
        elif c ==6:
            score3 = 20

Label(rt,text="",bg='red').grid(row=6)    
Button(rt,text="Exit",command=rt.destroy,bg='yellow').grid(row=7,column=2)
Button(rt,text="Clear",command=clear,bg='yellow').grid(row=7,column=1)
Button(rt,text="Enter",command=fn,bg='yellow').grid(row=7,column=0)
rt.mainloop()

t2= time.time()

import pymysql
conn=pymysql.connect(host="localhost", database= "game_records" ,\
                     password = "root", user="root")
cur=conn.cursor()
"""
for i in cur :
    if i == ("leaderboard",):
        break
    else:
        cur.execute("Create table leaderboard (Name varchar(25), Score int(3),\
                    time_taken varchar(10))")"""
        
score = score1 + score2 +score3
time = int(t2 - t1)
l_val= (name,score,str(time))
cur.execute("insert into leaderboard values (%s,%s,%s)",l_val)

cur.execute(" Select * from leaderboard ORDER BY Score DESC,time_taken ASC")

rank=[]
for x in cur:
    rank.append(x)
    
    
l_board=Tk()
l_board.title("Leader Board")
Label(l_board, text="Name", font = "Stencil").grid(row = 0, column = 0)
Label(l_board, text="Score", font = "Stencil").grid(row = 0, column = 1)
Label(l_board, text="Time", font = "Stencil").grid(row = 0, column = 2)
for y in range (3):
    for z in range (1,len(rank)+1):
        e = Entry(l_board)
        e.grid(column = y , row = z)
        e.insert(END, rank[z-1][y])

conn.commit()        
l_close= Button(l_board, text = "Close Leaderboard", command= l_board.destroy)
l_close.grid(row = z+1, column = 1)

l_board.mainloop()