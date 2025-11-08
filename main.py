import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Мое первое предложение'
    greeting_text = ft.Text("Hello world")
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_history  = []
    history_text = ft.Text('История приветстий:')



    def on_button_click(_):
        name = name_input.value.strip() #type: ignore
        # print(name)

        # print(greeting_text.value)
        timestamp = datetime.now().strftime("%H:%M")
        if name:
           greeting_text.value = f"{timestamp}Hello {name}"
           name_input.value = ""

        #  greeting_history.append(timestamp + "-" + name)
           greeting_history.append(f"{timestamp} - {name}")
           history_text.value = f"История приветствий: \n" + f"\n.join(greeting_history)"
        else:
            greeting_text.value = "Введите коректное имя"
            greeting_text.color = ft.Colors.RED
        # print(greeting_text.value)

        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)
    name_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, on_click=on_button_click)

    def clear_history(_):
        print(greeting_history)
        greeting_history.clear()
        print(greeting_history)
        history_text.value = 'История приветствий:'
        page.update()


    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    def theme_mode(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()

    theme_mode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=theme_mode)

    # name_button_text = ft.TextButton('send')
    # name_button_icon = new_func()

    page.add(greeting_text, name_input, name_button, clear_button, theme_mode_button)


ft.app(target=main, view=ft.WEB_BROWSER) #type: ignore









