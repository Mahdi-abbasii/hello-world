import os 


Directory=os.getcwd()

def Is_Name_Directory(Root_Path='.',Target_ext='.c'):
    Extensions=set()
    List_File=[]
    for Dirpath, Dirnames, Filenames in os.walk(Root_Path):
        for dirname in Dirnames:
            print( os.path.join(Dirpath,'\n','\n','\t','is name:',dirname))
            
        for FaleName in Filenames:
            _,ext=os.path.splitext(FaleName)
            if ext.lower()==Target_ext:
                 Extensions.add(ext.lower()) 
                 List_File.append(os.path.join(Dirpath,FaleName))
                

                 print(List_File)


        File=open('Directory_File_c.txt','w')  
        for Path in List_File:  
           File.write(Path+'\n')
(Is_Name_Directory(Directory))


