import pymssql
import codecs
import pandas as pd


login_file = open('login_info.txt',  'r')
server1 =login_file.readline()[:-1]
port1   = login_file.readline()[:-1]
username1 =login_file.readline()[:-1]
password1 = login_file.readline()[:-1]
login_file.close

#print(server1 + ','+port1+' , '+ username1+' , '+ password1)

def reservation_list_per_location(list_arealoc, days='0'):
    cnxn =  pymssql.connect(server = server1, port = port1, user = username1, password = password1)
    sql= pd.read_sql_query ('select l.Entitycode Arealoc,e.Name as Brand, CONVERT(date,StartDate) as Date, EntityReservationId as Reservation, p.Name as Product'
                            ' from Reservations r '
                            ' left join AppDeviceOwnerEntititiesRentalLocations l '
                            ' on r.StartRentalLocationId =l.idAppDeviceOwnerEntityRentalLocationId '
                            ' left join AppDeviceOwnerEntities e '
                            ' on e.idAppDeviceOwnerEntity= l.idAppDeviceOwnerEntity '
                            ' left join AppProductTypes p '
                            ' on p.idAppProductType = r.idProductType '
                            ' where StartDate between getdate()-1 and  getdate()+'+days+' and l.Entitycode in ('+ list_arealoc+')',cnxn)
    cnxn.close
    df = pd.DataFrame(sql, columns = ['Arealoc','Brand', 'Date', 'Reservation','Product'])
    return df


def reservation_group_per_location_day(list_arealoc, days='6'):
    cnxn =  pymssql.connect(server = server1, port = port1, user = username1, password = password1)
    sql= pd.read_sql_query (' select l.Entitycode Arealoc,e.Name as Brand,CONVERT(date,StartDate) as Date, Count(EntityReservationId)as Reservation,  p.Name as Product'
                            ' from Reservations r '
                            ' left join AppDeviceOwnerEntititiesRentalLocations l '
                            ' on r.StartRentalLocationId =l.idAppDeviceOwnerEntityRentalLocationId '
                            ' left join AppDeviceOwnerEntities e '
                            ' on e.idAppDeviceOwnerEntity= l.idAppDeviceOwnerEntity '
                            ' left join AppProductTypes p '
                            ' on p.idAppProductType = r.idProductType '
                            ' where StartDate between getdate()-1 and  getdate()+'+days+' and l.Entitycode in ('+ list_arealoc+')'
                            ' group by l.Entitycode, e.Name, StartDate, p.Name order by StartDate',cnxn)
    cnxn.close
    df = pd.DataFrame(sql, columns = ['Arealoc','Brand', 'Date', 'Reservation','Product'])
    return df

def reservation_group_per_day(list_arealoc, days='6'):
    cnxn =  pymssql.connect(server = server1, port = port1, user = username1, password = password1)
    sql= pd.read_sql_query (' select CONVERT(date,StartDate) as Date, Count(EntityReservationId)as Reservation'
                            ' from Reservations r '
                            ' left join AppDeviceOwnerEntititiesRentalLocations l '
                            ' on r.StartRentalLocationId =l.idAppDeviceOwnerEntityRentalLocationId '
                            ' left join AppDeviceOwnerEntities e '
                            ' on e.idAppDeviceOwnerEntity= l.idAppDeviceOwnerEntity '
                            ' left join AppProductTypes p '
                            ' on p.idAppProductType = r.idProductType '
                            ' where StartDate between getdate()-1 and  getdate()+'+days+' and l.Entitycode in ('+ list_arealoc+')'
                            ' group by StartDate order by StartDate',cnxn)
    cnxn.close
    df = pd.DataFrame(sql, columns = ['Date', 'Reservation'])
    return df
