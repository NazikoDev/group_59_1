import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Мое первое предложение"
    greeting_text = ft.Text("Hello world")
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_history = []
    history_text = ft.Text("История приветствий:")

    with open("history.txt", "r", encoding="utf-8") as file:
        for line in file.readlines():
            greeting_history.append(line.strip())
    if greeting_history:
        history_text.value = "История приветствий:\n" + "\n".join(greeting_history)

    def update_history_display(history_list):
        if history_list:
            history_text.value = "История приветствий:\n" + "\n".join(history_list)
        else:
            history_text.value = "История приветствий:"
        page.update()

    def on_button_click(_):
        name = name_input.value.strip() #type: ignore
        timestamp = datetime.now().strftime("%H:%M")
        if name:
            greeting_text.value = f"{timestamp} Hello {name}"
            name_input.value = ""
            entry = f"{timestamp} - {name}"
            greeting_history.append(entry)
            with open("history.txt", "a", encoding="utf-8") as file:
                file.write(entry + "\n")
            update_history_display(greeting_history)
        else:
            greeting_text.value = "Введите корректное имя"
            greeting_text.color = ft.Colors.RED
        page.update()

    name_input = ft.TextField(label="Введите имя", on_submit=on_button_click)
    name_button = ft.ElevatedButton("send", icon=ft.Icons.SEND, on_click=on_button_click)

    def clear_history(_):
        greeting_history.clear()
        with open("history.txt", "w", encoding="utf-8") as file:
            file.write("")
        update_history_display(greeting_history)

    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    def theme_mode(_):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.update()

    theme_mode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=theme_mode)

    def show_morning(_):
        morning = []
        for h in greeting_history:
            if int(h.split(":")[0]) < 12:
                morning.append(h)
        update_history_display(morning)

    def show_evening(_):
        evening = []
        for h in greeting_history:
            if int(h.split(":")[0]) >= 12:
                evening.append(h)
        update_history_display(evening)

    morning_button = ft.ElevatedButton("Показать утренние", on_click=show_morning)
    evening_button = ft.ElevatedButton("Показать вечерние", on_click=show_evening)

    page.add(greeting_text, name_input, name_button, clear_button, theme_mode_button, morning_button, evening_button, history_text)

ft.app(target=main)

