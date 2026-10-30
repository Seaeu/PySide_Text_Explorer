import os
import json
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt, QObject, QEvent
#from PySide6.QtGui import QKeyEvent
# GLOBAL VARIABLE
import game_state as state
# SAVE MANAGER
import savemanager as save
# INITIALIZE STATE.DATA
save.load_game()
#Other Files.py
from gamewindow import Ui_Window
import stats as stat

# Global Variables cause ts PMO
escape_menu_status = False
World_Map = None
World_1 = None

class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Window()
        self.ui.setupUi(self)

        # Initialization #
        self.ui.Map.mapChanged.connect(self.ui.MapLabel.changeText)



        self.update_ui_elements()

        # --- LINK YOUR SCRIPT MENU BUTTONS HERE --- #
        # Main Menu
        self.ui.NewGame.clicked.connect(lambda: self.NewGame())
        self.ui.LoadGame.clicked.connect(lambda: self.LoadGame())
        self.ui.Options.clicked.connect(lambda: self.OpenOptions())
        self.ui.Quit.clicked.connect(lambda: self.QuitGame())
        # Dev Button
        self.ui.DevBtn.clicked.connect(lambda: self.ui.Tabs.setCurrentIndex(4))

        # Options Menu
        self.ui.LeaveOptions.clicked.connect(lambda: self.LeaveOptions())
        self.ui.TextSpeed_SpinBox.valueChanged.connect(lambda: self.TextSpeed_SpinBox())

        # Map Menu
        #self.ui.MapBtn1.clicked.connect(lambda: self.ui.Tabs.setCurrentIndex(0))

        # Game Play
        self.ui.SaveAndQuit.clicked.connect(lambda: self.SaveAndQuit())
        self.ui.MapMenuButton.clicked.connect(lambda: self.MapMenuButton())
        self.ui.InventoryBtn.clicked.connect(lambda: self.OpenInventory())


    # -- UI Refresh Helper -- #
    def update_ui_elements(self):
        # Main Menu
        if state.data["game_stage"] >= 1:
            self.ui.LoadGame.setEnabled(True)
        else:
            self.ui.LoadGame.setEnabled(False)
        # Options
        current_speed = state.options["text_speed"]
        self.ui.TextSpeed_SpinBox.setValue(current_speed)
        # Game Play
        self.ui.SaveAndQuit.setVisible(globals()['escape_menu_status'])
        self.EscapeMenu()
        # Map Menu
        temp = state.data["world_status"]
        state.world_map = temp["zone_0"]
        state.world_1 = temp["zone_1"]

    # -- Main Menu Scripts -- #
    def NewGame(self):
        save.new_game()
        save.load_game()
        self.update_ui_elements()
        self.ui.Tabs.setCurrentIndex(2)
        self.LoadMap(state.world_map)
        self.update_ui_elements()

    def LoadGame(self):
        self.update_ui_elements()
        self.ui.Tabs.setCurrentIndex(2)
        self.update_ui_elements()

    def OpenOptions(self):
        self.ui.Tabs.setCurrentIndex(1)

    def QuitGame(self):
        QApplication.quit()

    # -- Options Menu Scripts -- #
    def LeaveOptions(self):
        save.save_game()
        self.ui.Tabs.setCurrentIndex(0)

    def TextSpeed_SpinBox(self):
        state.options["text_speed"] = self.ui.TextSpeed_SpinBox.value()

    # -- Game Play Scripts -- #
    def EscapeMenu(self):
        self.eventFilter = EscapeMenu_KeyDetector(self)
        if self.ui.Tabs.currentIndex() == 2:
            self.ui.GamePlay.installEventFilter(self.eventFilter)

    def SaveAndQuit(self):
        save.save_game()
        self.ui.Tabs.setCurrentIndex(0)
        globals()['escape_menu_status'] = False
        self.update_ui_elements()

    def MapMenuButton(self):
        self.ui.Tabs.setCurrentIndex(4)

    def OpenInventory(self):
        self.ui.Tabs.setCurrentIndex(3)

    # -- Map Menu scripts
    def LoadMap(self,Map):
        self.ui.Map.MapCreate(Map)



class EscapeMenu_KeyDetector(QObject):
    def eventFilter(self, widget, event):
            if event.type() == QEvent.KeyPress:
                key = event.key()
                if key == Qt.Key_Escape:
                    if globals()['escape_menu_status'] == False:
                        globals()['escape_menu_status'] = True
                    elif globals()['escape_menu_status'] == True:
                        globals()['escape_menu_status'] = False
                    window.update_ui_elements()
                    return True
            return super().eventFilter(widget, event)


# -- RUN LOOP -- #
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec())
