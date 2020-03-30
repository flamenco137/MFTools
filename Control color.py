import maya.cmds as cmds
if cmds.window('Drawing_override', ex=True):
    cmds.deleteUI('Drawing_override')
cmds.window('Drawing_override', t='Drawing Override')
cmds.window('Drawing_override', e=True, wh=(500, 250))
cmds.columnLayout('colum1', adj=True, bgc=(0.169, 0.169, 0.169))
cmds.text(l='\n Set ControlColor \n', h=100, bgc=(0.43, 0.43, 0.43))
cmds.separator(h=40)
cmds.rowLayout('rowLayout1', numberOfColumns=3, columnWidth3=(1, 200, 20), adjustableColumn=2, 
                columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)])
cmds.text(l='')
cmds.colorIndexSliderGrp('colorindex', l='Set Color ', min=1, max=32, dc='colgrp()', cc='colgrp()', cw=(1, 80), h=50)
cmds.text('number', l=1, bgc=(0, 0, 0))
cmds.showWindow('Drawing_override')




def colgrp():
    selCtls = cmds.ls(sl=True)
    shapes = []
    get_c = (cmds.colorIndexSliderGrp('colorindex',q=True, v=True)-1)
    cmds.text('number', e=True, l=get_c)
    for str in selCtls:
        sortShape = cmds.listRelatives(str, pa=True)
        for SortSp in cmds.ls(sortShape):
            if cmds.objectType(SortSp) == 'transform':
                continue
            elif cmds.objectType(SortSp) == 'nurbsCurve':
                shapes.append(SortSp)
    for i, setShape in enumerate(shapes):
        print i,'\t'+setShape
        cmds.setAttr(setShape + '.overrideEnabled', 1)
        cmds.setAttr(setShape + '.overrideColor', get_c)