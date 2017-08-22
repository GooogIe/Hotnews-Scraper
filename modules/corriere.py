#!/usr/bin/env python
# -*- coding: utf-8 -*-

from news import News
from source import Source
import requests
from bs4 import BeautifulSoup

class Corriere(Source):
	def __init__(self):
		self.homepage = "http://www.corriere.it"
		self.name = "Corriere"
		self.lastNews = News("","","")
		Source.__init__(self,self.homepage,self.lastNews,self.name)

	def getArticle(self):
		data = requests.get(self.homepage+"/notizie-ultima-ora/index.shtml").content
		page = BeautifulSoup(data,"lxml")
		article = page.findAll("li",attrs={"class" : "listing-item"})[0]
		try:
			art_url = article.findAll("a",href=True)[2]['href']
		except:
			art_url = article.findAll("a",href=True)[1]['href']
		art_date = article.find("span",attrs={"class" : "news-date"}).text
		art_time = article.find("span",attrs={"class" : "news-time"}).text
		art_title= article.find("h5",attrs={"class" : "news-title"}).text
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
