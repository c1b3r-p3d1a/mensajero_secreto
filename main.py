from tkinter import messagebox, simpledialog, Tk
import sys
import time

def mecanografiar_texto(texto_a_mecanografiar):
    texto_a_mecanografiar_convertido_a_lista = texto_a_mecanografiar.split()
    for palabra in texto_a_mecanografiar_convertido_a_lista:
        print(palabra, end="")
        time.sleep(.2)



def _header_():
	print ('\033[1;31m')
	print (r"""
    cccc   i   bbbb    eeeeee   rrrrrrr
   cc      i   b   b   eeeeee   rr   rrr
   cc      i   b b     eee      rrrrrr      ------   P3d1A
   cc      i   b   b   eeeeee   rr rrrr
    cccc   i   bbbb    eeeeee   rr  rrr                                                                    """)

print ('\033[0m')

_header_()

print("")
print ('\033[1;31m')
mecanografiar_texto("[+] A b r i e n d o . . .")
print ('\033[0m')

time.sleep(1)

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
        print('\033[1;31m')
        print (r"""[-] Cerrando...""")
        print('\033[0m')
        time.sleep(1)
        sys.exit(1)
        break

root.mainloop()
