people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


def splitnames(person):
    title = person.split()[0]
    firstname = person.split()[1]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

print(list(map(splitnames, people)))