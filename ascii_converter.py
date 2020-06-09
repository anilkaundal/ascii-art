from tkinter import filedialog
from tkinter import *
import PIL.Image
import time

def open_file():
	global path, label_1
	root.filename =  filedialog.askopenfilename(initialdir = "/",
		title = "Open file",filetypes = (("jpeg files","*.jpg"),
		("all files","*.*")))
	path = root.filename
	label_1 =Label(root,text = "Path:" + root.filename, bg = "#0052cc",
		fg = "#ffffff", font = 'Courier 12 bold')
	if(path != ""):
		label_1.pack(pady=10)
	else:
		label_5 = Label(root, text = "Please 'Enter' a valid path",
			bg = "#0052cc", fg = "#ffffff")
		label_5.pack(pady = 10)
		root.after(1000, label_5.destroy)
		
def openNewWindow():
	global path
	if(path == ""):
		label_3 = Label(root, text= "Please open a image file",
			bg = "#0052cc", fg = "#ffffff")
		label_3.pack(pady = 10)
		root.after(1000, label_3.destroy)
	else:
		main()
		path = ""
		root.after(1000, label_1.destroy)

def about():
	newWindow = Toplevel(root)
	newWindow.title('About')
	newWindow.geometry("300x100")
	e_mail = "anilkaundal1999@gmail.com"
	T = Text(newWindow, height = 2, width = 52)
	label_4 =Label(newWindow,text = "Developer: Anil Kaundal \n E-mail:",
		fg = "#000000", font = 'Courier 15 bold')
	label_4.pack()
	T.pack()
	T.insert(END, e_mail)

# resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)    

def main(new_width=100):
    # attempt to open image from user-input
    try:
        image = PIL.Image.open(path)
    except:
        print(path, " is not a valid pathname to an image.")
        return
  
    # convert image to ascii    
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    
    # format
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] 
    for index in range(0, pixel_count, new_width)])
    
    newWindow = Toplevel(root)
    newWindow.title('ASCII Image')
    txt_edit = Text(newWindow, bg = "black", fg = "#ffffff", height = 50,
		width=100) 
    txt_edit.pack()
    txt_edit.insert(END, ascii_image)
    
    '''
    # save result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
	'''
	
root = Tk()
root.title("Image to ASCII converter")
root.geometry("500x150")
path = ""
menu = Menu(root)
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu)  
filemenu.add_command(label='Open...', command=open_file) 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About', command= about)
label =Label(root,text='CONVERT YOUR IMAGE INTO ASCII CHARACTERS',
	bg = "black", fg = "white", font = 'Helvetica 15 bold')
label.pack(pady = 10)

# create button
button = Button(root, text='Convert', command = openNewWindow)
button.pack()

# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."] 
mainloop() 

