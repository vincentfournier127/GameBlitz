from ursina import *
from sample import color, Texture
from typing import Callable
from pion import Pion
from board import Board

class Arbiter(Entity):
    def __init__(self):
        super().__init__()
        self.text_announcer = Text(text='Non initialise!')
        self.text_announcer.position = window.top_left * 0.9
        
    def game_start(self):
        self.text_announcer.text = "À vous de jouer!\n Appuyer sur Espace pour continuer."
    
    def player_ready(self, id_joueur, range_dice):
        self.text_announcer.text = f"Joueur {id_joueur},\n lancez le dé ({range_dice[0]},{range_dice[1]})"
    
    def throw_dice(self,id_joueur, range_dice:tuple):
        result = random.randint(*range_dice)
        self.text_announcer.text = f"Joueur {id_joueur}\n a lancé le dé ({result})"
        return result
    
    def callback_player_arrive(self, id_joueur, status):
        if not status:
            self.text_announcer.text = f"Joueur {id_joueur}\n rien de spécial"
        else:
            self.text_announcer.text = f"Joueur {id_joueur}\n est maintenant {status}"
    
    def player_winning(self, id_joueur):
        self.text_announcer.text = f"Bravo {id_joueur}!!!!!"
    
# app = Ursina()    
# application.hot_reloader.hotreload = True

# a = Arbiter()

# s= Sequence(
#     Func(a.game_start),
#     Wait(2),
#     Func(a.player_ready,0,(1,6)),
#     Wait(2),
#     Func(a.throw_dice,0,(1,6)),
#     Wait(2),
#     Func(a.callback_player_arrive,0,"CouchPotato"),
#     Wait(2),
#     Func(a.callback_player_arrive,0,None),
#     Wait(2),
#     Func(a.player_winning,0)
#     )
# s.start()

# app.run()


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
    
