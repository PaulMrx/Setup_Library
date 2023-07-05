
def add_setup():
    '''get data and add it to csv file'''
    print()
    domain = input("domain ").strip().title()
    project = input("project ").strip().title()
    name = input("name ").strip().title()
    version = input("version ").strip()
    print()
    add_to_csv(domain, project, name, version)

def add_to_csv(domain="FX", project = None, name = None, version="v00"):
    '''Add setup data to csv file'''
    with open("setup_list.csv", "a", encoding="utf8") as file:
        file.write(f"{domain},{project},{name},{version} \n")


if __name__ == "__add_setup__":
    add_setup()