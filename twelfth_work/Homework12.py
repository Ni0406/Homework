import os
class Fail_manage():
    def inspection(self, folder):
        try:
            return os.listdir(path=folder)
        except OSError as ek:
            print(f"Ошибка при перечислении содержимого {folder}: {ek}")
            return []

    def new_dir(self, path):
        if not os.path.isdir(path):
            os.mkdir(path)

    def remove_dir(self, direct):
        if os.path.isdir(direct):
            os.rmdir(direct)
        if os.path.isfile(direct):
            os.remove(direct)

    def copy_file(self, source, destination):
        shutil.copy2(source, destination)
        print(f"Файл {source} успешно скопирован в {destination}")

    def replace_file(self, file, where):
        os.replace(file, where)

    def file_search(self, name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                print(os.path.join(root, name))


    def access_level(self, path, permission):
        os.chmod(path, permission)
