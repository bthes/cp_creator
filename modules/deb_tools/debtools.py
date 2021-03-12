import os
import subprocess


def download_deb(debName,dstPath):
    """
    download deb via apt-get download
    """
    cmd = "apt-get download " + debname
    os.chroot()