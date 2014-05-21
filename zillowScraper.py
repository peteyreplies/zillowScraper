##scrape zillow for information fed in from CSV 
##by @peteyreplies

import xmltodict
import csv 
import urllib
import urllib2


##set variables
ZKEY = 'X1-ZWz1dtw75sqd57_39zrb'
address = '69+Summer+St+Apt+2'
citystate = 'Watertown%2C+MA'
baseGetResults = 'http://www.zillow.com/webservice/GetSearchResults.htm'

##get & parse results
resultURL = baseGetResults + '?zws-id=' + ZKEY + '&address=' + address + '&citystatezip=' + citystate
resultParsed = xmltodict.parse(result)

print resultParsed

data=xmltodict.parse(urllib2.urlopen(url).read())
