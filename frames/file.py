from customtkinter import CTkButton, CTkFrame, CTkLabel, filedialog

from utils import get_file_details

__all__ = ('SelectFileFrame', )

class SelectFileFrame(CTkFrame):
    name = "SELECT A PDF"
    selected_file = ""
    file_details = None

    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        self.title = CTkLabel(self, text=self.name, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.pdf_name = CTkLabel(self, text=self.file_name)
        self.pdf_name.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        self.pdf_path = CTkLabel(self, text=self.file_path)
        self.pdf_path.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")

        self.button = CTkButton(self, text=self.name, command=self.button_click)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
    
    @property
    def file_name(self):
        if self.file_details:
            return f"Selected PDF: {self.file_details['name']}"
        else:
            return "No PDF selected"
    
    @property
    def file_path(self):
        path = "PDF Path: "
        return path + self.file_details["path"] if self.file_details else path
    
    def button_click(self):
        if self.selected_file:
            self.remove_file()
        else:
            self.select_file()
    
    def remove_file(self):
        self.selected_file = ""
        self.file_details = None

        self.pdf_name.configure(text=self.file_name)
        self.pdf_path.configure(text=self.file_path)

        self.button.configure(
                text=self.name,
                fg_color="#3a7ebf",
                hover_color="#325882"
            )

    def select_file(self):
        filetypes = (
            ('text files', '*.pdf'),
        )

        file_name = filedialog.askopenfilename(
            title='Open a file',
            initialdir='~/',
            filetypes=filetypes
        )

        if file_name:
            self.selected_file = file_name
            self.file_details = get_file_details(file_name)

            self.pdf_name.configure(text=self.file_name)
            self.pdf_path.configure(text=self.file_path)

            self.button.configure(
                text="REMOVE PDF",
                fg_color="firebrick2",
                hover_color="firebrick3"
            )
