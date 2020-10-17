import click, os, shutil



def cli():

    path = 'D:\Misc'

    sourcepath=path
    sourcefiles = os.listdir(sourcepath)
    destinationpath = path + '\PYTHON-FILES'
    for file in sourcefiles:
        if file.endswith('.py'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
            

    sourcepath=path
    sourcefiles = os.listdir(sourcepath)
    destinationpath = path + '\PICTURES'
    for file in sourcefiles:
        if file.endswith('.png'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
        if file.endswith('.jpeg'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
        if file.endswith('.jpg'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
        if file.endswith('.gif'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
        if file.endswith('.jiff'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
        if file.endswith('.psd'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
        if file.endswith('.jfif'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))


    sourcepath=path
    sourcefiles = os.listdir(sourcepath)
    destinationpath = path + '\EXECUTABLES'
    for file in sourcefiles:
        if file.endswith('.exe'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))


    sourcepath=path
    sourcefiles = os.listdir(sourcepath)
    destinationpath = path + '\MS-WORD-DOCS'
    for file in sourcefiles:
        if file.endswith('.doc'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
        if file.endswith('.docx'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
        

    sourcepath=path
    sourcefiles = os.listdir(sourcepath)
    destinationpath = path + '\PDF'
    for file in sourcefiles:
        if file.endswith('.pdf'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
 
    sourcepath=path
    sourcefiles = os.listdir(sourcepath)
    destinationpath = path + '\TEXT-DOCS'
    for file in sourcefiles:
        if file.endswith('.txt'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
