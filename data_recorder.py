import json
import os

class DataRecorder:
    def __init__(self, json_file="/Users/an-opunch/An/USTC/Work/Find_cite_Scripts/help_us_quickly_registe/research_data.json"):
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

def get_paper_name(paper_name):
    recorder.get_paper_name(paper_name)

def get_fellow_authors(authors_list):
    recorder.get_fellow_authors(authors_list)

def get_universities(universities_list):
    recorder.get_universities(universities_list)

def get_countries(countries_list):
    recorder.get_countries(countries_list)

def finalize_current_entry():
    recorder.finalize_current_entry()

def main():
    print("开始测试数据记录功能...")
    
    # 测试第一条完整记录
    print("\n1. 测试第一条记录:")
    get_paper_name("Attention Is All You Need")
    authors1 = [
        ["Ashish Vaswani", "IEEE Fellow", "谷歌院士", "JMLR", ""],
        ["Noam Shazeer", "", "", "", ""]
    ]
    get_fellow_authors(authors1)
    get_universities(["Google", "University of Toronto"])
    get_countries(["美国", "加拿大"])
    finalize_current_entry()
    print("第一条记录完成")
    
    # 测试第二条记录
    print("\n2. 测试第二条记录:")
    get_paper_name("BERT: Pre-training of Deep Bidirectional Transformers")
    authors2 = [
        ["Jacob Devlin", "", "", "", ""],
        ["Ming-Wei Chang", "ACM Fellow", "", "Nature AI", ""]
    ]
    get_fellow_authors(authors2)
    get_universities(["Google AI", "University of Washington"])
    get_countries(["美国"])
    finalize_current_entry()
    print("第二条记录完成")
    
    # 测试第三条记录 - 包含图灵奖获得者
    print("\n3. 测试第三条记录:")
    get_paper_name("Deep Learning")
    authors3 = [
        ["Ian Goodfellow", "IEEE Fellow", "", "", ""],
        ["Yoshua Bengio", "ACM Fellow", "加拿大院士", "Neural Networks", "图灵奖"],
        ["Aaron Courville", "", "", "", ""]
    ]
    get_fellow_authors(authors3)
    get_universities(["University of Montreal", "MIT"])
    get_countries(["加拿大", "美国"])
    finalize_current_entry()
    print("第三条记录完成")
    
    # 读取并显示最终结果
    print("\n4. 最终JSON文件内容:")
    try:
        with open("research_data.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(json.dumps(data, ensure_ascii=False, indent=2))
    except FileNotFoundError:
        print("JSON文件未找到")
    
    print("\n测试完成！")

if __name__ == "__main__":
    main()