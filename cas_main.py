import tkinter as tk
from tkinter.filedialog import *
from BioBoot_new import *

len_of_min_spey = 3
len_of_max_spey = 3
count_of_missing = 1

def download_data_from_file():
    """Открывает диалоговое окно выбора имени файла,
    сохраняет данные входного файла в массив fasta
    """
    global fasta
    input_filename = askopenfilename(filetypes=(("Text file", ".txt"),))

    with open(input_filename) as file:
        fasta = file.readlines()
    fasta = [string_fasta.strip() for string_fasta in fasta]

def start_execute():
    """
    Функция запускается после нажатия на кнопку start_button
    запускает обработку данных, и вызывает диологовое окно
    для сохранения результата, в выбранный файл, например result.txt
    """
    global fasta
    l_spic_min = int(len_of_min_spey.get())
    l_spic_max = int(len_of_max_spey.get())
    missing_can = count_of_missing.get()
    max_spey, speys = execute(fasta, l_spic_min, l_spic_max, missing_can)
    save_data_to_file(max_spey, speys)

def save_data_to_file(max_spey, speys):
    """
    Функция сохраняет данные максимального спейсера, его длины,
    а также другие спейсеры, которые смогла выявить программа той же или меньшей длины
    """
    output_filename = asksaveasfilename(filetypes=(("Text file", ".txt"),))
    with open(output_filename, 'w') as out_file:
        out_file.write("%s\n" % (max_spey))
        out_file.write("%s\n" % (speys))


def main():
    global len_of_min_spey
    global len_of_max_spey
    global count_of_missing

    window = tk.Tk()
    window.columnconfigure(1)
    window.rowconfigure(0)

    frame1 = tk.Frame(relief=tk.SUNKEN, borderwidth=3, bg='light goldenrod')
    frame1.grid(row=0, column=0, padx=5, pady=5)

    frame2 = tk.Frame(relief=tk.SUNKEN, borderwidth=3, bg='light goldenrod')
    frame2.grid(row=0, column=1, sticky='s')

    frame5 = tk.Frame(frame2)
    frame5.pack(side=tk.TOP)

    frame3 = tk.Frame(frame2)
    frame3.pack(side=tk.TOP)

    frame4 = tk.Frame(frame2)
    frame4.pack(side=tk.TOP)

    #Отформатировать текст
    text1 = tk.Label(frame1, text='Цель программы заключается в поиске спейсера для системы CRISPR-CAS13b.', bg='light goldenrod')
    text1.grid(sticky="w")
    text2 = tk.Label(frame1, text='Программе выдается FASTA-файл с геномами штаммов вирусов.', bg='light goldenrod')
    text2.grid(sticky="w")
    text3 = tk.Label(frame1, text='На выходе выдается последовательность(и) нуклеотидов спейсера с учетом ', bg='light goldenrod')
    text3.grid(sticky="w")
    text4 = tk.Label(frame1, text='особенностей, указанных в окнах настройки интерфейса. В общем случае это несколько', bg='light goldenrod')
    text4.grid(sticky="w")
    text5 = tk.Label(frame1, text='ответов в виде : спейсер - количество штаммов, у которого он встречается.', bg='light goldenrod')
    text5.grid(sticky="w")
    text6 = tk.Label(frame1, text='Если один спейсер обезвреживает все штаммы, то  выводится только он.  ', bg='light goldenrod')
    text6.grid(sticky="w")
    text7 = tk.Label(frame1, text='Таким образом программа предоставляет пользователь список спейсеров по ', bg='light goldenrod')
    text7.grid(sticky="w")
    text8 = tk.Label(frame1, text='убыванию частоты встречаемости, используя который можно обезвредить все ', bg='light goldenrod')
    text8.grid(sticky="w")
    text9 = tk.Label(frame1, text='выделенные штаммы. Программа эффективно работает для 2-50 штаммов.', bg='light goldenrod')
    text9.grid(sticky="w")
    text10 = tk.Label(frame1, text='указанных в окнах настройки интерфейса. В общем случае это несколько', bg='light goldenrod')
    text10.grid(sticky="w")
    text11 = tk.Label(frame1, text=' Возможности настройки:', bg='light goldenrod')
    text11.grid(sticky="w")
    text12 = tk.Label(frame1, text='1)Максимальная длина спейсера', bg='light goldenrod')
    text12.grid(sticky="w")
    text13 = tk.Label(frame1, text='2)Минимальная длина спейсера', bg='light goldenrod')
    text13.grid(sticky="w")
    text14 = tk.Label(frame1, text='3)Количество “ошибок” в спейсере (1 либо 0)', bg='light goldenrod')
    text14.grid(sticky="w")

    #кнопки, отвечающие за загрузку данных и запуск программы
    start_button = tk.Button(master=frame2, text='Запустить\nпрограмму!', bg='gold', command=start_execute, width=20, height=3)
    start_button.pack(side=tk.RIGHT)

    download_button = tk.Button(master=frame2, text='Загрузить файл', bg='gold', command=download_data_from_file, width=20, height=3)
    download_button.pack(side=tk.RIGHT)

    #Min число нукеолтидов в спейсере
    len_of_min_spey = tk.DoubleVar()
    len_of_min_spey.set(3)
    entr1 = tk.Entry(frame3, textvariable=len_of_min_spey)
    entr1.pack(side=tk.RIGHT)

    labe1 = tk.Label(frame3, text='Min нукеолтидов в спейсере', bg='light goldenrod')
    labe1.pack(side=tk.LEFT)

    #Max число нукеолтидов в спейсере
    len_of_max_spey = tk.DoubleVar()
    len_of_max_spey.set(3)
    entr2 = tk.Entry(frame4, textvariable=len_of_max_spey)
    entr2.pack(side=tk.RIGHT)

    labe2 = tk.Label(frame4, text='Max нукеолтидов в спейсере', bg='light goldenrod')
    labe2.pack(side=tk.LEFT)

    #Допускается ошибок
    count_of_missing = tk.DoubleVar()
    count_of_missing.set(1)
    entr3 = tk.Entry(frame5, textvariable=count_of_missing)
    entr3.pack(side=tk.RIGHT)

    labe3 = tk.Label(frame5, text='Допускается ошибок', bg='light goldenrod')
    labe3.pack(side=tk.LEFT)

    window.mainloop()

if __name__ == "__main__":
    main()