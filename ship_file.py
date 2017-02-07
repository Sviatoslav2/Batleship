import read_data
import string
lst_data = read_data.readFile('data.txt')
lst_of_grid = read_data.read_field(lst_data)
lst_alfabet = [i for i in string.ascii_uppercase]
def has_ship(lst_of_grid,tpl_ship):
    for i in lst_of_grid:
        if (tpl_ship == i[0]):
            if (i[1] == '*'):
                return True
            else :
                return False
def ship_size(lst_of_grid: object, tpl_ship: object) -> object:


    n = 0
    if has_ship(lst_of_grid, tpl_ship):
        n = 1
        while (has_ship(lst_of_grid, (tpl_ship[0], tpl_ship[1] + n)) == True):
            n += 1
        while (has_ship(lst_of_grid, (tpl_ship[0], tpl_ship[1] - n)) == True):
            n += 1
        while (has_ship(lst_of_grid, (lst_alfabet[lst_alfabet.index(tpl_ship[0]) + n], tpl_ship[1])) == True):
            n += 1
        while (has_ship(lst_of_grid, (lst_alfabet[lst_alfabet.index(tpl_ship[0]) - n], tpl_ship[1])) == True) :
            n += 1
    return n

print(lst_of_grid)
print(has_ship(lst_of_grid,('A',0)))
print('size = ',ship_size(lst_of_grid,('C',5)))
                
