# -*- coding: utf-8 -*-
"""
This software is provided 'as-is', without any express or implied
warranty.  In no event will the authors be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not
   claim that you wrote the original software. If you use this software
   in a product, an acknowledgment in the product documentation would be
   appreciated but is not required.

2. Altered source versions must be plainly marked as such, and must not be
   misrepresented as being the original software.

Author:
eduardo.simioni@gmail.com
http://www.eksod.com
"""

import os
import re
from pyfbsdk import *

# Animations, if not characterized, MUST HAVE TPOSE on first frame.
# As with any retargeting procedure on Motionbuilder, all bones must be above 0 y.



"""
         from 3dsMaxBipedTemplate, edited
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


# For biped, all bones have the following naming scheme <BipedName> <BipedBone>. Set this variable to 
# False if you have Custom Skeleton.
bipedPrefixNamingScheme = True

# This is the biped map mapping all bipeds Name to Mobu Names.
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
             
# This is the Motionbuilder mapping to use the same function. Edit this list or create your own.
mobuMap = {'Reference' : 'reference',
            'Hips':'Hips',
             'LeftUpLeg' : 'LeftUpLeg',
             'LeftLeg' : 'LeftLeg',
             'LeftFoot' : 'LeftFoot',
             'RightUpLeg' : 'RightUpLeg',
             'RightLeg' : 'RightLeg',
             'RightFoot' : 'RightFoot',
             'Spine' : 'Spine',
             'LeftArm' : 'LeftArm',
             'LeftForeArm' : 'LeftForeArm',
             'LeftHand' : 'LeftHand',
             'RightArm' : 'RightArm',
             'RightForeArm' : 'RightForeArm',
             'RightHand' : 'RightHand',
             'Head' : 'Head',
             'LeftShoulder' : 'LeftShoulder',
             'RightShoulder' : 'RightShoulder',
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
             'LeftHandThumb1' : 'LeftHandThumb1',
             'LeftHandThumb2' : 'LeftHandThumb2',
             'LeftHandThumb3' : 'LeftHandThumb3',
             'LeftHandIndex1' : 'LeftHandIndex1',
             'LeftHandIndex2' : 'LeftHandIndex2',
             'LeftHandIndex3' : 'LeftHandIndex3',
             'LeftHandMiddle1' : 'LeftHandMiddle1',
             'LeftHandMiddle2' : 'LeftHandMiddle2',
             'LeftHandMiddle3' : 'LeftHandMiddle3',
             'LeftHandRing1' : 'LeftHandRing1',
             'LeftHandRing2' : 'LeftHandRing2',
             'LeftHandRing3' : 'LeftHandRing3',
             'LeftHandPinky1' : 'LeftHandPinky1',
             'LeftHandPinky2' : 'LeftHandPinky2',
             'LeftHandPinky3' : 'LeftHandPinky3',
             'RightHandThumb1' : 'RightHandThumb1',
             'RightHandThumb2' : 'RightHandThumb2',
             'RightHandThumb3' : 'RightHandThumb3',
             'RightHandIndex1' : 'RightHandIndex1',
             'RightHandIndex2' : 'RightHandIndex2',
             'RightHandIndex3' : 'RightHandIndex3',
             'RightHandMiddle1' : 'RightHandMiddle1',
             'RightHandMiddle2' : 'RightHandMiddle2',
             'RightHandMiddle3' : 'RightHandMiddle3',
             'RightHandRing1' : 'RightHandRing1',
             'RightHandRing2' : 'RightHandRing2',
             'RightHandRing3' : 'RightHandRing3',
             'RightHandPinky1' : 'RightHandPinky1',
             'RightHandPinky2' : 'RightHandPinky2',
             'RightHandPinky3' : 'RightHandPinky3',
             'LeftFootThumb1' : 'LeftFootThumb1',
             'LeftFootThumb2' : 'LeftFootThumb2',
             'LeftFootThumb3' : 'LeftFootThumb3',
             'LeftFootIndex1' : 'LeftFootIndex1',
             'LeftFootIndex2' : 'LeftFootIndex2',
             'LeftFootIndex3' : 'LeftFootIndex3',
             'LeftFootMiddle1' : 'LeftFootMiddle1',
             'LeftFootMiddle2' : 'LeftFootMiddle2',
             'LeftFootMiddle3' : 'LeftFootMiddle3',
             'LeftFootRing1' : 'LeftFootRing1',
             'LeftFootRing2' : 'LeftFootRing2',
             'LeftFootRing3' : 'LeftFootRing3',
             'LeftFootPinky1' : 'LeftFootPinky1',
             'LeftFootPinky2' : 'LeftFootPinky2',
             'LeftFootPinky3' : 'LeftFootPinky3',
             'RightFootThumb1' : 'RightFootThumb1',
             'RightFootThumb2' : 'RightFootThumb2',
             'RightFootThumb3' : 'RightFootThumb3',
             'RightFootIndex1' : 'RightFootIndex1',
             'RightFootIndex2' : 'RightFootIndex2',
             'RightFootIndex3' : 'RightFootIndex3',
             'RightFootMiddle1' : 'RightFootMiddle1',
             'RightFootMiddle2' : 'RightFootMiddle2',
             'RightFootMiddle3' : 'RightFootMiddle3',
             'RightFootRing1' : 'RightFootRing1',
             'RightFootRing2' : 'RightFootRing2',
             'RightFootRing3' : 'RightFootRing3',
             'RightFootPinky1' : 'RightFootPinky1',
             'RightFootPinky2' : 'RightFootPinky2',
             'RightFootPinky3' : 'RightFootPinky3',
             'LeftUpLegRoll' : 'LeftUpLegRoll',
             'LeftLegRoll' : 'LeftLegRoll',
             'RightUpLegRoll' : 'RightUpLegRoll',
             'RightLegRoll' : 'RightLegRoll',
             'LeftArmRoll' : 'LeftArmRoll',
             'LeftForeArmRoll' : 'LeftForeArmRoll',
             'RightArmRoll' : 'RightArmRoll',
             'RightForeArmRoll' : 'RightForeArmRoll' }

def addJointToCharacter ( characterObject, slot, jointName ):    
    myJoint = FBFindModelByName(jointName)
    if myJoint:
        proplist = characterObject.PropertyList.Find(slot + "Link")    
        proplist.append (myJoint)
        
def CharacterizeBiped(rootname, useBipedPrefixNamingScheme, nameprefix, boneMap, models):
  
    system = FBSystem()
    app = FBApplication()    
      
    longname = models.LongName
    namespaceindex = longname.rfind(":")
    if namespaceindex != -1:
        namespace = longname[0:namespaceindex+1] 
        name = longname[namespaceindex + 1:]
    else:
        namespace = ""
        name = longname

    myBiped = FBCharacter("mycharacter")
    app.CurrentCharacter = myBiped
    
    # If in Biped mode, extract the character prefix name
    if useBipedPrefixNamingScheme:
        splitname = name.split()
        nameprefix = splitname[0] + " "
        # Override the rootname so it is the character orefix name            
        rootname = splitname[0]
        myBiped.LongName = namespace + rootname
    else:
        myBiped.LongName = namespace + nameprefix + rootname
   
                
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
            addJointToCharacter (myBiped, pslot, namespace + nameprefix + pjointName)
        progress += 1
        val = progress / len(boneMap)  * 100
        fbp.Percent = int(val)
                
    switchOn = myBiped.SetCharacterizeOn( True )    
    print "Character mapping created for " + (myBiped.LongName)
        
    # We must call FBDelete when the FBProgress object is no longer needed.
    fbp.FBDelete()
    return myBiped
"""
         end edited 3dsMaxBipedTemplate
"""



def plotAnim(char, animChar):
    """
    Receives two characters, sets the input of the first character to the second
    and plot. Return ploted character.
    """
    if char.GetCharacterize:
        switchOn = char.SetCharacterizeOn(True)

    plotoBla = FBPlotOptions()
    plotoBla.ConstantKeyReducerKeepOneKey = True
    plotoBla.PlotAllTakes = True
    plotoBla.PlotOnFrame = True
    plotoBla.PlotPeriod = FBTime( 0, 0, 0, 1 )
    #plotoBla.PlotTranslationOnRootOnly = True
    plotoBla.PreciseTimeDiscontinuities = True
    #plotoBla.RotationFilterToApply = FBRotationFilter.kFBRotationFilterGimbleKiller
    plotoBla.UseConstantKeyReducer = False
    plotoBla.ConstantKeyReducerKeepOneKey  = True

    char.InputCharacter = animChar
    char.InputType = FBCharacterInputType.kFBCharacterInputCharacter
    char.ActiveInput = True
    if (not char.PlotAnimation(FBCharacterPlotWhere.kFBCharacterPlotOnSkeleton, plotoBla)):
        FBMessageBox( "Something went wrong", "Plot animation returned false, cannot continue", "OK", None, None )
        return False

    return char    



def main():
    
    app = FBApplication()
    scene = FBSystem().Scene

    fileFormatMBox = FBMessageBox( "What format to load", "In which file format are the animations?", ".fbx" , ".bvh", "Cancel" )
    if fileFormatMBox == 1:
        fileFormat = ".fbx"
    elif fileFormatMBox == 2:
        fileFormat = ".bvh"
    else:
        FBMessageBox( "File format selection canceled", "Cannot continue without a specified format.", "OK", None, None )
        return False

    # asking for the character, already characterized
    newCharPopup = FBFilePopup();
    newCharPopup.Caption = "Select an already Characterized character"
    newCharPopup.Filter = "*.fbx"
    newCharPopup.Style = FBFilePopupStyle.kFBFilePopupOpen
    newCharPopup.Path = FBSystem().ApplicationPath
    if newCharPopup.Execute():
        filename = newCharPopup.FullFilename
    else:
        FBMessageBox( "Selection canceled", "Character selection canceled.", "OK", None, None )
        return False
        
    # asking for the animations folder
    # this part should be changed to load other formats
    # in theory it should work with any skeleton that can be characterized.
    oldAnimsPopup = FBFolderPopup()
    oldAnimsPopup.Caption = "Animations to retarget"
    oldAnimsPopup.Filter = "*" + fileFormat
    oldAnimsPopup.Path = newCharPopup.Path # easier to navigate

    fileList = []                
    if oldAnimsPopup.Execute():
        # Getting the names of the files in your previously selected folder
        # Using os to get the file names from the specified folder (above) and storing names of files in a list
        allList = os.listdir(oldAnimsPopup.Path)
        # Setting the regular expression to only look for .fbx or .bvh extenstion
        fbxRE = re.compile('^\w+.fbx$', re.I)
        bvhRE = re.compile('^\w+.bvh$', re.I)
        # Removing any files that do not have an .fbx extenstion
        for fname in allList:
            mo = fbxRE.search(fname)
            mi = bvhRE.search(fname)
            if mo or mi:
                fileList.append(fname)
    else:
        FBMessageBox( "Animations selection canceled", "Cannot continue without animations.", "OK", None, None )
        return False

   
    # get root name from the skeleton on the animations folder
    nomenclature = FBMessageBox( "Animations nomenclature", "The skeleton on the animations folder follow which nomenclature?", "Motionbuilder" , "3dsMax Biped", "Cancel" )
    if nomenclature == 1:
        userRoot = FBMessageBoxGetUserValue( "Hips/Pelvis", "Please type exact name of hips node on the animations:", "Hips", FBPopupInputType.kFBPopupString, "Ok" )
        boneMap = mobuMap
        bipedPrefixNamingScheme = False
        prefix = FBMessageBoxGetUserValue( "Prefix to nomenclature", "Please input the prefix used on the skeleton. Leave empty if none.", "", FBPopupInputType.kFBPopupString, "Ok" )
    elif nomenclature == 2:
        userRoot = FBMessageBoxGetUserValue( "Hips/Pelvis", "Please type exact name of hips/pelvis node on the animations:", "Bip01", FBPopupInputType.kFBPopupString, "Ok" )
        boneMap = bipedMap
        bipedPrefixNamingScheme = True
        prefix = ["",""] # so we can use prefix variable for both cases
    else:
        FBMessageBox( "Nomenclature selection canceled", "Bones must follow either Motionbuilder or 3dsMax Biped nomenclature. You can edit or add your own inside the script (line 160).", "OK", None, None )
        return False

    # iterate through animation list
    for animName in fileList:
        
        app.FileNew()
        scene.Evaluate()
        app.FileOpen(filename)
        newChar = app.CurrentCharacter
        if not newChar:
            FBMessageBox( "Not characterized", "No characterized character on the character scene.", "OK", None, None )
            return False

        # FileMerge() can load only native .fbx, and it loads characters if they are present, of course
        # FileImport() on the other hand just imports the file into the scene
        if fileFormat == ".fbx":
            # setup load/merge options
            lOptions = FBFbxOptions(True) # true = load options
            lOptions.CustomImportNamespace = "merged"
            app.FileMerge(oldAnimsPopup.Path + "\\" + animName, False, lOptions)
        else:
            app.FileImport(oldAnimsPopup.Path + "\\" + animName, False) # False means it will create objects regardless


        # if there's no character in the merged animation scene we need to characterize it
        if len(scene.Characters) == 1:
            
            # find root model to pass to CharacterizeBiped()
            # if merging FBX, it has custom namespace
            if fileFormat == ".fbx":
                oldAnimRoot = FBFindModelByName("merged:" + prefix[1] + userRoot[1])
            # if importing BVH, it will have it's own BVH: namespace
            else:
                oldAnimRoot = FBFindModelByName("BVH:" + prefix[1] + userRoot[1])
                
            if not oldAnimRoot:
                FBMessageBox( "Could not find hips object", "Check opened scene. Root node name must be given without namespace.", "OK", None, None )
                return False

            # characterize imported animation with modified 3dsmaxbipedtemplate.py
            oldAnimChar = CharacterizeBiped(userRoot[1], bipedPrefixNamingScheme, prefix[1], boneMap, oldAnimRoot)
            
        else:
            # merged FBX with an character present in the scene
            oldAnimChar = scene.Characters[1]

        # plot
        charToSave = plotAnim(newChar, oldAnimChar)

        # setup save options (for some reason, they were not working outside this loop...)
        sOptions = FBFbxOptions(False) # false = save options
        sOptions.SaveCharacter = True
        sOptions.SaveControlSet = False
        sOptions.SaveCharacterExtension = False
        sOptions.ShowFileDialog = False
        sOptions.ShowOptionsDialog = False
        
        # Saves out the character and rig animation
        app.SaveCharacterRigAndAnimation(newCharPopup.Path + "\\" + animName, charToSave, sOptions)
        if fileFormat != ".fbx":
            animName += ".fbx" # leaving .bvh and adding .fbx, so File saved: is printed correctly
        print "File saved: " + newCharPopup.Path + "\\" + animName


main()
del(bipedPrefixNamingScheme, bipedMap, mobuMap)