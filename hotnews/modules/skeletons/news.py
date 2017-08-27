#!/usr/bin/env python
# -*- coding: utf-8 -*-

class News():
	"""
	This class is considered to be a helper for handling 
	scraped news.

	"""
	def __init__(self,url,time,title,source="",source_name="",date=""):
		self.url = url
		self.time = time
		self.date = date
		self.title = title
		self.source = source
		self.source_name = source_name

	def getRawNews(self):
		"""

		Params: None
		Returns: Dictionary
	
		This method returns a dictionary containing all news info
		indexed by the following keys: url,time,date,title,source,source_name

		"""
		news = {}
		if self.url is not None: news.update({"url":self.url})
		if self.time is not None: news.update({"time":self.time})
		if self.date is not None: news.update({"date":self.date})
		if self.title is not None: news.update({"title":self.title})
		if self.source is not None: news.update({"source":self.source})
		if self.source_name is not None: news.update({"source_name":self.source_name})
		return news

	def getNews(self):
		"""

		Params: None
		Returns: String
	
		This method returns a string containing essentials info
		regarding the news

		"""
		return "Source: "+self.source_name + "\n" + self.time + " - " + self.title + "\nMore: "+self.url

	def equals(self,news):
		"""

		Params: News Object
		Returns: Bool
	
		This method returns True if the given news is equal to this one
		False if this isn't

		"""
		if news == None: return False
		if news == self: return True
		if self.url != news.url: return False
		if self.time != news.time: return False
		if self.date != news.date: return False
		if self.title != news.title: return False
		return True
