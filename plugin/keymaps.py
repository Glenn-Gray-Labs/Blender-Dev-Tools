import bpy
from .operators.search_docs import SearchDocs

keys = []


def register():
    global keys
    wm = bpy.context.window_manager

    # ANY WINDOW
    km = wm.keyconfigs.addon.keymaps.new(name="Window", space_type="EMPTY", region_type="WINDOW")

    kmi = km.keymap_items.new(SearchDocs.bl_idname, "SLASH", "PRESS", shift=True)
    keys.append((km, kmi))


def unregister():
    global keys
    for km, kmi in keys:
        km.keymap_items.remove(kmi)
    keys.clear()
