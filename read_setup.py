import csv

def readsetup():
    dict = []
    with open("setup_list.csv") as csvfile:
        spamreader = csv.reader(csvfile, quotechar = ",")
        for domain, project, name, version in spamreader:
            dict.append({"domain": domain , "project": project, "name": name, "version": version})

    for setup in sorted(dict, key=lambda setup:setup['name'], reverse=True):
        print(f"{setup['domain']} / {setup['project']} / {setup['name']} / {setup['version']}")
        # print(f"{setup['domain']} / {setup['project']}")
 
if __name__ == "__readsetup__":
    readsetup()
