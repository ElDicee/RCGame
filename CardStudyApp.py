from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import ObjectProperty, Widget
from os import listdir
from random import choice
from kivy.clock import Clock
from enum import Enum

class DImage():
    def __init__(self, path):
        self.path = path
        self.extensionName = path.split("/")[-1] if "/" in path else path
        self.name = self.extensionName[:-4] if "/" in path else self.extensionName[:-4]
        self.tag = self.name.split("-")[1]
        self.id = self.name.split("-")[0]


class rootWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.center_x = self.width/2
        self.center_y = self.height/2
        self.active_widgets = []
        self.showStarterMenu()

    def showStarterMenu(self):
        for i in self.active_widgets:
            self.remove_widget(i)
        sm = StarterMenu()
        sm.center_x = self.center_x
        sm.center_y = self.center_y
        sm.size = self.size
        self.add_widget(sm)
    def showGame(self):
        for i in self.active_widgets:
            self.remove_widget(i)
        self.add_widget(RCGame())

class StarterMenu(BoxLayout):
    pass

class RCGame(BoxLayout):
    inptxt = ObjectProperty(None)
    ansLabel = ObjectProperty(None)
    displayImg = ObjectProperty(None)
    correctLabel = ObjectProperty(None)
    img = DImage("images/" + choice(listdir("images")))

    def nextImage(self, time):
        l = listdir("images")
        if len(l) < 1:
            self.ansLabel.text = "DATA NOT FOUND"
        if len(l) > 1:
            l.remove(self.img.extensionName)
        self.img = DImage("images/" + choice(l))
        self.ansLabel.text = ""
        self.correctLabel.text = ""
        self.displayImg.source = self.img.path

    def checkAns(self):
        if not str(self.inptxt.text).rstrip().lstrip() == "":
            if str(self.img.tag).lower() == str(self.inptxt.text).lower():
                self.ansLabel.text = "CORRECT"
                print(Color.GREEN.value)
                self.ansLabel.color = Color.GREEN.value
                self.inptxt.text = ""
            else:
                self.ansLabel.text = "WRONG"
                self.ansLabel.color = Color.RED.value
                self.inptxt.text = ""
                self.correctLabel.text = self.img.tag
            self.img.path = ""
            Clock.schedule_once(callback=self.nextImage, timeout=1.5)
        else:
            self.ansLabel.text = "WAITING ANSWER..."


class RCApp(App):
    def build(self):
        root = rootWidget()
        return root


class Color(Enum):
    RED = [241, 36, 36, 1]
    GREEN = [91, 221, 77, 1]


if __name__ == "__main__":
    RCApp().run()