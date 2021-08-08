# Ek program likhiye jisse ki niche di hui dictionaries ek hi dictionary me 
# aa jaaye jaise ki niche Expected result me diya gaya hain or jisski bhi keys 
# same hai unki values add ho jai. Example :- Input :- Output :- 


dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
for x in dic1:
  if x in dic2:
    dic2[x]=dic2[x]+dic1[x]
    dic2.update(dic3)
  else:
    dic2[x]=dic1[x]
print(dic2)


  




