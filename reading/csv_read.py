import pandas as pd
import numpy as np

csv_read = pd.read_csv('reading/locations.csv', usecols=['Loan_id','Product_name'],index_col='Loan_id', engine='python', sep=',')
# python indexleme yapmasın ya da index olarak loan_id kullanılsın istedik.
print(csv_read)

locations = np.loadtxt('reading/locations.csv',delimiter=',' , skiprows=1, dtype=str)



gen_locations = np.genfromtxt('reading/locations.csv', delimiter=',', skip_header=2,skip_footer=2, usecols=(0,3) ,dtype=str )


gen_locations1,gen_locations2 = np.genfromtxt('reading/locations.csv',
                                                            delimiter=',',
                                                            skip_header=2,
                                                            skip_footer=2,
                                                            usecols=(0,3) ,
                                                            dtype=str,
                                                            unpack=2 )
# print(gen_locations1,'\n \n\n',type(gen_locations2))

