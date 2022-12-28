import os
class FileReader:
  def __init__(self, path):
    self.path = path
    self.list_files = []
  
  def collect_files(self):
    # Get the list of all files and directories
    self.list_files = os.listdir(self.path)
    self.list_files = [ self.path +'/'+ x for x in self.list_files ]

  def show_files(self):
    for x in range(len(self.list_files)):
      print(x+1, "  ", self.list_files[x])