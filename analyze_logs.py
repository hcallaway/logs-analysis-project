#!/usr/bin/env python

from __future__ import print_function
import psycopg2
import sys

sys.stdout = open('logs_analysis.txt', 'wt')


# db connections
def establish_db_connection():
    """
    Establish database, and set cursor,
    returning a tuple of both to be acted on
    """
    DBNAME = "news"
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    return db, c


def most_popular_articles():
    """Query for top 3 articles all time, print those items"""
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

    for index, (title, views) in enumerate(articles, 1):
        print("{}. '{}' -- {} views".format(index, title, views))
    return


def most_popular_authors():
    """
    Query all authors, return all in descending order
    from most popular to least popular based on views on articles written
    """
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

    for index, (author, views) in enumerate(authors, 1):
        print("{}. {} -- {} views".format(index, author, views))
    return


def high_error_days():
    """
    Query all all status responses, get % of error,
    return those over 1% error rate
    """
    print(
        "\n================================================"
            )
    print('\n')
    print(
        'Question 3: On which days did more than'
        ' 1% of requests lead to errors?\n'
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
        select to_char(requests.day, 'Mon DD, YYYY'),
            cast(
                (errors.count::float / requests.count::float) *
                100 as decimal(16, 2)
                )
                as error_percentage
        from requests, errors
        where requests.day = errors.day)
    select * from error_rate where error_percentage >1;
    """
    c.execute(query)

    error_days = c.fetchall()
    db.close()

    for (date, error_percentage) in error_days:
        print("- {} -- {}%% errors".format(date, error_percentage))
    return


if __name__ == "__main__":
    most_popular_articles()
    most_popular_authors()
    high_error_days()
