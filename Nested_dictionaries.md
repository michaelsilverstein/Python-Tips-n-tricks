#Nested counting dictionaries
For instances in which you want to generate a dictionary with counts of associated phenomenon  a, b, ..., etc. for a given set of events A, B, ... , etc.

For example,
`dic = {A : {a : 1, b : 0, c : 2}, B : {a : 2, b : 1, c : 3},...} `

```python
#After data has been loaded (Events A, B, ... , etc.)
data = [[event1,phenomenon_a],[event1,phenomenon_b],[event2,phenomenon_c],[event2,phenomenon_a],...]
dic = {}

for d in data:
  event = d[0]
  phen = d[1]
  dic[event] = dic.get(event,{}) #Creates dic = {a : {}, b : {}, ... } for each event
  
  #Initializes each inner dictionary to 0 and adds 1 (counts) each time a given event appears in the data
  # dic = {event : {a: 0, b: 0,...},...
  #Upon seeing event associated with event:
  # dic = {event : {a : 1, b : 0,...},...}
  
  dic[event][phen] = dic[event].get(phen,0) + 1
```

The trick to this code is the `dict` method `dict.get(key, default=None)`. This method allows you to assign keys on the fly and generate default values for a given entry if none is already provided (like how I initialized all of the entries in `dic` to have empty dictionaries as values). IF they key already exists for a given dictionary, the `dict.get()` method will not alter that value, but it will still call or '`get`' that objecct. This ideal for counting, because you can increase the value of a given key each time that key is called by adding `+ 1` after the `get` call.
