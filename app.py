#This is the main app
import requests
import csv
import time

from datetime import datetime


# Open File

# Create Writer Object

access_token = "PUT TOKEN IN HERE"


def getLikes():
   f = open("pages.txt")
   resultFile = open("output.csv",'a')
   wr = csv.writer(resultFile, dialect='excel')
   result = []
   result.append(str(datetime.now())[0:19])
   pages = []
   while 1:
      line = f.readline()
      if not line:
         break
      line = line.strip()
      pages.append(line)

   for page in pages:
      page = page + '?fields=likes'
      #print page
      r = requests.get(page)
      print page + " :" + str(r.json()['likes'])
      result.append(r.json()['likes'])
   getPosts(result, pages)
   wr.writerow(result)
   resultFile.close()
   f.close()

def getPosts(results, pages):
   results.append('SEPERATION')
   for page in pages:
      sum = 0
      page = page[:4] +'s' + page[4:] + '/posts?access_token=397068537067020|WSBnjxOru0C601SZsWYQpDeFT7U'
      r = requests.get(page)
      for i in range(len(r.json()['data'])):
         if 'likes' in r.json()['data'][i].keys():
            sum += r.json()['data'][i]['likes']['count']
      results.append(sum)
   results.append('SEPERATION')
   for page in pages:
      page = page[:4] +'s' + page[4:] + '/posts?access_token=397068537067020|WSBnjxOru0C601SZsWYQpDeFT7U'
      r = requests.get(page)
      numOfPosts = len(r.json()['data'])
      results.append(numOfPosts)
   print "DONE"

   
   
   
while 1:
   getLikes()
   time.sleep(1800)
   
   

