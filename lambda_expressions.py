name = lambda first_name, last_name: first_name.strip().title() + " " + last_name.strip().title()


def fullname(first_name, last_name):
    return name(first_name, last_name)


print(fullname(' chaRles', 'OKoyoH'))
