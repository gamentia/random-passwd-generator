import random
import string
from tkinter import *
from tkinter import ttk


class PassGene:


    def __init__(self, master):
        self.master = master
        self.master.title("Random Password Generator")
        self.master.geometry("500x300+400+200")
        self.master.config(bg='#37B884')
        self.master.resizable(False, False)

        self.Sel_lbl = Label(self.master, text="Length of Password: ", font=('', 15, 'bold'), bg='#37B884')
        self.Sel_lbl.place(x=10, y=20)

        self.Pass_sld = Scale(self.master, cursor='cross', from_=5, to=25, tickinterval=2, orient=HORIZONTAL, bd=0, relief='flat')
        self.Pass_sld.set(15)
        self.Pass_sld.place(x=10, y=50, width=480)

        self.Gene_btn = ttk.Button(self.master, text="GENERATE...", command=self.generator)
        self.Gene_btn.place(x=10, y=120, width=480)

        self.Reset_btn = ttk.Button(self.master, text="RESET", command=self.reset)
        self.Reset_btn.place(x=10, y=150, width=480)
        
        self.Randomly_btn = ttk.Button(self.master, text="RANDOMLY", command=self.randomly)
        self.Randomly_btn.place(x=10, y=180, width=480)

        self.Show_lbl = Label(self.master, text='', font=('', 12, 'bold'), bg='#37B884', fg='#503F60')
        self.Show_lbl.place(x=10, y=220, width=480)
        
        self.Creator_lbl = Label(self.master, text="CODE BY: Qamar Imam", font=('', 10, 'bold'), bg='#37B884', fg='#F93016')
        self.Creator_lbl.place(x=340, y=280)
        
        self.save_var = IntVar()
        self.Save_Chec = Checkbutton(self.master, text="Save Password", bg='#37B884', variable=self.save_var)
        self.Save_Chec.place(x=10, y=260, width=100)


    def generator(self):
        all_let = string.ascii_letters + string.digits + string.punctuation

        lst_all = [ ]
        pass_len = int(self.Pass_sld.get())

        while len(lst_all) != pass_len:
            a = random.randint(0,93)

            lst_all.append(all_let[a])

        self.simple(lst_all)


    def simple(self, raw_lst):
        raw_lst = raw_lst
        raw_var = ""

        for i in range(len(raw_lst)):
            if raw_lst[i] != '':
                raw_var += raw_lst[i]
        
        if self.save_var.get() == 1:
            self.update(raw_var)

        self.Show_lbl.config(text=raw_var)


    def update(self, passwd):
        file = open(r'passwd.txt', 'a')
        file.write(passwd)
        file.write('\n')
        file.close()

    
    def reset(self):
        self.Pass_sld.set(15)
        self.Show_lbl.config(text='')
    
    
    def randomly(self):
        pass_len = random.randint(5, 25)
        
        all_let = string.ascii_letters + string.digits + string.punctuation

        lst_all = [ ]

        while len(lst_all) != pass_len:
            a = random.randint(0,93)

            lst_all.append(all_let[a])

        self.Pass_sld.set(pass_len)
        self.simple(lst_all)


def main():
    root = Tk()
    PassGene(root)

    root.mainloop()


if __name__ == '__main__':
    main()
