
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


##Need something for encryption as well as removing items from text/crossing off or ticking. Whichever is possible. 
##Also some sort of reminder function that works with time in OS module
item = []
c = num_of_entries(input("How many entries?\n#:"))
c-=1
print("Please input each task")

while len(item) <= c:
    iapp = input("$:")
    item.append(iapp)
item = '\n'.join(item)
istr = str(item)
nl = "\n".join(istr)
print(str_to_list(istr))
file_creator("entries.txt", istr)
#print(ilist)



#filename = "entries.txt"
#answ=os.path.exists(filename)
#with open(filename, 'a' if answ else "w") as f:
#   if(answ):
#       f.write("\n")
#   f.write(istr)

