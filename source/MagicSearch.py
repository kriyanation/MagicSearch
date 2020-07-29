import logging
import sys
import tkinter as tk
from tkinter import ttk
import webbrowser, urllib.parse
_isLinux = sys.platform.startswith('linux')
logger = logging.getLogger("MagicLogger")
BACKGROUND_COLOR = 'gray18'
FOREGROUND_COLOR = 'snow'
BOX_BACKGROUND_COLOR = "gray21"
BOX_FOREGROUND_COLOR = "snow"
class MagicSearch(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(background=BACKGROUND_COLOR)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('BlueSearch.TButton', background='steel blue', foreground='white', font=('helvetica', 10, 'bold'))

        s.map('BlueSearch.TButton', background=[('active', '!disabled', 'dark turquoise'), ('pressed', 'white')],
              foreground=[('pressed', 'white'), ('active', 'white')])
        self.buttons_frame = tk.Frame(self,background=BACKGROUND_COLOR)
        self.search_google_button = ttk.Button(self.buttons_frame, text="Google Images",command=self.search_images_google, style="BlueSearch.TButton")
        self.search_cc_button = ttk.Button(self.buttons_frame, text="Creative Commons", command=self.search_images_images_cc,
                                               style="BlueSearch.TButton")
        self.search_button_video_google = ttk.Button(self.buttons_frame, text="Google Videos",command=self.search_video_google, style="BlueSearch.TButton")
        self.search_button_video_archive = ttk.Button(self.buttons_frame, text="Internet Archives", command=self.search_images_video_ar,
                                                     style="BlueSearch.TButton")
        self.search_button_wiktionary = ttk.Button(self.buttons_frame, text="Wiktionary", command=self.search_def_wiktionary,
                                                      style="BlueSearch.TButton")

        self.search_label = tk.Label(self,
                                    borderwidth=3, highlightcolor="gray18", width=20,
                                    text="Search Text",
                                    font=("Helvetica", 12, 'bold'), background=BOX_BACKGROUND_COLOR,
                                    foreground=BOX_FOREGROUND_COLOR)
        self.search_label_help = tk.Label(self,
                                     borderwidth=3, highlightcolor="gray18",

                                     text="Requires Internet - Opens Browser with the search text passed to the respective sites",
                                     font=("Helvetica", 10, 'bold'), background=BOX_BACKGROUND_COLOR,
                                     foreground='Aquamarine')
        self.textvarimage = tk.StringVar()

        self.search_entry = tk.Entry(self,width=60,textvariable=self.textvarimage)
        self.search_label.grid(row=0,column=0,columnspan=2,padx=30,pady=10)
        self.search_entry.grid(row=0, column=2,columnspan=2,padx=30,pady=10)
        self.buttons_frame.grid(row=1,columnspan=5,column=1,padx=50,pady=10)
        self.search_google_button.grid(row=1, column=0,padx=15,pady=10)
        self.search_cc_button.grid(row=1, column=1, padx=15,pady=10)
        self.search_button_video_google.grid(row=1, column=2, padx=15, pady=10)
        self.search_button_video_archive.grid(row=1, column=3, padx=15, pady=10)
        self.search_button_wiktionary.grid(row=1, column=4, padx=15, pady=10)

        self.search_label_help.grid(row=2, column=1,columnspan=5,padx=10, pady=10)


    def search_images_google(self):
         qstring = urllib.parse.quote(self.textvarimage.get())
         search_url_g = "https://www.google.com/search?tbm=isch&q="+qstring
         webbrowser.open(search_url_g)


    def search_images_images_cc(self):
        qstring = urllib.parse.quote(self.textvarimage.get())
        search_url_c = "https://ccsearch.creativecommons.org/search?q="+qstring
        webbrowser.open(search_url_c)


    def search_images_video_ar(self):
        qstring = urllib.parse.quote(self.textvarimage.get())
        search_url_ar = "https://archive.org/search.php?query=title%3A%28"+qstring+"%29%20AND%20mediatype%3A%28movies%29"
        webbrowser.open(search_url_ar)


    def search_video_google(self):
        qstring = urllib.parse.quote(self.textvarimage.get())
        search_url_g = "https://www.google.com/search?tbm=vid&q=" + qstring
        webbrowser.open(search_url_g)



    def search_def_wiktionary(self):
        qstring = urllib.parse.quote(self.textvarimage.get())
        search_url_w = "http://en.wiktionary.org/w/wiki.phtml?search=" + qstring
        webbrowser.open(search_url_w)






if __name__== "__main__":
        app = MagicSearch()
        app.geometry("1000x150")
        app.configure(background="gray18")



        app.mainloop()

