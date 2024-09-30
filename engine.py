from ursina import *
from sample import color, Texture
from typing import Callable
from pion import Pion
from board import Board
from arbiter import Arbiter
from enum import Enum

class GameState(Enum):
    GAME_START = 1
    PLAYER_READY = 2
    THROW_DICE = 3
    PLAYER_ARRIVE = 4
    PLAYER_WINNING = 5

class Engine(Entity):
    def __init__(self):
        super().__init__()
        self.arbiter = Arbiter()
        self.arbiter.game_start()
        
        p1 = Pion(color.red, Texture.lava, offset=Vec3(0,0,-0.25),name="Gabriel/Daniel")
        p2 = Pion(color.blue_flame, Texture.ice, offset=Vec3(0,0,0.25),name="MA/JF")
        self.players = (p1,p2)
        self.active_player = p1
        self.active_player_index = 0
        
        self.board = Board()
        p1.teleport(self.board.tile_to_pos(0))
        p2.teleport(self.board.tile_to_pos(0))
        
        camera.position = Vec3(15,13,-15)
        board_center = Vec3(3,0,3)
        camera.look_at(board_center)
        
        self.game_state = GameState.GAME_START
        
    def input(self,key):
        if key == "space":
            match self.game_state:
                case GameState.GAME_START:
                    self.game_state = GameState.PLAYER_READY
                    self.arbiter.player_ready(self.active_player.name,self.active_player.compute_rule())
                case GameState.PLAYER_READY:
                    self.game_state = GameState.THROW_DICE
                    dice_result = self.arbiter.throw_dice(self.active_player.name,self.active_player.compute_rule())
                    self.active_player.animate_to(self.generate_position_list(dice_result),self.on_animate_to_end)
                    self.active_player.board_position += dice_result
                case GameState.THROW_DICE:
                    # player arrive is trigger by animation
                    pass
                case GameState.PLAYER_ARRIVE:        
                    
                    # UGLY STATE CHANGE CAREFULL NOT GOOD
                    if self.board.is_winning(self.active_player.get_board_position()):
                        self.game_state = GameState.PLAYER_WINNING
                    else:
                        self.game_state = GameState.GAME_START
                        self.active_player_index = (self.active_player_index+1)%2
                        self.active_player = self.players[self.active_player_index]
                    self.input("space")
                case GameState.PLAYER_WINNING:
                    self.arbiter.player_winning(self.active_player.get_name())
                
    def on_animate_to_end(self):
        if self.game_state == GameState.THROW_DICE:
            self.game_state = GameState.PLAYER_ARRIVE
            self.arbiter.callback_player_arrive(self.active_player.get_name(),None)
            
                
    def generate_position_list(self,dice_result):
        board_position = self.active_player.get_board_position()
        list_index =  range(board_position,board_position+dice_result)
        return [self.board.tile_to_pos(x) for x in list_index]
                    