import os

Root = os.path.dirname('lib')
project_name = 'my_project'
paths1 = [os.path.join('settings'), os.path.join('mainapp'), os.path.join('adminapp'), os.path.join('authapp')]
for paths2 in paths1:
    os.makedirs(os.path.join(Root, paths2), exist_ok=True)
