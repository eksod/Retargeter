import os
import re
from pyfbsdk import *
# from "C:\Program Files\Autodesk\Autodesk MotionBuilder 2011 32-bit\bin\config\Scripts\" import 3dsMaxBiped.py



"""
         from 3dsMaxBipedTemplate
"""

# Copyright 2009 Autodesk, Inc.  All rights reserved.
# Use of this software is subject to the terms of the Autodesk license agreement 
# provided at the time of installation or download, or which otherwise accompanies
# this software in either electronic or hard copy form.
#
# Script description:
# This script is executed when a template with the script name ((in Asset\Character)) is dragged on a character.
# It will Characterize a 3DS Max Biped so it fits the MoBu naming.
#
# Topic: FBFindModelByName,FBCharacter.SetCharacterizeOn,FBProgress
#


# These three variables controls how characterization is done

# This is the Root Name. For a Biped this will be the Biped Name. For Custom Skeleton user must set
# it according to their naming convention
bipedrootname = "<CharacterName>"

# For biped, all bones have the following naming scheme <BipedName> <BipedBone>. Set this variable to 
# False if you have Custom Skeleton.
bipedPrefixNamingScheme = True

# This is the biped map mapping all bipeds Name to Mobu Names.
# If you have a custom skeleton, you need to recreate this map according to your naming convention.
bipedMap = {'Reference' : 'Fbx_Root',
            'Hips':'',
             'LeftUpLeg' : 'L Thigh',
             'LeftLeg' : 'L Calf',
             'LeftFoot' : 'L Foot',
             'RightUpLeg' : 'R Thigh',
             'RightLeg' : 'R Calf',
             'RightFoot' : 'R Foot',
             'Spine' : 'Spine',
             'LeftArm' : 'L UpperArm',
             'LeftForeArm' : 'L Forearm',
             'LeftHand' : 'L Hand',
             'RightArm' : 'R UpperArm',
             'RightForeArm' : 'R Forearm',
             'RightHand' : 'R Hand',
             'Head' : 'Head',
             'LeftShoulder' : 'L Clavicle',
             'RightShoulder' : 'R Clavicle',
             'Neck' : 'Neck',
             'Spine1' : 'Spine1',
             'Spine2' : 'Spine2',
             'Spine3' : 'Spine3',
             'Spine4' : 'Spine4',
             'Spine5' : 'Spine5',
             'Spine6' : 'Spine6',
             'Spine7' : 'Spine7',
             'Spine8' : 'Spine8',
             'Spine9' : 'Spine9',
             'Neck1' : 'Neck1',
             'Neck2' : 'Neck2',
             'Neck3' : 'Neck3',
             'Neck4' : 'Neck4',
             'Neck5' : 'Neck5',
             'Neck6' : 'Neck6',
             'Neck7' : 'Neck7',
             'Neck8' : 'Neck8',
             'Neck9' : 'Neck9',
             'LeftHandThumb1' : 'L Finger0',
             'LeftHandThumb2' : 'L Finger01',
             'LeftHandThumb3' : 'L Finger02',
             'LeftHandIndex1' : 'L Finger1',
             'LeftHandIndex2' : 'L Finger11',
             'LeftHandIndex3' : 'L Finger12',
             'LeftHandMiddle1' : 'L Finger2',
             'LeftHandMiddle2' : 'L Finger21',
             'LeftHandMiddle3' : 'L Finger22',
             'LeftHandRing1' : 'L Finger3',
             'LeftHandRing2' : 'L Finger31',
             'LeftHandRing3' : 'L Finger32',
             'LeftHandPinky1' : 'L Finger4',
             'LeftHandPinky2' : 'L Finger41',
             'LeftHandPinky3' : 'L Finger42',
             'RightHandThumb1' : 'R Finger0',
             'RightHandThumb2' : 'R Finger01',
             'RightHandThumb3' : 'R Finger02',
             'RightHandIndex1' : 'R Finger1',
             'RightHandIndex2' : 'R Finger11',
             'RightHandIndex3' : 'R Finger12',
             'RightHandMiddle1' : 'R Finger2',
             'RightHandMiddle2' : 'R Finger21',
             'RightHandMiddle3' : 'R Finger22',
             'RightHandRing1' : 'R Finger3',
             'RightHandRing2' : 'R Finger31',
             'RightHandRing3' : 'R Finger32',
             'RightHandPinky1' : 'R Finger4',
             'RightHandPinky2' : 'R Finger41',
             'RightHandPinky3' : 'R Finger42',
             'LeftFootThumb1' : 'L Toe4',
             'LeftFootThumb2' : 'L Toe41',
             'LeftFootThumb3' : 'L Toe42',
             'LeftFootIndex1' : 'L Toe3',
             'LeftFootIndex2' : 'L Toe31',
             'LeftFootIndex3' : 'L Toe32',
             'LeftFootMiddle1' : 'L Toe2',
             'LeftFootMiddle2' : 'L Toe21',
             'LeftFootMiddle3' : 'L Toe22',
             'LeftFootRing1' : 'L Toe1',
             'LeftFootRing2' : 'L Toe11',
             'LeftFootRing3' : 'L Toe12',
             'LeftFootPinky1' : 'L Toe0',
             'LeftFootPinky2' : 'L Toe01',
             'LeftFootPinky3' : 'L Toe02',
             'RightFootThumb1' : 'R Toe4',
             'RightFootThumb2' : 'R Toe41',
             'RightFootThumb3' : 'R Toe42',
             'RightFootIndex1' : 'R Toe3',
             'RightFootIndex2' : 'R Toe31',
             'RightFootIndex3' : 'R Toe32',
             'RightFootMiddle1' : 'R Toe2',
             'RightFootMiddle2' : 'R Toe21',
             'RightFootMiddle3' : 'R Toe22',
             'RightFootRing1' : 'R Toe1',
             'RightFootRing2' : 'R Toe11',
             'RightFootRing3' : 'R Toe12',
             'RightFootPinky1' : 'R Toe0',
             'RightFootPinky2' : 'R Toe01',
             'RightFootPinky3' : 'R Toe02',
             'LeftUpLegRoll' : 'LThighTwist',
             'LeftLegRoll' : 'LCalfTwist',
             'RightUpLegRoll' : 'RThighTwist',
             'RightLegRoll' : 'RCalfTwist',
             'LeftArmRoll' : 'LUpArmTwist',
             'LeftForeArmRoll' : 'L ForeTwist',
             'RightArmRoll' : 'RUpArmTwist',
             'RightForeArmRoll' : 'R ForeTwist' }

def addJointToCharacter ( characterObject, slot, jointName ):    
    myJoint = FBFindModelByName(jointName)
    if myJoint:
        proplist = characterObject.PropertyList.Find(slot + "Link")    
        proplist.append (myJoint)
        
def CharacterizeBiped(rootname, useBipedPrefixNamingScheme, boneMap, models):
    # Create an empty FBModelList object.
    # models = FBModelList()
    
    # Obtain Bip01
    #FBGetSelectedModels(models)
    
    system = FBSystem()
    app = FBApplication()    
    
    # check if there is a selection
#    if len( models ) == 0:
#        FBMessageBox( "Message", "Please select a Biped joint.", "OK", None, None )
#    elif len( models ) > 1:
        # Only one biped joint must be selected else we can have problems if joints belongs to different bipeds.
#        FBMessageBox( "Message", "Only one Biped joint must be selected.", "OK", None, None )    
#    else:
        # Extract the name of the model including its namespace
        
        
    longname = models.LongName
    namespaceindex = longname.rfind(":")
    if namespaceindex != -1:
        namespace = longname[0:namespaceindex+1] 
        name = longname[namespaceindex + 1:]
    else:
        namespace = ""
        name = longname
        # If in Biped mode, extract the character prefix name
    bipednameprefix = ""            
    if useBipedPrefixNamingScheme:
        splitname = name.split()
        bipednameprefix = splitname[0] + " "
        # Override the rootname so it is the character orefix name            
        rootname = splitname[0]
    
    myBiped = FBCharacter("mycharacter")
    myBiped.LongName = namespace + rootname
    app.CurrentCharacter = myBiped
                
    # Create a FBProgress object and set default values for the caption and text.    
    fbp = FBProgress()
    fbp.Caption = ""
    fbp.Text = " -----------------------------------   Creating Biped character"
    progress = 0.0
    progresssteps = len(boneMap)

    # assign Biped to Character Mapping.
    for pslot, pjointName in boneMap.iteritems():
        if not pjointName:
            addJointToCharacter (myBiped, pslot, namespace + rootname)
        else:
            addJointToCharacter (myBiped, pslot, namespace + bipednameprefix + pjointName)
        progress += 1
        val = progress / len(boneMap)  * 100
        fbp.Percent = int(val)
                
    switchOn = myBiped.SetCharacterizeOn( True )    
    print "Character mapping created for " + (myBiped.LongName)
        
    # We must call FBDelete when the FBProgress object is no longer needed.
    fbp.FBDelete()
    return myBiped
# Call the Characterize Character Function with all bipeds defined variables.
# Characterize(bipedrootname, bipedPrefixNamingScheme, bipedMap)



"""
         end 3dsMaxBipedTemplate
"""








def plotAnim(riderChar, riderBip):

    if riderChar.GetCharacterize:
        switchOn = riderChar.SetCharacterizeOn(True)

    plotoBla = FBPlotOptions()
    plotoBla.ConstantKeyReducerKeepOneKey = True
    plotoBla.PlotAllTakes = True
    plotoBla.PlotOnFrame = True
    plotoBla.PlotPeriod = FBTime( 0, 0, 0, 1 )
#    plotoBla.PlotTranslationOnRootOnly = True
    plotoBla.PreciseTimeDiscontinuities = True
#    plotoBla.RotationFilterToApply = FBRotationFilter.kFBRotationFilterGimbleKiller
    plotoBla.UseConstantKeyReducer = False
    plotoBla.ConstantKeyReducerKeepOneKey  = True


    print "Character to plot: ", riderChar.Name
    riderChar.InputCharacter = riderBip
    riderChar.InputType = FBCharacterInputType.kFBCharacterInputCharacter
#    print riderChar.InputType.Name
#    riderChar.InputCharacter(riderBip)
    print "Input character on riderChar: " ,riderChar.InputCharacter.Name
    print "Active inpute on riderChar: ", riderChar.ActiveInput 
    riderChar.ActiveInput = True
    print "Active inpute on riderChar: ", riderChar.ActiveInput 
    if (not riderChar.PlotAnimation(FBCharacterPlotWhere.kFBCharacterPlotOnSkeleton, plotoBla)):
        FBMessageBox( "Something went wrong", "Plot animation returned false, cannot continue", "OK", None, None )
        return False

    #del(sys, scene, bipedMap, plotoBla)
    return riderChar    



def main():
    
    app = FBApplication()
    scene = FBSystem().Scene

    # asking for the character, already characterized
    newCharPopup = FBFilePopup();
    newCharPopup.Caption = "Select an already Characterized character"
    newCharPopup.Filter = '*.fbx'
    newCharPopup.Style = FBFilePopupStyle.kFBFilePopupOpen
    newCharPopup.Path = r"N:\SBK2011\SrcTBConv_GEM\GFX\Characters\rider" #FBSystem().ApplicationPath
    if newCharPopup.Execute():
        filename = newCharPopup.FullFilename
    else:
        FBMessageBox( "Selection canceled", "Character selection canceled", "OK", None, None )
        return False
        
    # asking for the animations folder
    oldAnimsPopup = FBFolderPopup()
    oldAnimsPopup.Caption = "Animations in fbx to retarget"
    oldAnimsPopup.Filter = '*.fbx'    
    oldAnimsPopup.Path = newCharPopup.Path # easier to navigate
    fbxList = []
    if oldAnimsPopup.Execute():
        # Getting the names of the files in your previously selected folder
        # Using os to get the file names from the specified folder (above) and storing names of files in a list
        fileList = os.listdir(oldAnimsPopup.Path)
        # Setting the regular expression to only look for .fbx extenstion
        fbxRE = re.compile('^\w+.fbx$', re.I)
        # Removing any files that do not have an .fbx extenstion
        for fname in fileList:
            mo = fbxRE.search(fname)
            if mo:
                fbxList.append(fname)
    else:
        FBMessageBox( "Animations selection canceled", "Cannot continue without animations", "OK", None, None )
        return False

    strRootToSearch = "Bip01" #ask this to the user

    # iterate through animation list
    for animName in fbxList:

        app.FileOpen(filename) # resets scene, no need to app.FileNew()
        newChar = app.CurrentCharacter

        app.FileMerge(oldAnimsPopup.Path + "\\" + animName)

        oldAnimRoot = FBFindModelByName(strRootToSearch)
        
        # characterize imported animation with modified 3dsmaxbipedtemplate.py
        oldAnimChar = CharacterizeBiped(strRootToSearch, bipedPrefixNamingScheme, bipedMap, oldAnimRoot)
        
        # plot
        charToSave = plotAnim(newChar, oldAnimChar)
        
        # Saves out the character and rig animation
        # SaveCharacterRigAndAnimation (str pFileName, FBCharacter pCharacter, bool pSaveCharacter, bool pSaveRig, bool pSaveExtensions)
        lOptions = FBFbxOptions(False)## save options
        lOptions.SaveCharacter = True
        lOptions.SaveControlSet = False
        lOptions.SaveCharacterExtension = False
        lOptions.ShowFileDialog = False
        lOptions.ShowOptionsDialog = False
        app.SaveCharacterRigAndAnimation(newCharPopup.Path + "\\" + animName, charToSave, lOptions)
        print newCharPopup.Path + "\\" + animName
        # FBApplication().FileSave(popupoChar.Path + fname, lOptions)
        # Closing the current file, not really necessarily needed since the FBApplication::FileOpne replaces the current scene
        # FBApplication().FileNew()
    
        
        
        
    
main()