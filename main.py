#!/usr/bin/env python
# -*- coding: utf-8 -*-

from modules import tgcom,ansa,corriere,tiscali

sources = []

sources.append(tgcom.Tgcom())
sources.append(ansa.Ansa())
sources.append(corriere.Corriere())
sources.append(tiscali.Tiscali())

def getAllNews():
	news = []
	for source in sources:
		news.append(source.getNews())
	return news

for item in getAllNews():
	print item.getNews()+"\n"
