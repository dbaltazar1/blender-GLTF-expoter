import bpy 
import os
bl_info={"name":"GLTF-EXport single batch files",
	"description":"Exporter that exports single gltf files each one by one",
        "author": "Moti Daniel",  
        "version":(1,0),
	"blender": (3, 2, 1),
        "location": "Sidebar shortcut N"}

class gltft(bpy.types.Operator):
    bl_idname = 'test.testgltf'
    bl_label = 'gltftest'
    bl_options = {'PRESET','UNDO'}
    def execute(self, context):
        bpy.ops.object.select_all(action='SELECT')
        basedir = os.path.dirname(bpy.data.filepath)
        view_layer = bpy.context.view_layer
        obj_active = view_layer.objects.active
        selection = bpy.context.selected_objects
        bpy.ops.object.select_all(action='DESELECT')
        for obj in selection:
            obj.select_set(True)
            view_layer.objects.active = obj
            name = bpy.path.clean_name(obj.name)
            fn = os.path.join(basedir, name)
            bpy.ops.export_scene.gltf(filepath=fn + ".glb", use_selection=True)
            obj.select_set(False)
        view_layer.objects.active = obj_active
        for obj in selection:
            obj.select_set(True)
        return {'FINISHED'}

class panel(bpy.types.Panel):
    bl_label = 'GLTF Single Batch Exporter'
    bl_idname = 'P_PT_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'GLTF EX'
    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.operator(gltft.bl_idname, text='EXport GLTF files')

from bpy.utils import register_class, unregister_class
_classes = [panel, gltft]
def register():
    for cls in _classes:
        register_class(cls)
def unregister():
    for cls in _classes:
        unregister_class(cls)
if __name__ == '__main__':
    register()