
import os

os.system('rm -f *.idx')

os.system('sort -u terms.txt -o terms.txt')
os.system('sort -u dates.txt -o dates.txt')
os.system('sort -u tweets.txt -o tweets.txt')

os.system('perl break.pl < terms.txt | db_load -c duplicates=1 -T -t btree te.idx')
os.system('perl break.pl < dates.txt | db_load -c duplicates=1 -T -t btree da.idx')
os.system('perl break.pl < tweets.txt| db_load -c duplicates=1 -T -t hash tw.idx')


os.system('db_dump -p -f 1.txt tw.idx')
os.system('db_dump -p -f 2.txt te.idx')
os.system('db_dump -p -f 3.txt da.idx')
