import requests
from bs4 import BeautifulSoup
import concurrent.futures
#from threading import Lock
import multiprocessing
from multiprocessing import Lock 
import os

class getappledata():

	lock = Lock()
	#2048
	def getid(self,url):
		try:
			
			
			open(os.path.dirname(os.path.realpath(__file__))+"/ids.txt","a").writelines(list(map(lambda id: id.get("href")[8:]+'\n',BeautifulSoup(requests.get(url,headers= {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15"}).content, "html.parser").find_all(class_ = "content-post-title unread"))))
			#self.lock.acquire()
			print(url)
			#self.lock.release()
			return 0

		except Exception as error:
			print(error)
	
			
	def readin_urls(self):
		try:
			return open(os.path.dirname(os.path.realpath(__file__))+"/urls.txt","r").read().splitlines()
		except Exception as error:
			print(error)

	def count_ids(self):
		try:
			 print("# of ids: ",len(open(os.path.dirname(os.path.realpath(__file__))+"/ids.txt","r").read().splitlines()))
			 return 0
		except Exception as error:
			print(error)

	def useThread(self,funcion,datas):
		try:
			with concurrent.futures.ThreadPoolExecutor() as executor:
				executor.map(funcion,datas)
			return 0
		except Exception as error:
			print(error)

	def useProcess(self,funcion,datas):
		try:
			
			with concurrent.futures.ProcessPoolExecutor() as executor:
				executor.map(funcion,datas)
			return 0
		except Exception as error:
			print(error)

if __name__ == '__main__':
	try:
		
		obj = getappledata()
		obj.useProcess(obj.getid,obj.readin_urls())
		obj.count_ids()
	except Exception as error:
		print(error)




