def most_frequent():
  count=0
  a=input("please enter a string:")
  dict={}
  for i in a:
    keys=dict.keys()
    if i in keys:
      dict[i]+=1
    else:
      dict[i]=1

  print(dict)
  #l=list(dict)
  #print(l)
  l=sorted(dict.values(),reverse=True)
  print(l)
  sorted_dict = {}
  sorted_keys = sorted(dict, key=dict.get)  # [1, 3, 2]

  for w in sorted_keys:
    count+=1
    sorted_dict[w] = dict[w]

  for i in  range (count,0):
    print(sorted_dict[count])
    
    
    print(sorted_dict)
    
    
    
    
    
    
    
    
    
    
    most_frequency():
    please enter a string:mississippi
    {'M':1,'i':4,'s':4,'p':2}
    [4,4,2,1]
    {'M':1,'p':2,'i':4,'s':4}
