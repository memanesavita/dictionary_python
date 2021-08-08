# Ek list lijiye aur uske andar dictionaries me keys and
# values likhiye jaisa ki niche dikhaya gaya hai (Sample Data) 
# aur uske baad saare unique values ko ek list me print karaye. Example :- Input :-
 
#  [
#      {"first":"1"}, 
#      {"second": "2"}, 
#      {"third": "1"}, 
#      {"four": "5"}, 
#      {"five":"5"}, 
#      {"six":"9"},
#      {"seven":"7"}
# ] 


b=[{"first":"1"},{"second":"2"},{"third":"1"},{"four":"5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
u_value=set (val for dic in b for val in dic .values())
print("unique value:",u_value)











# 