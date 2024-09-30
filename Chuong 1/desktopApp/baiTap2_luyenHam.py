from customtkinter import *
from PIL import Image
#TODO: Functions
# Hàm có tham số/parameter (giá trị được truyền vào hàm)
def change_theme(new_theme:str ):
    set_appearance_mode(new_theme)

def switch_func():
    # print("click switch")
    # lấy giá trị của switch_value
    value = switch_value.get() 
    if value == "on":
        img_label = CTkLabel(right_frame, image=on_img, text = "")
        img_label.grid(row = 0, column = 0, padx = 20, pady = 20)
    else:
        img_label = CTkLabel(right_frame, image=off_img, text = "")
        img_label.grid(row = 0, column = 0, padx = 20, pady = 20)

#TODO Màn hình chính
app = CTk()
app.geometry("600x400")
app.title("Bài tập đổi theme & hình")

app.grid_columnconfigure((0,1), weight=1)
#mặc định màu tối
set_appearance_mode("Dark") #modes: "System", "Dark", "Light"

#TODO: Tạo Frame
left_frame = CTkFrame(app)
right_frame = CTkFrame(app)

#TODO: Hiển thị frame
#padding - khoảng cách, padx (trái, phải), pady (trên, dưới)
left_frame.grid(row = 0, column = 0,padx = (0, 20), sticky="nswe")
left_frame.grid_columnconfigure(0, weight=1)

right_frame.grid(row = 0, column = 1, sticky="nswe")

#TODO: Widget
theme_label = CTkLabel(left_frame, text="Theme mode: ", text_color="#3B8ED0" )
theme_label.grid(row = 0, column = 0, padx = 10, pady = (5,0))
# List 
theme_optionmenu = CTkOptionMenu(left_frame, values=["Dark", "Light"],command=change_theme )
theme_optionmenu.grid(row = 1, column = 0, padx = 10, pady = (5,0))

switch_label = CTkLabel(left_frame, text="Switch bulb On/Off ", text_color="#3B8ED0" )
switch_label.grid(row = 2, column = 0, padx = 10, pady = (5,0))

switch_value = StringVar(value="on") #mặc định bật bóng đèn 
switch_button = CTkSwitch(left_frame,command=switch_func,variable=switch_value,onvalue="on", offvalue="off" )
switch_button.grid(row = 3, column = 0, padx = 10, pady = (5,0))

on_img = CTkImage(light_image=Image.open("./bongDen/DenMo.png"), size=(300, 400))
off_img = CTkImage(light_image=Image.open("./bongDen/denTat.png"), size=(300, 400))
# Hien thi hinh bang CTKLabel
img_label = CTkLabel(right_frame, image=on_img, text = "")
img_label.grid(row = 0, column = 0, padx = 20, pady = 20)

#Run màn hình
app.mainloop()