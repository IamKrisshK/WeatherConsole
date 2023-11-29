import tkinter
from tkinter import *
import customtkinter,requests
import pyglet
from PIL import Image, ImageTk

# System
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

pyglet.font.add_file(r'Ketika-Light.ttf')

# Api
api_key = '30d4741c779ba94c470ca1f63045390a'

# Functions
def function():
    user_input = input1.get()
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        label2.configure(text='City Not Found')
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        celsius = (temp - 32) * 5/9

        label2.configure(text=f"It is {weather} at {user_input}")
        label3.configure(text=f"The temperature is: {celsius:.2f}ºC")



#images_function
        if weather == "Clouds":
            label4.configure(image=imgcloud, width=500, height=90)
        elif weather == "Rain" or "Drizzle":
            label4.configure(image=imgrain, width=500, height=90)
        elif weather == "Clear":
            label4.configure(image=imgclear, width=500, height=90)
            
app = customtkinter.CTk()
app.geometry("640x480")
app.minsize(640,480)
app.maxsize(640,480)
bgimg=ImageTk.PhotoImage(Image.open(r"bg.png"),master=app)
limg=Label(app,image=bgimg)
limg.place(x=0,y=0,relheight=1,relwidth=1)
app.title("Weather Console")
app.attributes("-alpha",0.76)
app.iconbitmap(r"Weat.ico")

# Images
imgcloud = ImageTk.PhotoImage(Image.open(r"clouds.png"))
imgclear = ImageTk.PhotoImage(Image.open(r"clear.png"))
imgrain = ImageTk.PhotoImage(Image.open(r"rain.png"))
imgdefault = ImageTk.PhotoImage(Image.open(r"default.png"))
label4 = Label(image=imgdefault, width=5, height=9)
label4.pack()


# Widgets
frame = customtkinter.CTkFrame(app)
frame.pack(padx=20, pady=20, expand=True)

label = customtkinter.CTkLabel(frame, text="Weather Console", text_color="white", font=customtkinter.CTkFont(family='Roboto',size=19), width=300, height=80)
label.pack(padx=20, pady=20)

input1 = customtkinter.CTkEntry(frame, placeholder_text="Enter the city")
input1.pack(padx=20, pady=3)

btn = customtkinter.CTkButton(frame, text="Check", command=function)
btn.pack(padx=20, pady=3)

label2 = customtkinter.CTkLabel(frame, text="Weather", text_color="white", font=('Arial', 19), width=300, height=80)
label2.pack(padx=20, pady=3)

label3 = customtkinter.CTkLabel(frame, text="Temperature", text_color="white", font=('Arial', 19), width=300, height=80)
label3.pack(padx=20, pady=3)

# Run the app
app.mainloop()
