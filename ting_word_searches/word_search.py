def exists_word(word, instance):
    resul = []
    corr_word = []

    for index, line in enumerate(instance.search(0)["linhas_do_arquivo"]):
        if word.lower() in line.lower():
            corr_word.append({"linha": index + 1})

    if len(corr_word):
        resul.append(
            {
                "palavra": word,
                "arquivo": instance.search(0)["nome_do_arquivo"],
                "ocorrencias": corr_word,
            }
        )
    return resul


def search_by_word(word, instance):
    resul = []
    corr_word = []

    for index, line in enumerate(instance.search(0)["linhas_do_arquivo"]):
        if word.lower() in line.lower():
            corr_word.append(
                {
                    "linha": index + 1,
                    "conteudo": line
                }
            )

    if len(corr_word):
        resul.append(
            {
                "palavra": word,
                "arquivo": instance.search(0)["nome_do_arquivo"],
                "ocorrencias": corr_word,
            }
        )
    return resul
