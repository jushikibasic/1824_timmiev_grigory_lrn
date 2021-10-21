from task_6_4 import user_hobby_fn


def cli_user_hobby(argv):
    program, file_names_in, file_hobby_in, file_out = argv
    user_hobby_fn(file_names_in, file_hobby_in, file_out)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        sys.exit(3)
    exit(cli_user_hobby(sys.argv))
