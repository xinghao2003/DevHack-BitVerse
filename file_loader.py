from zipfile import ZipFile
from regex import R
from config import temp_path
import os


def load_files(files, process):
    if (type(files) is not list):
        files = [files]

    for file in files:
        process.write(f"Creating temporary file for {file.name}")
        create_temp_file(file)


def create_temp_file(file):
    initialization()

    bytes_data = file.read()

    if not os.path.exists(temp_path + file.name):
        open(temp_path + file.name, 'xb').write(bytes_data)
    else:
        open(temp_path + file.name, 'wb').write(bytes_data)

    return True


def initialization():
    if not os.path.exists(temp_path):
        os.mkdir(temp_path)


def combine_resumes(resumes):
    # Create a ZipFile Object
    with ZipFile(f'{temp_path}resumes.zip', 'w') as zip_object:
        # Adding files that need to be zipped
        for resume in resumes:
            zip_object.write(
                f'{temp_path}{resume["file"]}', arcname=resume["file"])
            # Check to see if the zip file is created
    if os.path.exists(f'{temp_path}resumes.zip'):
        return True
    else:
        return False
