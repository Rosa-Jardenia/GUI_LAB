import flet as ft

def main(page):

    def login(event):

        if not Entrada_Nome.value:
            Entrada_Nome.error_text = "Nome não informado"
          
        if not Entrada_Senha.value:
            Entrada_Senha.error_text = "Senha não informada"
            

        nome = Entrada_Nome.value
        senha = Entrada_Senha.value
        print(f"Nome: {nome}, Senha:{senha}")
        page.clean()
        page.add(ft.Text(value = f"Bem vindo (a), {nome} \n Seja Bem-vindo!" ))
        
        pass

    Entrada_Nome =  ft.TextField(label="NOME:")
    Entrada_Senha = ft.TextField(label="SENHA")

    page.add(
        Entrada_Nome,
        Entrada_Senha,
        ft.ElevatedButton(text="Entrar", on_click= login)
    )
    pass



ft.app(target = main)

