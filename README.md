# Clinter - A Validator for Claude Skills

## Format Validation

Claude skills require a specific format in their `SKILL.MD` file in order to properly serve their purpose and import cleanly. This can be done manually or reliant on a model, but this risks hallucination and oversight. Instead, a robust validator can quicken the process and increase its effectiveness.

## Linting Steps

See the Complete Guide to Writing Claude Skills below to see a comprehensive list of steps this linter takes to ensure proper formatting (page 10).

## Setup

Dependencies: Python 3

### Windows

Set up pipx and setuptools:

```powershell
pip install pipx setuptools
pipx ensurepath
```

Close the terminal window, then run:

```powershell
git clone https://github.com/spiritualhost/clinter.git
cd clinter
pipx install --editable .
pipx ensurepath
```

### Arch

Set up pipx and setuptools:

```bash
sudo pacman -S python-pipx python-setuptools
pipx ensurepath
exec $SHELL
```

Get the program set up:

```bash
git clone https://github.com/spiritualhost/clinter.git
cd clinter
pipx install --editable .
pipx ensurepath
exec $SHELL
```

## Invocation

### Single File

```bash
clinter -f {path/to/SKILL.md}
```

### Full Directory

```bash
grep -rl " " --include="SKILL.md" | xargs -I{} clinter -f {}
```

## Updates

```bash
cd clinter
git pull
```

## Removal

```bash
pipx uninstall clinter
```

## Future Improvements

* Handling of multi-line descriptions
* Handling of optional fields in frontmatter

## Resources

* [Complete Guide to Writing Claude Skills](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)
