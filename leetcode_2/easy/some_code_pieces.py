# 1. reverse a string or list

my_str = "ABCDE"
reversed_str = my_str[::-1]
print(reversed_str)

# 2. uppercase with the first character of each word

my_str = "what the fuck"
print(my_str.title())

# 3. find all characters in a string
print(''.join(set("ajdjdjfjjdfaklh")))

# 4. print a string or list n times
n = 3
my_str = "abcd"
l = [1, 2, 3]
print(my_str * n)
print(l * 3)

# 5. exchange the values between 2 variables
a, b = 1, 3
a, b = b, a
print(a, b)

# 6. check a symmetry string
my_str = "abcba"
print(my_str == my_str[::-1])

# 7. count the numbers of occurrences
from collections import Counter

my_list = [1, 2, 3, 4, 5, 3, 4]
count = Counter(my_list)
print(count.most_common(1))
print(count[3])

# 8. check elements difference between 2 string
a = 'abc2'
b = '2acb'
count1 = Counter(a)
count2 = Counter(b)
print(count1 == count2)

# 9. try - except - else
a, b = 1, 0
try:
    print(a / b)
except ZeroDivisionError as e:
    print(e)
else:
    print("fucking awesome")
finally:
    # close connection, release resource, ...
    print("end!")

# 10. enumerate to have index + value pairs
my_arr = [1, 2, 3, 4, 5]
for i, value in enumerate(my_arr):
    print(i, value)

# 11. check size of object
import sys

num = 20
print(sys.getsizeof(num), "bytes")

# 12. combine 2 dicts
dict_1 = {'apple': 9, 'banana': 6}
dict_2 = {'banana': 4, 'orange': 8}

combined_dict = {**dict_1, **dict_2}
print(combined_dict)

for k, v in combined_dict.items():
    if k in dict_1 and k in dict_2:
        combined_dict[k] = [v, dict_1[k]]

print(combined_dict)

# 13. flattening the list
l = [[1, 2], [3, 4, 5]]
flatten_list = [ele for sublist in l for ele in sublist]

# 14. get a sample from a list
import random

my_list = [1, 2, 4, 6, 8]
num_samples = 2
samples = random.sample(my_list, num_samples)
print(samples)

# 15. map an integer to a list of numbers
num = 123456
list_of_digits = list(map(int, str(num)))
print(list_of_digits)
list_of_digits = [int(x) for x in str(num)]
