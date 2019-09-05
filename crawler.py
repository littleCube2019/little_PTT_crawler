import requests
from PTT_data import PTT_data
from pyquery import PyQuery as pq

# preprocess
def Crawler(goods=0,today=1):
    base_url = "https://www.ptt.cc"

#boards wanted to crawler
    boards = ["joke","Beauty","Gossiping","marvel","C_Chat","StupidClown"] 

    my_data = {
        'from' :  '/bbs/Beauty/index.html',
        'yes' : 'yes'}

# for over-18 verify
    S = requests.session()
    S.post("https://www.ptt.cc/ask/over18?from=%2Fbbs%2FBeauty%2Findex.html",my_data)


    for curBoard in boards:

        #crate the instanse of data storage
        article_data = PTT_data()

        #print("------------------------------")
        #print("#Start crawling: "+ curBoard)

        article_data.board = curBoard

        for page in range(2):
            #requests
            if page == 0:
                res = S.get(base_url + "/bbs/" + curBoard)

            else:
                res = S.get(base_url + next_url)

            #pyquery
            doc=pq(res.text)        
            articles=doc('.r-ent')
        



            for curArticle in articles:

                #parse the infromation
                url = pq(curArticle)('.title a').attr('href')
                title=pq(curArticle)('.title a').text()
                author=pq(curArticle)('.meta .author').text()
                date=pq(curArticle)('.meta .date').text()
                push = pq(curArticle)('.nrec span').text()

            # Store data   
                if(title != ""):
                    article_data.title = title
                    article_data.url = base_url+url
                    article_data.author = author
                    article_data.date = date
                    article_data.push = push

                    #print data
                    yield (article_data.Get(goods,today))
               
            

            #next page
            next_url =pq(doc('.btn')('a')[3]).attr('href')

        
        #print("#Finish crawling: "+ curBoard)
        #print("------------------------------")
