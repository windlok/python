import sys
#sys modülü, Python'un standart kütüphanesinde bulunan bir modüldür ve Python programlarının çalışma ortamı hakkında bilgi sağlar. sys.argv, komut satırından geçirilen argümanları içeren bir liste olarak kullanılır. Bu, PyQt5 uygulamasının başlatılması sırasında komut satırından argümanlar almasına olanak tanır.
from PyQt5 import QtWidgets
#PyQt5, Python programlama dili için bir grafik kullanıcı arayüzü (GUI) kütüphanesidir. PyQt5, Qt framework'ünün Python bağlamasıdır ve Python geliştiricilerine Qt'nin güçlü özelliklerini kullanarak GUI uygulamaları oluşturma imkanı sağlar.
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow , QToolTip
#QApplication, QWidget, QMainWindow ve QToolTip sınıflarını PyQt5.QtWidgets modülünden içe aktarır. Bu sınıflar, PyQt5 uygulamalarında sıklıkla kullanılan temel bileşenlerdir.
from PyQt5.QtGui import QIcon

def window():
    #app bu bir QApplication nesnesi oluşturur. QApplication, PyQt5 uygulamasının temelini oluşturur ve uygulamanın çalışması için gereklidir.
    app = QApplication(sys.argv)
    #QWidget, PyQt5'te temel bir pencere sınıfıdır. QWidget, diğer tüm kullanıcı arayüzü öğelerinin temelini oluşturur ve kendi başına bir pencere olarak kullanılabilir.
    win = QWidget()
    #QMainWindow, PyQt5'te daha gelişmiş bir pencere sınıfıdır. QMainWindow, menü çubuğu, araç çubuğu, durum çubuğu gibi özelliklere sahip bir ana pencere sağlar.
    win=QMainWindow()
    #setWindowTitle() metodu, pencerenin başlığını belirlemek için kullanılır. 
    # Bu başlık, pencerenin üst kısmında görüntülenir ve kullanıcıya pencerenin ne hakkında olduğunu belirtir.
    win.setWindowTitle("PyQt5 App")
    #setGeometry() metodu, pencerenin konumunu ve boyutunu belirlemek için kullanılır. 
    #Bu metodun parametreleri sırasıyla x koordinatı, y koordinatı, genişlik ve yüksekliktir. 
    #Örneğin, setGeometry(100, 100, 300, 200) ifadesi, pencereyi ekranın (100, 100) konumuna yerleştirir ve genişliğini 300 piksel, yüksekliğini ise 200 piksel olarak ayarlar.
    win.setGeometry(200, 200, 300, 200)
    #show() metodu, pencereyi ekranda görünür hale getirir. Bu metodu çağırmadan önce pencere oluşturulmuş olsa da, kullanıcıya gösterilmez.
    
    #setWindowIcon() metodu, pencerenin simgesini belirlemek için kullanılır. Bu metodun parametresi, simge olarak kullanılacak bir QIcon nesnesidir.
    win.setWindowIcon(QIcon('icon.png'))
    #setToolTip() metodu, bir widget'ın üzerine gelindiğinde görüntülenecek olan araç ipucunu (tooltip) ayarlamak için kullanılır.
    win.setToolTip('This is a <b>QWidget</b> widget')
    
    win.show()
    sys.exit(app.exec_())

window()    