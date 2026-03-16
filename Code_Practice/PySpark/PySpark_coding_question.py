#Find duplicates repeated multiple times
#Soultion
df \
.groupby(['column1', 'column2']) \
.count() \
.where('count > 1') \
.sort('count', ascending=False) \
.show()

#delete_duplicate
df.dropDuplicates(['id', 'name']).show()
