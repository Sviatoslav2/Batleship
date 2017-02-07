n1 = eval(input("Enter the size: ",))
import read_data
import ship_file
import string
import random
lst_data = read_data.readFile('data.txt')
lst_of_grid = read_data.read_field(lst_data)
lst_alfabet = [i for i in string.ascii_uppercase]
def is_valid (lst_of_grid):
    lst = []
    assert isinstance(n1, object)
    n1 = 0
    n2 = 0 
    n3 = 0
    n4 = 0
    if len(lst_of_grid)**(1/2) == n1:
        for i in lst_of_grid:

            if ship_file.ship_size(lst_of_grid, i[0]) == 1:
                lst.append(1)
                n1+=1                
            elif ship_file.ship_size(lst_of_grid, i[0]) == 2:
                lst.append(2)
                n2+=1 
            elif ship_file.ship_size(lst_of_grid, i[0]) == 3:
                lst.append(3)
                n3+=1 
            elif ship_file.ship_size(lst_of_grid, i[0]) == 4:
                lst.append(4)
                n4+=1 

    if (set(lst) == {1,2,3,4})and(n1 == 4)and(n2 == 3)and(n3 == 2)and(n4 == 4):
        return True
    else :
        return False
def  generate_field ():
    s = ''
    lst_of_size = [1,2,3,4]
    for i in range(n1**2):
        s +=' '
    for i in lst_of_size:
        l = random.randint(1, n1 ** 2)
        k = random.randint(1, n1 - 4)
        s[l+k] = '*'
        for j in range(1,i+1):
            s[l + k+j] = '*'
    for i in range(1,n1+1):
        s[i*10]=s[i*10]+'\n'
    return s
str_generate_field = generate_field ()
def writeToFile(X):
    f = open("result.txt", 'w')
    for x in X:
        f.write("{0}, ".format(x))
print(generate_field (generate_field ()))