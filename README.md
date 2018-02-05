# Python
Practice makes perfect


----
## Contents
|  :yum: |  :yellow_heart:| :metal:  |
| :------------:|:------------:|:------------:|
| [Resources](#resources) | [Dictionary](#dictionary-peach) | [List](#list-strawberry) |
| [Variable Type](#variable-type-pineapple) | [Matpltlib](#matplotlib-green_apple)| TBD |

----
## Resources
* [Matplotlib Bar chart examples](https://pythonspot.com/matplotlib-bar-chart/)
* [Sample plots in Matplotlib](https://matplotlib.org/tutorials/introductory/sample_plots.html)
* [Matpltlib colors](https://matplotlib.org/users/colors.html)

----
## Dictionary :peach:
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

* Cases

      1. Get list of values from dict:
            list(d.values())

      2. Sum all the values in a dict:
            sum(d.values())
   
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

* Zip

      1. Zip a List

            list_a = [1, 2, 3, 4, 5]
            list_b = ['a', 'b', 'c', 'd', 'e']
            zipped_list = zip(list_a, list_b)
            print (zipped_list)
            >>> [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')] 
         
      2. Unzip a List
                 
                   zipper_list = [(1, 'a'), (2, 'b'), (3, 'c')]
                   list_a, list_b = zip(*zipper_list)
                   print (list_a)               
                   print (list_b)         
                   >>> (1, 2, 3)
                   >>> ('a', 'b', 'c')

* Cases

      1. Turn all numbers in a list into their negative counterparts:
            list2 = [-x for x in list1]   
            
      2. Compare Two String:
            >>> a = 'pub' 
            >>> b = ''.join(['p', 'u', 'b'])
            >>> a == b
            True
            >>> a is b
            False

      3. Finding the index of an item in a list
            >>> ["foo", "bar", "baz"].index("bar")
            1

----
## Variable Type :pineapple:
      String to Int(no rounding)           ->         int(float("23.5")) = 23
      String to Int(rounding)              ->         int(round(float("23.5"))) = 24

      String to Float                      ->         float("545.2222")
      String to Float to 2 decimal places  ->         '%.2f' % 1.234 = 1.23

      Check variable type                  ->         isinstance(12, str) = False 
                                                      isinstance(1, int) = True
                                                      isinstance('aaaa', float) = False

----
## Matplotlib :green_apple:
      1. plt bar chart sample(vertical):
            plt.bar([1,2,3,4,5], [11,22,33,44,55], width = 1, color = 'blue')

      2. x, y ticks
            plt.xticks([1,2,3,4,5],['a', 'b', 'c', 'd', 'e'], fontsize=5)
            plt.yticks([1,2,3,4,5],['a', 'b', 'c', 'd', 'e'], fontsize=5)
      
      3. x, y lables
            plt.xlabel('Fiscal Year', fontsize = 6)
            plt.ylabel('Number of Donors', fontsize = 6)

      4. title
            plt.title('title')

      5. text
            plt.text(2, 6, 'aaaaaa', fontsize=15)
      
      6. Legend
            lgd = plt.legend((p5, p4, p3, p2, p1),(
                  '<100','>=100 to <500','>=500 to <1k','>=1k to <10k','>=10k'),
                   fontsize = 6,
                   bbox_to_anchor=(1.05, 1), 
                   loc=2, 
                   borderaxespad=0.,
                   title = 'donation amount',
                   shadow = True
                   )

      7. save img
            plt.savefig('test.png', bbox_inches="tight", dpi = 300)

----
