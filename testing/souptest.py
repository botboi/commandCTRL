from bs4 import BeautifulSoup
import urllib

query = "http://forcast.weather.gov/shmrn.php?mz=amz117&syn=amz101"
with urllib.request.urlopen(query) as amz117:
    document = BeautifulSoup(amz117.read())
