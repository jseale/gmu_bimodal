import pandas as pd
import sys
import glob
import json

data_path = 'mmimdb/dataset/'

movies = pd.DataFrame()
for file in glob.glob('{}*.json'.format(data_path)): 
	data = json.load(open(file))
	title = data['title']
	plot = u' '.join(data['plot'])
	text = u'{} {}'.format(title, plot)
	genres = u' '.join(data['genres'])
	data_df = pd.DataFrame({'text' : text, 'tags' : genres}, index=[0])
	movies = movies.append(data_df)

movies.to_csv('text_labels.csv', index=False, encoding='utf-8')



