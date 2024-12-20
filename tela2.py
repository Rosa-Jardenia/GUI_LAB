import flet as ft




def main(page):

    def login(e):
        nome = EntradaNome.value
        senha = EntradaSenha.value
        


    EntradaNome =  ft.TextField(label="NOME:")
    EntradaSenha = ft.TextField(label="SENHA")

    page.add(
        EntradaNome,
        EntradaSenha,
        ft.ElevatedButton(text="Entrar", on_click= "login")
    )
    pass



