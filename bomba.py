from tkinter import *
import time
import webbrowser

global cont, estado
cont = 6
estado = False

def activar():
	global cont, estado
	estado = True
	contador()

def contador():
	global cont, estado
	if estado == True:
		cont-=1
		b2.config(state="normal")
		b1.config(state="disabled")
		var_bomba.set(cont)
		if cont == 0:
			var_bomba.set("\U0001f4a5")
			estado = False
			cont = 0
			start()
		label.after(1000, contador);

def desactivar():
	global cont, estado
	estado = False
	b1.config(state="normal")
	b2.config(state="disabled")
	if cont > 0:
		var_bomba.set(cont)
	else:
		var_bomba.set("\U0001f4a3")
		cont = 6

def start2():
	print("Bomba explota")

def start():
	time.sleep(1)
	n=0
	while n <= 2:
		webbrowser.open('https://www.xnxx.com/video-mnn8ff5/gay_sexy_trap_brazilian_porn_actors_male')
		n+=1
		
def main():
	global b1, b2, label
	frame = Frame(root).pack(expand="True", fill="both")
	label = Label(frame, textvariable=var_bomba, bg="pink", font=("Consolas", 200))
	label.pack(expand="True", fill="both")
	b1 = Button(frame, text="Activar Bomba",bg="red", width=15, font=("Consolas", 30), command=activar)
	b1.pack()
	b2 = Button(frame, text="Stop Bomba",bg="green", width=15, font=("Consolas", 30), command=desactivar, state="disabled")
	b2.pack()

if __name__ == "__main__":
	root = Tk()
	root.title("BOMBA")
	root.resizable(False, False)
	root.config(padx=10, pady=10)
	var_bomba = StringVar()
	var_bomba.set("\U0001f4a3")
	main()
	root.mainloop()

