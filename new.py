########## INFO ############################
# Create instruction.md for machine of HTB #
######################        ##############
import os, pathlib

TMP = './helpers/template.md'
PWD = os.path.dirname(os.path.realpath(__file__))
DETAILS_MARK = '$DETAILS_TEMPLATE'

details: bool = False
details_template: list[str] = []

## Parse template on lines
def parse_template(line: str):
    global details, details_template

    if line == '<details>':
        details = True
        return line + '\n'
    elif line == '</details>':
        details = False
        return DETAILS_MARK + '\n' + line + '\n'
    elif details == True:
        details_template.append(line)
        return ''
    
    splits = line.split('$')
    for i in range(1, len(splits), 2):
        splits[i] = input('Value for ' + splits[i] + ':')

    return '$'.join(splits) + '\n'

def fill_details():
    output = ""
    user_input = 'Y'
    while user_input != 'N':
        if user_input == 'Y':
            for line in details_template:
                output += parse_template(line) + '\n'
        user_input = input('Are there any other questions? (Y/n):').upper()
    
    return output
    

## Get instructuons asked user
def generate_instruction():
    output = ''

    with open(TMP, 'r') as f:
        template = f.readlines()
    
    for line in template:
        line = line.replace('\n', '')
        output += parse_template(line)

    return output

def save(pathdir, text):
    path = pathlib.Path(PWD + '/' + pathdir)
    path.mkdir(parents=True, exist_ok=True)
    with open(pathdir + 'README.md', 'w') as fp:
        fp.write(text)

## MAIN
def main():
    instruction = generate_instruction().replace(DETAILS_MARK, fill_details())
    pathdir = input('Save to (dir):')
    save(pathdir, instruction)
    
## RUN
if __name__ == '__main__':
    main()

###### ####
# THE END #
### #######
