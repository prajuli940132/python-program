from tkinter import * 
import backend

def get_selected_row(event):
    global selected_tuple
    index=list_box.curselection()[0]
    selected_tuple=list_box.get(index)
    t4.delete(0,END)
    t4.insert(END,selected_tuple[1])
    t5.delete(0,END)
    t5.insert(END,selected_tuple[2])
    t6.delete(0,END)
    t6.insert(END,selected_tuple[3])
    t7.delete(0,END)
    t7.insert(END,selected_tuple[4])
def view_command():
    list_box.delete(0,END)
    for row in backend.view():
        list_box.insert(END,row)
def search():
    list_box.delete(0,END)
    for row in backend.search(e1.get(),e2.get(),e3.get(),e4.get()):
        list_box.insert(END,row)
def add():
    backend.insert(e1.get(),e2.get(),e3.get(),e4.get())
    list_box.delete(0,END)
    list_box.insert(END,"INSERTED SUCCESSFULLY !!")
def update():
    backend.update(selected_tuple[0],e1.get(),e2.get(),e3.get(),e4.get())
def delete():
    backend.delete(backend.delete(selected_tuple[0]))

window=Tk()
window.wm_title="Book Store"

l1=Label(window,text="TItle")
l1.grid(row=0,column=0)
l2=Label(window,text="Author")
l2.grid(row=0,column=2)
l3=Label(window,text="Year")
l3.grid(row=1,column=0)
l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

e1=StringVar()
t4=Entry(window,textvariable=e1)
t4.grid(row=0,column=1)

e2=StringVar()
t5=Entry(window,textvariable=e2)
t5.grid(row=0,column=3)

e3=StringVar()
t6=Entry(window,textvariable=e3)
t6.grid(row=1,column=1)


e4=StringVar()
t7=Entry(window,textvariable=e4)
t7.grid(row=1,column=3)

list_box=Listbox(window,height=6,width=35)
list_box.grid(row=2,column=0,rowspan=6,columnspan=2,padx=25)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list_box.configure(yscrollcommand=sb1.set)
sb1.configure(command=list_box.yview)

list_box.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View All",width=12,command=view_command)
b1.grid(row=2,column=3)
b2=Button(window,text="Search Entry",width=12,command=search)
b2.grid(row=3,column=3)
b3=Button(window,text="Add Entity",width=12,command=add)
b3.grid(row=4,column=3)
b4=Button(window,text="Update",width=12,command=update)
b4.grid(row=5,column=3)
b5=Button(window,text="Delete",width=12,command=delete)
b5.grid(row=6,column=3)
b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)


window.mainloop()