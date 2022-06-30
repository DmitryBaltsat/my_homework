def thesaurus(*args):
    workers_dict = {}
    for name in args:
        val = workers_dict.setdefault(name[0], [name])
        if name not in val:
            workers_dict[name[0]].append(name)
    return workers_dict


print(thesaurus("Вадим Сергеев", "Сергей Иванов", "Константин Евсеев", "Денис Амбарцумян", "Андрей Васильев", "Денис Варфоломеев"))
