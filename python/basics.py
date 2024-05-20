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


tpl = ("a", "b", "c")
tpl2 = ("a",)
tpl3 = ("abc")
# tpl[0] = "f"                                               # Error (You can't change tuple)
new = tpl + tpl2
tpl *= 3
print("a" in tpl, "f" not in tpl)
tpl4 = tuple(string)
print(tpl4)
txt = "!".join(tpl4)
a, b, c, d, e = tpl4
print(a, b, c, d , e)