# saba-python
### [English](https://github.com/BinaryCoderXY/saba-python/blob/main/README.md)
给项目[Saba](https://github.com/benikabocha/saba)写的python支持| MMD (MikuMikuDance) 实时渲染 &amp; 由python控制骨骼，可以渲染vmd动作和pmx模型.由一名初中生制作。
# Features
- Saba MMD的Python 绑定
- 加载PMX模型
- 加载并播放任何VMD动作
- 完整的骨骼和表情支持
- GLFW作为渲染窗口

# Installation
通过cmake和make进行编译
```bash
mkdir build 
cd build
cmake ..
make
```
编译完成后，你会得到一个文件名类似于 mmd-cpython*.so 的文件,目前仅支持glfw创建窗口.在你的python环境中运行
```bash
pip install glfw
```
# Example
使用前保证 mmd-cpython*.so 文件在 **同一个文件夹下** 
## 渲染一个MMD的PMX模型和VMD动作
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
viewer.set_resource_path("/path/to/your/resource") #Resource资源文件夹一般在编译完成后的build/saba文件夹内
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
## 控制骨骼和表情
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
这个**blend** 参数是用来调整骨骼和动作原本vmd动画和人工设计的混合比例between .**混合blend数值越大，人工调整越明显.******
