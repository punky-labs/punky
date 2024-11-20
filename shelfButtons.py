'''
import maya.cmds as cmds
import punky.shelfButtons as shelfButtons
import importlib

importlib.reload(shelfButtons)


'''
import maya.cmds as cmds

# Groups multiple shape nodes under a single node 
def parentShapes():
    selected = cmds.ls(sl=True)

    shapes = cmds.listRelatives(selected, s=True)
    if shapes is not None:
        new_group = cmds.group(empty=True)
        for shape in shapes:
            cmds.parent(shape, new_group, relative=True,  shape=True)
        for object in selected:
            cmds.delete(object)
    else:
        cmds.error('Please select only shapes')