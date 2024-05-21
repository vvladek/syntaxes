# python --version


# print("Hello world")
# input("Write text: ")


n = 1 + 1 - 1 * 1 / 1 // 1 ** 1                            # 1.0 Exponentiation has priority except for operations in parentheses


string = ("a" + "-") * 2 + "a"                             # a-a-a
multi_line_string = """
Hello world!
This string is multi-line!
"""


last_char = string[-1]                                     # Common pattern for everything
length = len(string)                                       # Common pattern for everything


lst = [True, False, None, None, float(n), str(n), int(n)]  # [True, False, None, None, 1.0, '1.0', 1]
del lst[0]                                                 # [False, None, None, 1.0, '1.0', 1]
print(lst.pop(0), lst.pop())                               # [None, None, 1.0, '1.0'] "pop" got and deleted first and last item
lst.remove(None)                                           # lst has 2 items None. Operator "remove" deleted only the first one
lst.reverse()                                              # ['1.0', 1.0, None]
lst.clear()                                                # []
lst.append(4)                                              # [4]
lst += sorted([1, 3, 2])                                   # [4, 1, 2, 3]
lst.sort(reverse=True)                                     # [4, 3, 2, 1]
lst.extend(list(string))                                   # [4, 3, 2, 1, 'a', '-', 'a', '-', 'a']
lst.insert(1, "a")                                         # [4, 'a', 3, 2, 1, 'a', '-', 'a', '-', 'a']
print(lst.index("a"), lst.index("a", 4, -1))               # 1 5 (4 and -1 are start and end of search)
print("a" in lst, lst.count("a"))                          # True 4 (lst has "a" and lst has 4 items "a")
new_lst = string.split("-") + string.split()               # ['a', 'a', 'a', 'a-a-a']
print("_".join(new_lst))                                   # a_a_a_a-a-a ("join" only works with string items)


tpl = ("a", "b", "c")                                      # You can't change data in tuple
new_tpl = tpl + ("a",) + tuple("abc")                      # ('a', 'b', 'c', 'a', 'a', 'b', 'c')
tpl *= 2                                                   # ('a', 'b', 'c', 'a', 'b', 'c')
print("a" in tpl, "b" not in tpl)                          # True False
txt = "!".join(tpl)                                        # a!b!c!a!b!c
e1, e2 = ("a", "b")                                        # tuple unpacking works for a list too
list_from_tuple = list(tpl)                                # ['a', 'b', 'c', 'a', 'b', 'c']


print("abcdef"[1:-1])                                      # bcde
print("abcdef"[1:])                                        # bcdef
print("abcdef"[:2])                                        # ab
print("abcdef"[1:-1:2])                                    # bd (last number 2 is sampling step)
print("abcdef"[::2])                                       # ace
print("abcdef"[:])                                         # abcdef (The entire slice may be needed to copy the original object)
print("abcdef"[::-1])                                      # fedcba (Reverse object)
new_lst_from_tuple = list(tuple("abcdef"))
del new_lst_from_tuple[1:4]                                # Slice is also used to delete data
print(new_lst_from_tuple)                                  # ['a', 'e', 'f']