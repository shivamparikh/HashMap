# Created by Shivam Parikh
#  Application for KPCB Fellows Program, 2017-2018
#  Fixed Length HashMap Testing

from hash import HashMap
import time

def short_test():
    list1 = ["s", "h", "i", "v", "a", "m"]
    list2 = ["p", "a", "r", "i", "k", "h"]

    h = HashMap(5)
    for i in range(len(list1)):
        h.set(list1[i], list2[i])

def all_character_test(num_chars, offset):
    ls = gen_test(num_chars)
    t0 = time.time()
    h = HashMap(num_chars*26, offset)
    t1 = time.time()
    print("Construction time for size %s was %s" % (num_chars*26, t1-t0))
    t1 = time.time()
    for each in ls:
        h.set(each[0], each[1])
    t2 = time.time()
    print("Insertion time for size %s was %s" % (num_chars*26, t2-t1))
    return h


def gen_test(num):
    base = ""
    ls = []
    for i in range(num):
        for b in range(26):
            ls.append((base+chr(97+b), (i+1)*(b+1)))
        base = chr(97+i)
    return ls


print("Running Test On Speed Optimized Parameter")
a1 = all_character_test(3, 0)
print("Trying to add element 'xyz' with value 999 %s" % a1.set("xyz", 999))
print("Trying to get element 'aa' with value --> %s" % a1.get("aa"))
print("Trying to delete element 'aa'? %s " % a1.delete("aa"))
print("Trying to delete element 'xyz' should not exist? %s " % a1.delete("xyz"))
print(a1)

print("Running Test On Memory Optimized Parameter")
a2 = all_character_test(3, 1)
print("Trying to add element 'xyz' with value 999 %s" % a2.set("xyz", 999))
print("Trying to get element 'aa' with value --> %s" % a2.get("aa"))
print("Trying to delete element 'aa'? %s " % a2.delete("aa"))
print("Trying to delete element 'xyz' should not exist? %s " % a2.delete("xyz"))
print(a2)
