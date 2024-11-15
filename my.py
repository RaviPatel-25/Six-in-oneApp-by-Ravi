from tkinter import*
import tkinter
import turtle
from turtle import*
import colorsys
import random
from PIL import ImageTk
from tkinter import messagebox
from time import strftime
import time
import datetime as dt

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login system")
        self.root.geometry("1020x2080+0+0")
        self.root.resizable(False,False)
        self.bg=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Bgimg.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        firstapp=Label(self.root,text=" My First App ",bg="purple",fg="cyan",bd=0,font=("times new roman",15,'bold','underline')).place(x=220,y=450)
        coding=Label(self.root,text=" CODING ",bg="purple",fg="cyan",bd=0,font=("times new roman",7,'bold','underline')).place(x=420,y=690)
        voding=Label(self.root,text=" VODING ",bg="purple",fg="cyan",bd=0,font=("times new roman",7,'bold','underline')).place(x=420,y=1350)
        
        btn1=Button(self.root,command=self.calculator,text="Calculator",bg="black",fg="cyan",bd=0,font=("times new roman",5,'bold','underline')).place(x=10,y=890,height=50,width=160)
        btn2=Button(self.root,command=self.time,text="Time",bg="black",fg="cyan",bd=0,font=("times new roman",5,'bold','underline')).place(x=10,y=960,height=50,width=160)
        btn3=Button(self.root,command=self.photo,text="Photos",bg="black",fg="cyan",bd=0,font=("times new roman",5,'bold','underline')).place(x=10,y=1030,height=50,width=160)
        
        btn1=Button(self.root,command=self.snakegame,text="Snake",bg="black",fg="cyan",bd=0,font=("times new roman",5,'bold','underline')).place(x=850,y=890,height=50,width=160)
        btn2=Button(self.root,command=self.tiktaktoe,text="TikTakToe",bg="black",fg="cyan",bd=0,font=("times new roman",5,'bold','underline')).place(x=850,y=960,height=50,width=160)
        btn3=Button(self.root,command=self.graphics,text="Graphics",bg="black",fg="cyan",bd=0,font=("times new roman",5,'bold','underline')).place(x=850,y=1030,height=50,width=160)
       
        
    def calculator(self):
        frame=Frame(self.root,bg="white").place(x=310,y=840,height=500,width=420)
        
        global equation
        equation=""
        text_label=StringVar()  
       
        label_result=Label(frame,bg="gray",textvariable=text_label,fg="black",font=("arial",8)).place(x=320,y=850,height=100,width=400)
        label_bg=Label(frame,bg="black",text="",font=("arial",8)).place(x=320,y=950,height=380,width=400)
        
        def show(value):
        	global equation
        	equation=equation+value
        	text_label.set(equation)
        	
        def equals():
        	try:
        		global equation
        		total=str(eval(equation))
        		text_label.set(total)
        		equation=total
        	
        	except ZeroDivisionError:
        		text_label.set("Infinite")
        		equation=""
        		
        	except SyntaxError:
        		text_label.set("")
        		equation=""
       
     
        def clear():
        	global equation
        	text_label.set("")
        	equation=""
   
        Button(label_bg,text="C",font=("arial",5,"bold"),bd=5,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=332,y=960,height=64,width=87)
        Button(label_bg,text="/",font=("arial",5,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("/")).place(x=429,y=960,height=64,width=87)
        Button(label_bg,text="%",font=("arial",5,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("%")).place(x=526,y=960,height=64,width=87)
        Button(label_bg,text="*",font=("arial",5,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("*")).place(x=623,y=960,height=64,width=87)
        
        Button(label_bg,text="7",font=("arial",5,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("7")).place(x=332,y=1034,height=64,width=87)
        Button(label_bg,text="8",font=("arial",5,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("8")).place(x=429,y=1034,height=64,width=87)
        Button(label_bg,text="9",font=("arial",5,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("9")).place(x=526,y=1034,height=64,width=87)
        Button(label_bg,text="-",font=("arial",5,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("-")).place(x=623,y=1034,height=64,width=87)
        
        Button(label_bg,text="4",font=("arial",5,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("4")).place(x=332,y=1108,height=64,width=87)
        Button(label_bg,text="5",font=("arial",5,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("5")).place(x=429,y=1108,height=64,width=87)
        Button(label_bg,text="6",font=("arial",5,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("6")).place(x=526,y=1108,height=64,width=87)
        Button(label_bg,text="+",font=("arial",5,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("+")).place(x=623,y=1108,height=64,width=87)
        
        Button(label_bg,text="1",font=("arial",5,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("1")).place(x=332,y=1182,height=64,width=87)
        Button(label_bg,text="2",font=("arial",5,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("2")).place(x=429,y=1182,height=64,width=87)
        Button(label_bg,text="3",font=("arial",5,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("3")).place(x=526,y=1182,height=64,width=87)
        Button(label_bg,text="=",font=("arial",5,"bold"),bd=1,fg="#fff",bg="#fe9037",command=lambda: equals()).place(x=623,y=1182,height=138,width=87)
        
        Button(label_bg,text="0",font=("arial",5,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("0")).place(x=332,y=1256,height=64,width=184)
        Button(label_bg,text=".",font=("arial",5,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show(".")).place(x=526,y=1256,height=64,width=87)
       
    def time(self):
        frame=Frame(self.root,bg="white").place(x=310,y=840,height=500,width=420)
        label_bg=Label(frame,bg="black",text="",font=("arial",8)).place(x=320,y=850,height=480,width=400)
        
        def time(self):
        	canvas = Canvas(master = self.root,width = 400, height = 480)
        	canvas.place(x=320,y=850)
        	t = turtle.RawTurtle(canvas)
        	t1=turtle.RawTurtle(canvas)
        	t.speed(0)
        	t1.speed()
        	t1.ht()
        	t.ht()
        	t1.up()
        	t1.lt(90)
        	t1.fd(170)
        	t1.rt(90)
        	t1.bk(120)
        	t1.color("blue")
        	t1.write("Time now", font=("Arial", 10, "bold","underline"))
        	
        	sec = dt.datetime.now().second
        	min = dt.datetime.now().minute
        	hr = dt.datetime.now().hour
        	
        	t.speed(1)
        	t.up()
        	t.bk(120)
        	t.hideturtle()
        	t.clear()
        	
        	t.write(str(hr).zfill(2)+ ":"+str(min).zfill(2)+":"+ str(sec).zfill(2),font=("Arial Narrow", 10, "bold"))
        	sec += 1
        	if sec == 60:
        		sec = 0
        		min += 1
        	if min == 60:
        		min = 0
        		hr += 1
        	if hr == 13:
        	   hr = 1
        	to=dt.datetime.today()
       
        	t.rt(90)
        	t.fd(100)
        	t.write(str(to.day)+" "+str(to.month)+" "+str(to.year),font=("Arial Narrow", 10, "bold"))
       
        time(self)
    	
          
    def photo(self):
        self.frame=Frame(self.root,bg="white").place(x=310,y=840,height=500,width=420)
        self.pic1=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Newpy/Pic1.jpg")
        self.pic2=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Newpy/Pic2.jpg")
        self.pic3=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Newpy/Pic3.jpg")
        self.pic4=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Newpy/Pic4.jpg")
        self.pic5=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Newpy/Pic5.jpg")
        self.pic6=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Newpy/Pic6.jpg")
        self.pic7=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Newpy/Pic7.jpg")
        self.pic8=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Newpy/Pic8.jpg")
        self.pic9=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Newpy/Pic9.jpg")
        self.pic10=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Newpy/Pic10.jpg")
        
        photos=[self.pic1,self.pic2,self.pic3,self.pic4,self.pic5,self.pic6,self.pic7,self.pic8,self.pic9,self.pic10]
        
        self.label=Label(self.frame,image=photos[0]).place(x=320,y=850)
       
        global num
        num=1
        def shown():
        	global num
        	if num>9:
        		num=0
        	label=Label(self.frame,image=photos[num]).place(x=320,y=850)
        	num+=1
        	self.btnn=Button(self.root,text="Pre",font=("Arial Narrow", 4, "bold"),bg="black",fg="cyan",height=2,width=3,command=shown)
        	self.btnn.place(x=320,y=1270,height=60,width=60)
        	self.btnp=Button(self.root,text="Next",font=("Arial Narrow", 4, "bold"),bg="black",fg="cyan",height=2,width=3,command=showp)
        	self.btnp.place(x=660,y=1270,height=60,width=60)
        	
       
        def showp():
        	global num
        	if num<0:
        		num=9
        	label=Label(self.frame,image=photos[num]).place(x=320,y=850)
        	num-=1
        	self.btnp=Button(self.root,text="Next",font=("Arial Narrow", 4, "bold"),bg="black",fg="cyan",height=2,width=3,command=showp)
        	self.btnp.place(x=660,y=1270,height=60,width=60)
        	self.btnn=Button(self.root,text="Pre",font=("Arial Narrow", 4, "bold"),bg="black",fg="cyan",height=2,width=3,command=shown)
        	self.btnn.place(x=320,y=1270,height=60,width=60)
        	
        self.btnn=Button(self.root,text="Pre",font=("Arial Narrow", 4, "bold"),bg="black",fg="cyan",height=2,width=3,command=shown)
        self.btnn.place(x=320,y=1270,height=60,width=60)
        self.btnp=Button(self.root,text="Next",font=("Arial Narrow", 4, "bold"),bg="black",fg="cyan",height=2,width=3,command=showp)
        self.btnp.place(x=660,y=1270,height=60,width=60)
        	  
    def snakegame(self):
        frame=Frame(self.root,bg="white").place(x=310,y=840,height=500,width=420)

        def play():
        	WIDTH = 420
        	HEIGHT = 380
        	SPEED = 200
        	SPACE_SIZE = 20
        	BODY_SIZE = 2
        	SNAKE = "#00FF00"
        	FOOD = "#FFFFFF"
        	BACKGROUND = "#000000"
        	global direction
        	global score
        	
        	class Snake:
        	    def __init__(self):
        	    	self.body_size = BODY_SIZE
        	    	self.coordinates = []
        	    	self.squares = []
        	    	
        	    	for i in range(0, BODY_SIZE):
        	    		self.coordinates.append([0, 0])
        	    		
        	    	for x, y in self.coordinates:
        	    	     square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE,fill=SNAKE, tag="snake")
        	    	     self.squares.append(square)
        	    	     
        	
        	class Food:
        		def __init__(self):
        		    x = random.randint(0,(WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        		    y = random.randint(0,(HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        		    
        		    self.coordinates = [x, y]
        		    canvas.create_oval(x, y, x + SPACE_SIZE, y +SPACE_SIZE, fill=FOOD,tag="food")
        		    
        	
        	def next_turn(snake, food):
        		
        		x, y = snake.coordinates[0]
        		
        		if direction == "up":
        			y -= SPACE_SIZE
        		elif direction == "down":
        			y += SPACE_SIZE
        		elif direction == "left":
        			x -= SPACE_SIZE
        		elif direction == "right":
        			x += SPACE_SIZE
        			
        		snake.coordinates.insert(0, (x, y))
        		
        		square = canvas.create_rectangle(x, y, x + SPACE_SIZE,y + SPACE_SIZE, fill=SNAKE)
        		
        		snake.squares.insert(0, square)
        		
        		if x == food.coordinates[0] and y == food.coordinates[1]:
        			
        			global score
        			score += 1
        			
        			label.config(text="Points:{}".format(score))
        			
        			canvas.delete("food")
        			
        			food = Food()
        			
        		else:
        			del snake.coordinates[-1]
        			canvas.delete(snake.squares[-1])
        			del snake.squares[-1]
        			
        		if check_collisions(snake):
        			game_over()
        			
        		else:
        			self.root.after(SPEED, next_turn, snake, food)
        			
        	
        	def change_direction(new_direction):
        		
        		global direction
        		
        		if new_direction == 'left':
        		     if direction != 'right':
        		     	direction = new_direction
        		elif new_direction == 'right':
        		     if direction != 'left':
        		     	direction = new_direction
        		elif new_direction == 'up':
        		     if direction != 'down':
        		     	direction = new_direction
        		elif new_direction == 'down':
        		     if direction != 'up':
        		     	direction = new_direction
        		     	
        	
        	def check_collisions(snake):
        		
        		x, y = snake.coordinates[0]
        		
        		if x < 0 or x >= WIDTH:
        			return True
        		elif y < 0 or y >= HEIGHT:
        			return True
        			
        		for body_part in snake.coordinates[1:]:
        		     if x == body_part[0] and y == body_part[1]:
        		     	return True
        		     return False
        		 
        	
        	def game_over():
        		canvas.delete(ALL)
        		canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas', 10),text="GAME OVER", fill="red",tag="gameover")
        	
        	score = 0
        	direction = 'down'
        	
        	
        	
        	label = Label(self.root, bg="white",text="Points:{}".format(score),font=('consolas', 6))
        	label.place(x=320,y=1220)
        	
        	canvas = Canvas(self.root,bg=BACKGROUND,height=HEIGHT, width=WIDTH)
        	canvas.place(x=310,y=840)
        	
        	def left():
        		change_direction('left')
        	def right():
        		change_direction('right')
        	def up():
        		change_direction('up')
        	def down():
        		change_direction('down')
        		
        	btnn=Button(self.root,text="Left",font=("Arial Narrow", 4, "bold"),bg="black",fg="cyan",height=2,width=3,command=left)
        	btnn.place(x=380,y=1280,height=60,width=60)
        	btnn=Button(self.root,text="Right",font=("Arial Narrow", 4, "bold"),bg="black",fg="cyan",height=2,width=3,command=right)
        	btnn.place(x=440,y=1280,height=60,width=60)
        	btnn=Button(self.root,text="Up",font=("Arial Narrow", 4, "bold"),bg="black",fg="cyan",height=2,width=3,command=up)
        	btnn.place(x=560,y=1220,height=60,width=60)
        	btnn=Button(self.root,text="Down",font=("Arial Narrow", 4, "bold"),bg="black",fg="cyan",height=2,width=3,command=down)
        	btnn.place(x=560,y=1280,height=60,width=60)
        	
        	snake = Snake()
        	food = Food()
        	
        	next_turn(snake, food)        		
        	
        play()        			
        
        
        
     
        pass
    def tiktaktoe(self):
        frame=Frame(self.root,bg="white").place(x=310,y=840,height=500,width=420)
        def play():
        	global clicked
        	global count
        	clicked=True
        	count=0
        	global b1,b2,b3,b4,b5,b6,b7,b8,b9
        	#rest function..
        	def reset():
        		global b1,b2,b3,b4,b5,b6,b7,b8,b9
        		global clicked,count
        		b1["text"]=" "
        		b2["text"]=" "
        		b3["text"]=" "
        		b4["text"]=" "
        		b5["text"]=" "
        		b6["text"]=" "
        		b7["text"]=" "
        		b8["text"]=" "
        		b9["text"]=" "
        		b1.config(bg="yellow")
        		b2.config(bg="yellow")
        		b3.config(bg="yellow")
        		b4.config(bg="yellow")
        		b5.config(bg="yellow")
        		b6.config(bg="yellow")
        		b7.config(bg="yellow")
        		b8.config(bg="yellow")
        		b9.config(bg="yellow")
        		b1.config(state=NORMAL)
        		b2.config(state=NORMAL)
        		b3.config(state=NORMAL)
        		b4.config(state=NORMAL)
        		b5.config(state=NORMAL)
        		b6.config(state=NORMAL)
        		b7.config(state=NORMAL)
        		b8.config(state=NORMAL)
        		b9.config(state=NORMAL)
        		
        		clicked=True
        		count=0
        		
        	
        	def disable_all_buttons():
        		b1.config(state=DISABLED)
        		b2.config(state=DISABLED)
        		b3.config(state=DISABLED)
        		b4.config(state=DISABLED)
        		b5.config(state=DISABLED)
        		b6.config(state=DISABLED)
        		b7.config(state=DISABLED)
        		b8.config(state=DISABLED)
        		b9.config(state=DISABLED)
        		
        		
        	
        	def checkiwon():
        		global winner
        		winner=False
        		
        		if b1["text"] == "X" and b2["text"] == "X" and b3["text"] =="X":
        		    b1.config(bg="red")
        		    b2.config(bg="red")
        		    b3.config(bg="red")
        		    winner=True
        		    messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X Wins!!")
        		    disable_all_buttons()
        		    
        		elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] =="X":
        		    b4.config(bg="red")
        		    b5.config(bg="red")
        		    b6.config(bg="red")
        		    winner=True
        		    messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X Wins!!")
        		    disable_all_buttons()
        		    
        		elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] =="X":
        		    b7.config(bg="red")
        		    b8.config(bg="red")
        		    b9.config(bg="red")
        		    winner=True
        		    messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X Wins!!")
        		    disable_all_buttons()
        		    
        		elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] =="X":
        		    b1.config(bg="red")
        		    b4.config(bg="red")
        		    b7.config(bg="red")
        		    winner=True
        		    messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X Wins!!")
        		    disable_all_buttons()
        		    
        		elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] =="X":
        		    b2.config(bg="red")
        		    b5.config(bg="red")
        		    b8.config(bg="red")
        		    winner=True
        		    messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X Wins!!")
        		    disable_all_buttons()
        		    
        		elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] =="X":
        		    b3.config(bg="red")
        		    b6.config(bg="red")
        		    b9.config(bg="red")
        		    winner=True
        		    messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X Wins!!")
        		    disable_all_buttons()
        		    
        		elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] =="X":
        		    b1.config(bg="red")
        		    b5.config(bg="red")
        		    b9.config(bg="red")
        		    winner=True
        		    messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X Wins!!")
        		    disable_all_buttons()
        		    
        		elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] =="X":
        		    b3.config(bg="red")
        		    b5.config(bg="red")
        		    b7.config(bg="red")
        		    winner=True
        		    messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X Wins!!")
        		    disable_all_buttons()
        		    
        		    
        		    
        		elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] =="O":
        		    b1.config(bg="red")
        		    b2.config(bg="red")
        		    b3.config(bg="red")
        		    winner=True
        		    messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O Wins!!")
        		    disable_all_buttons()
        		    
        		elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] =="O":
        		    b4.config(bg="red")
        		    b5.config(bg="red")
        		    b6.config(bg="red")
        		    winner=True
        		    messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O Wins!!")
        		    disable_all_buttons()
        		    
        		elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] =="O":
        		    b7.config(bg="red")
        		    b8.config(bg="red")
        		    b9.config(bg="red")
        		    winner=True
        		    messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O Wins!!")
        		    disable_all_buttons()
        		    
        		elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] =="O":
        		    b1.config(bg="red")
        		    b4.config(bg="red")
        		    b7.config(bg="red")
        		    winner=True
        		    messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O Wins!!")
        		    disable_all_buttons()
        		    
        		elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] =="O":
        		    b2.config(bg="red")
        		    b5.config(bg="red")
        		    b8.config(bg="red")
        		    winner=True
        		    messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O Wins!!")
        		    disable_all_buttons()
        		    
        		elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] =="O":
        		    b3.config(bg="red")
        		    b6.config(bg="red")
        		    b9.config(bg="red")
        		    winner=True
        		    messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O Wins!!")
        		    disable_all_buttons()
        		    
        		elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] =="O":
        		    b1.config(bg="red")
        		    b5.config(bg="red")
        		    b9.config(bg="red")
        		    winner=True
        		    messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O Wins!!")
        		    disable_all_buttons()
        		    
        		elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] =="O":
        		    b3.config(bg="red")
        		    b5.config(bg="red")
        		    b7.config(bg="red")
        		    winner=True
        		    messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O  Wins!!")
        		    disable_all_buttons()
        		    
        	def b_click(b):
        		global clicked,count
        		
        		if b["text"] ==" " and clicked==True:
        		    b["text"]="X"
        		    clicked=False
        		    count+=1
        		    checkiwon()
        		    
        		elif b["text"] ==" " and clicked==False:
        		    b["text"]="O"
        		    clicked=True
        		    count+=1
        		    checkiwon()
        		    
        		else:
        			messagebox.showerror("Tic Tac Toe","Hey! \nThat box has already \nbeen selected\npick Another Box....")
        			
        			
        	b1=Button(frame,text=" ",font=("Helvetica",20),bd=10,bg="yellow",command=lambda: b_click(b1))
        	b2=Button(frame,text=" ",font=("Helvetica",20),bd=10,bg="yellow",command=lambda: b_click(b2))
        	b3=Button(frame,text=" ",font=("Helvetica",20),bd=10,bg="yellow",command=lambda: b_click(b3))
        	
        	b4=Button(frame,text=" ",font=("Helvetica",20),bd=10,bg="yellow",command=lambda: b_click(b4))
        	b5=Button(frame,text=" ",font=("Helvetica",20),bd=10,bg="yellow",command=lambda: b_click(b5))
        	b6=Button(frame,text=" ",font=("Helvetica",20),bd=10,bg="yellow",command=lambda: b_click(b6))
        	
        	b7=Button(frame,text=" ",font=("Helvetica",20),bd=10,bg="yellow",command=lambda: b_click(b7))
        	b8=Button(frame,text=" ",font=("Helvetica",20),bd=10,bg="yellow",command=lambda: b_click(b8))
        	b9=Button(frame,text=" ",font=("Helvetica",20),bd=10,bg="yellow",command=lambda: b_click(b9))
        	
        	
        	b1.place(x=310,y=840,height=140,width=140)
        	b2.place(x=450,y=840,height=140,width=140)
        	b3.place (x=590,y=840,height=140,width=140)
        	
        	b4.place (x=310,y=980,height=140,width=140)
        	b5.place (x=450,y=980,height=140,width=140)
        	b6.place (x=590,y=980,height=140,width=140)
        	
        	b7.place (x=310,y=1120,height=140,width=140)
        	b8.place (x=450,y=1120,height=140,width=140)
        	b9.place (x=590,y=1120,height=140,width=140)
        	
        	
        	rst=Button(frame,text="RESET",font=("Helvetica",5),bg="yellow",command=reset)
        	rst.place(x=470,y=1280,height=50,width=100)
  
        play()
        
    def graphics(self):
        frame=Frame(self.root,bg="white").place(x=310,y=840,height=500,width=420)
        def play():
        	canvas = Canvas(master = self.root,width = 400, height = 480)
        	canvas.place(x=320,y=850)
        	t = turtle.RawTurtle(canvas)
        	t.speed(0)
        	t.ht()
        	h=0.001
        	length=100
        	t.pensize(5)
        	t.up()
        	t.goto(-50,50)
        	t.down()
        	for i in range(200):
        		c=colorsys.hsv_to_rgb(h,1,1)
        		t.color(c)
        		t.fd(length)
        		t.rt(89)
        		
        		length+=1
        		h+=0.05
        play()
     
        pass
        
        
root=Tk()
obj=Login(root)
root.mainloop()

