from Tkinter import *
import tkMessageBox as mb
import Tkinter,tkFileDialog

 
class DemoLogin:
    def __init__(self, induk, judul):
        self.induk = induk
         
        self.induk.title(judul)
        self.induk.resizable(False, False)
         
        self.upload()
         
         
    def upload(self):
        # atur frame utama
        frameUtama = Frame(self.induk, bd=10)
        frameUtama.pack(fill=BOTH, expand=YES)
         
        # atur frame data
        frData = Frame(frameUtama, bd=5)
        frData.pack(fill=BOTH, expand=YES)
         
        # atur input username
        Button(frData, text='Masukan Gambar ', fg='blue', command=self.bukagambar).grid(row=0, column=0, sticky=W)
        self.hasil = Entry(frData)
        self.hasil.grid(row=0, column=1)
        # atur input password
        Button(frData, text='Tulis Pesan', fg='green', command=self.bukatxt).grid(row=1, column=0, sticky=W)
        self.hasil2 = Entry(frData)
        self.hasil2.grid(row=1, column=1)


        
         
        # atur frame tombol
        frTombol = Frame(frameUtama, bd=5)
        frTombol.pack(fill=BOTH, expand=YES)
         
        # atur tombol login
        self.btnLogin = Button(frTombol, text='Proses', command=self.proses)
        self.btnLogin.pack(side=LEFT, fill=BOTH, expand=YES)
         
        self.btnBatal = Button(frTombol, text='Batal', command=self.Tutup)
        self.btnBatal.pack(side=LEFT, fill=BOTH, expand=YES)

    def bukagambar(self):
        gif1 = PhotoImage(file = 'pinguin.png')
        if gif1 != None:    
            ubah = "upload gambar sukses"
            self.hasil.insert(0,ubah)

    def bukatxt(self):
        file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
        if file != None:
            data = file.read()
        
            file.close()
        # print "I got %d bytes from this file." % len(data)
        ket = "upload txt sukses"
        self.hasil2.insert(0,ket)
    def proses(self):
        # zip -r secret-file.zip file
        # stepic -e -i  -t file -o coba.png
        print  "tes"
    def prosesLogin(self, event=None):
        # ambil data input dari pengguna
        nmUser = self.entUser.get()
        passUser = self.entPass.get()
         
        # logika pemrograman
        if nmUser=='':
            mb.showwarning('Pesan Salah', 'Nama User tidak boleh kosong!', parent=self.induk)
            self.entUser.focus_set()
        elif passUser=='':
            mb.showwarning('Pesan Salah', 'Kata Kunci tidak boleh kosong!', parent=self.induk)
            self.entPass.focus_set()
        elif (nmUser==datUser) and (passUser==datPassword):
            mb.showinfo("Login", "Selamat Tahun Baru 2013!!!", parent=self.induk)
            self.Tutup()
        else:
            mb.showwarning('Pesan Salah', 'Nama Pengguna atau Kata Kunci SALAH!!', parent=self.induk)
            self.Hapus()
             
    def lihatPassword(self, event=None):
        nilaiCek = self.cek.get()
         
        if nilaiCek== 1:
            self.entPass['show'] = ''
        else:
            self.entPass['show'] = '*'
         
    def Tutup(self, event=None):
        self.induk.destroy()
         
    def Hapus(self, event=None):
        self.entUser.delete(0, END)
        self.entPass.delete(0, END)
        self.entUser.focus_set()        
         
if __name__ == '__main__':
    root = Tk()
     
    app = DemoLogin(root, ":: Demo Keamanan Sistem Informasi ::")
     
    root.mainloop()