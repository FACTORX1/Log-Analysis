Launching the Virtual Machine:

Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  $ vagrant up
Then Log into this using command:
  $ vagrant ssh
Change directory to /vagrant and look around with ls.
Setting up the database and Creating Views:

Load the data in local database using the command:
  psql -d news -f newsdata.sql
The database includes three tables:

The authors table includes information about the authors of articles.
The articles table includes the articles themselves.
The log table includes one entry for each time a user has accessed the site.
views:
Q1.
CREATE VIEW author_info AS
SELECT authors.name, articles.title, articles.slug
FROM articles, authors
WHERE articles.author = authors.id
ORDER BY authors.name;

CREATE VIEW path_view AS
SELECT path, COUNT(*) AS view
FROM log
GROUP BY path
ORDER BY path;

CREATE VIEW article_vie AS
SELECT author_info.name, author_info.title, path_view.view
FROM author_info, path_view
WHERE path_view.path = CONCAT('/article/', author_info.slug)
ORDER BY author_info.name;

Q2.

create view article_view as select title,author,count(*) as views from articles,log where 
  log.path like concat('%',articles.slug) group by articles.title,articles.author 
  order by views desc;
  
  
Q3.
CREATE VIEW error_view AS
SELECT date(time), COUNT(*) AS errors
FROM log WHERE status = '404 NOT FOUND' 
GROUP BY date(time) 
ORDER BY date(time);
CREATE VIEW error_rate AS
SELECT total_view.date, (100.0*error_view.errors/total_view.views) AS percentage
FROM total_view, error_view
WHERE total_view.date = error_view.date
ORDER BY total_view.date;