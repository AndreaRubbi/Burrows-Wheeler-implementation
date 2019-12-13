from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk

def called():
    def rotations(t):
        tt = t*2
        return [ tt[ i : i+len(t) ] for i in range(0, len(t)) ]

    def bwm(t):
        return sorted(rotations(t))

    def bwt(Bwm):
        return ''.join(map(lambda x: x[-1], Bwm))

    def reverse(Bwt):
        n={x:Bwt.count(x) for x in Bwt}
        num= sorted([[x,n[x]] for x in n])
        s = [x[0] for x in num]
        e = Bwt[0]
        seq = e
        row = 0
        while e != '$' :
            count = 0
            x = 0
            q = s.index(e)
            while x < q:
                count += num[x][1]
                x += 1
            p = Bwt[ : row]
            row = p.count(e) + count
            e = Bwt[row]
            seq += e        
        return(seq[::-1])

    def search(query, Bwm):
        query = query[::-1]
        F = ''.join(map(lambda x: x[0], Bwm))
        L = ''.join(map(lambda x: x[-1], Bwm))
        o = {x:L.count(x) for x in L}
        num = sorted([[x,o[x]] for x in o])
        p = [x[0] for x in num]
        if len(query) == 1:
            c = F.count(query)
            print(c , ' matches founded')
            return 
        search_space = [x for x in range(len(F))]
        for x in range(len(query)-1):
            step = []
            for y in search_space:
                if F[y] == query[x]:
                    step.append(y)
            search_space = []
            for j in step:
                if L[j] == query[x+1]:
                    let = L[j]
                    s = L[:j]
                    n = s.count(let)
                    ind = p.index(let)
                    d = 0
                    while d < ind:
                        n += num[d][1]
                        d += 1
                    search_space.append(n)     
            if len(search_space) == 0:
                print('Pardon, no match found')
                return
        range_set = []
        for x in search_space:
            y = 0
            while Bwm[x][y] != '$':
                y += 1
            range_set.append(len(F)-y-1)
        label4.configure(text= "You're lucky: "+ str(len(search_space)) + ' matches founded')
        label5.configure(text= 'Indexes: '+ str(sorted(range_set)) )
    
    finestra = Tk()
    finestra.title('BWM-BWT')
    tab_control = ttk.Notebook(finestra)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)
    tab_control.add(tab1, text = 'Input')
    tab_control.add(tab2, text = 'BWM_BWT')
    tab_control.add(tab3, text = 'Matches')

    label1 = Label(tab1, text='Reference sequence:', font = ('Arial',10), fg = 'green')
    label2 = Label(tab1, text='Query sequence:', font = ('Arial',10), fg = 'green')
    label1.grid(row=0,column=0)
    label2.grid(row=1,column=0)
    inp1 = Entry(tab1,width = 20,font = ('Arial',10),fg = 'blue')
    inp2 = Entry(tab1,width = 20,font = ('Arial',10),fg = 'blue')
    inp1.grid(row=0,column=1)
    inp2.grid(row=1,column=1)

    txt = scrolledtext.ScrolledText(tab2,width=40,height=10, font = ('Arial',10), fg = 'blue')
    txt.grid(column=0,row=3)

    label3 = Label(tab2, font = ('Arial',10), fg = 'blue')
    label4 = Label(tab3, font = ('Arial',10), fg = 'blue')
    label5 = Label(tab3, font = ('Arial',10), fg = 'blue')
    label3.grid(row=3,column=1)
    label4.grid(row=0,column=0)
    label5.grid(row=1,column=0)

    def main():
        seq = inp1.get()
        seq = '$' + seq
        Bwm = bwm(seq)
        Bwt = bwt(Bwm)
        result = (Bwm, Bwt , reverse(Bwt))   
        txt.insert(INSERT, result[0])
        label3.configure(text = result[1] + '\n' + result[2])
        query = inp2.get()
        search(query, Bwm)

    but = Button(tab1, text = 'Start', font = ('Arial Bold',20), fg = 'red' , bg = 'yellow', command = main)
    but.grid(row=2,column=0)
    tab_control.pack(expand=1, fill='both')
    finestra.mainloop()

if __name__== '__main__':
    called()


