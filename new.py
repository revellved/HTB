########## INFO ############################
# Create instruction.md for machine of HTB #
######################        ##############
import os, pathlib
from re import split

TMP = './helpers/template.md'
PWD = os.path.dirname(os.path.realpath(__file__))
DETAILS_MARK = '$DETAILS_TEMPLATE'

details: bool = False
details_template: list[str] = []

## Parse template on lines
def parse_template(line: str, global_template: bool = True):
    global details, details_template

    if global_template:
        if line.strip() == '</details><br>':
            details = False
            details_template.append(line) 
            return DETAILS_MARK
        elif line.strip() == '<details>':
            details = True
            details_template.append(line) 
            return ''
        elif details == True:
            details_template.append(line)
            return ''
    
    splits = line.split('$')
    for i in range(1, len(splits), 2):
        splits[i] = input('Value for ' + splits[i] + ': ')
        if splits[i] == '':
            return ''

    return ''.join(splits)

def fill_details():
    print('\n-- Fill Details')

    output = ""
    user_input = ''
    while user_input != 'N':
        if user_input == '' or user_input == 'Y':
            print()
            for line in details_template:
                output += parse_template(line, False)
            print()
        user_input = input('Are there any other questions? (Y/n): ').upper()
    
    return output
    

## Get instructuons asked user
def generate_instruction():
    output = ''

    with open(TMP, 'r') as f:
        template = f.readlines()
    
    for line in template:
        output += parse_template(line)

    return output

def save(pathdir, text):
    print('Save to ' + pathdir)

    path = pathlib.Path(PWD + '/' + pathdir)
    path.mkdir(parents=True, exist_ok=True)
    with open(pathdir + 'README.md', 'w') as fp:
        fp.write(text)

## MAIN
def main():
    print('-- Hello, let\'s generating instruction\n')
    instruction = generate_instruction().replace(DETAILS_MARK, fill_details())
    pathdir = input('\nSave to (dir): ')
    if not pathdir.endswith('/'):
        pathdir += "/"

    save(pathdir, instruction)
    
## RUN
if __name__ == '__main__':
    main()

###### ####
# THE END #
### #######
