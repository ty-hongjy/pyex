import tkinter as tk

window=tk.Tk()
window.title("my window")
window.geometry("200x100")

var=tk.StringVar()
#l=tk.Label(window,textvariable=var ,bg="green",font=("Arial",12),width=15,height=12)
l=tk.Label(window,textvariable=var ,bg="green",font=("Arial",12),width=15,height=12)
l.pack()

on_hit=False
def hit_me():
	global on_hit
	if on_hit ==False:
		var.set('you hit me')
		on_hit=True
	else:
		var.set("")
		on_hit=False

def insert_point():
	var=e.get()
	t.insert("insert",var)

def insert_end():
	var=e.get()
	t.insert("end",var)

b=tk.Button(window,text="hit me",width=15,height=2,command=hit_me)
b.pack()

e=tk.Entry(window,show=None)
e.pack()

b1=tk.Button(window,text="insert point",width=15,height=2,command=insert_point)
b1.pack()

b2=tk.Button(window,text="insert end",width=15,height=2,command=insert_end)
b2.pack()

t=tk.Text(window,height=2)
t.pack()

window.mainloop()
