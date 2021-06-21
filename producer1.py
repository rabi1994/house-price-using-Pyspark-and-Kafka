from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

from csv import reader
# skip first line i.e. read header first and then iterate over each row od csv as a list
with open('kc_prices1.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Check file as empty
    if header != None:
        # Iterate over each row after the header in the csv
        for row in csv_reader:
           # row variable is a list that represents a row in csv
           producer.send('sales', value=row)	
           sleep(2.5)
            
