outer_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
inner_list = ["h", "i", "j"]
outer_list[2][1][2].extend(inner_list)

print(outer_list)

#['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']