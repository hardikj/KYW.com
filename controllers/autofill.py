from bs4 import BeautifulSoup
import re,urllib2,sys
import MySQLdb as mdb

def fill():
    page = urllib2.urlopen("https://www.cia.gov/library/publications/the-world-factbook/index.html")
    soup = BeautifulSoup(page)
    ul_tag = soup.find_all('ul',class_="af")
    ul_tag = ul_tag[0]
    a_tag = ul_tag.find_all('a')
    
    db.sdata.truncate()

    for tag in a_tag:
        tag = str(tag)
        soup2 = BeautifulSoup(tag)
        if soup2.a.string != 'World':
            country=str(soup2.a.string)
        else:
            continue
        c_id = soup2.a['href']
        url = "https://www.cia.gov/library/publications/the-world-factbook/"+soup2.a['href']
        page2 = urllib2.urlopen(url)
        soup3 = BeautifulSoup(page2)
        data1 = soup3.find_all('div',class_='CollapsiblePanel')
        final = ""
        content = ""
        for d in data1 :
            content = ""
            head = "<h3 class=\"head\">"+d.span.contents[0].string + d.span.contents[1].string+"</h3>"
            table_tag = d.find_all('table',class_='CollapsiblePanelContent')
            class_name = table_tag[0].tr.find('tr')['class'][0]
            tr1 = table_tag[0].find_all('tr',class_="%s"%class_name)
            div = table_tag[0].find_all('td',id="data")
            for t1,t2 in zip(tr1,div):
                content =str(content)+ "<div id=\"subhead\">"+str(t1.div.a.contents[0].string)+"</div>"+str(t2)    
            final =str(final)+str(head)+ "<div id = \"panel\">"+str(content) + "</div>"
        db.sdata.insert(country_id=c_id,country=country,data=final)
        db.commit()
    return dict(message="filling the database")
