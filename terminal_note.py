import os
import sys
import multiprocessing

this_dir = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')
note_directory = 'C:/notes/'

note_file_name = 'notes'
note_text = ''
if len(sys.argv) == 3:
    note_file_name = sys.argv[1]
    note_text = sys.argv[2]
elif len(sys.argv) == 2:
    note_text = sys.argv[1]
else:
    print "Atleast 1 argument required"
    exit()



def main():
    try:
        file_path = note_directory + note_file_name + '.txt'
        f = open(file_path, 'a+')
        f.write(note_text + '\n')
        f.close()
        print "Saved"
    except:
        print "Error"



if __name__ == '__main__':
    #BUILD STANDALONE EXECUTABLE:
    #pyinstaller -F automine.py
    multiprocessing.freeze_support()

    main()








