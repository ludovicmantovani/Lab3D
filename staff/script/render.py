import sys, os
import shutil
from subprocess import *

import tag_img

FRAME_NUMBER = 1
LOGO_PATH = "..\..\img\logo3.jpg"

blender_test = False
src_test = False
dst_test = False

if len(sys.argv) == 4:
    blender_path = sys.argv[1]
    src_path = sys.argv[2]
    dst_path = sys.argv[3]

    if os.path.exists(blender_path) and os.path.basename(blender_path) == "blender.exe":
        print 'Blender path \t\t\tOK'
        blender_test = True

    if (blender_test):
        if (os.path.exists(src_path) and os.path.isdir(src_path)):
            print 'Source folder path \t\tOK'
            src_test = True
    else:
        print 'Blender path failed'

    if (src_test):
        if (os.path.exists(dst_path) and os.path.isdir(dst_path)):
            print 'Destination folder path \tOK\n'
            dst_test = True
    else:
        print 'Source folder failed'

    if (dst_test):
        for folder in os.listdir(src_path):
            folder_src_path = os.path.join(src_path, folder)
            if os.path.isdir(folder_src_path):
                for file in os.listdir(folder_src_path):
                    
                    file_src_path = os.path.join(folder_src_path, file)
                    
                    if os.path.isfile(file_src_path) and file.endswith(".blend"):

                        folder_dest_path = os.path.join(dst_path, folder)
                        folder_dest_path_source = os.path.join(folder_dest_path, "source")
                        folder_dest_path_rendu = os.path.join(folder_dest_path, "rendu")
                        
                        if (not os.path.exists(folder_dest_path)):
                            os.mkdir(folder_dest_path)
                        if (not os.path.exists(folder_dest_path_source)):
                            os.mkdir(folder_dest_path_source)

                        file_dest_path_source = os.path.join(folder_dest_path_source, file)

                        if not(os.path.exists(file_dest_path_source) and os.path.isfile(file_dest_path_source)):
                            shutil.copy(file_src_path, file_dest_path_source);
                        else:
                            print 'Skip blender file: ' + file + ' in ' + folder

                        if (not os.path.exists(folder_dest_path_rendu)):
                            os.mkdir(folder_dest_path_rendu)

                        name = os.path.splitext(file)[0]
                        file_dest_path_rendu = os.path.join(folder_dest_path_rendu, name)

                        if not(os.path.exists(file_dest_path_rendu) and os.path.isfile(file_dest_path_rendu)):
                            print (folder + '\n\t' + name)
                            commande = [blender_path, "-b", file_src_path, "-o", file_dest_path_rendu, "-F", "JPEG", "-x", "1", "-f", str(FRAME_NUMBER)]
                            out = Popen(commande,stdout=PIPE)
                            (sout,serr)=out.communicate()
                            #if sout and len(sout) > 0:
                                #print "Sout : " + sout
                            #if serr and len(serr) > 0:
                                #print "Error : " + serr
                            blender_generate_path_file = file_dest_path_rendu + str(FRAME_NUMBER).rjust(4,'0') + '.jpg'
                            os.rename(blender_generate_path_file, file_dest_path_rendu + ".jpg")
                            tag_img.tag(LOGO_PATH,file_dest_path_rendu + ".jpg")
                        else:
                            print 'Skip rendu ' + file + ' in ' + folder
    else:
        print 'Destination folder failed'
else:
    print '[usage]: python ' + sys.argv[0] + ' "blender path" ' +'"source folder" ' + '"destination folder"'



