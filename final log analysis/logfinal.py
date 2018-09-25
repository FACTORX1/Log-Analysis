#! /usr/bin/env python3
#PROJECT:-LOG ANALYSIS
import psycopg2
import time
def connect(database_name="news"):
    """Connect to the PostgreSQL database. Returns a database connection """
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print ("Unable to connect to the database")
	
query1="""
      SELECT article_vie.title, article_vie.view
      FROM article_vie
      ORDER BY article_vie.view DESC
      LIMIT 3;
    """
query2="""select authors.name,sum(article_view.views) as views from
article_view,authors where authors.id = article_view.author
group by authors.name order by views desc"""

query3="""
    SELECT *
    FROM error_rate
    WHERE error_rate.percentage > 1
    ORDER BY error_rate.percentage DESC;
    """

def popular_article(query1):
    db=connect()
    c=db.cursor()
    c.execute(query1)
    results=c.fetchall()
    for i in range(len(results)):
        title=results[i][0]
        views=results[i][1]
        print("%s--%d" % (title,views))
    db.close()

def popular_authors(query2):
    db=connect() 
    c=db.cursor()
    c.execute(query2)
    results=c.fetchall()
    for i in range(len(results)):
        name=results[i][0]
        views=results[i][1]
        print("%s--%d" % (name,views))
    db.close()

def error_percent(query3):
    db=connect()
    c=db.cursor()
    c.execute(query3)
    results=c.fetchall()
    for i in range(len(results)):
        date=results[i][0]
        err_prc=results[i][1]
        print("%s--%.1f %%" %(date,err_prc))

if __name__ == "__main__":
  print("THE LIST OF POPULAR ARTICLES ARE:")
  popular_article(query1)
  print("\n")
  print("THE LIST OF POPULAR AUTHORS ARE:")
  popular_authors(query2)
  print("\n")
  print("PERC ERROR MORE THAN 1.0:")
  error_percent(query3)
    
    