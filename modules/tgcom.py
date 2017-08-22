#!/usr/bin/env python
# -*- coding: utf-8 -*-

from news import News
from source import Source
import requests
from bs4 import BeautifulSoup

class Tgcom(Source):
	def __init__(self):
		self.homepage = "http://tgcom24.mediaset.it"
		self.name = "Tgcom24"
		self.lastNews = News("","","")
		Source.__init__(self,self.homepage,self.lastNews,self.name)

	def getArticle(self):
		data = requests.get(self.homepage+"/ultimissima/oraxora.shtml").content
		page = BeautifulSoup(data,"lxml")

		articles = page.find("ul",attrs={"class" : "rt rt__hour"})

		art_date = articles.findAll("time")[0].text
		art_url = articles.findAll("a",href=True)[0]['href']
		art_time = articles.findAll("time")[1].text
		art_title= articles.findAll("h3")[0].text
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
