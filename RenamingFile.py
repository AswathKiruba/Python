import os
def rename():
    ### get file names
    file_list = os.listdir(r"C:\Users\aswat\Downloads\prank")

    saved_path = os.getcwd()
    print("current working directory"+saved_path)

    os.chdir(r"C:\Users\aswat\Downloads\prank")

    #rename
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
        

rename()
