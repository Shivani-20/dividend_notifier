## Working:-

* Using Windows Task Scheduler, my script (notifier.py) executes every wednesday and sends me the list of dividend stocks on my email.

* Conditions for the stock is based on how much premium I can pay with respect to the dividend offere and the market price to trade it in the ex-fividend week.

* Script request dps=dividend per share of companies 
whose ex-dividend date falls on day T where T: 
can be any day in the range {x1..x5} from every week's wednesday
Example if today is 27 august, day is a wednesday


    * x1=28+10 => 8th of sept
    * x2=28+11 => 9th of sept
    * x3=28+12 => 10th of sept
    * x4=28+13 => 11th of sept
    * x5=28+14 => 12th of sept

    return the dividend list from 8th to 12th september

* The list contains five key points:
    * Name of the stock
    * Dividend offered,
    * Ex-dividend Date 
    * current market price
    * stock Exchange

* The api used to fetch dividend data:
    https://groww.in/v1/api/stocks_data/equity_feature/v2/corporate_action/event/

* The api used to fetch market prices:
    https://www.google.com/finance/quote/

