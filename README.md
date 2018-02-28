# Python
Practice makes perfect


----
## Contents
|  :yum: |  :yellow_heart:| :metal:  |
| :------------:|:------------:|:------------:|
| [Resources](#resources) | [Dictionary](#dictionary-peach) | [List](#list-strawberry) |
| [Variable Type](#variable-type-pineapple) | [Matpltlib](#matplotlib-green_apple)| [MachineLearning](#machine-learning-notes-panda_face) |

----
## Resources
* [Matplotlib Bar chart examples](https://pythonspot.com/matplotlib-bar-chart/)
* [Sample plots in Matplotlib](https://matplotlib.org/tutorials/introductory/sample_plots.html)
* [Matpltlib colors](https://matplotlib.org/users/colors.html)
* [matplotlib.colors documentation](https://matplotlib.org/api/colors_api.html)

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


      7. save img
            plt.savefig('test.png', bbox_inches="tight", dpi = 300)

----
## Machine Learning notes :panda_face:
* [Machine Learning Tutorial for Beginners](https://www.kaggle.com/kanncaa1/machine-learning-tutorial-for-beginners)
* [Random Forests](http://blog.yhat.com/posts/random-forests-in-python.html)
* [Random Forest Classifier Example](https://chrisalbon.com/machine_learning/trees_and_forests/random_forest_classifier_example/)

      Random forest is a highly versatile machine learning method with numerous 
      applications ranging from marketing to healthcare and insurance. It can 
      be used to model the impact of marketing on customer acquisition, retention, 
      and churn or to predict disease risk and susceptibility in patients.

      Random forest is capable of regression and classification. It can handle 
      a large number of features, and it's helpful for estimating which of your 
      variables are important in the underlying data being modeled.
