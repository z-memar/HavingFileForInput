def AskForFileName():
    """This function will ask the use for the name of the input file."""
    file_doesnot_exsit = True
    file_name = None
    while file_doesnot_exsit:
        try:
            file_name = input("What is the name of the input file?")
            file = open(file_name, 'r')
            file_doesnot_exsit = False
        except FileNotFoundError:
            print("File is not found")
    return file_name

def ReadFileContents(file_name):
    """Now, we are going to open and read all the line of the input file through ReadFileContents function.""" 
    all_file_contents = open(file_name, 'r').readlines()
    return all_file_contents

def BuildHeadList(all_file_contents):
    """ Head of the input's file will be shown in this function"""
    head_list = []
    list_all_file_contents = (all_file_contents)
    for line in list_all_file_contents: 
        if line[0:4] != 'ATOM':
            head_list.append(line)
        else:
            break

    return head_list

def BuildAtomList(all_file_contents):
    """ Atom part's of the input's file will be recognize in this function"""
    atom_list = []
    list_all_file_contents = (all_file_contents)
    for line in list_all_file_contents:
        if line[0:4] == "ATOM":
            atom_list.append(line)
    return atom_list

def BuildTailList(all_file_contents):
    """ Tail of the input's file will be shown in BuildTailList function"""
    tail_list = []
    list_all_file_contents = (all_file_contents)
    tail_start = False
    for line in list_all_file_contents:
        word = line[0:3]
        if word == "TER":
            tail_start = True
        if tail_start == True:
            tail_list.append(line)
        if word == "END":
            break
        
    return tail_list

def WriteNewFile(head_list, atom_list, tail_list):
    """ In this function we are goint to make an output that includes head,atom and tail body"""
    file = open("output.txt", 'w')
    output_head = ''.join(map(str,head_list))
    output_atom = ''.join(map(str,atom_list))
    output_tail = ''.join(map(str,tail_list))
    output = ((output_head)+(output_atom)+(output_tail))
    file.write(output)

def Run():
    """ This Run function will run the program"""
    file_name = AskForFileName()
    file_content = ReadFileContents(file_name)
    head_list = BuildHeadList(file_content)
    atom_list = BuildAtomList(file_content)
    tail_list = BuildTailList(file_content)
    WriteNewFile(head_list, atom_list, tail_list)
    
if __name__=='__main__':
    Run()
    
    
