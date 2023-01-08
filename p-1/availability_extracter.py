import mysql.connector as db
import pandas as pd
import re




class date_extractor:

    def __init__(self):
        pass

    
    def insert_info(self,start_date,end_date):

        rn = pd.date_range(start_date, end_date, freq='D')
        # rn = pd.date_range('2014-05-01', '2014-05-05', freq='D')
        rn=list(rn)
        o_date_list = ''
        for i in rn:
            i=str(i)
            i=i[0:10]
            o_date_list = o_date_list + ',' + i
        occupied_dates = o_date_list[1:]
        
        mydb = db.connect(host = "localhost", user = "root", password = "c0d3r123" ,database='vehical_info')
        cur = mydb.cursor()
        query = f'''insert into dates_info(start_date,end_date,occupied_dates)values("{start_date}","{end_date}","{occupied_dates}");'''
        cur.execute(query)
        cur.execute("commit;")
        mydb.close()


    def check_availability(self,booking_date):
        mydb = db.connect(host = 'localhost' , user = 'root',password = 'c0d3r123' ,database = 'vehical_info')
        cur = mydb.cursor()
        query = f'''select occupied_dates from dates_info;'''
        cur.execute(query)
        data = cur.fetchall()
        # print(data)
        all_dates = []
        for i in range(len(data)):
            # print(i)
            str_dates = data[i][0]
            dates = re.findall(r'\d{4}-\d{2}-\d{2}',str_dates)
            all_dates.append(dates)
        # print(all_dates)


        query2 = f'''select vehical_no from dates_info;'''
        cur.execute(query2)
        data = cur.fetchall()
        # print(data)
        all_num = []
        for i in range(len(data)):
            # print(i)
            num = data[i][0]
            # print(num)
            # print(type(num))
            # print(num)
            all_num.append(num)
        # print(all_num)
        mydb.close()

        all_avail_vehicals = []
        for i in all_dates:
            if booking_date not in i:
                avail_vehical_index = all_dates.index(i)
                all_avail_vehicals.append(all_num[avail_vehical_index])
        print('The vahical numbers available :')
        for i in all_avail_vehicals:
            print(i)


obj = date_extractor()
# obj.insert_info('2012-04-25','2012-05-07')
obj.check_availability('2012-04-25')
