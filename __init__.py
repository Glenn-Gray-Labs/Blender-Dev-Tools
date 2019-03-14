import bpy
from . import autoload, keymaps

bl_info = {
    "name": "Dev Tools for 2.80",
    "author": "Nicholas Glenn",
    "description": "Utilities for developing addons in Blender 2.80",
    "version": (2019, 1),
    "blender": (2, 80, 0),
    "location": "",
    "warning": "",
    "wiki_url": "https://github.com/NickGlenn/Blender-Dev-Tools",
    "tracker_url": "https://github.com/NickGlenn/Blender-Dev-Tools/issues",
    "category": "Development"
}

autoload.init()


def register():
    autoload.register()
    keymaps.register()


def unregister():
    autoload.unregister()
    keymaps.unregister()
