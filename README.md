## Gumtree AU Quality Engineer Code Test

Hello! :wave:

## The Tasks
- **Task #1: Text Processor** (please implement with your favourite programming language)
  
  i) get list of words that appear in `input.txt`, put them to words.txt with one word each line in upper case ordered alphabetically. 
  
  Example: the string “From fairest creatures we desire increase,” should generate following words: 
  
     CREATURES
     
     DESIRE
     
     FAIREST
     
     FROM
     
     INCREASE
     
     WE
     
  ii) find all of the words in words.txt that are not found in `dictionary.txt`, print the words (one word each line). Lastly, print the total of words that are not found in dictionary.txt.

- **Solution:
    Python has been used as the programming language and 3 different functions have been used to do separate functionality. TextProcessor can be run to run all the functions together.

- **Task #2: Kubernetes**
Create a pod manifest file (nginx.yaml) with following pod specifications:
name => nginx
namespace => test
label => app: nginx
image => nginx
exposed port => 80
liveness check => http on path: / at port: 80

- **Solution
    Issue command - kubectl create -f NginxPod.yml

- **Task #3: Stress Test**
Write a test script which will stress test the following endpoint
https://ecg-api.gumtree.com.au/api/papi/ads/search?categoryId=0&categoryRedirected=1&includeTopAds=1&keyword=Table&locationId=3003435&page=1&size=20&sortType=DATE_DESCENDING

Vary the number of users and cpus 
The response is in a json format e.g.
{
  "ads": [],
  "paging": {
     "links": [],
     "numFound": 23273
  },
  "adSearchOptions": {
    "keyword": "Table",
    "locationId": 3003435,
    "categoryId": 0,
    "categoryRedirected": false
  }
}

Count the number of results that have numFound > 0 and output the percentage of requests that had a status of 200.

- **Solution
    Jmeter is used as the performance test tool. Stress test has been configured with 500 concurrent users with duration of 1.5 hrs in total. I have added a JSON extractor to print the numFound parameter.
    The observation was the numFound would be 0 or < 0 only on error and this count can be known in the number of failures recorded in Aggregate results of jmeter
    Similarly for percentage of 200 response code of requests, we can calculate it based on the Error% recorded in Aggregate result listener.


## Tips
- Try to apply quality mindsets as you start to work on the tasks.
- Once you finish, please upload the code to your git repository and share it to user _yuzhhan_ and let us know where we can access it.
- You could send your code to Dan if you do not have a git account.