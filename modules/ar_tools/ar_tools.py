import os
import subprocess
import re

def extract_deb(file,destination):
    """ 
    extract .deb file with ar 
    Parameters:
        srcPath: path to deb file
        dstPath: root to extract to
    """
    # execute ar x on .dep
    # call tar xf on 
    pass

def extract_tar(file,destination):
    """
    extract files from extracted from .deb (control.x, data.x ) with tar xf
    """
    cmd = "tar xf" + fileName + " -C " + destination
    subprocess.check_output(get_deb.split(), stderr=subprocess.DEVNULL)

    
def extract_control_files():
    """
    extract 
    """
    pass









if __name__ == '__main__':
    # not ment to be called directly
    pass