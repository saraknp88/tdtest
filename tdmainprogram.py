from treasuredatamainpackage import user_input_script
import pandas_td as td
from tabulate import tabulate
import os

#initiate connection to treasure data through api
apikey=os.environ['MASTER_TD_API_KEY']
con= td.connect(apikey, endpoint='https://api.treasuredata.com/')
################################
try:
    while True:
        dbName= input('please enter databasename (test_1): ')
        if dbName=='test_1':
            break
        print("wrong value, try again")
except:
    print('something went wrong')
#=====================================

try:
    while True:
        tabName= input('please enter table name (tab_1): ')
        if tabName=='tab_1':
            break
        print("wrong value, try again")
except:
    print('something went wrong')

#============enter query engin ===================
try:
    queryEngine= input('would you like to specify your query engine? yes/no: ')
except:
    print("something went wrong")

if queryEngine=='yes':
    qEngine=user_input_script.getqueryengine()
else:
    qEngine='presto'
################################################

try:
    colInput= input('Would you like to enter name of columns? yes/no: ')
except:
    print("something went wrong")

if colInput=='yes': #not working as expected
    try:
        colName=input('Please enter columns with space: **id event class time**: ')
        colList=colName.split()
        print(colList)
    except:
        print("something went wrong")

else:
        colList=user_input_script.getdefaultcolumnlist(tabName, dbName, qEngine)
        print(colList)

#============enter min time stamp =========================
try:
    mintStampEnter= input('Would you like to enter min time stamp? yes/no: ')
except:
    print("something went wrong")
if mintStampEnter=='no':
    mintStamp=None
else:
    try:
         mintStamp= input('please enter mintstamp following the format : yyyy-mm-dd hh:mm:ss : ')
    except:
        print("something went wrong")

#============enter min time stamp =========================
try:
    maxtStampEnter= input('Would you like to enter max time stamp? yes/no: ')
except:
    print("something went wrong")
if maxtStampEnter=='no':
    maxtStamp=None
else:
    try:
         maxtStamp= input('please enter maxtstamp following the format : yyyy-mm-dd hh:mm:ss : ')
    except:
        print("something went wrong")

#============min max time stamp validation ===================
user_input_script.validateminmaxtimestamp(mintStamp, maxtStamp)

#============enter query limit ===================
try:
    queryLimit= input('would you like to specify your query limit? yes/no: ')
except:
    print("something went wrong")

if queryLimit=='yes':
    qLimit=user_input_script.getquerylimit()
else:
    qLimit=None

#============output format ===================
try:
    outputFormat= input('would you like to specify output format?yes/no?  ')
except:
    print("something went wrong")

if outputFormat=='yes':
    outFormat=user_input_script.outputformat()
else:
    outFormat='tabular'

#============issue query in treasure data based on user inputs ===================
engine = con.query_engine(database=dbName, type=qEngine)
df=td.read_td_table(tabName, engine, limit=qLimit, time_range=(mintStamp,maxtStamp), columns=colList)
df

#======================Download or display results================================
if outFormat=='csv':
        df.to_csv('result.csv')
else:
    print(tabulate(df, headers=df.columns, tablefmt="grid"))

#####################################################
