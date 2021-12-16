import tkinter as tk
from tkinter.filedialog import *
from BioBoot_new import *

len_of_min_spey = 0
len_of_max_spey = 0
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
    title = window.title("Настройки программы CAS Poject")
    window.columnconfigure(1)
    window.rowconfigure(0)

    frame1 = tk.Frame(relief=tk.SUNKEN, borderwidth=3, bg='tomato')
    frame1.grid(row=0, column=0, padx=5, pady=5)

    frame2 = tk.Frame(relief=tk.SUNKEN, borderwidth=3,bg='tomato')
    frame2.grid(row=0, column=1, padx=5, pady=5, sticky='s')

    frame5 = tk.Frame(frame2)
    frame5.pack(side=tk.TOP)

    frame3 = tk.Frame(frame2)
    frame3.pack(side=tk.TOP)

    frame4 = tk.Frame(frame2)
    frame4.pack(side=tk.TOP)

    frame6 = tk.Frame(frame1)
    frame6.grid(row=0, column=1)

    #Отформатировать текст
    text1 = tk.Label(frame1, text='Цель программы заключается в поиске спейсера для системы CRISPR-CAS13b.', bg='tomato')
    text1.grid(sticky="w")
    text2 = tk.Label(frame1, text='Программе выдается FASTA-файл с геномами штаммов вирусов.', bg='tomato')
    text2.grid(sticky="w")
    text3 = tk.Label(frame1, text='На выходе выдается последовательность(и) нуклеотидов спейсера с учетом ', bg='tomato')
    text3.grid(sticky="w")
    text4 = tk.Label(frame1, text='особенностей, указанных в окнах настройки интерфейса. В общем случае это несколько', bg='tomato')
    text4.grid(sticky="w")
    text5 = tk.Label(frame1, text='ответов в виде : спейсер - количество штаммов, у которого он встречается.', bg='tomato')
    text5.grid(sticky="w")
    text6 = tk.Label(frame1, text='Если один спейсер обезвреживает все штаммы, то  выводится только он.  ', bg='tomato')
    text6.grid(sticky="w")
    text7 = tk.Label(frame1, text='Таким образом программа предоставляет пользователю список спейсеров по ', bg='tomato')
    text7.grid(sticky="w")
    text8 = tk.Label(frame1, text='убыванию частоты встречаемости, используя который можно обезвредить все ', bg='tomato')
    text8.grid(sticky="w")
    text9 = tk.Label(frame1, text='выделенные штаммы. Программа эффективно работает для 2-50 штаммов.', bg='tomato')
    text9.grid(sticky="w")
    text11 = tk.Label(frame1, text=' Возможности настройки:', bg='tomato')
    text11.grid(sticky="w")
    text12 = tk.Label(frame1, text='1)Максимальная длина спейсера', bg='tomato')
    text12.grid(sticky="w")
    text13 = tk.Label(frame1, text='2)Минимальная длина спейсера', bg='tomato')
    text13.grid(sticky="w")
    text14 = tk.Label(frame1, text='3)Количество “ошибок” в спейсере', bg='tomato')
    text14.grid(sticky="w")

    #кнопки, отвечающие за загрузку данных и запуск программы
    start_button = tk.Button(master=frame2, text='Запустить\nпрограмму!', bg='firebrick3', command=start_execute, width=20, height=3)
    start_button.pack(side=tk.RIGHT)

    download_button = tk.Button(master=frame2, text='Загрузить файл', bg='firebrick3', command=download_data_from_file, width=20, height=3)
    download_button.pack(side=tk.RIGHT)

    #Min число нукеолтидов в спейсере
    len_of_min_spey = tk.DoubleVar()
    len_of_min_spey.set(3)
    entr1 = tk.Entry(frame3, textvariable=len_of_min_spey)
    entr1.pack(side=tk.RIGHT)

    labe1 = tk.Label(frame3, text='Min нукеолтидов в спейсере', bg='tomato')
    labe1.pack(side=tk.LEFT)

    #Max число нукеолтидов в спейсере
    len_of_max_spey = tk.DoubleVar()
    len_of_max_spey.set(3)
    entr2 = tk.Entry(frame4, textvariable=len_of_max_spey)
    entr2.pack(side=tk.RIGHT)

    labe2 = tk.Label(frame4, text='Max нукеолтидов в спейсере', bg='tomato')
    labe2.pack(side=tk.LEFT)

    #Допускается ошибок
    count_of_missing = tk.DoubleVar()
    count_of_missing.set(1)
    entr3 = tk.Entry(frame5, textvariable=count_of_missing)
    entr3.pack(side=tk.RIGHT)

    labe3 = tk.Label(frame5, text='Данное количество ошибок', bg='tomato')
    labe3.pack(side=tk.LEFT)

    #вставка изображений. Дизайн дисплея
    Virus_image = tk.PhotoImage(file='Viruson5.png')
    Virus_image = Virus_image.subsample(5, 5)
    Virus_label = tk.Label()
    Virus_label.image = Virus_image
    Virus_label['image'] = Virus_label.image
    Virus_label.place(x=680, y=5)

    DNA_image = tk.PhotoImage(file='dna3.png')
    DNA_image = DNA_image.subsample(5, 6)
    DNA_label = tk.Label()
    DNA_label.image = DNA_image
    DNA_label['image'] = DNA_label.image
    DNA_label.place(x=540, y=12)

    window.mainloop()

if __name__ == "__main__":
    main()
