# Class to validate a SKILL.md
import re, os

class Skill:
    # Initialize new skill objects
    def __init__(self, filepath):
        self.filepath = filepath
        self.skillfolder = os.path.dirname(self.filepath)
    
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
    def frontmatter(self):
        return 0 
