# Create New App
# Create New Folder("management") 
# Create New Folder("commands") 
# Create New File("rename.py") 

import os

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Renames a Django Project'

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help='The New Django Project Name')

        # parser.add_argument('-p', '--prefix')
    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']

        ##Logic to Rename Project
        ## Replace Demo with current project name 
        files_to_rename = ['demo/settings.py', 'demo/wsgi.py', 'demo/asgi.py', 'manage.py']
        folder_to_rename = 'demo'

        for files in files_to_rename:
            with open(files, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace('demo', new_project_name)

            with open(files, 'w') as file:
                file.write(filedata)

        os.rename(folder_to_rename, new_project_name)                    

        self.stdout.write(self.style.SUCCESS(f'Project has been renamed to {new_project_name}'))






















