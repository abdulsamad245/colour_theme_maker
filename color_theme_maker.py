import tkinter
from tkinter  import BOTH,Scale,DISABLED,IntVar,filedialog

#Define root window
root =tkinter.Tk()
root.title('Color Theme Maker')
root.iconbitmap('')
root.geometry("450x500")
root.resizable(0,0)


def get_red(slider_value):
    #print(slider_value)
    global red_value
   
    red_value=hex(int(slider_value))
    #print(red_value)
    red_value=red_value.lstrip("0x")
    #print(red_value)

    while len(red_value) <2:
          red_value="0"+str (red_value)
    print(red_value)
    update_colour()

def get_green(slider_value):
    #print(slider_value)
    global green_value
   
    green_value=hex(int(slider_value))
    #print(red_value)
    green_value=green_value.lstrip("0x")
    #print(red_value)

    while len(green_value)<2:
          green_value="0"+str (green_value)
    #print(green_value)
    update_colour()


def get_blue(slider_value):
    #print(slider_value)
    global blue_value
   
    blue_value=hex(int(slider_value))
    #print(red_value)
    blue_value=blue_value.lstrip("0x")
    #print(red_value)

    while len(blue_value)<2:
          blue_value="0"+str (blue_value)
    #print(blue_value)
    update_colour()
    print("r"+"r")


def update_colour():
    colour_box=tkinter.Label(input_frame,bg="#"+red_value+green_value+blue_value,height=6,width=15)
    colour_box.grid(row=1,column=3,columnspan=2 ,padx=35,pady=10)

    colour_tuple.config(text='('+str(red_slider.get())+'),('+str(green_slider.get())+'),('+str(blue_slider.get())+')')
    colour_hex.config(text='#'+red_value+green_value+blue_value)
    

    #colour_tuple.config(text='('+str(red_value)+'),'+'('+str(green_value)+'),'+'('+str(blue_value)+')')


def set_colours(r,g,b):
    red_slider.set(r)
    green_slider.set(g)
    blue_slider.set(b)

def store_colour():

    red=str(red_slider.get())
    if len(red) <3:
        red="0" + red
        #print(red)

    green=str(green_slider.get())
    while len(green) <3:
          green="0" + green


    blue=str(blue_slider.get())
    while len(blue) <3:
          blue="0" + blue

    stored_red=red_slider.get()
    stored_green=green_slider.get()
    stored_blue=blue_slider.get()


    recall_button=tkinter.Button(output_frame,text='Recall Colour',command=lambda:set_colours(stored_red,stored_green,stored_blue))

    #new_colour_tuple=tkinter.Label(output_frame,text='('+str(red_slider.get())+'),('+str(green_slider.get())+'),('+str(blue_slider.get())+')')
    new_colour_tuple=tkinter.Label(output_frame,text='('+red+'),('+green+'),('+blue+')')
    new_colour_hex=tkinter.Label(output_frame,text='#'+red_value+green_value+blue_value)
    new_colour_black_box=tkinter.Label(output_frame,bg='black',width=3,height=1)
    new_colour_box=tkinter.Label(output_frame,bg='#'+red_value+green_value+blue_value,width=3,height=1)
    print(type(red_value+green_value+blue_value))

    recall_button.grid(row=stored_colour.get(),column=1,padx=20)
    new_colour_tuple.grid(row=stored_colour.get(),column=2,padx=20)
    new_colour_hex.grid(row=stored_colour.get(),column=3,padx=20)
    new_colour_black_box.grid(row=stored_colour.get(),column=4,pady=2,ipadx=5,ipady=5)
    new_colour_box.grid(row=stored_colour.get(),column=4)

    stored_colours[stored_colour.get()]=[new_colour_tuple.cget('text'),new_colour_hex.cget('text')]
    # print(stored_colours)
    # print(stored_colour.get())
    print(stored_colours[0])
    for saved_entry in stored_colours:
                # print(saved_entry[0] +'\n' +saved_entry[1] +'\n\n')
                print(saved_entry)


    if stored_colour.get() <5:
          stored_colour.set(stored_colour.get()+1)



def save_colour():
    print(stored_colours)
    print(stored_colour.get())

    save_colours=filedialog.asksaveasfilename(initialdir="./",title="Save Colours",filetypes=(("Text Files","*.txt"),("All Files","*.*")))
    with open(save_colours,"w") as f:
        f.write('Colour Theme Maker\n')
        for saved_entry in stored_colours.values():
            f.write(saved_entry[0] +'\n' +saved_entry[1] +'\n\n')
            # f.write(stored_colours[saved_entry][0]+stored_colours[saved_entry][1])

    



    



input_frame=tkinter.LabelFrame(root,padx=5,pady=5)
output_frame=tkinter.LabelFrame(root)
input_frame.pack(fill=BOTH,expand=True,padx=5,pady=5)
output_frame.pack(fill=BOTH,expand=True,padx=5,pady=5)




red_label=tkinter.Label(input_frame,text='R')
red_slider=tkinter.Scale(input_frame,from_=0,to=225,command=get_red)
red_button=tkinter.Button(input_frame,text='Red',command=lambda:set_colours(255,0,0))

green_label=tkinter.Label(input_frame,text='G')
green_slider=tkinter.Scale(input_frame,from_=0,to=225,command=get_green)
green_button=tkinter.Button(input_frame,text='Green',command=lambda:set_colours(0,255,0))


blue_label=tkinter.Label(input_frame,text='B')
blue_slider=tkinter.Scale(input_frame,from_=0,to=225,command=get_blue)
blue_button=tkinter.Button(input_frame,text='Blue',command=lambda:set_colours(0,0,255))


cyan_button=tkinter.Button(input_frame,text='Cyan',command=lambda:set_colours(0,255,255))
yellow_button=tkinter.Button(input_frame,text='Yellow',command=lambda:set_colours(255,255,0))
magenta_button=tkinter.Button(input_frame,text='Magenta',command=lambda:set_colours(255,0,255))


store_button=tkinter.Button(input_frame,text='Store Colour',command=store_colour)
save_button=tkinter.Button(input_frame,text='Save',command=save_colour)
quit_button=tkinter.Button(input_frame,text='Quit',command=root.destroy)


red_label.grid(row=0,column=0,sticky='W')
red_slider.grid(row=1,column=0,sticky='W')
red_button.grid(row=2,column=0,padx=1,pady=1,ipadx=20)

green_label.grid(row=0,column=1,sticky='W')
green_slider.grid(row=1,column=1,sticky='W')
green_button.grid(row=2,column=1,padx=1,pady=1,ipadx=15)

blue_label.grid(row=0,column=2,sticky='W')
blue_slider.grid(row=1,column=2,sticky='W')
blue_button.grid(row=2,column=2,padx=1,pady=1,ipadx=18)

yellow_button.grid(row=3,column=0,padx=1,pady=1,sticky='WE')
cyan_button.grid(row=3,column=1,padx=1,pady=1,sticky='WE')
magenta_button.grid(row=3,column=2,padx=1,pady=1,sticky='WE')
store_button.grid(row=4,column=0,padx=1,pady=1,sticky='WE',columnspan=3)
save_button.grid(row=4,column=3,padx=1,pady=1,sticky='WE')
quit_button.grid(row=4,column=4,padx=1,pady=1,sticky='WE')


colour_box=tkinter.Label(input_frame,bg='black',height=6,width=15)
colour_tuple=tkinter.Label(input_frame,text='(0),(0),(0)')
colour_hex=tkinter.Label(input_frame,text='000000')

colour_box.grid(row=1,column=3,columnspan=2 ,padx=35,pady=10,ipadx=10,ipady=10)
colour_tuple.grid(row=2,column=3,columnspan=2)
colour_hex.grid(row=3,column=3,columnspan=2)

stored_colours={}
stored_colour=IntVar()

for i in range(6):
    radio=tkinter.Radiobutton(output_frame,variable=stored_colour,value=i)
    radio.grid(row=i,column=0,columnspan=3,sticky='W')

    recall_button=tkinter.Button(output_frame,text='Recall Colour',state=DISABLED)
    new_colour_tuple=tkinter.Label(output_frame,text='(255),(255),(255)')
    new_colour_hex=tkinter.Label(output_frame,text='#ffffff')
    new_colour_black_box=tkinter.Label(output_frame,bg='black',width=3,height=1)
    new_colour_box=tkinter.Label(output_frame,bg='white',width=3,height=1)

    recall_button.grid(row=i,column=1,padx=20)
    new_colour_tuple.grid(row=i,column=2,padx=20)
    new_colour_hex.grid(row=i,column=3,padx=20)
    new_colour_black_box.grid(row=i,column=4,pady=2,ipadx=5,ipady=5)
    new_colour_box.grid(row=i,column=4,pady=2)
    #print(i)


    #stored_colours[stored_colour.get()]=[new_colour_tuple.cget('text'),new_colour_hex.cget('text')]
    print(stored_colour.get())
    print(stored_colour)


    red_value='00'
    green_value='00'
    blue_value='00'
    

#radio=tkinter.Radiobutton(output_frame,variable=1,value=1)
#radior=tkinter.Radiobutton(output_frame,variable=1,value=2)

#radio.grid(row=0,column=5,columnspan=3,sticky='W')
#radior.grid(row=1,column=5,columnspan=3,sticky='W')
print(type(red_value+green_value+blue_value))




root.mainloop()