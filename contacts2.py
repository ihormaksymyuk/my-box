
import tkinter as tk
from tkinter import RIGHT, VERTICAL, ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename 
from tkinter import *
from encodings import utf_8
import re
import sqlite3
ss = "id"

def main():
    #tk.iconbitmap("srch.ico")
    window = tk.Tk()
    #window.iconbitmap('doc.ico')
    window.title("Контакти")

    
    # Создается новая рамка `frm_form` для ярлыков с текстом и
    # Однострочных полей для ввода информации об адресе.
    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    # Помещает рамку в окно приложения.
    frm_form.pack()
    
    #frame1 = tk.Frame(master=window, height=50, bg="light gray")
    #frame1.pack(fill=tk.X)

    frame2 = tk.Frame(master=window, height=50, bg="gray")
    frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    lbl_first_name = tk.Label(master=frm_form, text="Програма відкриває файл VCF та зберігає список контактів в TXT форматі")
    lbl_first_name.grid(row=0, column=0, sticky="e")
    
    global i
    
        #print(s)
    
    def open_dir():
        global ss
        print(ss)
        filepath = askopenfilename(
            filetypes=[("vcf файли", "*.vcf"), ("Всі файли", "*.*")]
        )
        if not filepath:
            return
        result.delete("1.0", tk.END)
        with open(filepath, "r",encoding='utf_8') as file:
            name =()
            phone = ()
            email = ()
            adress = []
            adress1 = []
            
            i=1
            for line in file:  
                if re.match('FN:', line):
                    n=line.find(':')
                    name=line[n+1:-1] 
                    adress.append(name)
                    i += 1
                if re.match('FN:\n', line):
                    continue              
                if re.match('NICKNAME', line):
                    n=line.find(':')
                    name=line[n+1:-1] 
                    adress.append(name)
                if re.match('TEL', line):
                    n=line.find(':')
                    phone='телефон' + line[n:-1]
                    adress.append(phone)
                if re.match('EMAIL', line):
                    n=line.find(':')
                    email='пошта' + line[n:-1]
                    adress.append(email)
                if re.match('END:VCARD', line):   
                    adress1.append(adress)
                    adress = []
            global adress3  
            adress3=[]
            for line in adress1:
                if line[0] == '':
                    line.remove('')
                a=0
                for j in line:
                    a += 1
                s = " "
                if a == 0:
                    continue
        
                if a == 1:
                    line.append(s)
                    line.append(s)
                    line.append(s)
                if a == 2:
                    line.append(s)
                    line.append(s)
                if a == 3:
                    line.append(s)
                if a == 5:
                    line.pop()
    
                b=0
                for d in line:
                    b += 1
                adress2=tuple(line)
                adress3.append(adress2)
            #print(adress3)


                #result.insert(tk.END, adress2)
                #result.insert(tk.END, '\n')
            
            window.title(f"Контакти - {filepath}")

        with sqlite3.connect(":memory:") as db:
            cursor=db.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS my_contakts(
                id INTEGER PRIMARY KEY AUTOINCREMENT ,
                name VARCHAR,
                telephone VARCAR,
                telephone_email VARCAR,
                email VARCAR   
            )""")
           
            #print(s)
            #cursor.executemany("INSERT INTO my_contakts(name, telephone,telephone_email,email) VALUES(?,?,?,?)",adress3)
            if   ss == "id":
                cursor.executemany("INSERT INTO my_contakts(name, telephone,telephone_email,email) VALUES(?,?,?,?)",adress3)
                for data in cursor.execute("SELECT * FROM my_contakts ORDER BY id"):
                #print(data)
                    data1 = str(data)
                    data2=data1.replace("(", "")
                    data3=data2.replace(")", "")
                    data4=data3.replace("'", "")
                    data5=data4.replace("  ,", "")
                    data6=data5.replace(",", ".",1)
                    #print(data5)
                
                    result.insert(tk.END,data6)
                    result.insert(tk.END, '\n')
            
                 
                
    #directory.insert(0, s_directory)
    # Использует менеджер геометрии grid для размещения ярлыка и
    # однострочного поля для ввода текста в первый и второй столбец
    # первой строки сетки.
    

    def sort_a():
        with sqlite3.connect(":memory:") as db:
            cursor=db.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS my_contakts1(
                
                name VARCHAR,
                telephone VARCAR,
                telephone_email VARCAR,
                email VARCAR   
            )""")
        cursor.executemany("INSERT INTO my_contakts1(name, telephone,telephone_email,email) VALUES(?,?,?,?)",adress3)
        n=1
        for data in cursor.execute("SELECT * FROM my_contakts1 ORDER BY name"):
            data1 = str(data)
            data2=data1.replace("(", "")
            data3=data2.replace(")", "")
            data4=data3.replace("'", "")
            data5=data4.replace("  ,", "")
            data6=data5.replace(",", ".",1)
            result.insert(tk.END,n)
            result.insert(tk.END,". ")
            result.insert(tk.END,data6)
            result.insert(tk.END, '\n')
            n += 1
    result = tk.Text(master=frame2)
    scr = ttk.Scrollbar(master=frame2, orient=VERTICAL, command=result.yview )
    scr.pack(side=RIGHT, fill='y')
    result.configure(yscrollcommand=scr.set)
    result.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    result.bind('<Configure>', lambda e: result.configure(scrollregion=result.bbox("all")))

    def clear_all():
        result.delete("1.0","end")
    
        
    frm_buttons = tk.Frame()
    
    frm_buttons.pack(fill=tk.X, ipadx=0, ipady=5)
    
    
               
                    
                  

    

    
    def save_file():
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Текстові файли", "*.txt"), ("Всі файли", "*.*")],)
        if not filepath:
            return
        with open(filepath, "w",encoding='utf_8') as output_file:
            text = result.get("1.0", tk.END)
            output_file.write(text)
        window.title(f"Простий пошук файлів - {filepath}")
        
    

    my_menu = Menu(window)
    window.config(menu=my_menu)
    file_menu = Menu(my_menu,tearoff=0)
    file_menu.add_command(label="Відкрити VCF файл", command=open_dir)
    file_menu.add_command(label="Зберегти як...", command=save_file)
    my_menu.add_cascade(label="Файл", menu=file_menu)

    edit_menu = Menu(my_menu,tearoff=0)
    edit_menu.add_command(label="Очистити", command=clear_all)
    edit_menu.add_command(label="Відсорувати в алфавітному порядку", command=sort_a)
    my_menu.add_cascade(label="Редагувати", menu=edit_menu)
    
    

    window.mainloop()
    

main()
    
