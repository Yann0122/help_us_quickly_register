import pandas as pd
import json
import os

def parse_author(data):

    existing_authors = {}
    for entry in data:
        authors = entry.get("著名学者（院士+IEEE/ACM Fellow）", "")
        authors_list = [s.strip() for s in authors.split("; ") if s]
        for author in authors_list:
            if " (" in author:
                name, details = author.split(" (", 1)
                details = details.rstrip(")")
            else:
                raise ValueError(f"Author format error: {author}")
            if name in existing_authors:
                existing_authors[name]["fellow"] = details
            else:
                existing_authors[name] = {"fellow": details, "editor": "", "award": ""}
        editors = entry.get("国际期刊主编", "")
        editors_list = [s.strip() for s in editors.split("; ") if s]
        for editor in editors_list:
            if " (" in editor:
                name, journal = editor.split(" (", 1)
                journal = journal.rstrip(")")
            else:
                raise ValueError(f"Editor format error: {editor}")
            if name in existing_authors:
                existing_authors[name]["editor"] = journal
            else:
                existing_authors[name] = {"fellow": "", "editor": journal, "award": ""}
        awards = entry.get("知名荣誉获得者（诺贝尔、图灵奖等）", "")
        awards_list = [s.strip() for s in awards.split("; ") if s]
        for award in awards_list:
            if " (" in award:
                name, details = award.split(" (", 1)
                details = details.rstrip(")")
            else:
                raise ValueError(f"Award format error: {award}")
            if name in existing_authors:
                existing_authors[name]["award"] = details
            else:
                existing_authors[name] = {"fellow": "", "editor": "", "award": details}

    return existing_authors

def parse_universities_countries(data):
    universities = set()
    countries = set()
    for entry in data:
        unis = entry.get("所有机构", "")
        counts = entry.get("国家", "")
        uni_list = [s.strip() for s in unis.split("; ") if s]
        countries_list = [s.strip() for s in counts.split("; ") if s]
        for uni in uni_list:
            universities.add(uni)
        for country in countries_list:
            countries.add(country)
    return list(universities), list(countries)

def main():
    json_file = "research_data.json"
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    universities, countries = parse_universities_countries(data)
    authors = parse_author(data)

    df = pd.DataFrame.from_dict(authors, orient='index')
    df.index.name = 'Name'
    df.reset_index(inplace=True)
    with pd.ExcelWriter("research_data.xlsx", engine="openpyxl", mode="w") as writer:
        df.to_excel(writer, sheet_name="authors", index=False)
        uni_country_df = pd.DataFrame({
            "University/Organization": universities,
            "Country": countries + [""] * (len(universities) - len(countries)) if len(universities) > len(countries) else countries[:len(universities)]
        })
        uni_country_df.to_excel(writer, sheet_name="universities&countries", index=False)
        df = pd.DataFrame(data)
        df.to_excel(writer, sheet_name="research_data", index=False)
    print("Data has been successfully written to research_data.xlsx")


if __name__ == '__main__':
    main()