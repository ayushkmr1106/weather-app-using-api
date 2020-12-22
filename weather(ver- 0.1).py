from tkinter import *
from PIL import Image, ImageTk
import requests
import json
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox


root = Tk()
root.iconbitmap("weather_images\\icon_bit.ico")
root.title("Weather")
# root.geometry("644x344")
# root.minsize(344,144)
root.config(bg='#34495E')
root.resizable(0, 0)


def find():

    try:
        myList = myEntry.get().split(',')[:2]
        main = Toplevel()
        main.resizable(FALSE, FALSE)
        now = datetime.now()
        request_data = requests.get(
            "https://api.weatherbit.io/v2.0/current?city="+myList[0]+"&country="+myList[1]+"&key=3654eb2eda5d4d66ac51d2ca60e4e6f5")
        data = json.loads(request_data.content)
        modified_data = data['data'][0]
        
        panedwindow = ttk.PanedWindow(main, orient=HORIZONTAL)
        panedwindow.pack(fill=BOTH, expand=True)

        frame = Frame(panedwindow, borderwidth=7, relief = RIDGE)
        frame.grid(row=0, column=0 ,columnspan= 2)

        myLabel = Label(frame, text="Last Updated on " + now.strftime("%B %d %Y %H:%M"), font = "Helvetica 14 bold", width = 43, bg = 'sky blue')
        myLabel.grid(row=0, column=0, columnspan=2)

        frame1 = Frame(panedwindow, relief=SUNKEN,borderwidth=4)
        frame1.grid(row= 1, column=0, sticky = N+W+E+S, pady = 5)
    

        myLabel1 = Label(frame1, text="               Temperature              ", font="Helvetica 14 bold", justify= LEFT, relief = SUNKEN, pady = 5).grid(row=0, column=0, sticky = E+W)
        myLabel2 = Label(frame1, text="               City Name              ", font="Helvetica 14 bold", justify = LEFT, relief = SUNKEN, pady = 5).grid(row=1, column=0, sticky = E+W)
        myLabel3 = Label(frame1, text="               Country Code              ",
        font="Helvetica 14 bold", justify= LEFT, relief = SUNKEN, pady = 5).grid(row=2, column=0, sticky = E+W)
        myLabel4 = Label(frame1, text="               Wind Speed              ", font="Helvetica 14 bold", justify= LEFT, relief = SUNKEN, pady = 5).grid(row=3, column=0, sticky = E+W)
        myLabel5 = Label(frame1, text="               Aqi              ", font="Helvetica 14 bold", justify= LEFT, relief = SUNKEN, pady = 5).grid(row=4, column=0, sticky = E+W)
        myLabel6 = Label(frame1, text="               Time Zone              ", font="Helvetica 14 bold", justify= LEFT, relief = SUNKEN, pady = 5).grid(row=5, column=0, sticky = E+W)
        myLabel7 = Label(frame1, text="               Visibility              ", font="Helvetica 14 bold", justify= LEFT, relief = SUNKEN, pady = 5).grid(row=6, column=0, sticky = E+W)

        frame2 = Frame(panedwindow, relief=SUNKEN, borderwidth=4)
        frame2.grid(row=1, column=1, sticky=N+W+E+S, pady=5)
        

        resultLabel1 = Label(frame2, text ="               " + str(modified_data['temp']) + "           ", font = "Helvetica 14 bold", relief = SUNKEN, pady = 5).grid(row=0, column= 0, sticky = E+W)
        
        resultLabel2 = Label(frame2, text ="               " + modified_data['city_name'] + "           ", font = "Helvetica 14 bold", relief = SUNKEN, pady = 5).grid(row=1, column= 0, sticky = E+W)
        
        resultLabel3 = Label(frame2, text ="               " + modified_data['country_code'] + "           ", font = "Helvetica 14 bold", relief = SUNKEN, pady = 5).grid(row=2, column= 0, sticky = E+W)
        
        resultLabel4 = Label(frame2, text ="               " + str(modified_data['wind_spd']) + " MPH" + "           ", font = "Helvetica 14 bold", relief = SUNKEN, pady = 5).grid(row=3, column= 0, sticky = E+W)
        
        resultLabel5 = Label(frame2, text="               " + str(
        modified_data['aqi']) + "           ", font="Helvetica 14 bold", relief = SUNKEN, pady = 5).grid(row=4, column=0, sticky=E+W)
        
        resultLabel6 = Label(frame2, text ="               " + modified_data['timezone'] + "           ", font = "Helvetica 14 bold", relief = SUNKEN, pady = 5).grid(row=5, column= 0, sticky = E+W)
        
        resultLabel17 = Label(frame2, text ="               " + str(modified_data['vis']) + ' miles' + "           ", font = "Helvetica 14 bold", relief = SUNKEN, pady = 5).grid(row=6, column= 0, sticky = E+W)

    except Exception as e:
        main.destroy()
        message_response = messagebox.showerror(title= 'Error Message', message= "Sorry! \nCity Not Found...")


text_input = StringVar()
frame1 = Frame(root, relief=SUNKEN, bg='#7ce9fd')
frame1.pack(pady=5, padx=5)
image = ImageTk.PhotoImage(Image.open('weather_images\\cloud.png'))
imageLabel = Label(frame1, image=image)
imageLabel.grid(row=0, column=0, columnspan=3, pady=5)
myLabel = Label(frame1, text="Enter City: ", font="Helvetica 14 bold italic")
myLabel.grid(row=1, column=0)
myEntry = Entry(frame1, textvariable=text_input, width=25,
                borderwidth=5, bg='#f2dccb', font='Helvetica 14')
myEntry.grid(row=1, column=1)
myButton = Button(frame1, text="Find", padx=10, font='Helvetica 14 bold',
bg='#000121', command=find, relief=RAISED, fg='#ffffff')
myButton.grid(row=1, column=2, padx=10, pady=10)


root.mainloop()
