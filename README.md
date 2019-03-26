Requirements:

Python 2.7+
Python 3.6+
PyPy

Install:
pip install pandas
pip install pandas_td
pip install tabulate
pip install td-client
download and install toolbelt


Prerequisites:
  1. basic knowledge of Treasure Data
  2. A database, table and some database
  4.basic query scripting
  3.python 3.3+

Example:
     1. Import required packages and Initialize connection to treasuredata using your apikey.
          import pandas_td as td
          import pandas as pd
          import tdclient as tdc
          import os

          apikey=os.environ['MASTER_TD_API_KEY']
          con= td.connect(apikey, endpoint='https://api.treasuredata.com/')

     2. Generate query in treasure data and either display result in tabular format or download it in csv file in the current directory.

         df=td.read_td_table(tabName, engine, limit=queryLimit, time_range=(mintStamp,maxtStamp), columns=culumnsList)

         if outFormat=='csv':
                 df.to_csv('result.csv')
         else:
                print(tabulate(df, headers=df.columns, tablefmt="grid"))
