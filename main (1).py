import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    include_upper = upper_var.get()
    include_lower = lower_var.get()
    include_symbols = symbols_var.get()

    characters = ''
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_symbols:
        characters += string.punctuation

    if not characters:
        password_label.config(text="Выберите хотя бы один тип символов!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text=f"Сгенерированный пароль: {password}")

def copy_to_clipboard():
    root.clipboard_clear()  # Очистить буфер обмена
    root.clipboard_append(password_label.cget("text").replace("Сгенерированный пароль: ", ""))  # Копировать пароль
    root.update()  # Обновить буфер обмена
    copy_status_label.config(text="Пароль скопирован!")

# Создаем основное окно
root = tk.Tk()
root.title("Генератор паролей")

# Длина пароля
length_label = tk.Label(root, text="Длина пароля:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()
length_entry.insert(0, "12")  # Значение по умолчанию

# Включение больших букв
upper_var = tk.BooleanVar()
upper_checkbox = tk.Checkbutton(root, text="Включить большие буквы", variable=upper_var)
upper_checkbox.pack()

# Включение маленьких букв
lower_var = tk.BooleanVar()
lower_checkbox = tk.Checkbutton(root, text="Включить маленькие буквы", variable=lower_var)
lower_checkbox.pack()

# Включение символов
symbols_var = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(root, text="Включить символы", variable=symbols_var)
symbols_checkbox.pack()

# Кнопка генерации пароля
generate_button = tk.Button(root, text="Сгенерировать пароль", command=generate_password)
generate_button.pack()

# Метка для отображения пароля
password_label = tk.Label(root, text="")
password_label.pack()

# Кнопка для копирования пароля
copy_button = tk.Button(root, text="Скопировать пароль", command=copy_to_clipboard)
copy_button.pack()

# Метка для статуса копирования
copy_status_label = tk.Label(root, text="")
copy_status_label.pack()

# Запуск основного цикла приложения
root.mainloop()