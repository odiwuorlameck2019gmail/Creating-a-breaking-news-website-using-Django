# from django.shortcuts import render

# # Create your views here.


# def news_hotsport_view(request):
#     return render(request,"newshotsport.html")


# importing api
from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def news_hotsport_view(request):
	
	newsapi = NewsApiClient(api_key ='5a5993d67de04b27b411a2d12a15f3ef')
	top = newsapi.get_top_headlines(sources ='techcrunch,bbc-news,the-verge,google-news,cnn-news')

	l = top['articles']
	desc =[]
	news =[]
	img =[]

	for i in range(len(l)):
		f = l[i]
		news.append(f['title'])
		desc.append(f['description'])
		img.append(f['urlToImage'])
	mylist = zip(news, desc, img)

	return render(request, 'newshotsport.html', context ={"mylist":mylist})
