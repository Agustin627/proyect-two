from graficos import *
import sys
import pandas as pd
import matplotlib.pyplot as plt

from PyQt5 import uic, QtWidgets
 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

      #botones
        self.boton1.clicked.connect(self.getCSV)
        self.boton2.clicked.connect(self.plot)
       #funcion CSV    
    def getCSV(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if filePath != "":
            #imprimir la dirección del archivo
            self.resultado2.setText("    Directorio:\n" + filePath)
            self.df = pd.read_csv(str(filePath))
       #name creator
        nombre = "   Integrants:\n   Agustin.\n   Carlos.\n    Juan."
        self.resultado3.setText(nombre)

    def plot (self):
        x=self.df['col1']
        y=self.df['col2']
        plt.plot(x,y)
        plt.show()
        estad_st="Column stats 2: "+str(self.df['col2'].describe())
        self.resultado.setText(estad_st)

        
       

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())