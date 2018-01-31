# Python
Practice makes perfect

:yum: :yellow_heart: :metal:

----
## Contents
| :------------:|:---------------:|:-----:|
| [Resources](#Resources) | [Dictionary](#Dictionary) | [List](#List) |
| [Variable Type](#Variable Type) | [Matpltlib](#Matplotlib)|   TBD |
| TBD  | TBD | TBD |

----
## Resources
* [Matplotlib Bar chart examples](https://pythonspot.com/matplotlib-bar-chart/)

----
## Dictionary  :peach:
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
## List :strawberry: 
**A list keeps order, dict and set don't**
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

* Cases

      Turn all numbers in a list into their negative counterparts
            list2 = [-x for x in list1]

----
## Variable Type:pineapple:
      String to Int(no rounding)           ->         int(float("23.5")) = 23
      String to Int(rounding)              ->         int(round(float("23.5"))) = 24

      String to Float                      ->         float("545.2222")
      String to Float to 2 decimal places  ->         '%.2f' % 1.234 = 1.23

----
## Matplotlib :green_apple: