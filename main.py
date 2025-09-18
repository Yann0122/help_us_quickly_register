def get_paper_name():
    paper_name = input("Enter the paper name: ")
    return paper_name

def loop_input(prompt):
    s = ""
    while True:
        value = input(f"Enter what {prompt}, or directly press Enter to finish: ")
        if value.lower() == '':
            break
        s += value + ", "
    return s
        

def get_fellow_authors():
    authors_info = []
    while True:
        author_info = []
        author_name = input("Enter author name, or directly press Enter to finish: ")
        if author_name.lower() == '':
            break
        author_info.append(author_name)
        what_fellow = loop_input("fellow")
        author_info.append(what_fellow)
        what_yuanshi = loop_input("院士")
        author_info.append(what_yuanshi)
        author_magazine = loop_input("magazine")
        author_info.append(author_magazine)
        reward = loop_input("reward")
        author_info.append(reward)
        authors_info.append(author_info)
        print(f"Finish registering author: {author_name}\nStart registering next author.\n")
    print("Finish registering all authors.")
    return authors_info

def get_universities():
    universities = []
    while True:
        university = input("Enter university or organization name, or directly press Enter to finish: ")
        if university.lower() == '':
            break
        universities.append(university)
    return universities

def get_countries():
    countries = []
    while True:
        country = input("Enter country name, or directly press Enter to finish: ")
        if country.lower() == '':
            break
        countries.append(country)
    return countries

def test():
    paper_name = get_paper_name()
    fellow_authors = get_fellow_authors()
    universities = get_universities()
    countries = get_countries()
    print("Paper Name:", paper_name)
    print("Fellow Authors Info:", fellow_authors)
    print("Universities:", universities)
    print("Countries:", countries)

if __name__ == "__main__":
    test()