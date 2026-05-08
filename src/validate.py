# Class to validate a SKILL.md
import re, os

class Skill:
    # Initialize new skill objects
    def __init__(self, filepath):
        self.filepath = filepath
    
    # Check that the skill folder is in kebab-case
    def folder_name(self) -> bool:
        # Get just the folder's name, not the full path
        skill_folder = os.path.basename(os.path.dirname(self.filepath)) 

        # Verify with regex: starts and ends with lowercase/digit, allows hyphens in between
        kebab_pattern = r'^[a-z0-9]+(-[a-z0-9]+)*$'
        return bool(re.match(kebab_pattern, skill_folder))

    def frontmatter(self):
        return 0 
