#!/usr/bin/env python
# -*- coding: utf-8 -*-

from news import News
from source import Source
import requests
from bs4 import BeautifulSoup

class Ansa(Source):
	def __init__(self):
		self.homepage = "http://www.ansa.it"
		self.name = "Ansa"
		self.lastNews = News(None,None,None,None)
		Source.__init__(self,self.homepage,self.lastNews,self.name)


	def getArticle(self):
		"""

		Params: None
		Returns: News (Object)
	
		This method issue a requests to the website and scrape some informations
		such as, article time, url, date...

		"""
		data = requests.get(self.homepage+"/sito/notizie/topnews/index.shtml").content
		page = BeautifulSoup(data,"lxml")
		article = page.findAll("article",attrs={"class" : "news small"})[0]
		art_url = article.find("a",href=True)['href']
		art_date = article.find("em").text.replace("-","")
		art_time = article.find("span").text.replace("-","")
		art_title= article.find("h3",attrs={"class" : "news-title"}).text
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
