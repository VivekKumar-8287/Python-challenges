# Sets

st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
# print(st)

st.update(['item6','item7','item8'])
# print(st)

# Joining Sets

""" 
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}

st3 = st1.union(st2)    
print(st3)
 """

""" 
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'} 
"""
""" 
Checking Subset and Super Set
A set can be a subset or super set of other sets:

Subset: issubset()
Super set: issuperset
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) """