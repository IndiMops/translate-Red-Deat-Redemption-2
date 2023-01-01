from customtkinter import *

set_appearance_mode('System')
set_default_color_theme('dark-blue')

app_with = 500
app_height = 450
app_bg = '#282c34'


class App(CTk):
    def __init__(self):
        super().__init__()
        self.app_with = 500
        self.app_height = 450
        self.app_title = 'Тестова програма'
        self.text_label = 0
        self.geometry(f'{self.app_with}x{self.app_height}')

        self.frame = CTkFrame(master=self)
        self.frame.pack(pady=20, padx=60, fill='both', expand=True)

        self.label = CTkLabel(master=self.frame, text='Увійдіть в систему', font=('Arial', 24))
        self.label.pack(pady=12, padx=10)

        self.entry1 = CTkEntry(master=self.frame, placeholder_text='Логін')
        self.entry1.pack(pady=12, padx=10)

        self.entry2 = CTkEntry(master=self.frame, placeholder_text='Пароль', show='*')
        self.entry2.pack(pady=12, padx=10)

        self.button = CTkButton(master=self.frame, text='Увійти', command=self.login)
        self.button.pack(pady=12, padx=10)

        self.checkbox = CTkCheckBox(master=self.frame, text='Запам\'ятати мене')
        self.checkbox.pack(pady=12, padx=10)

        self.appearance_mode_label = CTkLabel(self.frame, text=self.text_label, anchor="w")
        self.appearance_mode_label.pack(pady=12, padx=10)
        self.appearance_mode_optionemenu = CTkOptionMenu(
            self.frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event
        )
        self.appearance_mode_optionemenu.pack(padx=20, pady=(10, 10))
        self.appearance_mode_optionemenu.set("Dark")

    @staticmethod
    def change_appearance_mode_event(new_appearance_mode: str):
        set_appearance_mode(new_appearance_mode)

    def login(self):
        print(self.text_label)
        self.text_label += 1


if __name__ == '__main__':
    app = App()
    app.mainloop()
