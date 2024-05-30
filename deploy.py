import os
import shutil

source_dir = 'C:\Users\Mateusz\deployment'

target_dir = '/home/kolesny/deployment'

shutil.copytree(source_dir, target_dir)

print('Deployment successful!')
