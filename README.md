# Python
Practice makes perfect

----
## Data Structure
* [Priority Queue](http://www.bogotobogo.com/python/python_PriorityQueue_heapq_Data_Structure.php)

----
## Contents
|  :yum: |  :yellow_heart:| :metal:  |
| :------------:|:------------:|:------------:|
| [Resources](#resources) | [Dictionary](#dictionary-peach) | [List](#list-strawberry) |
| [Variable Type](#variable-type-pineapple) | [Matpltlib](#matplotlib-green_apple)| [Class](#class-egg)|
| [File Transfer](#file-transfer-ramen) |[CSV](#csv-rabbit)||

----
## Resources
* [Matplotlib Bar chart examples](https://pythonspot.com/matplotlib-bar-chart/)
* [Sample plots in Matplotlib](https://matplotlib.org/tutorials/introductory/sample_plots.html)
* [Matpltlib colors](https://matplotlib.org/users/colors.html): some color example
* [Matplotlib.colors documentation](https://matplotlib.org/api/colors_api.html): documentation
* [Free online graphing calculator](https://www.desmos.com/calculator): from desmos.com.

----
## Dictionary :peach:
* Create

      data = {}                     
      data = dict()

      data = {'a':1,'b':2,'c':3}    
      data = dict(a=1, b=2, c=3)
      data = {k: v for k, v in (('a', 1),('b',2),('c',3))}

      *create a nested dictionary
              >>> d = {}
              >>> d['dict1'] = {}
              >>> d['dict1']['innerkey'] = 'value'
              >>> d
              {'dict1': {'innerkey': 'value'}}
     
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
    
* Sort dic by values
      To get the values:
          sorted(data.values())

      To get the matching keys:
          sorted(data, key=data.get)
      
      To get a list of tuples ordered by value:
          sorted(data.items(), key=lambda x:x[1])

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
      
      1. append
          x = [1, 2, 3]
          x.append([4, 5])
          print (x)
          gives you: [1, 2, 3, [4, 5]]
          
      2. extend
          x = [1, 2, 3]
          x.extend([4, 5])
          print (x)
          gives you: [1, 2, 3, 4, 5]
      
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

      4. Check if a tring is in a list:
            if 'abc' in my_list:

      5. Finding the index of an item given a list containing it
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
                                                      
                                           ->         print(type(x))
     
      Percentage                           ->         percentage = '{0:.2f}'.format((num1 / num2 * 100))
                                                      return percentage
                                                   
      check if a string contains           ->         if "blah" not in somestring: 
      substring or not                                  continue
      
                                                      s = "This be a string"
                                                      if s.find("is") == -1:
                                                          print "No 'is' here!"
                                                      else:
                                                          print "Found 'is' in the string."
                                                          
                                                          
      Use either a.item() or np.asscalar(a) to convert most NumPy values to a native Python type:
                                           ->
                                                      import numpy as np
                                                      # examples using a.item()
                                                      type(np.float32(0).item()) # <type 'float'>
                                                      type(np.float64(0).item()) # <type 'float'>
                                                      type(np.uint32(0).item())  # <type 'long'>
                                                      # examples using np.asscalar(a)
                                                      type(np.asscalar(np.int16(0)))   # <type 'int'>
                                                      type(np.asscalar(np.cfloat(0)))  # <type 'complex'>
                                                      type(np.asscalar(np.datetime64(0, 'D')))  # <type 'datetime.datetime'>
                                                      type(np.asscalar(np.timedelta64(0, 'D'))) # <type 'datetime.timedelta'>
                                                      ...

                                                   
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

          6.1. Multiple legends on the same Axes
                  http://matplotlib.org/users/legend_guide.html#multiple-legends-on-the-same-axes

                  import matplotlib.pyplot as plt
                  line1, = plt.plot([1,2,3], label="Line 1", linestyle='--')
                  line2, = plt.plot([3,2,1], label="Line 2", linewidth=4)

                  # Create a legend for the first line.
                  first_legend = plt.legend(handles=[line1], loc=1)

                  # Add the legend manually to the current Axes.
                  ax = plt.gca().add_artist(first_legend)

                  # Create another legend for the second line.
                  plt.legend(handles=[line2], loc=4)

                  plt.show()

          6.2. Manually add legend items 
                  https://stackoverflow.com/questions/39500265/manually-add-legend-items-python-matplotlib

          6.3. legend position:
                  http://jb-blog.readthedocs.io/en/latest/posts/0012-matplotlib-legend-outdide-plot.html
                  Note: if your legend is outside the box and is cut in half, set bbox_inches="tight" keyword argument!
                        e.g.  plt.savefig('test.png', dpi = 300, bbox_inches="tight")


      7. save img
            plt.savefig('test.png', bbox_inches="tight", dpi = 300)

      8. plots with different scales
              import numpy as np
              import matplotlib.pyplot as plt

              fig, ax1 = plt.subplots()
              t = np.arange(0.01, 10.0, 0.01)
              s1 = np.exp(t)
              ax1.plot(t, s1, 'b-')
              ax1.set_xlabel('time (s)')
              # Make the y-axis label, ticks and tick labels match the line color.
              ax1.set_ylabel('exp', color='b')
              ax1.tick_params('y', colors='b')

              ax2 = ax1.twinx()
              s2 = np.sin(2 * np.pi * t)
              ax2.plot(t, s2, 'r.')
              ax2.set_ylabel('sin', color='r')
              ax2.tick_params('y', colors='r')

              fig.tight_layout()
              plt.show()
        
      9. plot table example
            https://matplotlib.org/examples/pylab_examples/table_demo.html

----
## Class :egg:
* Definition Syntax

      class ClassName:
          <statement-1>
          .
          .
          <statement-N>

* Objects

      1. 
        class MyClass:
            i = 12345
            def f(self):
                return 'hello world'

      2.
        x = MyClass() 

      3.
        def __init__(self):
            self.data = []

      4.
        class Complex:
            def __init__(self, realpart, imagpart):
                self.r = realpart
                self.i = imagpart

        x = Complex(3.0, -4.5)
        x.r, x.i
        (3.0, -4.5)    

      5. 
        class Dog:
            kind = 'canine'         # class variable shared by all instances
            def __init__(self, name):
                self.name = name    # instance variable unique to each instance

        >>> d = Dog('Fido')
        >>> e = Dog('Buddy')
        >>> d.kind                  # shared by all dogs
        'canine'
        >>> e.kind                  # shared by all dogs
        'canine'
        >>> d.name                  # unique to d
        'Fido'
        >>> e.name                  # unique to e
        'Buddy'
        
----
## File Transfer :ramen:
* create a directory if not exist

      if not os.path.exists(dir):
          os.makedirs(dir)
        
* copy files to another directory

      from shutil import copyfile
      dst = '../../../aaa/'
      src = 'bbb/test.png'
      copyfile(src, dst)
      
----
## CSV :rabbit:
* Writing to a CSV (general case)

      dic = {"John": "john@example.com", "Mary": "mary@example.com"} #dictionary

      download_dir = "exampleCsv.csv" #where you want the file to be downloaded to 

      csv = open(download_dir, "w") 
      #"w" indicates that you're writing strings to the file

      columnTitleRow = "name, email\n"
      csv.write(columnTitleRow)

      for key in dic.keys():
            name = key
            email = dic[key]
            row = name + "," + email + "\n"
            csv.write(row)
        
* Writing Strings With Commas or Line Breaks in Them

      name = "Adams, John"
      nameInQuotes = "\"" + name + "\""
      csv.write(nameInQuotes)
      
* Writing Strings With Quotes In Them

      name = "\"John\""

      name = name.replace("\"", "\"\"") #Python's string replace function

      nameInQuotes = "\"" + name + "\""
      csv.write(nameInQuotes)
