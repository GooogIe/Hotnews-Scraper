#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Source():
	"""
	Guideline to the others news scraper modules
	"""
	def __init__(self,homepage,lastNews,websitename = ""):
		self.homepage = homepage
		self.websitename = websitename
		self.lastNews = lastNews
	def getNews(self):
		raise NotImplementedError
