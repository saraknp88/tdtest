
import pandas_td as td
import pandas as pd
import tdclient as tdc
import os

apikey=os.environ['MASTER_TD_API_KEY']
con= td.connect(apikey, endpoint='https://api.treasuredata.com/')
#####################################

def gettablename(tabName='tab_1'):
    '''gettablename function validates and returns name of the database
    Input: name of the table
    Output: name of the table'''
        #logging.info("Validate table name entered by user")
    tabFlag=False
    while not tabFlag:
        if tabName != 'tab_1':
                print("wrong value")
                break
        else:
            dbFlag=True
            break
    return tabName
#####################################

def getdefaultcolumnlist(tabName, dbName, qEngine):
        engine =con.query_engine(database=dbName, type=qEngine)
        df=td.read_td_table(tabName,engine)   #it throw an error bcz of engine!!!!
        colList=list(df.columns.values)
        return colList
#################################
def validateminmaxtimestamp(mintStamp, maxtStamp):
    '''
       getminmaxtimestamp validates entered time stamps to make sure min time stamp is larger than max time stamp
       Input= min and Max time stamps
       Output= Min and Max time stams
    '''
    #logging.info("Validation: min time stamp entered by user must be less than max time stamp")
    flag= False
    if mintStamp!=None and maxtStamp!=None:
        if mintStamp>=maxtStamp:
            print('minnimum timestamp must be smaller than maximmum time stamp')
            mintStamp=None
            maxtStamp=None
        return False
    else:
        return True
 ######################################

def getqueryengine():
    '''
       getqueryengine function take query engin as argument with default value: presto and return name query engin
       Input: query engin name
       Output: query engin name
    '''
    try:
        qEngine= input('plese specify your query engine:(hive, presto): ')
    except:
        print("something went wrong")
    return qEngine
 #######################################

def getquerylimit(qLimit=None):
    '''
    getquery limit takes users' query limit of their choice. it can be any number between 1-7
    Input: query limit number
    Output: query limit number
    '''
    try:
        qLimit=input('please enter your query limit: (there are only 7 row of sample data): ')
    except:
            print("something went wrong")

    return qLimit
#######################################
def outputformat():
    '''
       outputformat takes either csv or tabular as input and returns the chosen output format. default os tabular format
       Input: output format
       Output: output format
    '''
    try:
        outFormat= input('please specify output format: csv , tabular? ')
    except:
        print("something went wrong")
    return outFormat

#######################################
'''def querymaker(tabName, qLimit, mintStamp, maxtStamp, colList):
    df=td.read_td_table(tabName, engine, limit=qLimi, time_range=(mintStamp,maxtStamp), columns=colList)
    df'''


#######################################
'''def querymaker():
    with tdclient.Client(apikey) as client:
        job = client.query("sample_datasets", "SELECT COUNT(1) FROM www_access")
'''
