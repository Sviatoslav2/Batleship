#n = eval(input("Enter the size: ",))
#n2 = eval(input("Enter the size: ",))
import string

n = 10
n2 = 10

def readFile(file_name ) :#path --> 'NameFile'
    s1 = ''
    lst1 = []
    with open( file_name , 'r' ) as file:
        for line in file:
            s1+=line
    lst1 = [j for i in s1 for j in i ]
    for i in  lst1 :
        if i == '\n':
            lst1.remove(i)
    return lst1

lst_alfabet = [i for i in string.ascii_uppercase]
print(lst_alfabet)
lst_data = readFile('data.txt')
def read_field(lst_data):
    tpl = []
    lst = []
    lst_of_grid = []
    for i in lst_alfabet:
        for j in range(1,n2+1):
            tpl.append(i)
            tpl.append(j)
            tpl = tuple(tpl)
            lst.append(tpl)
            tpl = []

    for i in range(len(lst_data)):
        lst_of_grid.append([lst[i],lst_data[i]])    

    return lst_of_grid
lst_of_grid = read_field(lst_data)
print(lst_of_grid)