

def check_if_duplicates_list(list_of_elems):
    """ Check if given list contains any duplicates """
    set_of_elems = set()
    for elem in list_of_elems:
        if elem in set_of_elems:
            return True
        else:
            set_of_elems.add(elem)
    return False

