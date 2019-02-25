#!/usr/bin/env/python

from __future__ import print_function
import psycopg2
import sys

sys.stdout = open('Logs Analysis', 'wt')


# db connections
def establish_db_connection():
    DBNAME = "news"
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    return db, c


def most_popular_articles():

    print(
        'Question 1: What are the most popular three articles of all time?\n'
            )
    db, c = establish_db_connection()
    query = """
        select articles.title,
            count(*) as num
        from articles, log
        where '/article/' || articles.slug = log.path
        group by articles.title
        order by num desc
        limit 3
    """

    c.execute(query)
    articles = c.fetchall()
    db.close()

    for index, each in enumerate(articles):
        print("%s. '%s' -- %s views" % (index + 1, each[0], each[1]))
    return


def most_popular_authors():
    print(
        "\n================================================"
            )
    print(
        '\nQuestion 2: Who are the most popular article authors of all time?\n'
            )

    db, c = establish_db_connection()

    query = """
        select authors.name,
            count(*) as num
        from authors, articles, log
        where '/article/' || articles.slug = log.path
            and articles.author = authors.id
        group by authors.name
        order by num desc
    """
    c.execute(query)
    authors = c.fetchall()
    db.close()

    for index, each in enumerate(authors):
        print("%s. %s -- %s views" % (index+1, each[0], each[1]))
    return


def high_error_days():
    print(
        "\n================================================"
            )
    print('\n')
    print(
        'Question 3: On which days did more than'
        ' 1% of requests lead to errors?'
            )

    db, c = establish_db_connection()

    # define query needed
    query = """
        with requests as (
        select time::date as day, count(*)
        from log
        group by time::date
        order by time::date),
    errors as (
        select time::date as day, count(*)
        from log
        where status like '4%'
        group by time::date
        order by time::date),
    error_rate as (
        select requests.day,
            (errors.count::float / requests.count::float) * 100
                as error_percentage
        from requests, errors
        where requests.day = errors.day)
    select * from error_rate where error_percentage >1;
    """
    c.execute(query)

    error_days = c.fetchall()
    db.close()

    for each in error_days:
        print("- %s -- %s%% errors" % (each[0], each[1]))
    return


if __name__ == "__main__":
    most_popular_articles()
    most_popular_authors()
    high_error_days()
