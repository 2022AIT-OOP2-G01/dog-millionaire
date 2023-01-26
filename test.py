import sys
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout

app = QApplication(sys.argv)
window = QMainWindow()

# Create a label to display the GIF
label = QLabel(window)

# Create a movie object to load the gif from your file
movie = QMovie("dog.gif")

# Set the movie for the label
label.setMovie(movie)

# Start the movie
movie.start()

window.show()
sys.exit(app.exec_())


from PySide6.QtCore import QSize
from PySide6.QtGui import QMovie

movie = QMovie("animation.gif")
movie.setScaledSize(QSize(width, height))

