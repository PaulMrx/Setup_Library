
def main():
    '''get data and add it to csv file'''
    print()
    domain = input("domain ").strip().title()
    project = input("project ").strip().title()
    name = input("name ").strip().title()
    version = input("version ").strip()
    print()
    add_setup(domain, project, name, version)

def add_setup(domain="FX", project = None, name = None, version="v00"):
    '''Add setup data to csv file'''
    with open("setup_list.csv", "a", encoding="utf8") as file:
        file.write(f"{domain},{project},{name},{version} \n")

while True:
    use = input("Do you want to add a setup? ").strip().upper()
    if use == "Y":
        if __name__ == "__main__":
            main()
    else:
        break