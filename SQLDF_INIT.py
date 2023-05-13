from pandasql import sqldf
pysqldf = lambda q: sqldf(q,globals())

query = '''
SELECT * FROM df
'''
res = pysqldf(query)
