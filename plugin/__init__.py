import bpy
from . import operators as ops, keymaps

bl_info = {
    "name": "Dev Tools for 2.80",
    "author": "Nicholas Glenn",
    "description": "Utilities for developing addons in Blender 2.80",
    "version": (2019, 1),
    "blender": (2, 80, 0),
    "location": "View3D",
    "support": "COMMUNITY",
    "wiki_url": "https://github.com/NickGlenn/Blender-Dev-Tools",
    "tracker_url": "https://github.com/NickGlenn/Blender-Dev-Tools/issues",
    "category": "Development"
}

def register():
    ops.register()
    keymaps.register()


def unregister():
    keymaps.unregister()
    ops.unregister()
