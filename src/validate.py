# Class to validate a SKILL.md
import re, os

class Skill:
    # Initialize new skill objects
    def __init__(self, filepath):
        self.filepath = filepath
    
    # Check that the skill folder is in kebab-case
    def folder_name(self):
        skill_folder = os.path.dirname(self.filepath)
        print(skill_folder)
        return 0 

    def frontmatter(self):
        return 0 
