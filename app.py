from flask import Flask
import pandas as pd
import pysrt
import json
from markupsafe import escape


myapp = Flask(__name__)




@myapp.route("/")
def home():
    return "search api"



@myapp.route("/search/<string:input>",methods=['GET'])
def search_string(input):

    file_path = "./SS.srt"

    subtitles = pysrt.open(file_path)


    #create a dataset
    dataset = {"index":[],"time_from":[], "time_to":[], "text":[]}

    for subtitle in subtitles:
        dataset["index"].append(subtitle.index)
        dataset["time_from"].append(subtitle.start.to_time())
        dataset["time_to"].append(subtitle.end.to_time())
        dataset["text"].append(subtitle.text.replace("\n", " "))


    #create dataframe
    df = pd.DataFrame(dataset)

    #clean the text column
    replacement = {"♪":"","-":"","\"":"'"}
    df["text"].replace(replacement, regex=True, inplace=True)
    df["text"].str.strip()

    #filter the texts
    word = escape(input)
    pattern = r'(?:\s|^){ptn}(?:\s|$|\?|\!)'.format(ptn=word)
    filtered = df[df["text"].str.contains(pattern,regex=True)]

    #convert to json
    result = filtered.to_json(orient="index")
    parsed = json.loads(result)

    response = myapp.response_class(
                                        response=json.dumps(parsed, indent=4),
                                        status=200,
                                        mimetype='application/json'
                                    )
    
    return response

if __name__ == '__main__':
  myapp.run(host='0.0.0.0',debug=True)