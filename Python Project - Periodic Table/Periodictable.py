#Period Table of the Elements
#Practice parsing .csv files
#May want to update your pandas to 1.1 for this code to work :)

import csv
import pandas as pd 

#Reading the csv file
File = open('periodictable.csv', encoding='utf-8')
Csvreader = csv.reader(File)
elements = list(Csvreader)
File.close()
csvdata = pd.read_csv('periodictable.csv', header=None)

#Building the Pandas Dataframe
elements = pd.DataFrame(data=csvdata)
elements.reset_index(col_level=1)
elementsheader = [ "Atomic Number", 'Symbol', 'Element', 'Origin of Name', 'Group', 
'Period', 'Atomic weight', 'Density', 'Melting Point', 'Boiling Point', 'Specific Heat Capacity', 
'Electronegativty','Abundance in earth\'s crust']
elements.columns = elementsheader

#Searching dataframe based off of user input
while True:
  print('''            Periodic Table of Elements
           1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
         1 H                                                  He
         2 Li Be                               B  C  N  O  F  Ne
         3 Na Mg                               Al Si P  S  Cl Ar
         4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
         5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
         6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
         7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og
     
                 Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
                 Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr''')
  print('Enter a symbol or atomic number to examine, or QUIT to quit.')
  response = input('> ')
  
  if response.upper() == 'QUIT':
    break

  if response.isdigit():
    response = int(response)
    print(elements.iloc[response -1])
  
  elif not response.isdigit():
    response = str(response.title())
    rownumber  = elements[elements['Symbol'] == response].index
    print(elements.iloc[rownumber])
  else:
    print('try again')
