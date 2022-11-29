from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import ObjectProperty
from os import listdir
from random import choice
from kivy.clock import Clock


class DImage():

    def __init__(self, path):
        self.path = path
        self.extensionName = path.split("/")[-1] if "/" in path else path
        self.name = self.extensionName[:-3] if "/" in path else self.extensionName[:-3]


class RCGame(BoxLayout):
    inptxt = ObjectProperty(None)
    ansLabel = ObjectProperty(None)
    displayImg = ObjectProperty(None)
    img = DImage("images/img.png")

    def nextImage(self, time):
        l = listdir("images")
        if len(l) < 1:
            self.ansLabel.text = "DATA NOT FOUND"
        if len(l) > 1:
            l.remove(self.img.extensionName)
        self.img = DImage("images/" + choice(l))
        self.ansLabel.text = ""
        self.displayImg.source = self.img.path

    def checkAns(self):
        if self.img.name == self.inptxt.text:
            self.ansLabel.color = self.greenColor
            self.ansLabel.text = "CORRECT"
        else:
            self.ansLabel.color = self.redColor
            self.ansLabel.text = "WRONG"

        self.img.path = ""
        Clock.schedule_once(callback=self.nextImage, timeout=1.5)


class RCApp(App):
    def build(self):
        game = RCGame()
        return game


if __name__ == "__main__":
    RCApp().run()
