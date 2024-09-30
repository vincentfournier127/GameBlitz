from ursina import *
from sample import color, Texture
from typing import Callable
from pion import Pion
from board import Board

class Arbiter(Entity):
    def __init__(self):
        super().__init__()
        
    def game_start(self):
        pass
    
    def player_ready(self, id_joueur, range_dice):
        pass
    
    def throw_dice(self, range_dice:tuple):
        pass
    
    def player_arrive(self, id_joueur, list_status):
        pass
    
    def player_winning(self, id_joueur):
        pass
    
    te = TextField(text='1234')
    te.render()
    
app = Ursina()    
application.hot_reloader.hotreload = True
te = Text(text='1234')
app.run()


# if __name__ == "__main__":
# app = Ursina()
# 
# b = Board()
# p1 = Pion(color.fancy_orange, Texture.brick_wall, offset=Vec3(0,0,-0.25))
# p1.teleport(b.tile_to_pos(0))
# p2 = Pion(color.azure, Texture.grass_ground, offset=Vec3(0,0,0.25))
# p2.teleport(b.tile_to_pos(0))
# p1.animate_to([b.tile_to_pos(i) for i in range(1,10)], fin_tour)
# #EditorCamera()
# camera.position = Vec3(15,13,-15)
# board_center = Vec3(3,0,3)
# camera.look_at(board_center)
# app.run()
    
