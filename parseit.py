import argparse
import re
import os.path
import pandas as pd
#
# 
#
#
#
#
#
#
#
###


def setup():
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.max_rows', 10)

    parser = argparse.ArgumentParser(description='text search engine - processes only .txt files', prog='parseit.py')
    parser.add_argument('dir_names', type=str, nargs='+', help='target directory(ies) to be searched')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    #*GB* *ToDo* add flag for case-sensitive or not
    return parser

def get_args():
    args = parser.parse_args()
    for dir in args.dir_names:
        if not os.path.isdir(dir):
            print (dir + ': not a directory - exiting ...')
    return args

def scandir(dir):
    with os.scandir(dir) as it:
        df_dict={} # create empty dictionary to store file contents to load into pd.df
        for entry in it:
            if entry.name.endswith('.txt') and entry.is_file():
                with open(entry, 'r') as in_file:
                    line = in_file.read().replace("\n", " ")
                    df_dict.update({entry.name : line})
        #print(df_dict)
        print(str(len(df_dict)) + ' file(s) read in directory ' + dir)

    df2=pd.DataFrame.from_dict(df_dict, orient='index', columns=['contents'])

    print(df2)
    return df2

def test_setup():
    assert setup() == True
def test_scandir():
    assert scandir('./') == True
#####################################
# Entry 
#####################################
parser=setup()
args=get_args()
for dir in args.dir_names: # might remove list of dirs to single dir *GB* *ToDo*
    df2=scandir(dir)

while True:
    TrueorFalse = False
    search_terms = input('search> ') # get input search terms
    if search_terms=="": # if the input is empty - end the program
        break
    spl_txt = re.split('\'',search_terms) # produce a list of search terms delimited by quotes and spaces and nl
    print(spl_txt)
    spl_txt.remove('') # remove empty strings
    print(spl_txt)
    for term in spl_txt:  # remove trailing spaces
        
        term.rstrip() 
        print ('*'+term+'*')

        df3=df2[df2['contents'].str.contains(term, case=TrueorFalse, regex=False)]
   
  
        print(df3)
        input()