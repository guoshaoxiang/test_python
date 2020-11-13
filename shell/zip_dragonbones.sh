#!/bin/bash

user=andy
pass=!QAZ@WSX
folder=armature_ui
porjectPath=/E/haskell_anim/$folder
substr=.zip

function zipRoleArmatureFile() {
	cd $porjectPath
	for filename in `ls`
    do
        if [ -d $filename ]; then
            echo "-> CSV Folders : $filename"
			zip -r -j /E/haskell_anim/zip/$folder/$filename.zip1 ./$filename
        fi
    done
}

function unzipRoleArmatureFile() {
	cd $porjectPath
	for filename in `ls`
    do
        echo "-> CSV Folders : $filename"
		unzip  ./$filename -d ${filename/.zip1/''}
    done
}





function doSelectSign()
{
	
    echo "------------------------- Egret Publish -------------------------"
	echo -e "->\033[36m Enter 1 ZIP ROLE \033[0m"
	echo -e "->\033[36m Enter 2 unZIP ROLE \033[0m"
    echo "-> Enter e Exit"
    echo "--------------------------------------------------------------------------"
    read ANS
    case $ANS in    
	1) 
		echo "-> ZIP ROLE"
        zipRoleArmatureFile
        ;; 
	2) 
		echo "-> ZIP ROLE"
        unzipRoleArmatureFile
        ;; 
		 
    e|E|exit|Exit)
        echo "-> Exit"
        ;;
    *)
    esac
}

doSelectSign





