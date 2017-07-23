from traits.api import HasTraits, Range, Str,Color,Instance, on_trait_change
from traitsui.api import View, Item, Group
from mayavi.core.api import PipelineBase
from mayavi.core.ui.api import MayaviScene, SceneEditor, MlabSceneModel
from mayavi import mlab
 
from numpy import arange, pi, cos, sin
dphi = pi/300.
phi = arange(0.0, 2*pi + 0.5*dphi, dphi, 'd')
def curve(n_mer, n_long):
    mu = phi*n_mer
    x = cos(mu) * (1 + cos(n_long * mu/n_mer)*0.5)
    y = sin(mu) * (1 + cos(n_long * mu/n_mer)*0.5)
    z = 0.5 * sin(n_long*mu/n_mer)
    t = sin(mu)
    return x, y, z, t
 
class MyModel(HasTraits):
    n_meridional    = Range(0, 30, 6)
    n_longitudinal  = Range(0, 30, 11)
    n_tube_radius  = Range(0.01, 0.04, 0.025)
    s_colormap = Str('Spectral')
    background_color=Color(0x7B7B7B)
    s_representation=Str('surface')
#    points,wireframe,surface

    # 场景模型实例
    scene = Instance(MlabSceneModel, ())
    # 管线实例
    plot = Instance(PipelineBase)
    #当场景被激活，或者参数发生改变，更新图形
    @on_trait_change('n_meridional,n_longitudinal,n_tube_radius,s_colormap,background_color,s_representation,scene.activated')
    def update_plot(self):
        x, y, z, t = curve(self.n_meridional, self.n_longitudinal)
        if self.plot is None:#如果plot未绘制则生成plot3d
            self.plot = self.scene.mlab.plot3d(x, y, z, t,
                        tube_radius=self.n_tube_radius, colormap=self.s_colormap)

        else:#如果数据有变化，将数据更新即重新赋值
            self.plot.mlab_source.set(x=x, y=y, z=z, scalars=t,colormap=self.s_colormap)
            
            s=mlab.gcf()
            #设置scens 的背景色            
            s.scene.background=self.background_color.getRgbF()[0:3]
            
            #设置colormap            
            module_manager=s.children[0].children[0].children[0].children[0]#获得所属对象
            module_manager.scalar_lut_manager.lut_mode = self.s_colormap
            
            #设置表现方式
            surface=module_manager.children[0]#在module_manager获得下级所属对象
            surface.actor.property.representation = self.s_representation

# 建立视图布局
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=250, width=300, show_label=False),
                Group('_', 'n_meridional', 'n_longitudinal','background_color','s_colormap','s_representation'),
                resizable=True,title="hongjy1 test")

model = MyModel()
model.configure_traits()
