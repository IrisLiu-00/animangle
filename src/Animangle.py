"""The entry point for this application."""
import argparse
from controller.BasicController import BasicController
from model.Animation import Animation
from model.AnimationBuilder import file2Anim, FileFormatException
from view.GuiView import GuiView

def _run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--open", required=False)
    args = parser.parse_args()  # catch errors
    if args.open:  # user provided a file to load from
        try:
            anim = file2Anim(args.open)
        except (FileNotFoundError, FileFormatException) as e:
            print(e)
            return
    else:
        anim = Animation()
    view = GuiView(anim)
    controller = BasicController(anim, view)
    controller.go()


if __name__ == '__main__':
    _run()
