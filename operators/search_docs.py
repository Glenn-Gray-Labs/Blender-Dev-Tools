import bpy


class SearchDocs(bpy.types.Operator):
    bl_idname = "modulum.search_docs"
    bl_label = "Search 2.8 API Docs"
    bl_description = "Open and search Blender 2.8's API documentation in a new browser window or tab"

    section: bpy.props.EnumProperty(
        name="Section",
        description="The section or subject that will be opened",
        items=[
            ("SEARCH", "Search Results", "Perform a custom search"),
            ("HOME", "Home", "Opens the API documentation home page"),
            ("CONTEXT", "Context Access", "bpy.context"),
            ("DATA", "Data Access", "bpy.data"),
            ("OPS", "Operators", "bpy.ops"),
            ("PROPS", "Property Definitions", "bpy.props"),
            ("TYPES", "Types", "bpy.types"),
            ("UTILS", "Utilities", "bpy.utils"),
        ])

    query: bpy.props.StringProperty(
        name="Query",
        description="The search query that will be made.  If blank, then the home page for the docs will be shown")

    def execute(self, context):
        url = "https://docs.blender.org/api/blender2.8"

        if self.section == "SEARCH":
            url = "https://docs.blender.org/api/blender2.8/search.html?q={}&check_keywords=yes&area=default".format(self.query)
        elif self.section != "HOME":
            url = "https://docs.blender.org/api/blender2.8/bpy.{}.html".format(self.section.lower())

        bpy.ops.wm.url_open(url=url)
        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "section")
        if self.section == "SEARCH":
            layout.prop(self, "query")
        layout.label(text="")
