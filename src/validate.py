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

        # Verify with regex: starts and ends with lowercase/digit, allows hyphens in between -- this could be cleaned up, used multiple times
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
                    print(f"{sys._getframe().f_code.co_name}: line {index}: needs \'---\'")
                    lint = 1
                    pass
            
            elif index == 1:
                if "name" not in line:
                    print(f"{sys._getframe().f_code.co_name}: line {index}: needs 'name' field.")
                    lint = 1
                    pass

                else:
                    # Check that provided name is kebab case and matches folder name 
                    name_slice = line[line.find(' ') + 1:]

                    # Verify with regex: starts and ends with lowercase/digit, allows hyphens in between -- this could be cleaned up, used multiple times
                    kebab_pattern = r'^[a-z0-9]+(-[a-z0-9]+)*$'
                    if not bool(re.match(kebab_pattern, name_slice)):
                        print(f"{sys._getframe().f_code.co_name}: line {index}: name provided not kebab case.")
                        lint = 1
                        pass   
                    
                    # If name doesn't match skill folder name
                    if name_slice != os.path.basename(self.skillfolder):
                        print(f"{sys._getframe().f_code.co_name}: line {index}: name provided doesn't match skill folder name.")
                        lint = 1
                        pass
                    
                    # Follow Anthropic rules around skill naming
                    if "claude" in name_slice or "anthropic" in name_slice:
                        print(f"{sys._getframe().f_code.co_name}: line {index}: name can't contain 'claude' or 'anthropic'.")
                        lint = 1
                        pass                        

            elif index == 2:
                if "description" not in line:
                    print(f"{sys._getframe().f_code.co_name}: line {index}: needs 'description' field.")
                    lint = 1
                    pass

                else:
                    description_slice = line[line.find(' ') + 1:]

                    # Is it possible to check for what the skill does / when to use it here? might require some fuzzy guessing....

                    # See Complete Guide to Building a Skill for Claude Code
                    if len(description_slice) > 1024:
                        print(f"{sys._getframe().f_code.co_name}: line {index}: description must be under 1024 characters.")
                        lint = 1
                        pass

                    # Check for XML tags
                    if "<" in description_slice or ">" in description_slice:
                        print(f"{sys._getframe().f_code.co_name}: line {index}: XML tags present in description.")
                        lint = 1
                        pass                 
                    
                    # Is it possible to check for specific tasks users might say, check for relevant file types?

        return True if not lint else False

        
            

