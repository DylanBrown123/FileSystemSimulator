def mk_dir(file_sys, curr_dir):
    for i, sublist in enumerate(file_sys):
        if curr_dir in sublist:
            return i
    return -1

#    file_sys.insert(ins_posn, file_nam)
#    return file_sys
