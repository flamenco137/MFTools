import maya.cmds as cmds
import maya.api.OpenMaya as api

if cmds.window('AlignTool', ex=True):
    cmds.deleteUI('AlignTool')
cmds.window('AlignTool', t='AlignTool')
cmds.window('AlignTool', e=True, wh=(500, 250))
cmds.columnLayout('colum1', adj=True, bgc=(0.169, 0.169, 0.169))
cmds.text(l='\n Align Tool \n', h=100, bgc=(0.43, 0.43, 0.43))
cmds.separator(h=40)
cmds.radioButtonGrp('AlignRadio', label='', labelArray3=['All', 'Translate', 'Rotate'], numberOfRadioButtons=3, sl=1, h=70)
cmds.button(l='Go', c='AlgPosition()', bgc=(0.420, 0.87, 0.9))
cmds.setParent('colum1')
cmds.showWindow('AlignTool')



def AlgPosition():
    getSl = cmds.radioButtonGrp('AlignRadio', q=True, sl=True)
    sel = cmds.ls(sl=True, fl=True)
    if len(cmds.ls(sl=True)) > 1:
        if getSl == 1:
            posX_list = []
            posY_list = []
            posZ_list = []
            if cmds.objectType(cmds.ls(sl=True)[0]) == 'transform' or cmds.objectType(cmds.ls(sl=True)[0]) == 'joint':
                Obj_List = cmds.ls(sl=True)
                for index in range(len(Obj_List)-1):
                    getPos = cmds.xform(Obj_List[index], q=True, ws=True, sp=True)
                    posX_list.append(getPos[0])
                    posY_list.append(getPos[1])
                    posZ_list.append(getPos[2])
                sortX = (max(posX_list) + min(posX_list)) / 2
                sortY = (max(posY_list) + min(posY_list)) / 2
                sortZ = (max(posZ_list) + min(posZ_list)) / 2
                sortPos = (sortX, sortY, sortZ)
                cmds.xform(Obj_List[-1], ws=True, t=(sortX, sortY, sortZ))
                
            if cmds.objectType(cmds.ls(sl=True)[0]) == 'mesh':
                objects = []
                selObj = cmds.ls(sl=True, fl=True)
                for obj2 in selObj:
                    if cmds.objectType(obj2) != 'transform' and cmds.objectType(obj2) != 'joint':
                        objects.append(obj2)
                    cmds.select(objects, r=True)
                    
                    cmds.ConvertSelectionToVertices()
                    vtxList = cmds.ls(sl=True, fl=True)
                    for index in vtxList:
                        getPos = cmds.pointPosition(index, w=True)
                        posX_list.append(getPos[0])
                        posY_list.append(getPos[1])
                        posZ_list.append(getPos[2])
                    sortX = (max(posX_list) + min(posX_list)) / 2
                    sortY = (max(posY_list) + min(posY_list)) / 2
                    sortZ = (max(posZ_list) + min(posZ_list)) / 2
                    sortPos = (sortX, sortY, sortZ)
                    cmds.xform(selObj[-1], ws=True, t=(sortX, sortY, sortZ))
                    
            if cmds.objectType(cmds.ls(sl=True)[0]) == 'nurbsCurve' or cmds.objectType(cmds.ls(sl=True)[0]) == 'nurbsSurface':
                objects = []
                selObj = cmds.ls(sl=True, fl=True)
                for obj2 in selObj:
                    if cmds.objectType(obj2) != 'transform' and cmds.objectType(obj2) != 'joint':
                        objects.append(obj2)
                    cmds.select(objects, r=True)
                    
                    vtxList = cmds.ls(sl=True, fl=True)
                    for index in vtxList:
                        getPos = cmds.pointPosition(index, w=True)
                        posX_list.append(getPos[0])
                        posY_list.append(getPos[1])
                        posZ_list.append(getPos[2])
                    sortX = (max(posX_list) + min(posX_list)) / 2
                    sortY = (max(posY_list) + min(posY_list)) / 2
                    sortZ = (max(posZ_list) + min(posZ_list)) / 2
                    sortPos = (sortX, sortY, sortZ)
                    cmds.xform(selObj[-1], ws=True, t=(sortX, sortY, sortZ))
            cmds.select(sel)
            if len(sel) == 2:
                if cmds.objectType(cmds.ls(sl=True)[0]) == 'transform' or cmds.objectType(cmds.ls(sl=True)[0]) == 'joint':
                    cmds.xform(sel[1], ws=True, ro=cmds.xform(sel[0], q=True, ws=True, ro=True))
            cmds.select(cl=True)
        
        if getSl == 2:
            posX_list = []
            posY_list = []
            posZ_list = []
            if cmds.objectType(cmds.ls(sl=True)[0]) == 'transform' or cmds.objectType(cmds.ls(sl=True)[0]) == 'joint':
                Obj_List = cmds.ls(sl=True)
                for index in range(len(Obj_List)-1):
                    getPos = cmds.xform(Obj_List[index], q=True, ws=True, sp=True)
                    posX_list.append(getPos[0])
                    posY_list.append(getPos[1])
                    posZ_list.append(getPos[2])
                sortX = (max(posX_list) + min(posX_list)) / 2
                sortY = (max(posY_list) + min(posY_list)) / 2
                sortZ = (max(posZ_list) + min(posZ_list)) / 2
                sortPos = (sortX, sortY, sortZ)
                cmds.xform(Obj_List[-1], ws=True, t=(sortX, sortY, sortZ))
                
            if cmds.objectType(cmds.ls(sl=True)[0]) == 'mesh':
                objects = []
                selObj = cmds.ls(sl=True, fl=True)
                for obj2 in selObj:
                    if cmds.objectType(obj2) != 'transform' and cmds.objectType(obj2) != 'joint':
                        objects.append(obj2)
                    cmds.select(objects, r=True)
                    
                    cmds.ConvertSelectionToVertices()
                    vtxList = cmds.ls(sl=True, fl=True)
                    for index in vtxList:
                        getPos = cmds.pointPosition(index, w=True)
                        posX_list.append(getPos[0])
                        posY_list.append(getPos[1])
                        posZ_list.append(getPos[2])
                    sortX = (max(posX_list) + min(posX_list)) / 2
                    sortY = (max(posY_list) + min(posY_list)) / 2
                    sortZ = (max(posZ_list) + min(posZ_list)) / 2
                    sortPos = (sortX, sortY, sortZ)
                    cmds.xform(selObj[-1], ws=True, t=(sortX, sortY, sortZ))
                    
            if cmds.objectType(cmds.ls(sl=True)[0]) == 'nurbsCurve' or cmds.objectType(cmds.ls(sl=True)[0]) == 'nurbsSurface':
                objects = []
                selObj = cmds.ls(sl=True, fl=True)
                for obj2 in selObj:
                    if cmds.objectType(obj2) != 'transform' and cmds.objectType(obj2) != 'joint':
                        objects.append(obj2)
                    cmds.select(objects, r=True)
                    
                    vtxList = cmds.ls(sl=True, fl=True)
                    for index in vtxList:
                        getPos = cmds.pointPosition(index, w=True)
                        posX_list.append(getPos[0])
                        posY_list.append(getPos[1])
                        posZ_list.append(getPos[2])
                    sortX = (max(posX_list) + min(posX_list)) / 2
                    sortY = (max(posY_list) + min(posY_list)) / 2
                    sortZ = (max(posZ_list) + min(posZ_list)) / 2
                    sortPos = (sortX, sortY, sortZ)
                    cmds.xform(selObj[-1], ws=True, t=(sortX, sortY, sortZ))
            cmds.select(cl=True)
        if getSl == 3:
            sel = cmds.ls(sl=True, fl=True)
            if cmds.selectType(pf=True, q=True) == True and len(sel) == 2:
                getNormal = cmds.polyInfo(fn=True)
                normal = (float(getNormal[0].split(':')[1].split(' ')[1]), float(getNormal[0].split(':')[1].split(' ')[2]), float(getNormal[0].split(':')[1].split(' ')[3]))
                
                
                M_Vec = api.MVector(normal)
                target_Vec = api.MVector(0, 0, 1)
                getRot = M_Vec.rotateTo(target_Vec)
                MQuaternion = api.MQuaternion(getRot)
                getConjugate = MQuaternion.conjugate()
                
                
                MEulerRotation = api.MQuaternion(normal[0], normal[1], normal[2], 0)
                msel = api.MSelectionList()
                msel.add(sel[1])
                dagPath = msel.getDagPath(0)
                mfnTransform = api.MFnTransform(dagPath)
                M_Vec = api.MVector(normal)
                target_Vec = api.MVector(0, 0, 1)
                getRot = M_Vec.rotateTo(target_Vec)
                MQuaternion = api.MQuaternion(getRot)
                getConjugate = MQuaternion.conjugate()
                mfnTransform.setRotation(getConjugate, api.MSpace.kObject)
                
            if len(sel) == 2:
                if cmds.objectType(cmds.ls(sl=True)[0]) == 'transform' or cmds.objectType(cmds.ls(sl=True)[0]) == 'joint':
                    cmds.xform(sel[1], ws=True, ro=cmds.xform(sel[0], q=True, ws=True, ro=True))
                cmds.select(cl=True)
    cmds.select(sel[-1])