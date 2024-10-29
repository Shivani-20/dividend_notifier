## Working:-

* Using Windows Task Scheduler, my script (notifier.py) executes every wednesday and sends me the list of dividend stocks on my email.

* Conditions for the stock is based on how much premium I can pay with respect to the dividend offered and the market price to trade it in the ex-fividend week.

* Script requests dps=dividend per share of companies 
whose ex-dividend date falls on day T where T: 
can be any day in the range {Monday...Friday}
Example if today is 27 august, day is a wednesday


    * x1=27+12 => 8th of sept
    * x2=27+13 => 9th of sept
    * x3=27+14 => 10th of sept
    * x4=27+15 => 11th of sept
    * x5=27+16 => 12th of sept

        * return the dividend list from 8th to 12th september
        * Notification is received only on wednesday and 2 weeks prior to the Ex-date

* The list contains five key points:
    * Name of the stock
    * Dividend offered,
    * Ex-dividend Date 
    * Market price
    * Stock exchange - BSE or NSE

* The api used to fetch dividend data:
    https://groww.in/v1/api/stocks_data/equity_feature/v2/corporate_action/event/

* The api used to fetch market prices:
    https://www.google.com/finance/quote/


## Caveats:-
1. market sentiments must be positive to neutral
2. Stock must be listed on NSE

