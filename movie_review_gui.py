import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)


class MovieScore(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.search = QLineEdit()
        self.grade = QLabel("grade: ")

        search_button = QPushButton("search", self)
        self.grade_box = QTextEdit()

        search_button.clicked.connect(self.show_search_result)

        hbox_search = QHBoxLayout()
        hbox_search.addWidget(self.search)
        hbox_search.addWidget(search_button)

        hbox_grade = QHBoxLayout()
        hbox_grade.addWidget(self.grade)

        hbox_result = QHBoxLayout()
        hbox_result.addWidget(self.grade_box)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_search)
        vbox.addLayout(hbox_grade)
        vbox.addLayout(hbox_result)

        self.setLayout(vbox)
        self.setGeometry(300, 100, 1000, 2000)
        self.setWindowTitle('Assignment6')
        self.show()

    def show_search_result(self):
        self.grade_box.clear()
        movie_name = self.search.text()
        fname = "movie.txt"
        f = open(fname, "r")
        s = f.readlines()

        for i in s:
            if movie_name:
                text = ''
                index = i.find(movie_name)
                if index != -1:
                    text += i
                if text:
                    self.grade_box.append(text)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MovieScore()
    sys.exit(app.exec_())


