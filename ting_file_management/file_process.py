from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):

    for path in range(len(instance)):

        if instance.search(path)["nome_do_arquivo"] == path_file:
            return 0

    file = txt_importer(path_file)
    dic = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": (file),
        }

    instance.enqueue(dic)

    sys.stdout.write(str(dic))
    return dic


def remove(instance):

    if not instance:
        return sys.stdout.write("Não há elementos\n")

    file_path = instance.dequeue()["nome_do_arquivo"]

    sys.stdout.write(f"Arquivo {file_path} removido com sucesso\n")
