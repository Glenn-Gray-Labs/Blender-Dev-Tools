from bpy.utils import register_classes_factory
from .search_docs import SearchDocs

classes = (
    SearchDocs,
)

register, unregister = register_classes_factory(classes)
