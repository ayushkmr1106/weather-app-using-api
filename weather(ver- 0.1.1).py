from tkinter import *
from PIL import ImageTk
import PIL.Image
import requests
import json
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox


def requestData():
    try:
        # Get data from Entry Feild (myEntry)
        myList = myEntry.get().split(',')[:2]
        # Request Data From 'https://api.weatherbit.io'
        request_data = requests.get("https://api.weatherbit.io/v2.0/current?city="+myList[0]+"&country="+myList[1]+"&key=3654eb2eda5d4d66ac51d2ca60e4e6f5")
        data = json.loads(request_data.content)
        # Modify data after collecting 
        modified_data = data['data'][0]
        find(modified_data)
    except Exception as e:
        message_response = messagebox.showerror(title='Error Message', message="Sorry! \nCity Not Found...")

def find(data):
    try:
        main = Toplevel()
        main.resizable(FALSE, FALSE)

        #Frame-1 for Date And Time  
        frame = Frame(main, borderwidth=7, bg = 'sky blue')
        frame.grid(row=0, column=0 ,columnspan= 2)
        now = datetime.now()
        myLabel = Label(frame, text="Last Updated on " + now.strftime("%B %d %Y %H:%M"), font = "Helvetica 14 bold", width = 43, bg = 'sky blue')
        myLabel.grid(row=0, column=0)

        #Frame-2 for Labels (Temperature)
        frame1 = Frame(main, relief=SUNKEN, borderwidth=4, bg='#ffffff')
        frame1.grid(row= 1, column=0, sticky = N+W+E+S, pady = 5)

        myLabel1 = Label(frame1, text="               Conditions              ", font="Helvetica 14 bold", bg = '#ffffff', justify= LEFT, relief = SUNKEN, pady = 31).grid(row=0, column=0, sticky = E+W)
        myLabel2 = Label(frame1, text="               Temperature              ", font="Helvetica 14 bold", bg = '#ffffff', justify= LEFT, relief = SUNKEN, pady = 5).grid(row=1, column=0, sticky = E+W)
        myLabel3 = Label(frame1, text="               City              ", font="Helvetica 14 bold", bg = '#ffffff', justify = LEFT, relief = SUNKEN, pady = 5).grid(row=2, column=0, sticky = E+W)
        myLabel4 = Label(frame1, text="               Country Code              ",
        font="Helvetica 14 bold", bg = '#ffffff', justify= LEFT, relief = SUNKEN, pady = 5).grid(row=3, column=0, sticky = E+W)
        myLabel5 = Label(frame1, text="               Wind Speed              ", font="Helvetica 14 bold", bg = '#ffffff', justify= LEFT, relief = SUNKEN, pady = 5).grid(row=4, column=0, sticky = E+W)
        myLabel6 = Label(frame1, text="               Wind Direction              ", font="Helvetica 14 bold", bg = '#ffffff', justify= LEFT, relief = SUNKEN, pady = 5).grid(row=5, column=0, sticky = E+W)
        myLabel7 = Label(frame1, text="               Aqi              ", font="Helvetica 14 bold", bg = '#ffffff', justify= LEFT, relief = SUNKEN, pady = 5).grid(row=6, column=0, sticky = E+W)
        myLabel8 = Label(frame1, text="               Time Zone              ", font="Helvetica 14 bold", bg = '#ffffff', justify= LEFT, relief = SUNKEN, pady = 5).grid(row=7, column=0, sticky = E+W)
        myLabel9 = Label(frame1, text="               Visibility              ", font="Helvetica 14 bold", bg = '#ffffff', justify= LEFT, relief = SUNKEN, pady = 5).grid(row=8, column=0, sticky = E+W)

        #Frame-3 Resultant (Temperature) For Given City
        frame2 = Frame(main, relief=SUNKEN, borderwidth=4, bg='#ffffff')
        frame2.grid(row=1, column=1, sticky=N+W+E+S, pady=5)

        # Getting Condition Image from the function conditionIcon
        condition_image = conditionIcon(data['weather']['description'])
        resultLabel1 = Label(frame2, image= condition_image, text = data['weather']['description'], font = ('Helvetica', '12', 'bold'), bg = '#ffffff', relief = SUNKEN, pady = 5, compound= 'top')
        resultLabel1.img = condition_image
        resultLabel1.grid(row=0, column= 0, sticky = E+W)
        resultLabel2 = Label(frame2, text = str(data['temp']) + "°C", font = "Helvetica 14 bold", bg = '#ffffff', relief = SUNKEN, pady = 5).grid(row=1, column= 0, sticky = E+W)
        resultLabel3 = Label(frame2, text =data['city_name'], font = "Helvetica 14 bold", bg = '#ffffff', relief = SUNKEN, pady = 5).grid(row=2, column= 0, sticky = E+W)
        resultLabel4 = Label(frame2, text =data['country_code'], font = "Helvetica 14 bold", bg = '#ffffff', relief = SUNKEN, pady = 5).grid(row=3, column= 0, sticky = E+W)
        resultLabel5 = Label(frame2, text =str(data['wind_spd']) + " MPH", font = "Helvetica 14 bold", bg = '#ffffff', relief = SUNKEN, pady = 5).grid(row=4, column= 0, sticky = E+W)
        resultLabel6 = Label(frame2, text = data['wind_cdir_full'].upper(), font = "Helvetica 14 bold", bg = '#ffffff', relief = SUNKEN, pady = 5).grid(row=5, column= 0, sticky = E+W)
        resultLabel7 = Label(frame2, text=str(data['aqi']), font="Helvetica 14 bold", bg = '#ffffff', relief = SUNKEN, pady = 5).grid(row=6, column=0, sticky=E+W)
        resultLabel8 = Label(frame2, text ="               " + data['timezone'] + "           ", font = "Helvetica 14 bold", bg = '#ffffff', relief = SUNKEN, pady = 5).grid(row=7, column= 0, sticky = E+W)
        resultLabel19 = Label(frame2, text ="               " + str(data['vis']) + ' miles' + "           ", font = "Helvetica 14 bold", bg = '#ffffff', relief = SUNKEN, pady = 5).grid(row=8, column= 0, sticky = E+W)
    except Exception as e:
        print(e)

def conditionIcon(condition):
    if condition.lower() == 'clear sky':
        condition_image = ImageTk.PhotoImage(PIL.Image.open('weather_images\\clear_sky.jpg').resize((50, 50)))
    elif condition.lower() == 'light rain':
        condition_image = ImageTk.PhotoImage(PIL.Image.open('weather_images\\light_rain.jpg').resize((50, 50)))
    elif condition.lower() == 'overcast clouds':
        condition_image = ImageTk.PhotoImage(PIL.Image.open('weather_images\\overcast_cloud.jpg').resize((50, 50)))
    elif condition.lower() == 'scattered clouds':
        condition_image = ImageTk.PhotoImage(PIL.Image.open('weather_images\\scattered_clouds.jpg').resize((50, 50)))
    else:
        condition_image = ImageTk.PhotoImage(PIL.Image.open('weather_images\\haze.jpg').resize((50, 50)))
    return condition_image

if __name__ == "__main__":
    
    root = Tk()
    root.iconbitmap("weather_images\\icon_bit.ico")
    root.title("Weather")
    root.config(bg='#34495E')
    root.resizable(0, 0)

    text_input = StringVar()

    root_frame = Frame(root, relief=SUNKEN, bg='#7ce9fd')
    root_frame.pack(pady=5, padx=5)
    image = ImageTk.PhotoImage(PIL.Image.open('weather_images\\cloud.png'))
    imageLabel = Label(root_frame, image=image)
    imageLabel.grid(row=0, column=0, columnspan=3, pady=5)
    myLabell = Label(root_frame, text="Enter City: ", font="Helvetica 14 bold italic")
    myLabell.grid(row=1, column=0)
    myEntry = Entry(root_frame, textvariable=text_input, width=25, borderwidth=5, bg='#f2dccb', font='Helvetica 14')
    myEntry.grid(row=1, column=1)
    myButton = Button(root_frame, text="Find", padx=10, font='Helvetica 14 bold',bg='#000121', command=requestData, relief=RAISED, fg='#ffffff')
    myButton.grid(row=1, column=2, padx=10, pady=10)

    root.mainloop()