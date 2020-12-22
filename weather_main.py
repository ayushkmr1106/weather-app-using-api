from tkinter import *
from PIL import ImageTk
import PIL.Image
import requests
import json
from datetime import datetime
from tkinter import ttk
from tkinter.messagebox import showerror

def requestData():
    ''' Request Data from weatherbit api'''
    try:
        # Get data from Entry Feild (myEntry) From the Root Level
        cityValue = city_input.get().strip()
        countrycodeValue = countrycode_input.get().strip()
        # Request Data From 'https://api.weatherbit.io'
        request_data = requests.get("https://api.weatherbit.io/v2.0/current?city="+cityValue+"&country="+countrycodeValue+"&key=3654eb2eda5d4d66ac51d2ca60e4e6f5")
        data = json.loads(request_data.content)
        # Modify data after collecting
        modified_data = data['data'][0]
        main(modified_data)
    except Exception as e:
        message_response = showerror(title='Error Message', message="Sorry! \nCity Not Found...")

def main(data):
    ''' This function takes modified_data as data from requestData function and pack data in TopLevel Window '''
    try:
        # Creating a Top Level Window for Weather of Given City
        main = Toplevel(root)
        main.iconbitmap("weather_images\\icon_bit.ico")
        main.resizable(FALSE, FALSE)
        
        # Main frame
        frame = Frame(main)
        frame.pack()
        #Frame-1 for Showing Date And Time
        frame1 = Frame(frame, borderwidth=7, bg = 'sky blue')
        now = datetime.now()
        myLabel = Label(frame1, text="Last Updated on " + now.strftime("%B %d %Y %I:%M %p"), font = "Helvetica 14 bold", width = 43, bg = 'sky blue')

        # Packing Frames And Their Associated Labels
        myLabel.grid(row=0, column=0)
        frame1.grid(row=0, column=0 ,columnspan= 2)

        #Frame-2 for Labels (Temperature)
        frame2 = Frame(frame, relief=SUNKEN, borderwidth=4, bg='#ffffff')

        # Labels Under Frame-2
        myLabel1 = Label(frame2, text="               Conditions              ", font="Helvetica 14 bold", bg = '#ffffff', justify= LEFT, relief = SUNKEN, pady = 31)
        myLabel2 = Label(frame2, text="               Temperature              ", font="Helvetica 14 bold", bg = '#ffffff', justify= LEFT, relief = SUNKEN, pady = 5)
        myLabel3 = Label(frame2, text="               City              ", font="Helvetica 14 bold", bg = '#ffffff', justify = LEFT, relief = SUNKEN, pady = 5)
        myLabel4 = Label(frame2, text="               Country Code              ",
        font="Helvetica 14 bold", bg = '#ffffff', justify= LEFT, relief = SUNKEN, pady = 5)
        myLabel5 = Label(frame2, text="               Wind Speed              ", font="Helvetica 14 bold", bg = '#ffffff', justify= LEFT, relief = SUNKEN, pady = 5)
        myLabel6 = Label(frame2, text="               Wind Direction              ", font="Helvetica 14 bold", bg = '#ffffff', justify= LEFT, relief = SUNKEN, pady = 5)
        myLabel7 = Label(frame2, text="               Aqi              ", font="Helvetica 14 bold", bg = '#ffffff', justify= LEFT, relief = SUNKEN, pady = 5)
        myLabel8 = Label(frame2, text="               Time Zone              ", font="Helvetica 14 bold", bg = '#ffffff', justify= LEFT, relief = SUNKEN, pady = 5)
        myLabel9 = Label(frame2, text="               Visibility              ", font="Helvetica 14 bold", bg = '#ffffff', justify= LEFT, relief = SUNKEN, pady = 5)
        
        # Packing Frames And their Associated Labels
        myLabel1.grid(row=0, column=0, sticky = E+W)
        myLabel2.grid(row=1, column=0, sticky = E+W)
        myLabel3.grid(row=2, column=0, sticky = E+W)
        myLabel4.grid(row=3, column=0, sticky = E+W)
        myLabel5.grid(row=4, column=0, sticky = E+W)
        myLabel6.grid(row=5, column=0, sticky = E+W)
        myLabel7.grid(row=6, column=0, sticky = E+W)
        myLabel8.grid(row=7, column=0, sticky = E+W)
        myLabel9.grid(row=8, column=0, sticky = E+W)
        frame2.grid(row= 1, column=0, sticky = N+W+E+S, pady = 5)

        #Frame-3 Resultant (Temperature) For Given City
        frame3 = Frame(frame, relief=SUNKEN, borderwidth=4, bg='#ffffff')

        # Getting Condition Image from the function conditionIcon
        condition_image = conditionIcon(data['weather']['description'])
        
        # Labels Under Frame-3
        resultLabel1 = Label(frame3, image= condition_image, text = data['weather']['description'], font = ('Helvetica', '12', 'bold'), bg = '#ffffff', relief = SUNKEN, pady = 5, compound= 'top')
        resultLabel1.img = condition_image
        resultLabel2 = Label(frame3, text = str(data['temp']) + "°C", font = "Helvetica 14 bold", bg = '#ffffff', relief = SUNKEN, pady = 5)
        resultLabel3 = Label(frame3, text =data['city_name'], font = "Helvetica 14 bold", bg = '#ffffff', relief = SUNKEN, pady = 5)
        resultLabel4 = Label(frame3, text =data['country_code'], font = "Helvetica 14 bold", bg = '#ffffff', relief = SUNKEN, pady = 5)
        resultLabel5 = Label(frame3, text =str(data['wind_spd']) + " MPH", font = "Helvetica 14 bold", bg = '#ffffff', relief = SUNKEN, pady = 5)
        resultLabel6 = Label(frame3, text = data['wind_cdir_full'].upper(), font = "Helvetica 14 bold", bg = '#ffffff', relief = SUNKEN, pady = 5)
        resultLabel7 = Label(frame3, text=str(data['aqi']), font="Helvetica 14 bold", bg = '#ffffff', relief = SUNKEN, pady = 5)
        resultLabel8 = Label(frame3, text ="               " + data['timezone'] + "           ", font = "Helvetica 14 bold", bg = '#ffffff', relief = SUNKEN, pady = 5)
        resultLabel9 = Label(frame3, text ="               " + str(data['vis']) + ' miles' + "           ", font = "Helvetica 14 bold", bg = '#ffffff', relief = SUNKEN, pady = 5)

        # Packing Frames And Their Associated Label
        resultLabel1.grid(row=0, column=0, sticky=E+W)
        resultLabel2.grid(row=1, column=0, sticky=E+W)
        resultLabel3.grid(row=2, column=0, sticky=E+W)
        resultLabel4.grid(row=3, column=0, sticky=E+W)
        resultLabel5.grid(row=4, column=0, sticky=E+W)
        resultLabel6.grid(row=5, column=0, sticky=E+W)
        resultLabel7.grid(row=6, column=0, sticky=E+W)
        resultLabel8.grid(row=7, column=0, sticky=E+W)
        resultLabel9.grid(row=8, column=0, sticky=E+W)
        frame3.grid(row=1, column=1, sticky=N+W+E+S, pady=5)

    except Exception as e:
        print(e)

def conditionIcon(condition):
    ''' This function takes condition as argument and return image according to the conditions '''
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

def resetData():
    ''' Clear data written in Root Entry Widget'''
    cityEntry.delete(0,END)
    countrycodeEntry.delete(0,END)

root = Tk()
root.iconbitmap("weather_images\\icon_bit.ico")
root.title("Weather")
root.config(bg='#34495E')
root.resizable(0, 0)

city_input = StringVar()
countrycode_input = StringVar()

root_frame = Frame(root, relief=SUNKEN, bg='#7ce9fd')

image = ImageTk.PhotoImage(PIL.Image.open('weather_images\\cloud.png').resize((500,250)))
imageLabel = Label(root_frame, image=image)
cityLabel = Label(root_frame, text="City : ", font="Consolas 14 bold", bg = '#7ce9fd', anchor = 'e')
countrycodeLabel = Label(root_frame, text = "Country Code : ", font="Consolas 14 bold", bg= '#7ce9fd')
# Taking City and Country Code
cityEntry = ttk.Entry(root_frame, textvariable=city_input, width=16, font='Consolas 14')
countrycodeEntry = ttk.Entry(root_frame, textvariable= countrycode_input,width=16, font='Consolas 14')

find_image = ImageTk.PhotoImage(PIL.Image.open('weather_images\\findder.jpg').resize((30,30)))
findButton = Button(root_frame,image= find_image, text = 'Find', padx=10, pady =5, font='Consolas 14 bold',bg='#ffffff', command=requestData, fg='black', compound = 'left', relief= RIDGE)
reset_image = ImageTk.PhotoImage(PIL.Image.open('weather_images\\reset1.png').resize((30,30)))
resetButton = Button(root_frame, image=reset_image, text="Clear", padx=10, bg='#ffffff', font='Consolas 14 bold', pady=5, command=resetData, relief=RIDGE, fg='black', compound='left')

# Packing Root Frame And Their Associated Image Label, Entry, Button Widget
imageLabel.grid(row=0, column=0, columnspan=3, pady=5)
cityLabel.grid(row=1, column=0, sticky = E, pady=5)
countrycodeLabel.grid(row=2, column=0, sticky=E, pady=5)
cityEntry.grid(row=1, column=1, pady=5)
countrycodeEntry.grid(row=2, column=1)
findButton.grid(row=3, column=0,pady=10, sticky= E, padx = 4)
resetButton.grid(row=3, column=1, sticky=W)
root_frame.pack(pady=5, padx=5)

cityEntry.focus()

root.mainloop()
