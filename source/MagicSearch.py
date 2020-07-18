import logging
import sys
import tkinter as tk
from tkinter import ttk
import webbrowser
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
        s.configure('BlueSearch.TButton', background='steel blue', foreground='white', font=('helvetica', 12, 'bold'))

        s.map('BlueSearch.TButton', background=[('active', '!disabled', 'dark turquoise'), ('pressed', 'white')],
              foreground=[('pressed', 'white'), ('active', 'white')])

        self.search_button = ttk.Button(self, text="Search Images",

                                      command=self.search_images, style="BlueSearch.TButton")
        self.search_button_v = ttk.Button(self, text="Search Videos",

                                        command=self.search_videos, style="BlueSearch.TButton")
        self.search_label = tk.Label(self,
                                    borderwidth=3, highlightcolor="gray18", width=20,
                                    text="Search Text",
                                    font=("Helvetica", 14, 'bold'), background=BOX_BACKGROUND_COLOR,
                                    foreground=BOX_FOREGROUND_COLOR)
        self.search_label_help = tk.Label(self,
                                     borderwidth=3, highlightcolor="gray18",
                                     text="Requires Internet - Opens google and Creative Commons for Image Search."
                                          "Opens google and Internet Archive for Video Search.",
                                     font=("Helvetica", 11, 'bold'), background=BOX_BACKGROUND_COLOR,
                                     foreground='Aquamarine')
        self.textvarimage = tk.StringVar()
        self.search_entry = tk.Entry(self,width=50,textvariable=self.textvarimage)
        self.search_label.grid(row=0,column=0,padx=10,pady=10)
        self.search_entry.grid(row=0, column=1,padx=15,pady=10)
        self.search_button.grid(row=0, column=2,padx=15,pady=10)
        self.search_button_v.grid(row=0, column=3, padx=15,pady=10)
        self.search_label_help.grid(row=1, column=0,columnspan=4,padx=10, pady=10)


    def search_images(self):
         search_url_g = "https://www.google.com/search?tbm=isch&q="+self.textvarimage.get()
         search_url_c = "https://ccsearch.creativecommons.org/search?q="+self.textvarimage.get()

         webbrowser.open(search_url_g)
         webbrowser.open(search_url_c)


    def search_videos(self):
        search_url_g = "https://www.google.com/search?tbm=vid&q=" + self.textvarimage.get()
        search_url_ar = "https://archive.org/search.php?query=title%3A%28"+self.textvarimage.get()+"%29%20AND%20mediatype%3A%28movies%29"
        webbrowser.open(search_url_g)
        webbrowser.open(search_url_ar)





if __name__== "__main__":
        app = MagicSearch()
        app.geometry("1000x150")
        app.configure(background="gray18")



        app.mainloop()

