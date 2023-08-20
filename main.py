import customtkinter

from frames import AddKeyWordsFrame, SelectedKeywordsFrame, SelectFileFrame


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("PDF Redact")
        self.geometry("600x450")
        self.grid_columnconfigure((0, 1), weight=1, uniform="column")
        self.grid_rowconfigure(0, weight=1)


        self.select_file_frame = SelectFileFrame(self)
        self.select_file_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.add_keywords_frame = AddKeyWordsFrame(self)
        self.add_keywords_frame.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")

        self.show_keywords_frame = SelectedKeywordsFrame(self)
        self.show_keywords_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")


app = App()
app.resizable(False, False)
app.mainloop()
