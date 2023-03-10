from flask import Flask, render_template, request,jsonify

from binance.client import Client
from binance.enums import *
import time
import os
from dotenv import load_dotenv
from datetime import datetime

import concurrent.futures
import requests
import pytz
import json
import talib, numpy
import math


#import config


# object creation for flask
app = Flask(__name__)
app.secret_key = b'asfdadagsdf.srewtsdfh3rt5rty3eg4543'




#for runtime in flask for debugging purpse only, comment out when deploying to cloud
#client = Client(config.API_KEY, config.API_SECRET)




def get_klines(symbol,start_time,end_time,timestamp,interval_increment,timeframe):
    url = 'https://fapi.binance.com/fapi/v1/klines'
    

  
   
    if not start_time and not end_time:
         params = {'symbol': symbol, 'interval': '1d', 'limit': 2}
         response = requests.get(url, params=params)
         
         
         
    else:

        
        date_object = datetime.strptime(start_time, "%Y-%m-%d")
        date_object = pytz.timezone('UTC').localize(date_object)
        start_time= date_object.timestamp()*1000
        start_time=(str(int(start_time)))
        
        
        date_object2 = datetime.strptime(end_time, "%Y-%m-%d")
        date_object2 = pytz.timezone('UTC').localize(date_object2)
        end_time= date_object2.timestamp()*1000

        
        end_time=(str(int(end_time))) #offset
        #start_time= '1673794951000'

        if timestamp:
            end_time = timestamp


      
        interval_not_equal = True

        if(not(interval_not_equal)):

            #print('hello')
            params = {'symbol': symbol, 'interval': '1d', 'endTime': end_time, 'limit':2}
            response = requests.get(url, params=params)

        
        
            




      #######################

        if(interval_not_equal):

            #interval is 5m and timeframe i D for example
            if(convert_to_milliseconds(timeframe)>convert_to_milliseconds(interval_increment)):


                #print ("tf > interval")

                params_lf = {'symbol': symbol, 'interval': interval_increment,'endTime': end_time, 'limit':1}
                response_lf = requests.get(url, params=params_lf)


                params = {'symbol': symbol, 'interval': timeframe,'endTime': end_time, 'limit':2}
                response = requests.get(url, params=params)

                try:

                    #print(symbol,response.json()[-1][4], response_lf.json()[0][4])
                    data = response.json()
                    data[-1][4] = response_lf.json()[0][4]
                    response._content = json.dumps(data).encode()
                except:
                    
                    print('error',symbol)

                
               
                
                


            else:
                #print ("tf <= interval")
                params = {'symbol': symbol, 'interval': timeframe,'endTime': end_time, 'limit':2}
                response = requests.get(url, params=params)

         ######################

        
    #print(params)
    
    
    


   
    
    return (symbol,response.json())

#testFuncfion_1def get_symbol_info_change (**input):
#functions
def get_symbol_info_change_exp (**input):
    
    if input == {}:
        #print(input)
        start_time = ""
        end_time = ""
        timestamp = ""
        interval_increment = ""
        timeframe = ""

    else:
         #print(input['start_str'],input['end_str'])
         end_time = input['end_str']
         start_time = input['start_str']
         #print(start_time,end_time)
         timestamp = input['timestamp']
         interval_increment = input['interval_increment']
         timeframe = input['timeframe']

         

    
   
    #info = client.get_account()
    #balances = info['balances']
    #exchange_info = client.get_exchange_info()
    #symbols = exchange_info['symbols']


    #futures_exchange_info = client.futures_exchange_info()  # request info on all futures symbols
    #futures_trading_pairs = [info['symbol'] for info in futures_exchange_info['symbols']]
    #futures_trading_pairs_usdt = []
    #for x in futures_trading_pairs:
        #if 'USDT' in x:
            #futures_trading_pairs_usdt.append(x)

    #symbols_1 =  futures_trading_pairs_usdt
    


    symbols = ["1000BTTCUSDT", "1000LUNCUSDT", "1000SHIBUSDT", "1000XECUSDT", "1INCHUSDT", "AAVEUSDT", "ADAUSDT", "AKROUSDT", "ALGOUSDT", "ALICEUSDT", "ALPHAUSDT", "ANCUSDT", "ANKRUSDT", "ANTUSDT", "APEUSDT", "API3USDT", "APTUSDT", "ARPAUSDT", "ARUSDT", "ATAUSDT", "ATOMUSDT", "AUDIOUSDT", "AVAXUSDT", "AXSUSDT", "BAKEUSDT", "BALUSDT", "BANDUSDT", "BATUSDT", "BCHUSDT", "BELUSDT", "BLUEBIRDUSDT", "BLZUSDT", "BNBUSDT", "BNXUSDT", "BTCDOMUSDT", "BTCSTUSDT", "BTCUSDT", "BTSUSDT", "BTTUSDT", "BZRXUSDT", "C98USDT", "CELOUSDT", "CELRUSDT", "CHRUSDT", "CHZUSDT", "COMPUSDT", "COTIUSDT", "CRVUSDT", "CTKUSDT", "CTSIUSDT", "CVCUSDT", "CVXUSDT", "DARUSDT", "DASHUSDT", "DEFIUSDT", "DENTUSDT", "DGBUSDT", "DODOUSDT", "DOGEUSDT", "DOTECOUSDT", "DOTUSDT", "DUSKUSDT", "DYDXUSDT", "EGLDUSDT", "ENJUSDT", "ENSUSDT", "EOSUSDT", "ETCUSDT", "ETHUSDT", "FETUSDT", "FILUSDT", "FLMUSDT", "FLOWUSDT", "FOOTBALLUSDT", "FTMUSDT", "FTTUSDT", "GALAUSDT", "GALUSDT", "GMTUSDT", "GRTUSDT", "GTCUSDT", "HBARUSDT", "HNTUSDT", "HOTUSDT", "ICPUSDT", "ICXUSDT", "IMXUSDT", "INJUSDT", "IOSTUSDT", "IOTAUSDT", "IOTXUSDT", "JASMYUSDT", "KAVAUSDT", "KEEPUSDT", "KLAYUSDT", "KNCUSDT", "KSMUSDT", "LDOUSDT", "LENDUSDT", "LINAUSDT", "LINKUSDT", "LITUSDT", "LPTUSDT", "LRCUSDT", "LTCUSDT", "LUNA2USDT", "LUNAUSDT", "MANAUSDT", "MASKUSDT", "MATICUSDT", "MKRUSDT", "MTLUSDT", "NEARUSDT", "NEOUSDT", "NKNUSDT", "NUUSDT", "OCEANUSDT", "OGNUSDT", "OMGUSDT", "ONEUSDT", "ONTUSDT", "OPUSDT", "PEOPLEUSDT", "QNTUSDT", "QTUMUSDT", "RAYUSDT", "REEFUSDT", "RENUSDT", "RLCUSDT", "ROSEUSDT", "RSRUSDT", "RUNEUSDT", "RVNUSDT", "SANDUSDT", "SCUSDT", "SFPUSDT", "SKLUSDT", "SNXUSDT", "SOLUSDT", "SPELLUSDT", "SRMUSDT", "STGUSDT", "STMXUSDT", "STORJUSDT", "SUSHIUSDT", "SXPUSDT", "THETAUSDT", "TLMUSDT", "TOMOUSDT", "TRBUSDT", "TRXUSDT", "UNFIUSDT", "UNIUSDT", "VETUSDT", "WAVESUSDT", "WOOUSDT", "XEMUSDT", "XLMUSDT", "XMRUSDT", "XRPUSDT", "XTZUSDT", "YFIIUSDT", "YFIUSDT", "ZECUSDT", "ZENUSDT", "ZILUSDT", "ZRXUSDT"]



    list_symbol = []

    perf_start_time = time.time()

    results = []
   # print('params', start_time, end_time,timestamp,interval_increment,timeframe,'null')
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(get_klines, symbol, start_time, end_time,timestamp,interval_increment,timeframe): symbol for symbol in symbols}
        for future in concurrent.futures.as_completed(futures):
            symbol = futures[future]
            data = future.result()
            results.append([symbol, data])

    response_time = time.time() - perf_start_time
    print("Overall response time: ", response_time) 

    if timestamp:
        request_timestamp = datetime.fromtimestamp(int(int(timestamp)/1000))
        #print(request_timestamp)
        #print('hello')
        #print("Timestamp here", request_timestamp.year)
    else:
        # current date and time
        now = datetime.now()

        # convert from datetime to timestamp
        ts = datetime.timestamp(now)
        request_timestamp = datetime.fromtimestamp(ts)
        #print("Timestamp here", request_timestamp.year)


    

    for x in results:


       

       
        try:
            
             #if x[1][0]=='APEUSDT':
                #print (x[1][1][0])
             candle_timestamp = x[1][1][1][6]
             candle_close = x[1][1][1][4]
             candle_volume = x[1][1][1][5]
             candle_change_percent =   round((((float(x[1][1][1][4]))-(float(x[1][1][0][4])))/(float(x[1][1][1][4])))*100,2)
             initial_list = [x[1][0],candle_timestamp,candle_close,candle_volume,candle_change_percent]
             #print(initial_list)



             #filter date and remove not updated time coin
             #fixed the bug for filtering the not updated coin, this is still not yet robust..
             stamp_x = datetime.fromtimestamp(x[1][1][1][0]/1000)
             #print (request_timestamp, stamp_x)
             if request_timestamp.year == stamp_x.year and request_timestamp.month == stamp_x.month: 
               #print("het")
               #check volume not be zero:
               if float(candle_volume) != 0:
                    

                    list_symbol.append(initial_list)
               
 
        except: Exception
           
            
    
    return list_symbol




#functions


        
    
    #print(list_symbol)
    # here i will modify the list that will be pass towards HTML index.. for now, only the symbol extracted from the futures_exchange_info is available
    # using this one i will create a list that will contain information about the OHLC on the given day includng the previos close to compute the %


def numbers_to_months(argument):
    switcher = {
    
        '1': "Jan",
        '2': "Feb",
        '3': "Mar",
        '4': "Apr",
        '5': "May",
        '6': "Jun",
        '7': "Jul",
        '8': "Aug",
        '9': "Sep",
        '10': "Oct",
        '11': "Nov",
        '12': "Dec"

    }
 
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument)



def format_date_binance_api_req (date_format):

       
    date_format = date_format.split("-")
   

    #print(date_format[1][0])
    
    if  date_format[2][0] == '0':
        date_format[2] = date_format[2].replace('0','')

    if  date_format[1][0] == '0':
        date_format[1] = date_format[1].replace('0','')

    
    Day = date_format[2] + " "
    Year = date_format[0]
    Month = numbers_to_months(date_format[1]) + ", "
    string_date = Day + Month + Year

    
    return string_date

def convert_to_milliseconds(time_duration):
    # Dictionary to store the conversion factors
    conversion_factors = {
        "1d": 86400000,
        "1m": 60000,
        "3m": 180000,
        "5m": 300000,
        "15m": 900000,
        "30m": 1800000,
        "1h": 3600000,
        "2h": 7200000,
        "3h": 10800000,
        "4h": 14400000,
        "12h": 43200000,
        "1w": 604800000,
        "1M": 2678400000
    }
    # Check if the input is valid
    if time_duration not in conversion_factors:
        raise ValueError(f"Invalid input: {time_duration}. Please use one of the following: {', '.join(conversion_factors.keys())}")
    return conversion_factors[time_duration]





@app.route("/")
def index():
    title = '  Trading Environment Simulation'


    app_host = os.getenv("APP_HOST")
    app_port = os.getenv("APP_PORT")
    
    list_symbol = get_symbol_info_change_exp()

    #print(list_symbol)

        
    return render_template('index.html',title = title,  symbols = list_symbol, app_host = app_host, app_port=app_port)







@app.route("/sell")
def sell():
    return 'sell'

@app.route('/templates/<path:filename>')
def templates(filename):
    return render_template(filename)




@app.route("/update_prices", methods = ['POST'])
def update_prices():

    


    present_day = request.headers['present_day']
    prev_day = request.headers['prev_day']
    timestamp_input = request.headers['timestamp_input']
    interval_increment = request.headers['interval_input']
    timeframe = request.headers['timeframe']
    
    
    
   
    #print(present_day)
    #print(prev_day)
    #format for API binance date request
    #present_day = format_date_binance_api_req(present_day)
    #prev_day =  format_date_binance_api_req(prev_day)

    #print(present_day)
    #print(prev_day)
    
    list_symbol = get_symbol_info_change_exp(start_str = prev_day, end_str = present_day, timestamp = timestamp_input, interval_increment = interval_increment, timeframe = timeframe)



    return list_symbol
   



@app.route('/history', methods = ['POST'])


def history():

    timeframe = request.headers['timeframe']
    #print(timeframe)

    #candlesticks = client.get_historical_klines("BTCUSDT", timeframe)
    url = 'https://fapi.binance.com/fapi/v1/klines'
    params = {'symbol': "BTCUSDT", 'interval': timeframe}
    response = requests.get(url, params=params)
    candlesticks =response.json()
 
    processed_candlesticks = []

    for data in candlesticks:
         
        candlestick = { 
            "time": data[0]/1000, 
            "open": float(data[1]), 
            "high": float(data[2]), 
            "low": float(data[3]), 
            "close": float(data[4]),
            "value":float(data[4]) 
         }
    
        processed_candlesticks.append(candlestick)


    return jsonify(processed_candlesticks)



@app.route('/history_test', methods = ['POST'])
def history_test():
    
    #print("hello")
    #print(request.headers['Symbol'])

      # get the start time
    st = time.time()
    #print(request.headers['date_input'])
    timeframe = request.headers['timeframe']

    date = request.headers['date_input']
    #print(date)
    date = format_date_binance_api_req(date)
    #print(date)

    #print(date)
    interval_increment = request.headers['interval']
    #print('interval is:',interval_increment,timeframe)



    #timestamp_simlation_time
    simulation_timestamp = request.headers['date_input2']
    #print(simulation_timestamp)
    
    #print(simulation_timestamp)


    #candlesticks = client.get_historical_klines(request.headers['Symbol'], timeframe,'12 Dec, 2000', date)
    #print(type(timeframe))


   

    url = 'https://fapi.binance.com/fapi/v1/klines'
    url_continous = 'https://fapi.binance.com/fapi/v1/continuousKlines'



    is_continous = False
    interval_not_equal = True
    

    #print(request.headers['date_input'])
      
    date_object3 = datetime.strptime(request.headers['date_input'], "%Y-%m-%d")
    date_object3 = pytz.timezone('UTC').localize(date_object3)
    end_time= date_object3.timestamp()*1000
    end_time= str(int(end_time))







    #this is a scratch API call request hehehe need to remove
    
    if(not(is_continous and interval_not_equal) ):
        params = {'symbol': request.headers['Symbol'], 'interval': timeframe,'endTime': simulation_timestamp, 'limit':1000}
        response = requests.get(url, params=params)


    if(is_continous and interval_not_equal):

        params = {'pair': request.headers['Symbol'], 'interval': timeframe,'endTime': simulation_timestamp, 'limit':1000 , 'contractType': 'PERPETUAL'}
        response = requests.get(url_continous, params=params)


        



    if(interval_not_equal):
            
            

            #interval is 5m and timeframe i D for example
            if(convert_to_milliseconds(timeframe)>convert_to_milliseconds(interval_increment)):

                #print('hello',interval_increment)


                #print ("tf > interval")

                params = {'symbol': request.headers['Symbol'], 'interval': timeframe,'endTime': simulation_timestamp, 'limit':1000}
                response = requests.get(url, params=params)


                #get the opening timestamp of the current candle on higher tf
                opening_time = str(response.json()[-1][0])
                #print(type(opening_time),opening_time)
                
                #params_lf = {'symbol': request.headers['Symbol'], 'interval': interval_increment,'endTime': simulation_timestamp, 'limit':1}
                params_lf = {'symbol': request.headers['Symbol'], 'interval': interval_increment,'startTime':opening_time, 'endTime': simulation_timestamp}
                response_lf = requests.get(url, params=params_lf)


                #code to get the high and low of the present candle wrt to requested timestamp to be stored on the higher TF latest candle
                #print(type(response_lf.json()))

                list_high = []
                list_low = []
                for x in response_lf.json():
                    #header = ['open_time', 'open','high','low','close','x','close_time','x','x','x','x','x']
                    list_high.append(float(x[2]))
                    list_low.append(float(x[3]))
                

                current_high = max(list_high)
                current_low = min(list_low)

                #print(list_high)

                #print('json clos',response.json()[-1][4], response_lf.json()[0][4])

                
                data = response.json()

                data[-1][4] = response_lf.json()[-1][4] #change close price of the reqeusted higher tf candle
                data[-1][2] = str(current_high) #change high price of the reqeusted higher tf candle
                data[-1][3] = str(current_low) #change low price of the reqeusted higher tf candle
                
                response._content = json.dumps(data).encode()


            else:
                #print ("tf <= interval")
                
                #params = {'symbol': request.headers['Symbol'], 'interval': timeframe,'endTime': simulation_timestamp, 'limit':1000}
                #response = requests.get(url, params=params)



                params = {'symbol': request.headers['Symbol'], 'interval': timeframe,'endTime': simulation_timestamp, 'limit':1000}
                response = requests.get(url, params=params)

                interval_increment = '3m'
                #print('hi',interval_increment)

                #get the opening timestamp of the current candle on higher tf
                opening_time = str(response.json()[-1][0])
                #print(type(opening_time),opening_time)
                
                #params_lf = {'symbol': request.headers['Symbol'], 'interval': interval_increment,'endTime': simulation_timestamp, 'limit':1}
                params_lf = {'symbol': request.headers['Symbol'], 'interval': interval_increment,'startTime':opening_time, 'endTime': simulation_timestamp}
                response_lf = requests.get(url, params=params_lf)


                #code to get the high and low of the present candle wrt to requested timestamp to be stored on the higher TF latest candle
                #print(type(response_lf.json()))

                list_high = []
                list_low = []
                for x in response_lf.json():
                    #header = ['open_time', 'open','high','low','close','x','close_time','x','x','x','x','x']
                    list_high.append(float(x[2]))
                    list_low.append(float(x[3]))
                

                current_high = max(list_high)
                current_low = min(list_low)

                #print(list_high)

                #print('json clos',response.json()[-1][4], response_lf.json()[0][4])

                
                data = response.json()

                data[-1][4] = response_lf.json()[-1][4] #change close price of the reqeusted higher tf candle
                data[-1][2] = str(current_high) #change high price of the reqeusted higher tf candle
                data[-1][3] = str(current_low) #change low price of the reqeusted higher tf candle
                
                response._content = json.dumps(data).encode()














    candlesticks2 = response.json()
    #print(candlesticks2[-1])
    


   # print('connectr',candlesticks[0])
   # print('api',candlesticks2[0])




    

        # get the end time
    et = time.time()
    elapsed_time = et - st
    # print('Execution time:', elapsed_time, 'seconds')
 
    processed_candlesticks = []
    closes = []

    for data in candlesticks2:
         
        candlestick = { 
            "time": data[0]/1000, 
            "open": float(data[1]), 
            "high": float(data[2]), 
            "low": float(data[3]), 
            "close": float(data[4]),
            "time_close": data[6]
         }
        closes.append(candlestick['close'])
        processed_candlesticks.append(candlestick)



    #print(candlestick['close'])

    #compute for RSI:
    np_closes = numpy.array(closes)
    rsi = talib.RSI(np_closes)
    ma20 = talib.SMA(np_closes,20)
    ma50 = talib.SMA(np_closes,50)
    ma100 = talib.SMA(np_closes,100)
    #print(ma20)

    for index, candlestick in enumerate(processed_candlesticks):
        if math.isnan(rsi[index]):
             candlestick["rsi"] = None
        else:
             candlestick["rsi"] = rsi[index]
        if math.isnan(ma20[index]):
            candlestick["ma20"] = None
        else:
            candlestick["ma20"] = ma20[index]
        if math.isnan(ma50[index]):
            candlestick["ma50"] = None
        else:
            candlestick["ma50"] = ma50[index]
        if math.isnan(ma100[index]):
            candlestick["ma100"] = None
        else:
            candlestick["ma100"] = ma100[index]


    return jsonify(processed_candlesticks)










def create_dotenv():
    if not os.path.exists('.env'):
        host = input("Enter the IP address or domain name of your GCP instance or localhost: ")
        port = input("Enter the port of your application: ")

        with open('.env', 'w') as f:
            f.write(f'APP_HOST={host}\nAPP_PORT={port}')


if __name__ == '__main__':
    create_dotenv()
    load_dotenv()

    app.run(host='0.0.0.0',port=os.getenv("APP_PORT"))
    


