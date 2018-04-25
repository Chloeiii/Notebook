# Pandas: Python Data Analysis Library
****
### Convert categorical variable into dummy/indicator variables:smirk:
e.g.
         df = DataFrame({'A': ['a', 'b', 'a'], 'B': ['c', 'c', 'b'], 'C': [1, 2, 3]})  
         df

            A  B  C
         0  a  c  1
         1  b  c  2
         2  a  b  3

         pd.get_dummies(df)

            C  A_a  A_b  B_b  B_c
         0  1    1    0    0    1
         1  2    0    1    0    1
         2  3    1    0    1    0


e.g. You can do it for each column seperate and then concat the results
         
         df
         
            A  B
         0  a  x
         1  a  y
         2  b  z
         3  b  x
         4  c  x
         5  a  y
         6  b  y
         7  c  z

         pd.concat([pd.get_dummies(df[col]) for col in df], axis=1, keys=df.columns)

            A        B      
            a  b  c  x  y  z
         0  1  0  0  1  0  0
         1  1  0  0  0  1  0
         2  0  1  0  0  0  1
         3  0  1  0  1  0  0
         4  0  0  1  1  0  0
         5  1  0  0  0  1  0
         6  0  1  0  0  1  0
         7  0  0  1  0  0  1


e.g.
         pd.get_dummies(data=df, columns=['A', 'B'])  
         df
         
            A  B  C
         0  a  c  1
         1  b  c  2
         2  a  b  3

         pd.get_dummies(data=df, columns=['A', 'B'])
         
            C  A_a  A_b  B_b  B_c
         0  1  1.0  0.0  0.0  1.0
         1  2  0.0  1.0  0.0  1.0
         2  3  1.0  0.0  1.0  0.0

MYCODE:

         def test(fin, fout):
                  df = pd.read_csv(fin)
                  cols_to_transform = ['BIO_Marital_Status_Category', 'BIO_Title_Category']
                  df_with_dummies = pd.get_dummies(data=df, columns=cols_to_transform)
                  #store DataFram object into a csv file
                  df_with_dummies.to_csv(fout, encoding='utf-8', index=False) 


            
****
### Iterate and add values in pandas.DataFrame :dizzy_face:

MYCODE:

         def setlabel(file):
                  df = pd.read_csv(file)
                  df['label_2016'] = ''
                  for index, row in df.iterrows():
                           if row['Largest_Gift_before_2016']>25000 or row['Total_Gift_before_2016']>100000:
                                    df.set_value(index, 'label_2016', 1)
                           else:
                                    df.set_value(index, 'label_2016', 0)
                  df.to_csv(file, encoding='utf-8', index=False)

****
### [Dropping rows and columns in pandas Datafram](https://chrisalbon.com/python/data_wrangling/pandas_dropping_column_and_rows/) :feet:

MYCODE (drop rows with specific values):

	df1 = dftmp[dftmp.BIO_Age == -1]#2016 without age
	df2 = dftmp[dftmp.BIO_Age != -1]#2016 with age
	df3 = dftmp[dftmp.BIO_Age == -1]#2017 without age
	df4 = dftmp[dftmp.BIO_Age != -1]#2017 with age
         
e.g.(Drop a column):

         df.drop('reports', axis=1) #axis=1 denotes that we are referring to a column, not a row

