people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    title = person.split()[0]
    firstname = person.split()[1]
    lastname = person.split()[2]
    return '{} {}'.format(title, lastname)


print(list(map(split_title_and_name, people)))