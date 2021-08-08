# Ek program likhiye jo dictionary me se duplicate keys hata de. Example :- Input :-
 
dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
    } 


a = {}
for key,value in dic.items():
    if value not in a.values():
        a [key] = value
print(a)
