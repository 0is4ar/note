import os
import sys

def analy(dirname):

    for basename,dirname,filenames in os.walk(dirname):
        for file in filenames:
            try:
                notename = file.split('.')[0]
                type = file.split('.')[1]
                if type == 'md':
                    print('* '+'['+notename+']'+'('+basename+'/'+file+')')
            except:
                pass

def main():
    analy(sys.argv[1])

if __name__ == "__main__":
    main()
