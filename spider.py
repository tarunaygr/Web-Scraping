import requests
import bs4
for i in range(1,11):
    req=requests.get(f"https://quotes.toscrape.com/page/{i}/")
    body=bs4.BeautifulSoup(req.text,'lxml')
    div_container=body.find('div',attrs={"class":"container"})
    div_row=div_container.find_all('div',attrs={"class":"row"})[1]
    div_col=div_row.find_all('div',attrs={"class":"col-md-8"})
    div_quote=div_col[0].find_all('div',attrs={"class":"quote"})
    for div in div_quote:
        text=div.find('span',{"class":"text"})
        quote=text.text
        print("Quote:")
        print(quote)
        div_tags=div.find('div',{"class":"tags"})
        tag=div_tags.find_all('a')
        print("Tags:")
        for t in tag:
            try:
                print(t.text)
            except:
                print("NO TAG")
        print("\n")