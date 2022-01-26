def word_counter(l):
    count={ }
    for i in l:
        count[i]=l.count(i)
    return count
print(word_counter("surajshisavk"))
