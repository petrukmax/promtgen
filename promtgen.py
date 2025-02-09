import tkinter as tk
from tkinter import scrolledtext
import tkinter.scrolledtext as st
import pyperclip


def create_and_copy():
    # Получаем текст из всех трех текстовых областей
    text1 = text_area1.get("1.0", "end-1c").strip().split("\n")
    text2 = text_area2.get("1.0", "end-1c").strip().split("\n")
    text3 = text_area3.get("1.0", "end-1c").strip().split("\n")

    max_len = max(len(text1), len(text2), len(text3))
    
    result_lines = []
    for i in range(max_len):
        line1 = text1[i % len(text1)] if text1 else ""
        line2 = text2[i % len(text2)] if text2 else ""
        line3 = text3[i % len(text3)] if text3 else ""

        # Объединяем строки с пробелами и добавляем их в список
        combined_line = f"{line1} {line2} {line3}".strip()
        result_lines.append(combined_line)

    # Объединяем все строки через новую строку
    result_text = "\n".join(result_lines)
    pyperclip.copy(result_text)  # Копируем результат в буфер обмена
    print("Текст скопирован в буфер обмена:\n", result_text)


# Создание основного окна
root = tk.Tk()
root.title("Создать/Скопировать")
root.geometry("600x400")  # Начальный размер окна

# Настройка сетки для растяжения элементов
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Фрейм для текстовых областей
frame_text_areas = tk.Frame(root)
frame_text_areas.grid(row=0, column=0, sticky="nsew")

# Три текстовые области
text_area1 = st.ScrolledText(frame_text_areas, wrap=tk.WORD)
text_area2 = st.ScrolledText(frame_text_areas, wrap=tk.WORD)
text_area3 = st.ScrolledText(frame_text_areas, wrap=tk.WORD)

# Размещение текстовых областей в фрейме
text_area1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
text_area2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
text_area3.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

# Настройка столбцов для растяжения текстовых областей
frame_text_areas.grid_columnconfigure(0, weight=1)
frame_text_areas.grid_columnconfigure(1, weight=1)
frame_text_areas.grid_columnconfigure(2, weight=1)
frame_text_areas.grid_rowconfigure(0, weight=1)

# Кнопка
button = tk.Button(root, text="Создать/Скопировать", command=create_and_copy)
button.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

# Запуск главного цикла
root.mainloop()