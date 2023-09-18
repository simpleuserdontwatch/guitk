from tkinter import *
class GUI(Frame):
    def __init__(self,parent,width=200,height=200):
        Frame.__init__(self, parent,width=width,height=height,bg='lightgrey')
        self.pack_propagate(False)
class window(Frame):
    def on_drag_start(self,event):
        self._drag_start_x = event.x
        self._drag_start_y = event.y

    def on_drag_motion(self,event):
        new_x = self.winfo_x() - self._drag_start_x + event.x
        new_y = self.winfo_y() - self._drag_start_y + event.y
        self.place(x=new_x, y=new_y)

    def __init__(self,parent,width=200,height=200,title='Tk'):
        Frame.__init__(self, parent,width=width,height=height,bg='white',highlightbackground="black",highlightthickness=1)
        self.pack_propagate(False)
        self.titlebar = Frame(self,height=15,width=width,bg='blue')
        self.titlebar.pack_propagate(False)
        self.titlebar.pack()
        self.titlebar.bind("<Button-1>", self.on_drag_start)
        self.titlebar.bind("<B1-Motion>", self.on_drag_motion)
        Label(self.titlebar,fg='white',bg='blue',text=title).pack(side=LEFT)
        Button(self.titlebar,fg='white',bg='red',text='X', command=self.place_forget, borderwidth=0).pack(side=RIGHT)
