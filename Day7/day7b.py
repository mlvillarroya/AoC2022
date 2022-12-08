class file():
    def __init__(self,name,size):
        self.name = name
        self.size = size


class folder():
    def __init__(self, name):
        self.name = name
        self.files = []
        self.subfolders = []
        self.parent = None
        
    def __str__ (self):
        return f'Folder: {self.name}'
    
    def add_file(self,file):
        self.files.append(file)
    
    def add_folder(self,folder):
        self.subfolders.append(folder)
    
    def files_size(self):
        total = 0
        for file in self.files:
            total += file.size
        return total
    
    def total_files_size(self):
        if len(self.subfolders) == 0:
            return self.files_size()
        else: 
            total = 0
            for subfolder in self.subfolders:
                total += subfolder.total_files_size()
            return total + self.files_size()
    
alist = [line.rstrip().split(' ') for line in open('Day7/input.txt')]

def search_folder(folder_list,name):
    for folder in folder_list:
        if folder.name == name:
            return folder
    raise Exception('Folder not found')


root = folder('/')
folder_list = [root]
current_folder = root
for line in alist:
    if line[0] == '$':
        if line[1] == 'cd' and line[2] == '/':
            pass   
        elif line[1] == 'cd' and line[2] != '..':
            current_folder = search_folder(current_folder.subfolders,line[2])
        elif line[1] == 'cd' and line[2] == '..':
            current_folder = current_folder.parent
        elif line[1] == 'ls':
            pass
    elif line[0] == 'dir':
        new_folder = folder(line[1])
        folder_list.append(new_folder)
        current_folder.subfolders.append(new_folder)
        new_folder.parent = current_folder
    else:
        new_file = file(line[1],int(line[0]))
        current_folder.add_file(new_file)

needed_space = 30000000 - (70000000 - int(search_folder(folder_list,'/').total_files_size()))
free_space = []
for afolder in folder_list:
    if afolder.total_files_size() > needed_space:
        free_space.append(afolder.total_files_size())
free_space.sort()
print(free_space[0])

