from ursina import *
from engine import Engine

app = Ursina(borderless=False)    
application.hot_reloader.hotreload = True

e = Engine()

app.run()

