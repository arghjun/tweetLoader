import json
import os,glob

def extractTweetJSON(filename):
	with open (filename) as json_data:
	    for line in json_data:
	        try:
	            dataText = json.loads(line)
	        except ValueError:
	            print(filename)
	            continue

	        values = [ ]
	       	values.append(filename)
	       	values.append(dataText['created_at'])
	       
	        if isinstance(dataText['geo'], dict):
	            values.append('"' + str(dataText['geo']['coordinates'][0]) + ',' + str(dataText['geo']['coordinates'][1]) + '"')

	        else:
	            values.append("")

	        if isinstance(dataText['place'], dict):
	            values.append('"' + str(dataText['place']['full_name']) + '"')

	        else:
	            values.append("")

	        dq = dataText['text'].replace('"', '\\"')
	        dq = dq.replace('\n','\\n')
	        dq = dq.replace("'", "\\'")
	        dq = dq.replace(",", " ")
	        values.append('"' + dq + '"')

	        outputstr = ','.join(values)
	        return(outputstr)

of = open('./outexp.csv', 'w')
of.write('filename' + ',' + 'created_at' + ',' + 'geo' + ',' + 'place' +  ',' + 'text')
of.write("\n")

json_folder_path = './tweet/'
for filename in glob.glob(os.path.join(json_folder_path, '*.json')):
    print(filename)
    of.write(extractTweetJSON(filename))
    of.write("\n")


of.close()
