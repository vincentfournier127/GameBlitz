from ursina import *
import sample.Texture as Texture
import sample.color as color

# class SacPatate(Entity):
#     def __init__(self, no_player = 1, add_to_scene_entities=True, enabled=True, **kwargs):
#         super().__init__(add_to_scene_entities, enabled, **kwargs)
#         self.a = False

# app = Ursina(borderless=False)
# application.hot_reloader.hotreload = True


# def spin():
#     cube.animate('rotation_y', cube.rotation_y+360, duration=5, curve=curve.linear)
#     sphere.animate('rotation_x', cube.rotation_x+360, duration=5, curve=curve.linear)


app = Ursina()
e = Entity(model='quad')

def some_func():
    print('some_func')

s = Sequence(
    Func(some_func),
    Func(print, 'one'), # Callable: ... 
    Func(e.fade_out, duration=1), # retourne une sequenc,
    Func(e.animate_x, value=2,duration=1),
    Wait(1),
    Func(e.animate_y, value=2,duration=1),
    loop=True
    )

# s.__dict__


for i in range(8):
    s.append(Func(print, i))
    s.append(Wait(.2))

print(s)

def input(key):
    actions = {'s' : s.start, 'f' : s.finish, 'p' : s.pause, 'r' : s.resume}
    if key in actions:
        actions[key]()
        
EditorCamera()

app.run()

