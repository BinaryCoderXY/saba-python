# saba-python
### [English](https://github.com/BinaryCoderXY/saba-python/blob/main/README.md) [中文](https://github.com/BinaryCoderXY/saba-python/blob/main/README_ch.md) 
Python binding for [Saba](https://github.com/benikabocha/saba) library | MMD (MikuMikuDance) real-time rendering &amp; bone control in Python,can render VMD motion and PMX model **Modified Saba source code by myself.**.Made by a junior high school student.
## Features
- Python binding for Saba MMD renderer
- Load and render PMX / PMD models
- Load and play VMD motion files
- Full bone control & morph (face / lip-sync) support
- GLFW real-time window rendering
- Support adding multiple models
## Supported Platforms
 - ✅ macOS (Primary)
 - ✅ Linux (Untested, but should work with existing code)
 - ❌ Windows (Not supported yet; not recommended to run on Windows)
 - ❓ HarmonyOS (Uh-oh, I have no idea yet. I'll look into it when I have time >_<)
## Installation
Use git to clone the repository:
```bash
git clone https://github.com/BinaryCoderXY/saba-python.git
cd saba-python
git submodule update --init --recursive
```
Install by using pip:
```bash
pip install .
```
Compile by using cmake and make:
```bash
mkdir build 
cd build
cmake ..
make
```
After compilation, you will get file like saba-cpython*.so file,that is the python package. saba-python currently only support glfw window. Please run
```bash
pip install glfw
```
in your python environment.
## Example
If you used CMake and make for compiling, Make sure the saba-cpython*.so file **in the same folder** before using.
### Rendering PMX model and VMD motion:
``` python
import glfw
import saba as mmd
glfw.init()
# Optional: Enable transparent window (uncomment below).
#glfw.window_hint(glfw.TRANSPARENT_FRAMEBUFFER, glfw.TRUE) 
glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 2)
glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
glfw.window_hint(glfw.SAMPLES, 4)
window = glfw.create_window(1280, 800, "MMD", None, None)
glfw.make_context_current(window)
viewer = mmd.MMDViewer()
viewer.init()
model1 = mmd.Model("/path/to/your/first/model.pmx",viewer)
model2 = mmd.Model("/path/to/your/second/model.pmx",viewer)
viewer.add_model(model1)
viewer.add_model(model2)
model1.load_vmd("/path/to/your/motion1.vmd")
model2.load_vmd("/path/to/your/motion2.vmd")
while not glfw.window_should_close(window):
    w, h = glfw.get_framebuffer_size(window)
    viewer.resize(w, h)
    viewer.setup_camera()
    viewer.update()
    viewer.clear_screen() #Must clear the screen before drawing models.
    viewer.draw(model1)
    viewer.draw(model2)
    glfw.swap_buffers(window)
    glfw.poll_events()

viewer.close()
glfw.terminate()
```
### Controlling bones and morph:
``` python
#....your model and motion loading code
bone = model1.get_bone("頭") 
bone.set_manual_control(True)
morph = model1.get_morph("笑い")
morph.set_manual_control(True)
while not glfw.window_should_close(window):
    #...others....
    # Control bone: x, y, z, w (quaternion), blend ratio.
    bone.set_rotation(0.0, 0.5, 0.0, 1.0,0.4) 
    # Control bone position: x, y, z, blend ratio.
    bone.set_position(1,0.41,0.5,0.5)
    # Control morph weight: weight value, blend ratio.
    morph.set_weight(0.8,0.5) 
    viewer.draw(model1)
    #...others.....

viewer.close()
glfw.terminate()
```
The **blend** argument can set the blend ratio between manual settings and original VMD animation settings.**A higher blend value means your manual control has more influence.**

