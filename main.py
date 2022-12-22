import tkinter
import customtkinter
from pytube import YouTube
import os


#Setting the themes
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

#Creating the app window
app = customtkinter.CTk()
app.geometry("800x600")
app.title("Super Cool Youtube Converter")

# Create directory
dirName = 'SCYC'
dirPath = 'E'

try:
    # Create target Directory
    os.mkdir(dirName)
    dirPath = os.getcwd() + '/' + dirName
    print("Directory " , dirName ,  " Created ") 
    print("Directory " , dirPath ,  " Created ") 
except FileExistsError:
    print("Directory " , dirName ,  " already exists")
    dirPath = os.getcwd() + '/' + dirName


def download(link, video):
    if bool(video)==True:
        print('video')
        yt = YouTube(link)
        # Getting the highest resolution possible
        ys = yt.streams.get_highest_resolution()
        ys.download(output_path=dirPath)
    elif bool(video)==False:
        yt = YouTube(link)
        # extract only audio
        ys = yt.streams.filter(only_audio=True).first()
        # download the file
        out_file = ys.download(output_path=dirPath)
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

def button_callback():
    if combobox.get()=="MP4":
        download(entry_1.get(), True)
    elif combobox.get()=="MP3":
        download(entry_1.get(), False)
    print(combobox.get())

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)
    

optionmenu_var = customtkinter.StringVar(value="MP4")  # set initial value

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Youtube Converter By Adil")
label_1.pack(pady=10, padx=10)


entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Enter link...")
entry_1.pack(pady=10, padx=10)

combobox = customtkinter.CTkComboBox(master=frame_1,
                                     values=["MP4", "MP3"],
                                        command=optionmenu_callback,
                                     variable=optionmenu_var)
combobox.pack(padx=20, pady=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback, text="Convert")
button_1.pack(pady=10, padx=10)


app.mainloop()


