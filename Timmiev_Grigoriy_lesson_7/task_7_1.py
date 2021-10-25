import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def create_proj(proj_name: str = 'my_project',
                fld_1: str = 'settings', fld_2: str = 'mainapp',
                fld_3: str = 'adminapp', fld_4: str = 'authapp'):
    """
    Генерирует  корневую папку с вложенной структурой
    :param proj_name: имя корневой папки
    :param fld_1: а также следующие, задают имена вложенных папок
    """
    struct = []
    folder_root = os.path.join(BASE_DIR, proj_name)
    folder_1 = os.path.join(folder_root, fld_1)
    folder_2 = os.path.join(folder_root, fld_2)
    folder_3 = os.path.join(folder_root, fld_3)
    folder_4 = os.path.join(folder_root, fld_4)
    struct.extend((folder_1, folder_2, folder_3, folder_4))
    try:
        os.makedirs(folder_root)
    except FileExistsError as err:
        print(f'{err} проект с именем {proj_name} уже существует')
    else:
        for name in struct:
            os.makedirs(name)


create_proj('new_project')
