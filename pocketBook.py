def num_of_entries(i):
    """
    Counts number of entries
    this is used to count how many times user has entered something compared to how many entries he would like to make 
    """
    count = 0
    i = int(i)
    if i != 0:
        count = i
        return i

def str_to_list(string):
    li = list(string.split(" ")) 
    return li


def file_creator(f, l):
    """
    Looks for filename in directory,
    if not found will create and write
    if found will append
    """
    import os
    filename = f
    answ=os.path.exists(filename)
    with open(filename, 'a' if answ else "w") as file:
        if(answ):
            file.write("\n")
        file.write(l)

def file_reader(f):
    with open(f, 'r') as fh:
        return fh.read()

def line_count(f, e):
    """
    Uses basic file reading  func above.
    f = file
    e = element to be counted
    """
    count = 0
    file_reader(f)
    for e in f:
        count+=1
    return count

#def count_newline(newlist):
#   """
#   This is used to count number of \n 
#   in order to index selection of entries
#   as a whole, not as words
#   """
#   return str.count('\n')
##Need something for encryption as well as removing items from text/crossing off or ticking. Whichever is possible. 
##Also some sort of reminder function that works with time in OS module

item = []
c = num_of_entries(input("How many entries?\n#:"))
c-=1
print("Please input each task")
# Compares amount entered to user input 
while len(item) <= c:
    iapp = input("$:")
    item.append(iapp + ".")
# Seperates each new line inputted into a new line in a string
item = '\n'.join(item)
file_creator("entries.txt", item)
lc = line_count("entries.txt", '.')
read = file_reader('entries.txt')
print(read)
#print(type(item))
#itemCount = item.count('\n')
#itemCount+=1
#itemCount = str(itemCount)
#print(itemCount)
##print(itemCount.append(item))







#print(type(item))
#istr = str(item)
#nl = "\n".join(item)
#print(nl)
#print(type(nl))
#ilist = str_to_list(istr)
#print(ilist)
#print(count_newline(ilist))
#file_creator("entries.txt", istr)
#print(ilist)



#filename = "entries.txt"
#answ=os.path.exists(filename)
#with open(filename, 'a' if answ else "w") as f:
#   if(answ):
#       f.write("\n")
#   f.write(istr)

