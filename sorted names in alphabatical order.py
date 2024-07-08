#find the minimum and maximum names i sorted list 
def get_second_min_max_names(names):
    sorted_names=sorted(names)
    second_min=sorted_names[1]
    second_max=sorted_names[-2]
    return second_min,second_max
n= int(input("enter the  number of names"))
names=[]
for i in range(n):
    name=input("enter the name{}:".format(i+1))
    names.append(name)
sorted_names=sorted(names)
print("names in orginal order",names)
print("name in alphabetical order :",sorted_names)
second_min_name,second_max_name=get_second_min_max_names(sorted_names)
print("second minimum name",second_min_name)
print("second maximum name",second_max_name)