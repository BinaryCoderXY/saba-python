# saba-python
### [English](https://github.com/BinaryCoderXY/saba-python/blob/main/README.md)  [中文](https://github.com/BinaryCoderXY/saba-python/blob/main/README_ch.md) 
给项目[Saba](https://github.com/benikabocha/saba)写的python支持| MMD (MikuMikuDance) 实时渲染 （我修改了部分Saba的源代码）&amp; 由python控制骨骼，可以渲染vmd动作和pmx模型.由一名初中生制作。
# Features
- Saba MMD的Python 绑定
- 加载PMX模型
- 加载并播放任何VMD动作
- 完整的骨骼和表情支持
- GLFW作为渲染窗口
- 支持添加多模型

# Installation
通过cmake和make进行编译
```bash
git clone https://github.com/BinaryCoderXY/saba-python.git
cd saba-python
git submodule update --init --recursive
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
# 可选：启用透明窗口（取消下方注释）
#glfw.window_hint(glfw.TRANSPARENT_FRAMEBUFFER, glfw.TRUE) 
glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 2)
glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
glfw.window_hint(glfw.SAMPLES, 4)
window = glfw.create_window(1280, 800, "MMD", None, None)
glfw.make_context_current(window)
viewer = mmd.MMDViewer()
viewer.set_resource_path("/path/to/your/resource") #Resource资源文件夹一般在编译完成后的build/saba文件夹内
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
    viewer.clear_screen() #必须要在draw之前清屏
    viewer.draw(model1)
    viewer.draw(model2)
    glfw.swap_buffers(window)
    glfw.poll_events()

viewer.close()
glfw.terminate()
```
## 控制骨骼和表情
``` python
#....your model and motion loading code
bone = model1.get_bone("頭") 
bone.set_manual_control(True)
morph = model1.get_morph("笑い")
morph.set_manual_control(True)
while not glfw.window_should_close(window):
    #...others....
    # Control bone: x, y, z, w (quaternion), blend ratio
    bone.set_rotation(0.0, 0.5, 0.0, 1.0,0.4) 
    # Control bone position: x, y, z, blend ratio
    bone.set_position(1,0.41,0.5,0.5)
    # Control morph weight: weight value, blend ratio
    morph.set_weight(0.8,0.5) 
    viewer.draw(model1)
    #...others.....

viewer.close()
glfw.terminate()
```
这个**blend** 参数是用来调整骨骼和动作原本vmd动画和人工设计的混合比例between .**混合blend数值越大，人工调整越明显.**
