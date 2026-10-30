from PySide6.QtWidgets import QListWidgetItem, QGraphicsView
from PySide6.QtCore import Qt
# GLOBAL VARIABLE
import game_state as state

class Inventory(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
