#rgb color
from tkinter import *
from PIL import ImageTk, Image 

root = Tk()
root.title("sliders")
root.geometry("400x400")
#function to convert rbg into hex color code
def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'
    
def colorsel(val):
    r = slider_r.get()
    g = slider_g.get()
    b = slider_b.get()
    my_label.config(bg=rgbtohex(r,g,b))
    
#label for color viewing
my_label = Label(root, bg=rgbtohex(0,0,0))
my_label.grid(row=0, rowspan=3, column=1, padx=10, ipadx=100, pady=10, ipady=100)
#rgb value slider, doesn#t work properly with slider with command
#command needs a value in the function to give to, here ends up unused
slider_r = Scale(root, from_=0, to=255, orient=HORIZONTAL, command=colorsel)
slider_g = Scale(root, from_=0, to=255, orient=HORIZONTAL, command=colorsel)
slider_b = Scale(root, from_=0, to=255, orient=HORIZONTAL, command=colorsel)
slider_r.grid(row=0, column=0)
slider_g.grid(row=1, column=0)
slider_b.grid(row=2, column=0)
#button to update label
#my_button = Button(root, text="set color", command=colorsel)
#my_button.grid(row=3, column=1, columnspan=2, padx=10, pady=10, ipadx=100)

root.mainloop()