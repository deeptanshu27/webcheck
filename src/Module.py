import os
from Manager import Manager

class Module:
    def __init__(self, name):
        self.name = name
        self.msg = None
    
    def run(self):
        pass

    def create_dir(self, name):
        dir = Manager.get_dir()
        os.chdir(dir)
        if name not in os.listdir():
            os.mkdir(name)
        return dir + name + "/"