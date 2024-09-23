from ursina import *
from typing import Callable
import sample.color as color
import sample.Texture as Texture

class Pion(Entity):
    def __init__(self,color, texture, add_to_scene_entities=True, enabled=True, **kwargs):
        super().__init__(add_to_scene_entities, enabled,model=Cylinder(resolution=50,radius=0.25*0.5,start=0,height=0.05), color=color,texture=texture, **kwargs)
        self.model_body = Entity(model=Cylinder(resolution=50,radius=0.05,start=0.05,height=0.3), color=color,texture=texture,parent=self)
        self.model_head = Entity(model='sphere', color=color,texture=texture,scale=0.22,parent=self)
        self.model_head.position = Vec3(0,0.35,0)
        self.offset = Vec3(0,0,0)

         
    def set_offset(self, offset:Vec3):
        if isinstance(offset,Vec3):
            self.offset = offset
        else:
            raise Exception()
        
    def teleport(self,destination:Vec3):
        if isinstance(destination,Vec3):
            self.position = destination + self.offset
        else:
            raise Exception()
    
    def animate_to(self,liste_position,call_on_end_animation):
        #TODO Trouver comment avoir acces a un delegate quand l'animation est terminer
        if isinstance(liste_position, list) and len(liste_position) > 0 and isinstance(liste_position[-1],Vec3):
            animator = self.animate_position(liste_position[-1]+ self.offset,duration=1,curve=curve.in_out_expo)
            #animator.append()
        else:
            raise Exception()
        
        if isinstance(call_on_end_animation,Callable):
            call_on_end_animation(liste_position[-1]+ self.offset)
        else:
            raise Exception()
        
    def compute_rule(self):
        return tuple(1,6)
        
#if __name__ == "__main__":
app = Ursina(borderless=False)
application.hot_reloader.hotreload = True

p = Pion(color=color.blue_flame,texture=Texture.ice)
p.animate_to([Vec3(5,0,0),],p.teleport)
EditorCamera()
app.run()