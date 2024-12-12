import os

def uniquify_dir(path):
    path = os.path.normpath(path)
    counter = 1

    while os.path.exists(path):
        path = f'{path}_{counter}'
        counter += 1

    return path

def mk_project_dir(dir, run_name):
    path = os.mkdir(uniquify_dir(f'{dir}/{run_name}'))
    return path

def mk_project_img_dir(path):
    path_i = os.mkdir(f'{path}/images/')
    return path_i

def mk_project_vid_dir(path):
    path_v = os.mkdir(uniquify_dir(f'{path}/videos/'))
    return path_v