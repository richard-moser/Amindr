import tkinter as tk
from tkinter import filedialog
import os

from txt_to_df import txt_to_df
from instructions import instructions
from utils import open_file

import pandas as pd


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cwd = os.path.dirname(os.path.abspath(__file__))
        self.filename=""
        self.df = pd.DataFrame()

        self.title("My Tkinter App")
        self.geometry("800x500")

        # Create and place widgets here
        self.instruction = tk.Label(self, text=instructions, justify="left")
        self.instruction.pack()

        self.info = tk.Label(self, text="")
        self.info.pack()

        self.modify_categories_button = tk.Button(self, text="modify category definitions", command=self.edit_categories)
        self.modify_categories_button.pack()

        self.select_file_button = tk.Button(self, text="select .txt file", command=self.select_file)
        self.select_file_button.pack()

        self.load_content_button = tk.Button(self, text="load content from file", command=self.load_data)
        self.load_content_button.pack()
        
        self.save_csv_button = tk.Button(self, text="save as .csv-file", command=self.save_csv)
        self.get_labels_button = tk.Button(self, text="get labels", command=self.get_labels)

    def select_file(self):
        self.filename = filedialog.askopenfilename(initialdir=self.cwd)
        if self.filename:
            self.info.config(text="Selected file: {}".format(self.filename))

    def load_data(self):
        if self.filename=="":
            self.info.config(text="Please select a .txt file")
            return
        self.info.config(text="Loading data from {}".format(self.filename))
        self.load_content_button.config(text="Loading...", state=tk.DISABLED)
        self.df = txt_to_df(self.filename)
        print(self.df[:2])
        self.info.config(text = "Data successfully loaded")
        self.load_content_button.pack_forget()
        self.select_file_button.pack_forget()
        self.save_csv_button.pack()
        self.get_labels_button.pack()


    def get_labels(self):
        pass








    def save_csv(self):
        folder_path = filedialog.askdirectory(initialdir=self.cwd)
        self.df.to_csv(folder_path +'output.csv', index=False)

    def edit_categories(self):
        open_file("labels.py")
        pass















# folder_path = filedialog.askdirectory()



if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
