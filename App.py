import pandas as pd
from sqlalchemy import create_engine, update, Table, MetaData
from txt_to_df import txt_to_df
import tkinter as tk
from tkinter import filedialog
import os
from utils import open_file, instructions
from get_categories import Categorizer


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        super().configure(bg='white')
        self.engine = create_engine('sqlite:///publications.db')

        self.cwd = os.path.dirname(os.path.abspath(__file__))
        self.filename=""
        self.df = pd.DataFrame()

        self.title("Amindr labelling tool")
        self.geometry("800x500")

        # Create and place widgets here
        self.instruction = tk.Label(self, text=instructions, justify="left", bg='white')
        self.instruction.pack()

        self.info = tk.Label(self, text="", bg='white')
        self.info.pack()

        self.modify_categories_button = tk.Button(self, text="modify category definitions", command=self.edit_categories)
        self.modify_categories_button.pack()

        self.check_APIkey_button = tk.Button(self, text="Check API Key", command=self.check_API_Key)
        self.check_APIkey_button.pack()

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
        num_publications = self.df.shape[0]
        print(self.df[:2])
        self.df.to_sql('publications', con=self.engine, if_exists='replace', index=False)
        self.info.config(text = "Successfully loaded data from "+str(num_publications)+" publications")
        self.load_content_button.pack_forget()
        self.select_file_button.pack_forget()
        self.save_csv_button.pack()
        self.get_labels_button.pack()


    def get_labels(self):
        num_publications = self.df.shape[0]
        self.info.config(text="Getting the categories of "+str(num_publications)+" publications. This takes one second per publication.")
        self.get_labels_button.config(text="Loading...", state=tk.DISABLED)
        categorizer = Categorizer()
        categorizer.get_categories()
        remaining_publications = categorizer.get_unlabeled_publications()
        self.info.config(text = "Got labels for "+ str(num_publications-remaining_publications)+ " out of " + str(num_publications) + " publications")
        if remaining_publications == 0:
            self.get_labels_button.pack_forget()
        else:
            self.get_labels_button.config(text="Get the other labels", state=tk.ACTIVE, command=self.get_labels)

    def save_csv(self):
        self.df = pd.read_sql_query("SELECT * FROM publications", self.engine)
        folder_path = filedialog.askdirectory(initialdir=self.cwd)
        self.df.to_csv(folder_path +'/new_publications.csv', index=False)
        self.info.config(text="File successfully saved")

    def edit_categories(self):
        open_file("labels_all.py")
    
    def check_API_Key(self):
        path = self.cwd + "/.env"
        if os.path.exists(path):
            open_file(".env")
        else:
            with open(path, 'w') as f:
                f.write("GEMINI_KEY = \"\" #insert API key here")











if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
