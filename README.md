# saba-python
Python binding for [Saba](sslocal://flow/file_open?url=https%3A%2F%2Fgithub.com%2Fbenikabocha%2Fsaba&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=) library | MMD (MikuMikuDance) real-time rendering &amp; bone control in Python,can render VMD motion and PMX model.Made by a junior high school student.
# Features
- Python binding for Saba MMD renderer
- Load and render PMX / PMD models
- Load and play VMD motion files
- Full bone control & morph (face / lip-sync) support
- GLFW real-time window rendering

# Installation
Compile by using cmake and make
```bash
mkdir build 
cd build
cmake ..
make
```
After compilation, you will get file like mmd-cpython*.so file,that is the python package
saba-python currently  only support glfw window. Please run
```bash
pip install glfw
```
in your python environment.
# Example
Make sure the mmd-cpython*.so file **in the same folder** before using.
## Rendering PMX model and VMD motion:
``` python
import glfw
import mmd
glfw.init()
glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 2)
glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
glfw.window_hint(glfw.SAMPLES, 4)
window = glfw.create_window(1280, 800, "MMD", None, None)
glfw.make_context_current(window)
viewer = mmd.MMDViewer()
viewer.set_resource_path("/path/to/your/resource") #Resource usually in the build/saba folder
viewer.init()
viewer.load_model("/path/to/your/model.pmx")
viewer.load_vmd("/path/to/your/motion.vmd")
while not glfw.window_should_close(window):
    w, h = glfw.get_framebuffer_size(window)
    viewer.resize(w, h)
    viewer.setup_camera()
    viewer.update(1/60)
    viewer.draw()
    glfw.swap_buffers(window)
    glfw.poll_events()

viewer.close()
glfw.terminate()
```
## Controlling bones and morph:
``` python
#....your model and motion loading code
bone = model.get_bone("頭") 
bone.set_manual_control(True)
morph = model.get_morph("笑い")
morph.set_manual_control(True)
while not glfw.window_should_close(window):
    #...others....
    # Control bone: x, y, z, w (quaternion), blend ratio
    bone.set_rotation(0.0, 0.5, 0.0, 1.0,0.4) 
    # Control bone position: x, y, z, blend ratio
    bone.set_position(1,0.41,0.5,0.5)
    # Control morph weight: weight value, blend ratio
    morph.set_weight(0.8,0.5) 
    viewer.draw()
    #...others.....

viewer.close()
glfw.terminate()
```
The **blend** argument can set the blend ratio between manual settings and original VMD animation settings.**A higher blend value means your manual control has more influence.**
