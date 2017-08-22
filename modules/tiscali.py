#!/usr/bin/env python
# -*- coding: utf-8 -*-

from news import News
from source import Source
import requests
from bs4 import BeautifulSoup

class Tiscali(Source):
	def __init__(self):
		self.homepage = "http://notizie.tiscali.it"
		self.name = "Tiscali"
		self.lastNews = News(None,None,None,None)
		Source.__init__(self,self.homepage,self.lastNews,self.name)

	def getArticle(self):
		"""

		Params: None
		Returns: News (Object)
	
		This method issue a requests to the website and scrape some informations
		such as, article time, url, date...

		"""
		data = requests.get(self.homepage+"/ultimora/").content
		page = BeautifulSoup(data,"lxml")
		article = page.findAll("article")[0]
		art_url = article.findAll("a",href=True)[2]['href']
		art_date = article.findAll("time")[0].text
		art_time = article.findAll("time")[1].text
		art_title= article.find("h3").text
		return News(url = self.homepage+art_url,date = art_date,time = art_time,title = art_title,source = self.homepage,source_name = self.name)

	def getNews(self):
		"""

		Params: None
		Returns: News (Object)
	
		This method check whether if the last news is different from the 
		one scraped now, if it is, returns this one instead of
		the lastNews, and update that one

		"""
		tmp = self.getArticle()
		if self.lastNews.equals(tmp):
			return self.lastNews
		self.lastNews = tmp
		return self.lastNews
