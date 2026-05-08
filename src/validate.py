# Class to validate a SKILL.md
import re, os, sys

class Skill:
    # Initialize new skill objects
    def __init__(self, filepath):
        self.filepath = filepath
        self.skillfolder = os.path.dirname(self.filepath)

        content = []
        with open(self.filepath, 'r', encoding='utf-8') as file:
            for line in file:
                content.append(line.strip())
        self.content = content
    
    # Check that the skill folder is in kebab-case
    def folder_name(self) -> bool:
        # Get just the folder's name, not the full path
        skill_folder = os.path.basename(self.skillfolder) 

        # Verify with regex: starts and ends with lowercase/digit, allows hyphens in between
        kebab_pattern = r'^[a-z0-9]+(-[a-z0-9]+)*$'
        return bool(re.match(kebab_pattern, skill_folder))

    # Check that there isn't a README in the skill folder
    def reject_readme(self) -> bool:
        files = os.listdir(self.skillfolder)
        return False if "README.md" in files else True

    # Check that frontmatter is formatter properly
    def frontmatter(self) -> bool:
        content = self.content
        lint = 0

        for index, line in enumerate(content):
            
            if index == 0 or index == 3:
                if line != "---":
                    print(f"{sys._getframe().f_code.co_name}: line {index} needs \'---\'")
                    lint = 1
                    pass
            
            elif index == 1:
                if "name" not in line:
                    print(f"{sys._getframe().f_code.co_name}: line {index} needs 'name' field.")
                    lint = 1
                    pass
            
            elif index == 2:
                if "description" not in line:
                    print(f"{sys._getframe().f_code.co_name}: line {index} needs 'description' field.")
                    lint = 1
                    pass

        return True if lint == 0 else False

        
            

