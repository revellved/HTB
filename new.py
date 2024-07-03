########## INFO ############################
# Create instruction.md for machine of HTB #
######################        ##############
import os, pathlib, readline

########## INIT ############################
TMP = './helpers/template.md'
PWD = os.path.dirname(os.path.realpath(__file__))
DETAILS_MARK = '$DETAILS_TEMPLATE'
DEFAULT_SAVE = 'StartingPoint/Tier2/'

step: int = 0
placeholder: str = ''
name_machine: str = ''
details: bool = False
details_template: list[str] = []

########## HELPERS #########################
## Input with placeholder
def rlinput(prompt, prefill=''):
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   try:
      return input(prompt)
   finally:
      readline.set_startup_hook()

########## FUNCTIONS #######################
## All Strip!
def allstrip(text: str) -> str:
    return ' '.join(text.split())

## Parse template on lines
def parse_template(line: str, global_template: bool = True):
    global details, details_template, placeholder, name_machine

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
        value = allstrip(rlinput('Value for ' + splits[i] + ': ', placeholder))
        if splits[i] == 'NAME_MACHINE':
            name_machine = value

        splits[i] = value
        if splits[i] == '':
            return ''
        placeholder = ''

    return ''.join(splits)

def fill_details():
    global placeholder, step
    placeholder = 'TASK %i: ' % step
    output = ''
    user_input = ''

    print('\n-- Fill Details')
    while user_input != 'N':
        if user_input == '' or user_input == 'Y':
            step += 1
            placeholder = 'TASK %i: ' % step

            print()
            for line in details_template:
                output += parse_template(line, False)
            output += '\n'
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

########## MAIN ############################
def main():
    print('-- Hello, let\'s generating instruction\n')
    instruction = generate_instruction().replace(DETAILS_MARK, fill_details())
    pathdir = rlinput('\nSave to (dir): ', DEFAULT_SAVE + name_machine)
    if not pathdir.endswith('/'):
        pathdir += '/'

    save(pathdir, instruction)
    
if __name__ == '__main__':
    main()

###### ####
# THE END #
### #######
