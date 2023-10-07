# Basic tkinter template
from tkinter import *
root = Tk()
root.configure(bg="white")
canvas=Canvas(root,width=400,height=250)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E")

# Create all the labels required to be displayed

id = '1491061857'
name = 'Carl Samuel'
dob = '6/25/1979'
pin = '683956'
address = 'Springfield, Illinois'
vehicle = 'two four'

label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
label_id = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID :" + id)
label_name = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name :" + name)
label_dob = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth :" + dob)
label_pin = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. :" + pin)
label_address = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address :" + address)
label_vehicle_type = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles :" + vehicle)

# Define the function
def showInfo():
    label_id['text'] = id
    label_name['text'] = name
    label_dob['text'] = dob
    label_pin['text'] = pin
    label_address['text'] = address
    label_vehicle_type['text'] = vehicle

# Create a button
button1 = Button(root, text = 'Show Driving Licence', command = lambda: showInfo())
button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1.place(relx = 0.5, rely = 0.9, anchor = CENTER)
button1_window = canvas.create_window(200, 235, anchor=CENTER)
label_id_window = canvas.create_window(80, 60, anchor=CENTER)
label_name_window = canvas.create_window(100, 100, anchor=CENTER)
label_dob_window = canvas.create_window(140, 120, anchor=CENTER)
label_pin_window = canvas.create_window(85, 140, anchor=CENTER)
label_address_window = canvas.create_window(130, 160, anchor=CENTER)
label_vehicle_no_window = canvas.create_window(335, 180, anchor=CENTER)
canvas.pack()

# tkinter basic template end statement
root.mainloop()