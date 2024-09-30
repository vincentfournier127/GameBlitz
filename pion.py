from ursina import *
from typing import Callable
import sample.color as color
import sample.Texture as Texture

class Pion(Entity):
    def __init__(self,color, texture, offset,name, add_to_scene_entities=True, enabled=True, **kwargs):
        super().__init__(add_to_scene_entities, enabled,model=Cylinder(resolution=50,radius=0.25*0.5,start=0,height=0.05), color=color,texture=texture, **kwargs)
        self.model_body = Entity(model=Cylinder(resolution=50,radius=0.05,start=0.05,height=0.3), color=color,texture=texture,parent=self)
        self.model_head = Entity(model='sphere', color=color,texture=texture,scale=0.22,parent=self)
        self.model_head.position = Vec3(0,0.35,0)
        self.offset = offset
        self.name = name
        self.board_position = 0

    def get_name(self):
        return self.name
    
    def get_board_position(self):
        return self.board_position
         
    def set_offset(self, offset:Vec3):
        if isinstance(offset,Vec3):
            self.offset = offset
        else:
            raise TypeError()
        
    def teleport(self,destination:Vec3):
        if isinstance(destination,Vec3):
            self.position = destination + self.offset
        else:
            raise TypeError()
    
    def animate_to(self,list_position,call_on_end_anim):
        move_duration = 0.3
        s = Sequence()
        
        for v in list_position:
            if not isinstance(v,Vec3):
                raise TypeError()
            v += self.offset
            fx,fy,fz = v
            s.append(Func(self.animate_x, value=fx,duration=move_duration,curve=curve.in_out_expo))
            s.append(Func(self.animate_z, value=fz,duration=move_duration,curve=curve.in_out_expo))
            s.append(Wait(move_duration))
        s.append(Func(call_on_end_anim))
        s.start()
        
    def compute_rule(self):
        return (36,36)
        
#if __name__ == "__main__":
# app = Ursina(borderless=False)
# application.hot_reloader.hotreload = True

# p1 = Pion(color=color.blue_flame,texture=Texture.ice, offset=Vec3(0,0,0.25))
# p1.animate_to([Vec3(5,0,0),],p.teleport)

# EditorCamera()
# app.run()