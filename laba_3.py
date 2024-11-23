import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import pygame


def shift_block(block, shift):
    all_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    new_block = ""
    for char in block:
        if char in all_chars:
            index = (all_chars.index(char) + shift) % len(all_chars)
            new_block += all_chars[index]
    return new_block


def generate_key():
    block_1 = entry_block_1.get().upper()

    if len(block_1) != 5 or not all(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" for c in block_1):
        messagebox.showerror("Ошибка", "Введите первую часть ключа (5 символов A-Z, 0-9)")
        return


    block_2 = shift_block(block_1, 3)
    block_3 = shift_block(block_1, -5)


    generated_key = f"{block_1}-{block_2}-{block_3}"
    entry_key.delete(0, tk.END)
    entry_key.insert(0, generated_key)


    start_animation_and_music()


def start_animation_and_music():
    global direction
    direction = "right"
    move_text()
    play_music()


def move_text():
    global x_position, direction

    if direction == "right":
        x_position += 5
        if x_position >= 200:
            direction = "left"
    elif direction == "left":
        x_position -= 5
        if x_position <= 50:
            direction = "right"


    play_label.place(x=x_position, y=200)


    root.after(40, move_text)


def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("GTA San Andreas - Main Theme.mp3")
    pygame.mixer.music.play(-1)


root = tk.Tk()
root.title("GTA")
root.geometry("400x300")


my_image = Image.open("GTA_SanAndreas.jpg")
my_image = my_image.resize((400, 300))
my_photo = ImageTk.PhotoImage(my_image)


my_label = tk.Label(root, image=my_photo)
my_label.place(x=0, y=0, relwidth=1, relheight=1)


label_block_1 = tk.Label(root, text="1 блок ключа:", bg="white")
label_block_1.place(x=50, y=50)


entry_block_1 = tk.Entry(root, width=10)
entry_block_1.place(x=200, y=50)


label_key = tk.Label(root, text="Сгенерированный ключ:", bg="white")
label_key.place(x=50, y=100)


entry_key = tk.Entry(root, width=25)
entry_key.place(x=200, y=100)


button_generate = tk.Button(root, text="Сгенерировать", command=generate_key)
button_generate.place(x=150, y=150)


x_position = 50
play_label = tk.Label(root, text="PLAY", font=("Times New Roman", 28), fg="white", bg="black")
play_label.place(x=x_position, y=200)


direction = "right"

root.mainloop()

pygame.mixer.music.stop()
