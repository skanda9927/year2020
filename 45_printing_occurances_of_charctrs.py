#45. Write a Python program to count repeated characters in a string . Sample string: 'thequickbrownfoxjumpsoverthelazydog’.
#Expected output :
#o 4
#e 3
#u 2
#h 2
#r 2
#t 2



                                            #PSEUDOCODE
                #Step 1 : Input the string
                #Step 2 : Using built in function  len and findall find occurance of each small and Capital character
                #Step 3 : Store occurance of each character in variable count
                #Step 4 : Print the occurance of character if count is greater than zero

import re

# initializing string
test_str = input("enter the string")
print("character occurances in string are")
# using re + findall() to get count

count_a = len(re.findall("a", test_str)) + len(re.findall("A", test_str))
if (count_a>0) :
    print("a:",count_a)
count_b = len(re.findall("b", test_str)) + len(re.findall("B", test_str))
if (count_b>0) :
    print("b:",count_b)

count_c = len(re.findall("c", test_str)) + len(re.findall("C", test_str))
if (count_c>0) :
    print("c:",count_c)

count_d = len(re.findall("d", test_str)) + len(re.findall("D", test_str))
if (count_d>0) :
    print("d:",count_d)

count_e = len(re.findall("e", test_str)) + len(re.findall("E", test_str))
if (count_e>0) :
    print("e:",count_e)

count_f = len(re.findall("f", test_str)) + len(re.findall("F", test_str))
if (count_f>0) :
    print("f:",count_f)
count_g = len(re.findall("g", test_str)) + len(re.findall("G", test_str))
if (count_g>0) :
    print("g:",count_g)
count_h = len(re.findall("h", test_str)) + len(re.findall("H", test_str))
if (count_h>0) :
    print("h:",count_h)
count_i = len(re.findall("i", test_str)) + len(re.findall("I", test_str))
if (count_i>0) :
    print("i:",count_i)
count_j = len(re.findall("j", test_str)) + len(re.findall("J", test_str))
if (count_j>0) :
    print("j:",count_j)
count_k = len(re.findall("k", test_str)) + len(re.findall("K", test_str))
if (count_k>0) :
    print("k:",count_k)
count_l = len(re.findall("l", test_str)) + len(re.findall("L", test_str))
if (count_l>0) :
    print("l:",count_l)
count_m = len(re.findall("m", test_str)) + len(re.findall("M", test_str))
if (count_m>0) :
    print("m:",count_m)
count_n = len(re.findall("n", test_str)) + len(re.findall("N", test_str))
if (count_n>0) :
    print("n:",count_n)
count_o = len(re.findall("o", test_str)) + len(re.findall("O", test_str))
if (count_o>0) :
    print("o:",count_o)
count_p = len(re.findall("p", test_str)) + len(re.findall("P", test_str))
if (count_p>0) :
    print("p:",count_p)
count_q = len(re.findall("q", test_str)) + len(re.findall("Q", test_str))
if (count_q>0) :
    print("q:",count_q)
count_r = len(re.findall("r", test_str)) + len(re.findall("R", test_str))
if (count_r>0) :
    print("r:",count_r)
count_s = len(re.findall("s", test_str)) + len(re.findall("S", test_str))
if (count_s>0) :
    print("s:",count_s)
count_t = len(re.findall("t", test_str)) + len(re.findall("T", test_str))
if (count_t>0) :
    print("t:",count_t)
count_u = len(re.findall("u", test_str)) + len(re.findall("U", test_str))
if (count_u>0) :
    print("u:",count_u)
count_v = len(re.findall("v", test_str)) + len(re.findall("V", test_str))
if (count_v>0) :
    print("v:",count_v)
count_w = len(re.findall("w", test_str)) + len(re.findall("W", test_str))
if (count_w>0) :
    print("w:",count_w)
count_x = len(re.findall("x", test_str)) + len(re.findall("X", test_str))
if (count_x>0) :
    print("x:",count_x)
count_y = len(re.findall("y", test_str)) + len(re.findall("Y", test_str))
if (count_y>0) :
    print("y:",count_y)
count_z = len(re.findall("z", test_str)) + len(re.findall("Z", test_str))
if (count_z>0) :
    print("z:",count_z)
# printing result

