from tkinter import messagebox, simpledialog, Tk
import sys

def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message

def get_task():
    task = simpledialog.askstring('Tarea', 'Quieres encriptar o desencriptar?')
    return task

def get_message():
    message = simpledialog.askstring('Mensaje', 'Introduzca el mensaje: ')
    return message

root = Tk()
root.withdraw()

while True:
    task = get_task()
    if task == 'encriptar':
        message = get_message()
        encriptado = swap_letters(message)
        messagebox.showinfo('Mensaje encriptado: ', encriptado)
    elif task == 'desencriptar':
        message = get_message()
        desencriptado = swap_letters(message)
        messagebox.showinfo('Mensaje desencriptado: ', desencriptado)
    else:
        messagebox.showerror('Error', '[-] Datos no válidos')
        sys.exit(1)
        break

root.mainloop()