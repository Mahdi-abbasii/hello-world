import os 
import shutil

directory = os.getcwd()
'''dar in bakhsh addrs vard mikonim'''

def is_c_file(directory):
        _,file_extension=os.path.splitext(directory)
        return file_extension=='.c'
    
def is_h_file(directory):
        _,file_extendion_h=os.path.splitext(directory)
        return file_extendion_h=='.h'  
    
if os.path.exists(directory):
    
    files=os.listdir(directory)

  
        
    
    
    
    new_directore=os.path.join(directory,'new_directory.c')
    os.makedirs(new_directore,exist_ok=True)
    '''bra barsi directore kh vojod darad va sakhtan directory jadid bra .c'''
    
    new_directory_h=os.path.join(directory,'new_directore.h')
    os.makedirs(new_directory_h,exist_ok=True)
    '''bra barsi directore kh vojod darad va sakhtan directory jadid bra .h'''
        
        


    for file_name in files:
        if is_c_file(file_name):
                source=os.path.join(directory,file_name)
                destination=os.path.join(directory,file_name)
                shutil.move(source,destination)
         
         
    for file_name_h in files:
        if is_h_file(file_name_h):
             source_h=os.path.join(directory,file_name_h)
             destination_h=os.path.join(directory,file_name_h)
             shutil.move(source_h,destination_h)    
else:
    print(' directory is not file ')    
     