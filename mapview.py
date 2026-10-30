from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsTextItem, QLabel, QGraphicsObject
from PySide6.QtGui import QPen, QBrush, QColor, QFont
from PySide6.QtCore import Qt, Signal, QRectF

import random as r
#GLOBAL VARIABLE
import game_state as state


class NodeItem(QGraphicsObject):

    clickedWithSignal = Signal(object)

    def __init__(self, x, y, radius, name="Node", callback=None, visible=True, parent_view=None):
        super().__init__()
        self.setPos(x, y)
        self.radius = radius
        self.name = name
        self.callback = callback
        self.visible = visible
        self.parent_view = parent_view

        self.normal_brush = QBrush(QColor("#3498db"))
        self.pressed_brush = QBrush(QColor("#2980b9"))
        self.current_brush = self.normal_brush
        self.pen = QPen(QColor("#2c3e50"), 2)

        self.setFlags(QGraphicsObject.GraphicsItemFlag.ItemIsSelectable |
                      QGraphicsObject.GraphicsItemFlag.ItemSendsGeometryChanges)
        self.connected_lines = []

        self.label = QGraphicsTextItem(self.name, self)
        font = QFont("Arial",10, QFont.Weight.Bold)
        self.label.setFont(font)
        self.label.setDefaultTextColor(QColor("#ffffff"))
        self.center_text()
        self.setVisible(self.visible)

        if self.callback and self.callback != "None":
            self.setCursor(Qt.CursorShape.PointingHandCursor)

    def center_text(self):
        text_rect = self.label.boundingRect()
        self.label.setPos(-text_rect.width() /2, -text_rect.height() /2)

    def boundingRect(self):
        """Defines the outer boundaries where the node circle is allowed to draw"""
        return QRectF(-self.radius, -self.radius, self.radius * 2, self.radius * 2)

    def paint(self, painter, option, widget=None):
        """Draws the circle dynamically onto the graphics scene on your coordinates"""
        painter.setPen(self.pen)
        painter.setBrush(self.current_brush)
        painter.drawEllipse(-self.radius, -self.radius, self.radius * 2, self.radius * 2)

    def mousePressEvent(self, event):
        if self.callback and self.callback != "None":
            if event.button() == Qt.MouseButton.LeftButton:
                self.current_brush = self.pressed_brush
                self.update() # Triggers paint() instantly to show the dark color shift
                event.accept()
            else:
                super().mousePressEvent(event)
        else:
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if self.callback and self.callback != "None":
            if event.button() == Qt.MouseButton.LeftButton:
                self.current_brush = self.normal_brush
                self.update() # Reverts color back to light blue
                if self.boundingRect().contains(event.pos()):
                    self.on_button_clicked()
            event.accept()
        else:
            super().mouseReleaseEvent(event)

    def on_button_clicked(self):
        print(f"Button Clicked: {self.name}")

        if self.callback == "emit_signal":
            print(self.name)
            self.clickedWithSignal.emit(self.name)

        if "print(" in str(self.callback):
            try:
                eval(self.callback)
            except Exception as e:
                print(f"Callback Execution Error: {e}")

        elif self.parent_view and self.callback != "None":
            window = self.parent_view.window()
            if hasattr(window, "game_manager"):
                window.game_manager.switch_active_zone(self.callback)
                print(window.game_manager)


    def itemChange(self, change, value):
        if change == QGraphicsObject.GraphicsItemChange.ItemPositionChange:
            for line in self.connected_lines:
                line.update_position()
        return super().itemChange(change, value)

class EdgeItem(QGraphicsLineItem):
    def __init__(self, source_node, dest_node):
        super().__init__()
        self.source = source_node
        self.dest = dest_node
        self.source.connected_lines.append(self)
        self.dest.connected_lines.append(self)
        self.setPen(QPen(QColor("#7f8c8d"), 3, Qt.PenStyle.SolidLine))
        self.setZValue(-1)
        self.update_position()

    def update_position(self):
        self.setLine(self.source.pos().x(), self.source.pos().y(),
                     self.dest.pos().x(), self.dest.pos().y())




# ----- MapView ----- #
class MapLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Temp")

    def changeText(self,string):
        self.setText(str(string))
        self.repaint()
        self.update()
        print(string)

class MapView(QGraphicsView):

    mapChanged = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.setRenderHint(self.renderHints().Antialiasing)

    def MapCreate(self,map_data):
        self.scene.clear()
        self.NodeAdd(map_data)
        self.LineAdd(map_data)
        self.mapChanged.emit(map_data["world_name"])

    def NodeAdd(self,map_data):
        for node in map_data["nodes"]:
            name = node["name"]
            x = node["x"]
            y = node["y"]
            radius = node["radius"]
            if radius == None:
                radius = 20
            callback = node["callback"]
            visibility = node["visible"]
            location = NodeItem(x,y,radius,name,callback,visibility,parent_view=self)
            self.scene.addItem(location)

    def LineAdd(self, map_data):
        nodes_by_name = {}
        for item in self.scene.items():
            if hasattr(item, 'name') and not hasattr(item, 'source') and isinstance(item, NodeItem):
                nodes_by_name[item.name] = item

        for connection in map_data["connections"]:
            source_node = nodes_by_name.get(connection["source"])
            dest_node = nodes_by_name.get(connection["dest"])

            if source_node and dest_node:
                if source_node.visible == True and dest_node.visible == True:
                    edge = EdgeItem(source_node, dest_node)
                    self.scene.addItem(edge)
