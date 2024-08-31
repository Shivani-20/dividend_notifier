import requests
from datetime import datetime,timedelta
import json
from bs4 import BeautifulSoup

marketPriceUrl = "https://www.google.com/finance/quote/"
eventCalendarUrl = "https://groww.in/v1/api/stocks_data/equity_feature/v2/corporate_action/event/"

def calculateDateRange():
    min_date = (datetime.today()+timedelta(12)).strftime('%Y-%m-%d')
    max_date = (datetime.today()+timedelta(17)).strftime('%Y-%m-%d')
    return min_date,max_date


# determine if the share is good to buy
# A share is good if the following conditions are met for me
def vote(dps, mp):
    if dps>=5 and dps<=7 and mp<=650:
        return True
    elif dps>7 and dps<=10 and mp<=800:
        return True
    elif dps>10 and dps<=15 and mp<=1100:
        return True
    elif dps>15 and mp<=1300:
        return True
    else:
        return False
    

# get marketPrice of a shares whose dividend is >=5 rupees
def getMarketPrice(ticker,stockExchange):
    url = f'{marketPriceUrl}{ticker}:{stockExchange}'
    try: 
        res = requests.get(url,timeout=10)
    except:
        return -1
    try:
        priceClassId = "YMlKec fxKbKc"
        response = res.text
        if not response:
            return None
        soup = BeautifulSoup(response,'html.parser')
        classContent = soup.find(class_=priceClassId)
        currentMp = float(classContent.text[1:].replace(",",""))
        return currentMp
    except:
        return None
    

def getDividendDetails():
    min_date,max_date = calculateDateRange()
    params = {
        "from": min_date,
        "to": max_date
    }
    eventCalendar = []
    dividendTypeCalendar = []
    filteredDividendTypeCalendar = []
    try: 
        response = json.loads(requests.get(eventCalendarUrl,params,timeout=10).text)
        eventCalendar = response["exdateEvents"]
    except:
        return "Groww event calendar url not working"
    if(eventCalendar):
        dividendTypeCalendar = list(filter(lambda e: e["type"]=="DIVIDEND",eventCalendar))
        if not dividendTypeCalendar:
            return "No dividend type events in the forthcoming week"
        for d in dividendTypeCalendar:
            div_amount = float(d["details"][1:].replace(" per share",""))
            # I want to tade only those share who are offering dividend>=5
            if div_amount>=5:
                nseMp = None
                bseMp = None
                exchange = None
                mp = None
                # check which stock exchange bse or nse is offering lower market price to buy the share
                if "nseSymbol" in d:
                    nseMp = getMarketPrice(d["nseSymbol"],"NSE")
                if "bseSymbol" in d:
                    bseMp = getMarketPrice(d["bseSymbol"],"BOM")
                if nseMp == -1 or bseMp == -1:
                    return "Google finance market price url not working"
                if nseMp and bseMp:
                    if nseMp<=bseMp:
                        mp = nseMp
                        exchange = "NSE"
                    else:
                        mp = bseMp
                        exchange = "BSE"
                if not nseMp:
                    mp=bseMp
                    exchange = "BSE"
                if not bseMp:
                    mp=nseMp
                    exchange = "NSE"
                # bse or nse symbol data still there but stock might have got delisted  
                if(mp):
                    if(vote(div_amount, mp)):
                        item = dict(
                            Name = d["companyShortName"],
                            Dividend = div_amount,
                            ExDate = d["corporateEventPillDto"]["primaryDate"],
                            MarketPrice = mp,
                            Exchange = exchange
                        )
                        filteredDividendTypeCalendar.append(item)
        if filteredDividendTypeCalendar:
            return filteredDividendTypeCalendar
        else:
            return "No good dividends for you"
    else:
        return "No events for the forthcoming event"


if __name__=="__main__":
    getDividendDetails()
