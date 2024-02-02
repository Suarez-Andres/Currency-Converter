# CURRENCY COMPARATOR BASES IN EURO'S CUANTITIES
#### Video Demo:  <https://youtu.be/42VuRFUhF40>
#### Description:
Hi there. I am Andrés Suárez, the developer behind this proyect. Short presentation: I am 23 years old and come from Bogotá, Colombia.
So, my proyect is a currency comparator that works with an API request. The API link is [this.](https://exchangeratesapi.io/) Is called _exchangerates_ and once I request info from it using the requests library, it gives to me a json object, that my code can read as a dict object.

Allow me to list the operating order of mi code as follows:
1. The code will prompt the user for a date in YYYY-MM-DD format and after the user writes it, is going to check the format with the `check_format()` funtion. this is because the comparison of the currencies depends on the day the user wants, and this date is an important part of the URL that the code will use for the request.
> The `check_format()` funtion takes two arguments (the user prompt, named as *s* and the format to check, this can be *date* or *currency*) and its labor is to check the format of the user prompt using regexes patterns, in this case, *date*. If the date is in a format that is incorrect, or if is an incorrect date, the code will stop using the `sys` library and showing the user a message related with what is wrong in his promt.
2. The code will prompt the user for the cuantity of euros. in this case the user must write a positive integer, if not, the code will stop via `sys.exit()` due to the `isdigit()` method aplicated to the prompt.
3. The code will ask the user to prompt the currency that wants to be compared to the specified cuantity of euros. here I use the `check_format()` funtion for check the format of the prompt too.
> In this case, the arguments of the funtion are the user prompt and *currency*. for checking the currency, the funtion uses a regex pattern and if the user prompt matches it, look for his presense in a predefined tuple called `valid`. the content of this tuple is listed as follows:
- "CAD"
- "HKD"
- "ISK"
- "PHP"
- "DKK"
- "HUF"
- "CZK"
- "AUD"
- "RON"
- "SEK"
- "IDR"
- "INR"
- "BRL"
- "RUB"
- "HRK"
- "JPY"
- "THB"
- "CHF"
- "SGD"
- "PLN"
- "BGN"
- "TRY"
- "CNY"
- "NOK"
- "NZD"
- "ZAR"
- "USD"
- "MXN"
- "ILS"
- "GBP"
- "KRW"
- "MYR"

4. After all of the steps above, the code will look for the introduced currency requesting a json object from the mentioned API. depending on the currency, the code will call the `euro_to_dollar()` or the `euro_to_other_currency()` funtion, and these funtions are going to calculate the equivalent of the given euro(s) in the given currency.
> The `euro_to_dollar()` funtion takes two arguments: the cuantity of euros and the date given by the user. with these, the funtion fills the gaps in the URL that the code is using to requesting the info from the API. since the currency here is USD, is not necesary to specify that in this funtion.
> In the `euro_to_other_currency()` funtion the arguments are a little bit diferent. here the funtion needs 3, not 2 arguments: the cuantity of euros, the currency that the user is asking for and the date given by the user. Nevertheless, the procedure is almost the same that in the `euro_to_dollar()` funtion, having the difference in the URL for the request, since here it is going to have one gap more, that is going to be filled with the *currency* argument.