# binarize the data

'''
EX1:
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
'''







'''
EX2: You can do it for each column seperate and then concat the results:
         
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
'''







'''
EX3:
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
'''




'''
MYCODE:

         def test(fin, fout):
                  df = pd.read_csv(fin)
                  cols_to_transform = ['BIO_Marital_Status_Category', 'BIO_Title_Category']
                  df_with_dummies = pd.get_dummies(data=df, columns=cols_to_transform)
                  df_with_dummies.to_csv(fout, encoding='utf-8', index=False) #store DataFram object into a csv file
'''
