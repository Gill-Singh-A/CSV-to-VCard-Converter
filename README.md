# CSV to VCard Converter
A Python Program that Converts the given CSF Files to VCard(.vcf) Format

## Requirements
Language Used = Python3<br />
Modules/Packages used:
* datetime
* optparse
* colorama
* time
<!-- -->
Install the dependencies:
```bash
pip install -r requirements.txt
```

## Input
The csv_to_vcard_converter.py takes the following arguments through the command that is used to run the Python Program:
* '-c',"--csv" : CVS Files (separated by ',') ('*' for every CSV File present in the Folder)
* '-v',"--vcf" : Name of the Output VCard File (.vcf) (Default=Current Date and Time)

## Output
It generates the required VCard File

### Note
The Data inside the CSV File should be present in the following format<br />
>Name,Phone Number