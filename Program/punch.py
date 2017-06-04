from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from time import strftime
import qimage2ndarray
import cv2
import sys
import requests
import base64



class My_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self,None)
        x=768
        y=432
        self.video_size = QSize(x, y)
        self.url = "http://127.0.0.1:8080/attendancelst/" #insert your ip
        
        loader = QUiLoader()
        form = loader.load("./punch.ui",None)
        self.capture = cv2.VideoCapture(1)
        _, self.frame = self.capture.read()
        self.setCentralWidget(form)

        self.button = form.findChild(QPushButton,"Button")
        self.button.clicked.connect(self.submit)

        self.ID = form.findChild(QLineEdit,"lineEdit_ID")
        self.Pass = form.findChild(QLineEdit,"lineEdit_Pass")
        self.Pass.setEchoMode(QLineEdit.Password)

        self.image_label = form.findChild(QLabel,"label_im")
        self.image_label.setFixedSize(self.video_size)
        self.setup_camera()

    

    def setup_camera(self):
        """Initialize camera.
        """
        
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())

        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)

    def display_video_stream(self):
        """Read frame from camera and repaint QLabel widget.
        """
        _, self.frame = self.capture.read()
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.flip(self.frame, 1)
        image = qimage2ndarray.array2qimage(self.frame)  #SOLUTION FOR MEMORY LEAK
        self.image_label.setPixmap(QPixmap.fromImage(image))

    def submit(self):

        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.flip(self.frame, 1)
        ID=self.ID.text()
        ID = int(ID)
        Password=self.Pass.text()
        cv2.imwrite("pic.jpg",self.frame)
        f = open("pic.jpg","rb")
        data = f.read()
        data_url = "data:image/jpg;base64,%s" % base64.b64encode(data)
        data_url = data_url[0:22] + data_url[24:]
        print(data_url[0:50])
        r = requests.post(self.url,data={"employee":ID, "attendance_pic":data_url,"Password":Password})
        f.close()
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Result")
        text=r.content.decode()
        msgBox.setText(text)
        if(text != '"Success"'):
            msgBox.setIcon(QMessageBox.Critical)
        msgBox.exec_()


        

def main(): 
    app = QApplication(sys.argv)

    w = My_window()
    w.setWindowTitle("Punch The Clock")
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
        
