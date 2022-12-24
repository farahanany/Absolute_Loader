#!/Users/macbookpro/PycharmProjects/pythonProject1/main.py
import string
import pandas as pd
import tabloo
import os

ans=input('Enter to say whether the input is SIC or SIC/XE: ')
var1='SIC'
var2='SIC/XE'
flag=0
if ans==var1:
    flag=1
elif ans==var2:
    flag=0
if flag==1:
 df = pd.read_fwf('input.txt', header=None)
 df_list = df.values.tolist()

 res = []
 #using the first one that has the header
 for ele in df_list[0]:
    if ele.strip():
        res.append(ele)

 wanted = []
 #using the first one that has the header
 for ele in df_list[len(df_list)-2]:
    if ele.strip():
       wanted.append(ele)
#using the first one before the last that has the last address
 wanted_string = ' '.join(wanted)
 var_end=wanted_string[1:7]
 modi_end=hex(int(var_end,16))
 my_str = ' '.join(res)
 my_str=my_str.replace(" ", "")
 size = len(my_str)
 mod_string = my_str[:size - 6]
 start_length=mod_string[-6:]
 base16int = int(start_length, 16)
 hex_value = hex(base16int)
 start_length=hex_value
 df2 = pd.DataFrame(columns = ['Address', '0', '1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'])
 c_d = modi_end[-1:]
 if c_d != 0:
    sum = hex(int(modi_end, 16) - int(c_d, 16))
    sum = hex(int(sum, 16) + int('10', 16))
 elif c_d == 0:
    sum = modi_end

 addresses = []
 count = start_length
 while count <= sum:
    addresses.append(count)
    count = hex(int(count, 16) + int('10', 16))
 import numpy as np
 numpy_arr = np.array(addresses)
 numpy_list = numpy_arr.tolist()
 df2 = pd.DataFrame(columns = ['0', '1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'],index=numpy_list)
 size_T=len(df_list)-2
 df_list.pop(0)
 size_of_list=len(df_list)
 df_list.pop(size_of_list-1)
 # input parsing
 i = 0
 while i < len(df_list):
   result=str(df_list[i])
   result=result.replace('T','')
   df_list[i]=result
   i = i + 1
 count=len(df_list)
 import array
 import re

 for i in df_list:
    sth = i[4:8]
    # getting header for each one
    firstSix = "0x" + sth
    print(firstSix)

    # getting length of the text record
    sth2 = i[8:10]
    print(sth2)
    sth3 = int(sth2, 16)
    # counter so i knnow how many times i will separate the list item
    sth4 = i[10:len(i) - 2]
    # getting the ACTUAL TEXT RECORD
    print(sth4)
    partitions = re.findall('..', sth4)
    print(partitions)
    iterations = len(partitions)
    # adjusting it to get the location
    sth6 = i[4:7]
    # here im getting the row
    my_row = "0x" + sth6 + "0"
    # where i land please
    col = firstSix[-1].lower()
    print("column", col)

    for x in range(iterations):
        df2.loc[my_row][col] = partitions[x]
        if col == 'f':
            my_row = hex(int(my_row, 16) + int('10', 16))
            col = '0'
        else:
            # conversions to get to the colmn that i want
            temp = hex(int(col, 16) + int('1', 16))
            print(temp[-1])
            col = str(temp[-1])

 print(df2)

 from pandasgui import show
 show(df2)

#import tabloo

#tabloo.show(df2)
else:
    print(ans)
    df5 = pd.read_fwf('input2.txt', header=None)
    est = df5.values.tolist()


    def listToString(s):
            # initialize an empty string
            string = ""

            # traverse in the string
            for element in s:
                string += element

                # return string
            return string
            # here im gettinng the names and the number of the control sections


    counting_prog = 0
    control_sections = []
    sections_addresses = []
    sections_lengths = []
    for i in est:
        list_element = listToString(i)
        if list_element[0] == 'H':
            counting_prog = counting_prog + 1
            control_sections.append(list_element[1:7])
            print(list_element[1:7])
            print(list_element[8:14])
            sections_lengths.append(hex(int(list_element[-6:], 16)))
            sections_addresses.append(hex(int(list_element[8:14], 16)))

    import numpy as np

    control_arr = np.array(control_sections)
    control_list = control_arr.tolist()

    e_s = pd.DataFrame(index=None, columns=['Control Section', 'Address', 'Length'])
    e_s['Length'] = sections_lengths
    e_s['Control Section']=control_list
    e_s['Address']=sections_addresses
    wanted_address = "0x"

    for i in range(counting_prog):
        if i != 0:
            wanted_address = e_s.loc[i]['Address']
            wanted_address2 = e_s.loc[i - 1]['Address']
            wanted_address = wanted_address[2:]
            wanted_address2 = wanted_address2[2:]
            address_to_be_added = e_s.loc[i - 1]['Length']
            address_to_be_added = address_to_be_added[2:]
            print(wanted_address)
            print(address_to_be_added)
            wanted_address = hex(int(wanted_address, 16) + int(address_to_be_added, 16) + int(wanted_address2, 16))
            e_s.loc[i]['Address'] = wanted_address

    import re

    definition_section = []
    definition_address = []
    counting_prog2 = 0
    size_wanted = 0
    counting = 0
    counter = 0
    for i in est:
        list_element2 = listToString(i)

        if list_element2[0] == 'D':
            counting_prog2 = counting_prog2 + 1
            slices = re.findall('......', list_element2[1:])

            for m in slices:

                if counter % 2 != 0:
                    print(hex(int(m, 16) + int(e_s.loc[counting]['Address'], 16)))
                    definition_address.append(hex(int(m, 16) + int(e_s.loc[counting]['Address'], 16)))
                counter = counter + 1

            counting = counting + 1
            counter2 = 0
            for m in slices:

                if counter2 % 2 == 0:
                    definition_section.append(m)
                counter2 = counter2 + 1

    s_t_2 = pd.DataFrame()
    s_t_2['Symbol Name']=definition_section
    s_t_2['Symbol Address']=definition_address
    print(s_t_2)
    print(e_s)
#GENERATING THE EXTERNAL SYMBOL TABLE
    with open('Ext_Sym_Table.txt', mode='w') as file_object:
      print(s_t_2, file=file_object)
      print(e_s,file=file_object)