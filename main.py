import json
import os

class DataRecorder:
    def __init__(self, json_file="research_data.json"):
        self.json_file = json_file
        self.data = []
        self.current_entry = {
            "引用论文": "",
            "著名学者（院士+IEEE/ACM Fellow）": "",
            "国际期刊主编": "",
            "国家": "",
            "所有机构": "",
            "知名荣誉获得者（诺贝尔、图灵奖等）": ""
        }
        self._load_data()
    
    def _load_data(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, 'r', encoding='utf-8') as f:
                loaded_data = json.load(f)
                if isinstance(loaded_data, list):
                    self.data = loaded_data
                else:
                    self.data = []
    
    def _save_data(self):
        with open(self.json_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
    
    def _reset_current_entry(self):
        self.current_entry = {
            "引用论文": "",
            "著名学者（院士+IEEE/ACM Fellow）": "",
            "国际期刊主编": "",
            "国家": "",
            "所有机构": "",
            "知名荣誉获得者（诺贝尔、图灵奖等）": ""
        }
    
    def _finalize_entry(self):
        if self.current_entry["引用论文"]:
            self.data.append(self.current_entry.copy())
            self._save_data()
            self._reset_current_entry()
    
    def get_paper_name(self, paper_name):
        if self.current_entry["引用论文"]:
            self._finalize_entry()
        
        if paper_name and paper_name.strip():
            self.current_entry["引用论文"] = paper_name.strip()
    
    def get_fellow_authors(self, authors_list):
        fellow_names = []
        for author_info in authors_list:
            if len(author_info) >= 5:
                name = author_info[0]
                ieee_fellow = author_info[1] if author_info[1] else ""
                academy_member = author_info[2] if author_info[2] else ""
                
                fellow_parts = []
                if ieee_fellow:
                    fellow_parts.append(ieee_fellow)
                if academy_member:
                    fellow_parts.append(academy_member)
                
                if fellow_parts:
                    fellow_str = f"{name} ({', '.join(fellow_parts)})"
                    fellow_names.append(fellow_str)
        
        self.current_entry["著名学者（院士+IEEE/ACM Fellow）"] = "/".join(fellow_names) if fellow_names else ""
        
        editor_names = []
        for author_info in authors_list:
            if len(author_info) >= 5:
                name = author_info[0]
                journal_editor = author_info[3] if author_info[3] else ""
                
                if journal_editor:
                    editor_str = f"{name} ({journal_editor})"
                    editor_names.append(editor_str)
        
        self.current_entry["国际期刊主编"] = "/".join(editor_names) if editor_names else ""
        
        honor_names = []
        for author_info in authors_list:
            if len(author_info) >= 5:
                name = author_info[0]
                honor = author_info[4] if author_info[4] else ""
                
                if honor:
                    honor_str = f"{name} ({honor})"
                    honor_names.append(honor_str)
        
        self.current_entry["知名荣誉获得者（诺贝尔、图灵奖等）"] = "/".join(honor_names) if honor_names else ""
    
    def get_universities(self, universities_list):
        if universities_list:
            filtered_unis = [uni for uni in universities_list if uni and uni.strip()]
            self.current_entry["所有机构"] = "/".join(filtered_unis) if filtered_unis else ""
    
    def get_countries(self, countries_list):
        if countries_list:
            filtered_countries = [country for country in countries_list if country and country.strip()]
            self.current_entry["国家"] = "/".join(filtered_countries) if filtered_countries else ""
    
    def finalize_current_entry(self):
        self._finalize_entry()

recorder = DataRecorder()

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

def finalize_current_entry():
    recorder.finalize_current_entry()

def main():
    print("Start registering data...")

    while True:
        # 测试第一条完整记录
        paper_name = get_paper_name()
        recorder.get_paper_name(paper_name)
        authors = get_fellow_authors()
        recorder.get_fellow_authors(authors)
        universities = get_universities()
        recorder.get_universities(universities)
        countries = get_countries()
        recorder.get_countries(countries)
        finalize_current_entry()
        print("Finish this paper's data registration.\n")
    

if __name__ == "__main__":
    main()