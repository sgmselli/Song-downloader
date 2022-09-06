import tkinter as tk
from tkinter import messagebox
import urllib
import os
import re
import pytube

def get_data(entry):
   data = entry.get()
   return data

def clicked(entrySong, entryArt, entryDir):
    
    try:
        if entrySong.get() != '' and entryArt != '' and entryDir != '':
            urlTransformed = urlForm(entryArt.get()+entrySong.get())
            watchLink = getVideo(urlTransformed)
            download(watchLink, entryDir.get(), entrySong.get(), entryArt.get())
        
        else:
            messagebox.showerror('Error', 'Please fill all fields!')
            

    except:
        messagebox.showerror('Error', 'Directory or song not found!')


def urlForm(search):
    charArray = list(search)
    for i in range (len(search)):
        if charArray[i] == ' ':
            charArray[i] = '+'
    return ''.join(str(x) for x in charArray)

def getVideo(search):
    request_url = urllib.request.urlopen("https://www.youtube.com/results?search_query="+search)
    video_ids = re.findall(r"watch\?v=(\S{11})", request_url.read().decode())
    return video_ids[0]

def download(watchURL, directory, song, artist):

    yt = pytube.YouTube('https://www.youtube.com/watch?v='+watchURL)        
    old_file = yt.streams.filter(only_audio=True).first().download(r""+directory)
    new_file = directory+'/'+artist+' - '+song+'.mp3'
    os.rename(old_file, new_file)
    messagebox.showinfo('Downloaded', 'Download complete!')
    

m=tk.Tk()

#Title
m.title('Youtube Song Downloader')

#icon
m.iconbitmap('C:/Users/selli/OneDrive/Documents/Python Projects/youtubeDownload/icon.ico')


#geometry to center window
window_width = 600
window_height = 400
m.resizable(False, False)
# get the screen dimension
screen_width = m.winfo_screenwidth()
screen_height = m.winfo_screenheight()
# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
m.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


tk.Label(m,text = 'Youtube Song Downloader', font ='arial 20 bold').pack(pady=30)

song = tk.Label(m, text='Song: ', font ='arial 10')
song.pack(pady=10)
e1 = tk.Entry(m, width=35, font ='arial 10')
e1.pack()

artist = tk.Label(m, text='Artist: ', font ='arial 10')
artist.pack(pady=10)
e2 = tk.Entry(m, width=35, font ='arial 10')
e2.pack()

directory = tk.Label(m, text='Save to directory: ', font ='arial 10')
directory.pack(pady=10)
e3 = tk.Entry(m, width=70, font ='arial 10')
e3.pack()

button = tk.Button(m, text='Download', command=lambda:clicked(e1,e2,e3))
button.pack(pady=20)

m.mainloop()
