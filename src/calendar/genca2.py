#-*- coding:utf-8 –*-
import sys
import os
import datetime as dt;


#
shfe_dict = {
        2005:[(20050101,20050103),(20050207,20050215),(20050501,20050508),(20051001,20051009)],
        2006:[(20060101,20060103),(20060128,20060205),(20060501,20060507),(20061001,20061008)],
        2007:[(20070101,20070103),(20070217,20070225),(20070501,20070507),(20071001,20071007),(20071230,20071231)],
        2008:[(20080101,20080101),(20080206,20080212),(20080404,20080406),(20080501,20080503),(20080607,20080609),(20080913,20080915),(20080929,20081005)],
        2009:[(20090101,20090103),(20090125,20090131),(20090404,20090406),(20090501,20090503),(20090528,20090530),(20091001,20091008)],
        2010:[(20100101,20100103),(20100213,20100219),(20100403,20100405),(20100501,20100503),(20100614,20100616),(20100922,20100924),(20101001,20101007)],
        2011:[(20110101,20110103),(20110202,20110208),(20110403,20110405),(20110430,20110502),(20110604,20110606),(20110910,20110912),(20111001,20111007)],
        2012:[(20120101,20120103),(20120122,20120128),(20120402,20120404),(20120429,20120501),(20120622,20120624),(20120930,20121007)],
        2013:[(20130101,20130103),(20130209,20130215),(20130404,20130406),(20130429,20130501),(20130610,20130612),(20130919,20130921),(20131001,20131007)],
        2014:[(20140101,20140101),(20140131,20140206),(20140405,20140407),(20140501,20140503),(20140531,20140602),(20140906,20140908),(20141001,20141007)],
        2015:[(20150101,20150103),(20150218,20150224),(20150405,20150406),(20150501,20150503),(20150620,20150622),(20150927,20150927),(20151001,20151007)],
        2016:[(20160101,20160103),(20160207,20160213),(20160402,20160404),(20160430,20160502),(20160609,20160611),(20160915,20160917),(20161001,20161007)],
        2017:[(20170101,20170102),(20170127,20170202),(20170402,20170404),(20170429,20170501),(20170528,20170530),(20171001,20171008)],
        }

dce_dict = {
        2005:[(20050101,20050103),(20050207,20050215),(20050501,20050508),(20051001,20051009)],
        2006:[(20060101,20060103),(20060128,20060205),(20060501,20060507),(20061001,20061008)],
        2007:[(20070101,20070103),(20070217,20070225),(20070501,20070507),(20071001,20071007),(20071230,20071231)],
        2008:[(20080101,20080101),(20080206,20080212),(20080404,20080406),(20080501,20080503),(20080607,20080609),(20080913,20080915),(20080929,20081005)],
        2009:[(20090101,20090103),(20090125,20090131),(20090404,20090406),(20090501,20090503),(20090528,20090530),(20091001,20091008)],
        2010:[(20100101,20100103),(20100213,20100219),(20100403,20100405),(20100501,20100503),(20100614,20100616),(20100922,20100924),(20101001,20101007)],
        2011:[(20110101,20110103),(20110202,20110208),(20110403,20110405),(20110430,20110502),(20110604,20110606),(20110910,20110912),(20111001,20111007)],
        2012:[(20120101,20120103),(20120122,20120128),(20120402,20120404),(20120429,20120501),(20120622,20120624),(20120930,20121007)],
        2013:[(20130101,20130103),(20130209,20130215),(20130404,20130406),(20130429,20130501),(20130610,20130612),(20130919,20130921),(20131001,20131007)],
        2014:[(20140101,20140101),(20140131,20140206),(20140405,20140407),(20140501,20140503),(20140531,20140602),(20140906,20140908),(20141001,20141007)],
        2015:[(20150101,20150103),(20150218,20150224),(20150405,20150406),(20150501,20150503),(20150620,20150622),(20150927,20150927),(20151001,20151007)],
        2016:[(20160101,20160103),(20160207,20160213),(20160402,20160404),(20160430,20160502),(20160609,20160611),(20160915,20160917),(20161001,20161007)],
        2017:[(20170101,20170102),(20170127,20170202),(20170402,20170404),(20170429,20170501),(20170528,20170530),(20171001,20171008)],
        }

czce_dict = {
        2005:[(20050101,20050103),(20050207,20050215),(20050501,20050508),(20051001,20051009)],
        2006:[(20060101,20060103),(20060128,20060205),(20060501,20060507),(20061001,20061008)],
        2007:[(20070101,20070103),(20070217,20070225),(20070501,20070507),(20071001,20071007),(20071230,20071231)],
        2008:[(20080101,20080101),(20080206,20080212),(20080404,20080406),(20080501,20080503),(20080607,20080609),(20080913,20080915),(20080929,20081005)],
        2009:[(20090101,20090103),(20090125,20090131),(20090404,20090406),(20090501,20090503),(20090528,20090530),(20091001,20091008)],
        2010:[(20100101,20100103),(20100213,20100219),(20100403,20100405),(20100501,20100503),(20100614,20100616),(20100922,20100924),(20101001,20101007)],
        2011:[(20110101,20110103),(20110202,20110208),(20110403,20110405),(20110430,20110502),(20110604,20110606),(20110910,20110912),(20111001,20111007)],
        2012:[(20120101,20120103),(20120122,20120128),(20120402,20120404),(20120429,20120501),(20120622,20120624),(20120930,20121007)],
        2013:[(20130101,20130103),(20130209,20130215),(20130404,20130406),(20130429,20130501),(20130610,20130612),(20130919,20130921),(20131001,20131007)],
        2014:[(20140101,20140101),(20140131,20140206),(20140405,20140407),(20140501,20140503),(20140531,20140602),(20140906,20140908),(20141001,20141007)],
        2015:[(20150101,20150103),(20150218,20150224),(20150405,20150406),(20150501,20150503),(20150620,20150622),(20150927,20150927),(20151001,20151007)],
        2016:[(20160101,20160103),(20160207,20160213),(20160402,20160404),(20160430,20160502),(20160609,20160611),(20160915,20160917),(20161001,20161007)],
        2017:[(20170101,20170102),(20170127,20170202),(20170402,20170404),(20170429,20170501),(20170528,20170530),(20171001,20171008)],
        }
holiday_map = {"CZCE":czce_dict,"SHFE":shfe_dict,"DCE":dce_dict,"CFFEX":{}}

def load_cadict():
    f = open("ca.future")
    cadict = {}
    for line in f:
        s = line.upper()
        s = s.strip("\n").split(" ");
        exchange = s[0];
        product = s[2].split(":")[1]
        #print exchange, " ", product;
        #sys.exit(0);
        if cadict.has_key(product):
            pass
        #print "duplicate", s
        else:
            cadict[product]=exchange;
        #print len(cadict);
    return cadict;
    pass

cadict = load_cadict();


def get_date_list(start_date, end_date):
    day = start_date;
    mlist=[]
    while day <= end_date:
        mlist.append(day)
        day = day + dt.timedelta(days=1);
    return mlist
    pass



def is_holiday(exchange, date):
    holiday_list = holiday_map[exchange][date.year]
    tradeday = date.year * 10000 + date.month * 100 + date.day;
    for item in holiday_list:
        if tradeday > item[0] and tradeday < item[1]:
            return True
        if tradeday < item[1]:
            break;
    return False;


def gen_shfe(exchange, product):
    f = open(exchange + "/" + product + ".ca","a+")
    is_last_holiday=False;
    begin = dt.datetime(2005,1,1);
    mlist = get_date_list(dt.datetime(2005,1,1), dt.datetime(2017,12,30))
    for day in mlist:
        if  is_holiday(exchange,day):
            is_last_holiday = True
            continue;

        if day.weekday()==6 or day.weekday()==5:
            continue;
            pass

        #this is a trading day
        time_format = ","+"09:00-11:30" + "," + "13:30-15:00";
        if is_last_holiday:
            #not night
            #time_format = ","+"09:00-11:30" + "," + "13:30-15:00";
            is_last_holiday = False
        else:
            if day <= dt.datetime(2013,7,4):
                pass
            elif day >= dt.datetime(2013,7,5):
                if product == "AG" or product == "AU":
                    #au,ag 20130705 night
                    time_format = ","+"21:00-02:30" + "," + "09:00-11:30" + "," + "13:30-15:00";
                    pass
                elif day >= dt.datetime(2013,12,20) and (product == "CU" or product=="AL" or product =="PB" or product=="ZN") :
                    time_format = ","+"21:00-01:00" + "," + "09:00-11:30" + "," + "13:30-15:00";
                    #cu,al,pb,zn night
                elif day >= dt.datetime(2014,12,26) and (product == "RU"):
                    time_format = ","+"21:00-01:00" + "," + "09:00-11:30" + "," + "13:30-15:00";
                    pass
                elif day >= dt.datetime(2014,12,26) and day < dt.datetime(2016,5,3) and (product == "RB" or product == "BU" or product == "HC"):
                    time_format = ","+"21:00-01:00" + "," + "09:00-11:30" + "," + "13:30-15:00";
                    pass
                elif day >= dt.datetime(2016,5,3) and (product == "RB" or product == "BU" or product == "HC"):
                    time_format = ","+"21:00-23:00" + "," + "09:00-11:30" + "," + "13:30-15:00";
                    pass
                elif day >= dt.datetime(2014,12,26):
                    #default  SN, NI
                    time_format = ","+"21:00-01:00" + "," + "09:00-11:30" + "," + "13:30-15:00";
                    pass
                pass
            pass
        pass
        time_format = day.strftime('%Y%m%d')+time_format;
        f.write(time_format+"\n");
    #ss = time_format + "," + "09:00-11:30"+","+"13:30-15:00"+"\n";
    f.close()
    pass

def gen_czce(exchange,product):
    f = open(exchange + "/" + product + ".ca","a+")
    is_last_holiday=False;
    mlist = get_date_list(dt.datetime(2005,1,1), dt.datetime(2017,12,30))
    for day in mlist:
        if  is_holiday(exchange,day):
            is_last_holiday = True
            continue;

        if day.weekday()==6 or day.weekday()==5:
            continue;
            pass

        #this is a trading day
        time_format = ","+"09:00-11:30" + "," + "13:30-15:00";
        if is_last_holiday:
            #not night
            #time_format = ","+"09:00-11:30" + "," + "13:30-15:00";
            is_last_holiday = False
        else:
            if day >= dt.datetime(2014,12,12) and (product in ["MA","RM","CF","PTA","SR"]) :
                time_format = ","+"21:00-23:30" + "," + "09:00-11:30" + "," + "13:30-15:00";
                pass
        pass
        time_format = day.strftime('%Y%m%d')+time_format;
        f.write(time_format+"\n");
    #ss = time_format + "," + "09:00-11:30"+","+"13:30-15:00"+"\n";
    f.close()
    pass

def gen_dce(exchange,product):
    f = open(exchange + "/" + product + ".ca","a+")
    is_last_holiday=False;
    mlist = get_date_list(dt.datetime(2005,1,1), dt.datetime(2017,12,30))
    for day in mlist:
        if  is_holiday(exchange,day):
            is_last_holiday = True
            continue;

        if day.weekday()==6 or day.weekday()==5:
            continue;
            pass

        #this is a trading day
        time_format = ","+"09:00-11:30" + "," + "13:30-15:00";
        if is_last_holiday:
            #not night
            #time_format = ","+"09:00-11:30" + "," + "13:30-15:00";
            is_last_holiday = False
        else:
            if day >= dt.datetime(2014,7,4) and day < dt.datetime(2015,5,8) and (product in ["P","J"] ) :
                time_format = ","+"21:00-02:30" + "," + "09:00-11:30" + "," + "13:30-15:00";
                pass
            elif day>=dt.datetime(2014,12,16) and day < dt.datetime(2015,5,8) and (product in ["Y","M","P","J","A","B","JM","I"]):
                time_format = ","+"21:00-02:30" + "," + "09:00-11:30" + "," + "13:30-15:00";
                pass
            elif day>=dt.datetime(2015,5,8) and (product in ["Y","M","P","J","A","B","JM","I"]):
                time_format = ","+"21:00-23:30" + "," + "09:00-11:30" + "," + "13:30-15:00";
                pass

        pass
        time_format = day.strftime('%Y%m%d')+time_format ;
        f.write(time_format+"\n");
    #ss = time_format + "," + "09:00-11:30"+","+"13:30-15:00"+"\n";
    f.close()
    pass

def gen_trading_time(cadict):
    for product,exchange in  cadict.items():
        print exchange,product;
        os.system("mkdir -p %s" %exchange);
        if exchange == "SHFE":
            gen_shfe(exchange,product)
            pass
        if exchange == "CFFEX":
            pass
        if exchange == "DCE":
            gen_dce(exchange,product)
            pass
        if exchange == "CZCE":
            gen_czce(exchange,product)
            pass
        pass
#tmp = datetime.datetime.now()
#print tmp.weekday();
#sys.exit(0);


if __name__ == "__main__":
    now = dt.datetime(2017,1,1);
    #print now.weekday()
    #print now.year;
    #tradeday = now.year * 10000 + now.month * 100 + now.day;
    #print tradeday
    #a = (20170101,20170102)
    #if tradeday >= a[0] and tradeday <=a[1]:
    #    print a[0]
    #sys.exit(0);
    cadict = load_cadict();
    gen_trading_time(cadict)
    pass
