
import flet as ft
import flet_material as fm
import asyncio
#import cx_Oracle




PRIMARY = "teal"
BG = '#8A2BE2'
FWG = '#97b4ff'
FG = '#3450a1'
PINK = '#eb06ff'

fm.Theme.set_theme(theme=PRIMARY)

dummy_user_list: list = [["admin", "admin"]]

class CustomInputfield(ft.UserControl):
    def __init__(self, password: bool, title: str):
        self.input: ft.Control = ft.TextField(
            height=45,
            ###
            border_color="#bbbbbb",
            border_width=0.6,
            cursor_height=14,
            cursor_width=1,
            cursor_color="white",
            color="white",
            text_size=13,
            ###
            bgcolor=fm.Theme.bgcolor,
            password=password,
            on_focus= lambda e: self.focus_shadow(e),
            on_blur= lambda e: self.blur_shadow(e),
            on_change= lambda e: self.set_loader_animation(e)
        )

        self.input_box: ft.Container = ft.Container(
            expand=True,
            content=self.input,
            animate=ft.Animation(300, "ease"),
            shadow=None,
        )

        self.loader: ft.Control = ft.ProgressBar(
            value=0,
            bar_height=1.25,
            color=PRIMARY,
            bgcolor="transparent",
        )

        self.status: ft.Control = fm.CheckBox(
            shape="circle",
            value=False,
            disabled=True,
            offset=ft.Offset(1,0),
            bottom=0,
            right=1,
            top=1,
            animate_opacity=ft.Animation(200,"linear"),
            animate_offset=ft.Animation(350, "ease"),
            opacity=0,
        )

        self.object = self.create_input(title)

        super().__init__()

    async def set_ok(self):
        self.loader.value = 0
        self.loader.update()

        self.status.offset = ft.Offset(-0.5,0)
        self.status.opacity=1
        self.update()

        await asyncio.sleep(1)

        self.status.content.value = True
        self.status.animate_checkbox(e=None)
        self.status.update()

    def set_loader_animation(self, e):
        if len(self.input.value) != 0:
            self.loader.value = None
        else:
            self.loader.value = 0

        self.loader.update()
            

    def blur_shadow(self, e):
        self.input_box.shadow = None
        #self.input.border_color = "#eb06ff"
        self.input.border_color = "#bbbbbb"
        self.update()
        self.set_loader_animation(e=None)
    
    def focus_shadow(self, e):
        self.input.border_color = PRIMARY
        self.input_box.shadow= ft.BoxShadow(
            spread_radius=6,
            blur_radius=8,
            color=ft.colors.with_opacity(0.25, "black"),
            offset=ft.Offset(4,4),
        )
        self.update()
        self.set_loader_animation(e=None)

    def create_input(self, title):
        return ft.Column(
            spacing=5,
            controls=[
                ft.Text(title, size=11, weight="bold", color="white"),
                ft.Stack(
                    controls=[
                        self.input_box, 
                        self.status,
                    ],
                ),
                self.loader,
            ],
        )
    
    def build(self):
        return self.object

class MainFormUI(ft.UserControl):
    def __init__(self):

        self.email = CustomInputfield(False, "Email")
        self.password = CustomInputfield(True, "Password")

        self.submit = ft.ElevatedButton(
            width=400,
            height=45,
            text="Confirmar",
            on_click=lambda e: asyncio.run(self.validate_entries(e))
        )

        

        super().__init__()

    async def validate_entries(self, e):
        email_value = self.email.input.value
        password_value = self.password.input.value

        for user, password in dummy_user_list:
            if email_value == user and password_value == str(password):              
                await self.email.set_ok()                
                await self.password.set_ok()
                self.update()


    
    def build(self):
        return ft.Container(
            #theme=ft.Theme(color_scheme_seed=ft.colors.PURPLE_900),
            #theme_mode=ft.ThemeMode.DARK,
            width=450,
            height=550,
            bgcolor=ft.colors.with_opacity(0.01, "white"),
            border_radius=10,
            padding=40,
            content=ft.Column(
                horizontal_alignment="center",
                alignment="center",
                controls=[
                    ft.Text(
                        "RPA",
                        size=21,
                        weight="w800", color=ft.colors.with_opacity(0.85, "white"),
                    ),
                    ft.Text(
                        "Gerenciador de Reminders",
                        size=21,
                        weight="w800", color=ft.colors.with_opacity(0.85, "white"),
                    ),
                    ft.Divider(height=25, color="transparent"),
                    self.email,
                    ft.Divider(height=5, color="transparent"),
                    self.password,
                    ft.Divider(height=25, color="transparent"),
                    self.submit,
                    

                ],
            ),
        )






def main(page: ft.Page):   
    #page.bgcolor = fm.Theme.bgcolor
    page.bgcolor = BG
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    form = MainFormUI()
    page.add(form)
    page.update()

if __name__ == "__main__":
    ft.flet.app(target=main)