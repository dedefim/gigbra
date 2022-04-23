import shutil
import os

root_dir = os.path.join(os.path.dirname(__file__), 'my_project1')
dst_dir = os.path.join(os.path.dirname(__file__), 'my_project1', 'templates')
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)
for root, dirs, files in os.walk(root_dir):
    if root.count('templates'):
        for dir1 in dirs:
            if not os.path.exists(os.path.join(dst_dir, dir1)):
                os.makedirs(os.path.join(dst_dir, dir1))
        for file in files:
            scr_file = os.path.join(root, file)
            dst_file = os.path.join(dst_dir, os.path.basename(root))
            if not os.path.dirname(scr_file) == dst_file:
                shutil.copy(scr_file, dst_file)
