import sqlite3
import sys

from PyQt5 import QtTest
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class anaPencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Amiral Battı")
        self.statusBar()
        self.buton = QPushButton("Göster", self)
        self.buton.move(300, 800)
        self.buton.resize(150, 150)
        self.buton.setIcon(QIcon("ayarlar.png"))
        self.buton.clicked.connect(self.goster)
        self.buton1 = QPushButton("Ekle", self)
        self.buton1.move(1500, 100)
        self.buton1.resize(150, 150)
        self.buton1.setIcon(QIcon("ayarlar.png"))
        self.buton1.clicked.connect(self.gemiEkle)
        self.lineEditKelime = QLineEdit(self)
        self.lineEditKelime.move(200, 100)
        self.lineEditKelime.resize(300, 100)
        self.lineEditKelime.setPlaceholderText("Oyuncu adını giriniz")
        self.lineEditKelime1 = QLineEdit(self)
        self.lineEditKelime1.move(530, 100)
        self.lineEditKelime1.resize(400, 100)
        self.lineEditKelime1.setPlaceholderText("Gemi bölme sayısını girin")
        self.lineEditHarf = QLineEdit(self)
        self.lineEditHarf.move(950, 100)
        self.lineEditHarf.resize(240, 100)
        self.lineEditHarf.setPlaceholderText("Yatay değeri giriniz")
        self.lineEditHarf1 = QLineEdit(self)
        self.lineEditHarf1.move(1200, 100)
        self.lineEditHarf1.resize(240, 100)
        self.lineEditHarf1.setPlaceholderText("Dikey değeri giriniz")
        self.label = QLabel(self)
        self.label.move(300, 450)
        self.label.resize(300, 100)
        self.label.hide()  # labeli gizlemek için
        font = QFont()
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.Box)

    def goster(self):
        for i in range(1, 8):
            for k in range(1, 8):
                # self.label.hide()
                self.bik = QPushButton(str((i, k)), self)
                self.bik.clicked.connect(self.buttonClicked)
                self.bik.clicked.connect(self.tikla)
                self.bik.move(i * 150, k * 150)
                self.bik.resize(150, 150)
                self.bik.show()


    def tikla(self):
        baglanti = sqlite3.connect("database5.db")
        self.cursor = baglanti.cursor()
        oynad = self.lineEditKelime.text()
        gbs = int(self.lineEditKelime1.text())
        x1 = int(self.lineEditHarf.text())
        y1 = int(self.lineEditHarf1.text())
        sender = self.sender()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS gemiler (oyuncu_adi TEXT,gemi_bölme_sayi INT,yatay_deger INT,"
                            "dikey_deger INT)")
        self.cursor.execute("SELECT * FROM gemiler")
        datalar=self.cursor.fetchall()
        print(datalar)
        baglanti.commit()
        for data in datalar:
            print(data)
            print((data[2],data[3]))
            print(sender.text())

            if sender.text() == str((data[2],data[3])):
                sender.setIcon(QIcon("patlamanamlu1.gif"))
                sender.setIconSize(QSize(170, 200))
                if data[0] == "amiral":
                    QtTest.QTest.qWait(1000)
                    sender.setText("Amiral")
                    # QtTest.QTest.qWait(1000)  # 1sn bekletiyor
                    # sender.setIcon(QIcon("cancel.png"))
                    sender.setIconSize(QSize(170, 200))
                    # self.bik.setIcon(QIcon(QPixmap("cancel.png")))
                    # self.bik.setStyleSheet("background-color:red")
                    print("data:", data)
                    print("sender:", sender.text())
                if data[0] == "kruvazor":
                    QtTest.QTest.qWait(1000)
                    sender.setText("Krvz")
                    sender.setIconSize(QSize(170, 200))
                if data[0] == "muhrip":
                    QtTest.QTest.qWait(1000)
                    sender.setText("Mhrip")
                    sender.setIconSize(QSize(170, 200))
                if data[0] == "denizalti":
                    QtTest.QTest.qWait(1000)
                    sender.setText("Dnzalt")
                    sender.setIconSize(QSize(170, 200))


    def baglanti_olustur(self):
        baglanti = sqlite3.connect("database5.db")
        self.cursor = baglanti.cursor()
        oynad = self.lineEditKelime.text()
        gbs = int(self.lineEditKelime1.text())
        x1 = int(self.lineEditHarf.text())
        y1 = int(self.lineEditHarf1.text())

        self.cursor.execute("CREATE TABLE IF NOT EXISTS gemiler (oyuncu_adi TEXT,gemi_bölme_sayi INT,yatay_deger INT,"
                            "dikey_deger INT)")
        self.cursor.execute("INSERT INTO gemiler VALUES(?,?,?,?)",(oynad,gbs,x1,y1))
        #self.cursor.execute("SELECT * FROM gemiler WHERE yatay_deger = ? AND dikey_deger = ?",(self.sender.text()))
        baglanti.commit()
        baglanti.close()
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def gemiEkle(self):
        self.baglanti_olustur()



uygulama = QApplication(sys.argv)
pencere = anaPencere()
pencere.show()
uygulama.exec_()
