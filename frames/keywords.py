from customtkinter import (CTkButton, CTkCheckBox, CTkEntry, CTkFrame,
                           CTkLabel, CTkTextbox)

__all__ = ('AddKeyWordsFrame', 'SelectedKeywordsFrame')


class AddKeyWordsFrame(CTkFrame):
    name = "ADD KEY WORDS"
    state = "normal"
    color = "chartreuse3"

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.title = CTkLabel(self, text=self.name, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.entry = CTkEntry(self, placeholder_text="Keyword")
        self.entry.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.checkbox_1 = CTkCheckBox(self, text="Case Sensitive")
        self.checkbox_1.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_2 = CTkCheckBox(self, text="Full Text Search")
        self.checkbox_2.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")

        self.button = CTkButton(self, text="Add keyword", command=self.button_callback, fg_color="chartreuse3", hover_color="chartreuse4")
        self.button.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        # self.button.configure(state="disabled", fg_color="chartreuse4")
        pass


class SelectedKeywordsFrame(CTkFrame):
    name = "SELECTED KEY WORDS"

    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.title = CTkLabel(self, text=self.name, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.textbox = CTkTextbox(master=self, corner_radius=0)
        self.textbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.textbox.insert("0.0", "Some example text!\n" * 50)
