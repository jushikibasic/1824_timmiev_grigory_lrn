import os
import shutil
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def sample_copy(proj_name: str = 'my_project', tmp_name: str = 'templates') -> None:
    """
    проверяет наличие шаблонов "*.html" внутри папки "proj_name" и вложенных
    создает внутри папки "proj_name" папку "tmp_name" и копирует в нее все
    папки содержащие шаблоны.
    функция не будет работать ели внутри "proj_name" уже есть папка "tmp_name"
    необходимо задать другое имя при вызове функции.
    :param proj_name: имя проверяемой папки
    :param tmp_name: имя создаваемой папки с шаблонами
    :return: None
    """
    folder = os.path.join(BASE_DIR, proj_name)
    new_dir_templates = os.path.join(folder, tmp_name)
    if not os.path.exists(new_dir_templates):
        os.mkdir(new_dir_templates)
        with open('tmp.txt', 'w+', encoding='utf-8') as fw:
            for roots, dirs, files in os.walk(folder):
                if len(files) > 0:
                    for items in files:
                        if items.endswith('.html'):
                            _ = f'{roots} {items}\n'
                            fw.write(_)
        with open('tmp.txt', 'r', encoding='utf-8') as fr:
            for line in fr:
                path = line.split()[0]
                tmp = line.strip().split('/')[-1]
                names = tmp.split()
                new_dir_plus = os.path.join(new_dir_templates, names[0])
                if not os.path.exists(new_dir_plus):
                    os.mkdir(new_dir_plus)
                copy_name = os.path.join(path, names[1])
                shutil.copy2(copy_name, new_dir_plus)
                _ = os.path.join(BASE_DIR, 'tmp.txt')
                if os.path.exists(_):
                    os.remove(_)
    else:
        print(f'папка с именем {tmp_name} уже присутствует в корне объекта {proj_name}\n'
              f' необходимо задать другое имя для папки с копиями шаблонов')


sample_copy('my_project', 'templates')
