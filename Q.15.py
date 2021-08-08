



# . Write a Python script to concatenate following dictionaries to create a 
# new one. Go to the editor

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

for x in dic1:
  if x in dic2:
    dic2[x]=dic2[x]+dic1[x]
    dic2.update(dic3)
  else:
    dic2[x]=dic1[x]
print(dic2)












