from ursina import *
from typing import Callable
import sample.color as color
import sample.Texture as Texture

class Board(Entity):
    def __init__(self, add_to_scene_entities=True, enabled=True, **kwargs):
        super().__init__(add_to_scene_entities, enabled, **kwargs)
        self.tiles = []
        size_x = 6
        size_z = 6
        self.max_board_index = (size_x * size_z) - 1
        for i in range(0,size_x):
            for j in range(0,size_z):
                cur_color = color.white if (i+j)%2 else color.black66
                new_tile = Entity(model='cube', color=cur_color,parent=self)
                new_tile.position = Vec3(i,j,0)
        
    def tile_to_pos(self,board_index):
        pass
    
    def get_state(self,board_index):
        pass
    
    def is_winning(self,board_index):
        return board_index == self.max_board_index
    
    def is_at_start(self,board_index):
        return board_index == 0
    
    def can_move_to(self,board_index):
        return board_index >= 0 and board_index <= self.max_board_index













app = Ursina(borderless=False)
application.hot_reloader.hotreload = True
Board()

EditorCamera()
app.run()