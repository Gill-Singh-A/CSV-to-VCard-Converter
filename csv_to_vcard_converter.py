from os import listdir
from datetime import date
from optparse import OptionParser
from colorama import Fore, Back, Style
from time import strftime, localtime, time

status_color = {
    '+': Fore.GREEN,
    '-': Fore.RED,
    '*': Fore.YELLOW,
    ':': Fore.CYAN,
    ' ': Fore.WHITE,
}

def get_time():
    return strftime("%H:%M:%S", localtime())
def display(status, data):
    print(f"{status_color[status]}[{status}] {Fore.BLUE}[{date.today()} {get_time()}] {status_color[status]}{Style.BRIGHT}{data}{Fore.RESET}{Style.RESET_ALL}")

def get_arguments(*args):
    parser = OptionParser()
    for arg in args:
        parser.add_option(arg[0], arg[1], dest=arg[2], help=arg[3])
    return parser.parse_args()[0]

def makeSingleVCFString(contact):
    return f"BEGIN:VCARD\nVERSION:2.1\nN:{' '.join(contact[0].split(' ')[1:])};{contact[0].split(' ')[0]}\nFN:{contact[0]}\nTEL;CELL;VOICE:{contact[1]}\nREV:{str(date.today()).replace('-', '')}T{strftime('%H%M%S', localtime())}Z\nEND:VCARD\n"
def makeVCFString(contacts):
    return ''.join([makeSingleVCFString(contact) for contact in contacts])
def makeVCF(contacts, file_name):
    with open(file_name, 'w') as file:
        file.write(makeVCFString(contacts))

if __name__ == "__main__":
    data = get_arguments(('-c', "--csv", "cvs", "CVS Files (separated by ',') ('*' for every CSV File present in the Folder)"),
                         ('-v', "--vcf", "vcf", "Name of the Output VCard File (.vcf) (Default=Current Date and Time)"))
    if not data.csv:
        display('-', "Please specify the CSV Files")
        exit(0)
    elif data.csv == '*':
        data.csv = [csv_file for csv_file in listdir() if csv_file.endswith(".csv")]
    else:
        data.csv = data.csv.split(',')
    if not data.vcf:
        current_time = str(strftime("%H_%M_%S", localtime()))
        data.vcf = f"{date.today()} {current_time}.vcf"
    contacts = []
    for csv_file in data.csv:
        try:
            with open(csv_file) as file:
                contacts.extend([line.split(',') for line in file.read().split('\n') if line != ''])
        except FileNotFoundError:
            display('-', f"{Back.MAGENTA}{csv_file}{Back.RESET} not Found")
            continue
        except:
            display('-', f"Error while reading {Back.MAGENTA}{csv_file}{Back.RESET}")
            continue
    makeVCF(contacts, data.vcf)