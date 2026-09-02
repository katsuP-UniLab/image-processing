import os

def dirCheck (root):
    # Check dir
    if os.path.exists(root + 'out') != True:
        os.mkdir(root + 'out')