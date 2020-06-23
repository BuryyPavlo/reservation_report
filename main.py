import reservation as r
import datetime
from datetime import datetime, timedelta

locations = {'MCO':"'57413', '132416', '77439','132417', '132427', '132431', '132432'","LV":"'51413','117011','71419','51811','573523','117015'","LAX":"'110115','51022','71018','110104','110117' ","HNL":"'260111','59112','79115','260120','260139','260144'","MIA":"'57213','130115','77214','68438','88432','130127'","SFO":"'124115','52417','72418'"}
emails ={'MCO':'operations.us@itoorer.com',"LV":"operations.us@itoorer.com","LAX":"operations.us@itoorer.com","HNL":"operations.us@itoorer.com","MIA":"operations.us@itoorer.com","NYC":"operations.us@itoorer.com","SFO":"operations.us@itoorer.com"}



def reservation_all_locations():
    t = str(datetime.now().date())
    for name in locations:
        list_arealoc = locations[name]
        list_reservation = r.reservation_list_per_location(list_arealoc)
        filename = name+'_'+t+'.csv'
        list_reservation.to_csv(filename, sep=',', encoding='utf-8', header='true',index=False)

def reservation_overview():
    t = str(datetime.now().date())
    for name in locations:
        list_arealoc = locations[name]
        list_group_per_location_brand = r.reservation_group_per_location_day(list_arealoc)
        filename = name+'_group_per_day_and_brand_'+t+'.csv'
        list_group_per_location_brand.to_csv(filename, sep=',', encoding='utf-8', header='true',index=False)
        list_group_per_location = r.reservation_group_per_day(list_arealoc)
        filename = name+'_group_per_day_'+t+'.csv'
        list_group_per_location.to_csv(filename, sep=',', encoding='utf-8', header='true',index=False)


reservation_all_locations()
reservation_overview()
