DISCLAIMER:
This software is provided 'as-is', without any express or implied warranty.  In no event will the authors be held liable for any damages arising from the use of this software.


INSTRUCTIONS:
This is a script for Autodesk Motionbuilder to retarget automatically a folder with .fbx animation files over a characterized character. The animations on the folder can or not be characterized. If they are not, the skeleton need to follow either Motionbuilder or 3dsMax Biped nomenclature. If you want you can easily edit or create your own nomenclature mapping inside the script. Some considerations:

1) The new character needs to be already characterized. It's advisable to test out the retargeting first with a couple of animations, and tweak the Retargeting Reach and Offset values of this character to a "best match for all". This values are saved with the character and will be used to retarget all animations.

2) Only .fbx files on the animation folder will be "merged" into the scene with the new character. As mentioned, they can be already characterized, and if so will spare you a possible headache. If they are not already characterized they need fill two conditions:
    A) They *need* to be on tpose on frame 0 to be correctly characterized, otherwise the plot between skeletons will not work at all.
    B) The nomenclature of the bones must follow either the default 3dsMax Biped or Motionbuilder one. There's also a prompt asking for a prefix to the bones, if you use them. You can just leave it empty if there's no prefix. The file is merged with a namespace "merged", so both new character and old animation can have the same skeleton name.


INSTALL:
There's no install, on Motionbuilder just go to Window/Python Editor. On the second button chose to open retargeter.py from where you saved it. Then press Execute Active Work Area (fifth button, with the little arrow.)


If you have any questions, ideas, bugs or feature requests please contact the author at:
'Eduardo Simioni' <eduardo.simioni@gmail.com>
http://www.eksod.com