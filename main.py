from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class MenuWindow(Screen):
    pass

class StartWindow(Screen):
    pass

class IntroWindow(Screen):
    pass

class LookAroundWindow(Screen):
    pass

class BagWindow(Screen):
    pass

class OnFireWindow(Screen):
    pass

class LavaWindow(Screen):
    pass

class CreatureWindow(Screen):
    pass

class DefeatedMonsterWindow(Screen):
    pass

class WaterWindow(Screen):
    pass

class SwimWindow(Screen):
    pass

class IslandWindow(Screen):
    pass

class ForestWindow(Screen):
    pass

class HelpWindow(Screen):
    pass

class TunnelWindow(Screen):
    pass

class NonGreedyWindow(Screen):
    pass

class GenieWindow(Screen):
    pass

class CongratulationsWindow(Screen):
    pass

class InvisibilityWindow(Screen):
    pass

class StrengthWindow(Screen):
    pass

class FlightWindow(Screen):
    pass

class PathWindow(Screen):
    pass

class TrappedWindow(Screen):
    pass

class MonsterOverWindow(Screen):
    pass

class GreedOverWindow(Screen):
    pass

class TooNiceWindow(Screen):
    pass

class HeatWindow(Screen):
    pass

class DrownWindow(Screen):
    pass

class InnocentWindow(Screen):
    pass

class FallWindow(Screen):
    pass

class GuiltWindow(Screen):
    pass

class ColdWindow(Screen):
    pass

class GenieOverWindow(Screen):
    pass

class GameOverWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("rpg.kv")


class RPGApp(App):
    def build(self):
        return kv


if __name__=="__main__" :
    RPGApp().run()