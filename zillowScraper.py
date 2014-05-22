##scrape zillow for information fed in from CSV 
##by @peteyreplies

import xmltodict
import csv 
import urllib
import urllib2
import unicodedata

#need to redo w/ beautifulsoup 


##set variables
zkey = 'X1-ZWz1dtw75sqd57_39zrb'
address = '69+Summer+St+Apt+2'
citystate = 'Watertown%2C+MA'
baseGetResults = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm'

##get & parse results
resultURL = baseGetResults + '?zws-id=' + zkey + '&address=' + address + '&citystatezip=' + citystate + '&rentzestimate=True'
resultParsed = xmltodict.parse(urllib2.urlopen(resultURL).read())

#walk the xml tree (as per http://git.io/A_1SYA)
#then, load results into an ASCII string (as per http://goo.gl/MXQajp) for loading in dict
useCode = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['useCode']).encode('ascii','ignore')
zpid = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['zpid']).encode('ascii','ignore')
listing = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['links']['homedetails']).encode('ascii','ignore')
mapListing = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['links']['mapthishome']).encode('ascii','ignore')
latitude = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['address']['latitude']).encode('ascii','ignore')
longitude = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['address']['longitude']).encode('ascii','ignore')
baths = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['address']['bathrooms']).encode('ascii','ignore')
beds = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['bedrooms']).encode('ascii','ignore')
yearBuilt = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['yearBuilt']).encode('ascii','ignore')
zestimate = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['zestimate']['amount']['#text']).encode('ascii','ignore')
zestimate_updated = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['zestimate']['last-updated']).encode('ascii','ignore')
zestimate_low = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['zestimate']['valuationRange']['low']['#text']).encode('ascii','ignore')
zestimate_high = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['zestimate']['valuationRange']['high']['#text']).encode('ascii','ignore')
rentzestimate = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['rentzestimate']['amount']['#text']).encode('ascii','ignore')
rentzestimate_updated = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['rentzestimate']['last-updated']).encode('ascii','ignore')
rentzestimate_low = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['rentzestimate']['valuationRange']['low']['#text']).encode('ascii','ignore')
rentzestimate_high = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['rentzestimate']['valuationRange']['high']['#text']).encode('ascii','ignore')
taxAssessment = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['taxAssessment']).encode('ascii','ignore')
taxAssessmentYear = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['taxAssessmentYear']).encode('ascii','ignore')
lastSoldDate = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['lastSoldDate']).encode('ascii','ignore')
lastSoldPrice = unicodedata.normalize('NFKD', resultParsed['SearchResults:searchresults']['response']['results']['result']['lastSoldPrice']['#text']).encode('ascii','ignore')


thisProperty = {
				'hometype' = 
	
}



