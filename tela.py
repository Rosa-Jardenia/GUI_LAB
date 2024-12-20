import flet as f

def main (page: f.Page):
    ola = f.Text(value = "Olá, Mundo!", size = 30 , color = "red", weight = "bold")
    page.controls.append(ola)
    page.update()


f.app(target = main)