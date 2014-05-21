##scrape zillow for information fed in from CSV 
##by @peteyreplies

import xmltodict
import csv 
import urllib
import urllib2


##set variables
zpid = 'X1-ZWz1dtw75sqd57_39zrb'
address = '69+Summer+St+Apt+2'
citystate = 'Watertown%2C+MA'
baseGetResults = 'http://www.zillow.com/webservice/GetSearchResults.htm'
baseGetDeep = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm'

##get & parse results
resultURL = baseGetResults + '?zws-id=' + ZKEY + '&address=' + address + '&citystatezip=' + citystate
resultParsed = xmltodict.parse(urllib2.urlopen(resultURL).read())
u_zpid = data['SearchResults:searchresults']['response']['results']['result']['zpid']
zpid = str(u_zpid)

