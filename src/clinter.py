# Linter for Claude skills
import argparse, os, inspect
from validate import *

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=filepath, help='provide a filepath to lint.') 
    return parser.parse_args()

# Validate extensions
def filename_validate(desired_name: str, desired_ext: str, filepath: str) -> bool:
    name, extension = os.path.splitext(filepath)
    filename_only = os.path.splitext(os.path.basename(filepath))[0]
    return True if extension == desired_ext and filename_only == desired_name else False

# Validate filepaths
def filepath(filepath: str):
    if os.path.isfile(filepath):
        if filename_validate("SKILL", ".md", filepath):
            return filepath
        else:
            print("Error: bad filename")
            os._exit(1)
    else:
        raise argparse.ArgumentTypeError(f"Invalid path: {filepath}")

# Run all steps in a class
def runall(skill_instance):
    attrs = (getattr(skill_instance, name) for name in dir(skill_instance) if name != '__init__')
    methods = filter(inspect.ismethod, attrs)
    for method in methods:
        try:
            response = method()
            if not response:
                print(f"Lint: method {method.__name__} returned need for linting.")
        except Exception as e:
            print(f"Method error in {method}: {e}")

def main():
    parsed_args = parse_arguments()
    print(parsed_args)

    # Run all linting steps
    skill = Skill(filepath=parsed_args.file)
    runall(skill)

if __name__ == "__main__":
    main()