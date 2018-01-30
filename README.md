# Python
Practice makes perfect

:yum: :yellow_heart: :metal:

----
## Dictionary  
* Create

      data = {}                     
      data = dict()

      data = {'a':1,'b':2,'c':3}    
      data = dict(a=1, b=2, c=3)
      data = {k: v for k, v in (('a', 1),('b',2),('c',3))}
     
* Insert/Update

      data['a']=1  # Updates if 'a' exists, else adds 'a'
      data.update({'a':1})
      data.update(dict(a=1))
      data.update(a=1)
   
      data.update({'c':3,'d':4})  # Updates 'c' and adds 'd'
    
* Delete

      del data[key]  # Removes specific element in a dictionary
      data.pop(key)  # Removes the key & returns the value
      data.clear()   # Clears entire dictionary
    
* Check if a key is already in dictionary

      key in data
    
* Iterate

      for key in data:                # Iterates just through the keys, ignoring the values
      for key, value in d.items():    # Iterates through the pairs
   
----
## List  
* Create

      list = []          
      list = ['physics', 'chemistry', 1997, 2000]
      list = [1, 2, 3, 4, 5 ]
      list = ["a", "b", "c", "d"]
      
* Add

      list.append('Google')
      
* Delete/Remove

      del list[2] #2 is the index
      
* Reverse a list
     
      L.reverse()
      L[::-1]
      
----
