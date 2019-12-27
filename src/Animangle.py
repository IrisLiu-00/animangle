"""The entry point for this application."""
from controller.BasicController import BasicController
from model.Animation import Animation
from view.GuiView import GuiView

if __name__ == '__main__':
    anim = Animation()
    view = GuiView(anim)
    controller = BasicController(anim, view)
    controller.go()
