import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def create_proj(proj_name: str):
    struct = []
    folder_root = os.path.join(BASE_DIR, proj_name)
    folder_1 = os.path.join(folder_root, 'settings')
    folder_2 = os.path.join(folder_root, 'mainapp')
    folder_3 = os.path.join(folder_root, 'adminapp')
    folder_4 = os.path.join(folder_root, 'authapp')
    struct.extend((folder_1, folder_2, folder_3, folder_4))
    if os.path.exists(folder_root):
        raise FileExistsError(
            f'проект с именем {proj_name} уже существует')
    else:
        os.makedirs(folder_root)
        for name in struct:
            os.makedirs(name)


create_proj('new_project')
