from tkinter import *
import pyperclip
import qrcode
from PIL import ImageTk
import time



class Window:

    def __init__(self):
        self.active = True
        self.loop_delay = 2000   
        self.is_modifiable = False
        self.IS_HOST_PRESSED = False 
        self.win_size = (250,280)
        self.image_size = (250,250)
        self.win_location = (1290,0)
        self.window = None
        self.image_box=None
        self.text_box =None
        self.modify_btn = None
        self.ative_btn = None
        self.top_frame = None

        self.text=None
        self.win_generator()
        self.qrcode_generator()


        
    def process_loop(self):
        if self.active:
            self.qrcode_generator()


    def win_generator(self):
        self.window = Tk()
        self.window.overrideredirect(not self.is_modifiable)
        self.top_frame = Frame(self.window)
        self.top_frame.grid(row=1, column=0)
        # self.window.attributes('-alpha',0.8)

        self.window.geometry(f"{self.win_size[0]}x{self.win_size[1]}+{self.win_location[0]}+{self.win_location[1]}")
        self.modify_btn= Button(self.top_frame,text = "modify toggle",command=self.modify_mode , height=0, width=15)  
        self.modify_btn.grid(row=0, column=0)
        self.ative_btn= Button(self.top_frame, text = "active toggle",command=self.aactive_toggle , height=0, width=15)  
        self.ative_btn.grid(row=0, column=1)
        
        
        
          
    def qrcode_generator(self):
        self.window.after(self.loop_delay,self.process_loop)

        changed = self.text  != pyperclip.paste()
        if changed :
            self.text  = pyperclip.paste()

            qr = qrcode.QRCode(version=3, error_correction=qrcode.constants.ERROR_CORRECT_H)
            qr.add_data(self.text)
            qr.make(fit=True)
            qr_image = qr.make_image(fill_color="black", back_color="white")
            qr_image = qr_image.resize(self.image_size)
            img = ImageTk.PhotoImage(qr_image)
            if not self.image_box:
                self.image_flag = True
                self.image_box = Label(self.window, image = img ) 
                self.image_box.grid(row=0, column=0)
                # self.text_box = Label(self.window, text= text)
                # self.text_box.pack()
                
                mainloop()


            else:
                # self.text_box.configure(text=text)
                self.image_box.configure(image=img)
                mainloop()


        # mainloop()


    def aactive_toggle(self):
        temp = self.window.geometry().split("+")
        print(temp)
        if self.active:
            self.active = False
            self.image_box.destroy()
            self.image_box= None
            self.window.geometry("225x25"+"+" +temp[1]+"+"+temp[2])


        else:
            self.active = True
            self.text = ""
            self.window.geometry(f"{self.win_size[0]}x{self.win_size[1]}+"+temp[1]+"+"+temp[2])
            self.qrcode_generator()


    def modify_mode(self):
        self.is_modifiable = not self.is_modifiable
        self.window.overrideredirect(not self.is_modifiable)
        mainloop()
    def stop(self):
        self.window.destroy()



win = Window()