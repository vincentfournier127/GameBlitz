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
        is_tile_dark = True
        for i in range(0,size_z):
            is_pair = i%2==0
            for j in range(0,size_x):
                current_color = color.white if is_tile_dark else color.black33
                is_tile_dark = not is_tile_dark
                new_tile = Entity(model='cube', color=current_color, parent=self)
                if is_pair:
                    new_tile.position = Vec3(j,0,i)
                else:
                    new_tile.position = Vec3(size_x-1-j,0,i)
                self.tiles.append(new_tile)
        
    def tile_to_pos(self,board_index):
        if self.can_move_to(board_index):
            return self.tiles[board_index].position + Vec3(0,0.5,0)
        else:
            raise IndexError('pos board invalide')
    
    def get_state(self,board_index):
        pass
    
    def is_winning(self,board_index):
        return board_index == self.max_board_index
    
    def is_at_start(self,board_index):
        return board_index == 0
    
    def can_move_to(self,board_index):
        return board_index >= 0 and board_index <= self.max_board_index

    def set_offset(self, offset: Vec3):
        if isinstance(offset, Vec3):
            self.offset = offset
        else:
            raise Exception()


# if __name__ == "__main__":
# app = Ursina()
# application.hot_reloader.hotreload = True
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