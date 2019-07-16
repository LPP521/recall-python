from flask import Flask
from flask import request
from flask import jsonify
import json
from rubbish import queryByKeyWord, getSuggest

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

#查询某个东西所属分类
@app.route('/query', methods=['GET', 'POST'])
def query():
    keyword =  request.args.get("keyword")
    if keyword == '' or keyword == None:
        return ''
    return queryByKeyWord(keyword)

#建议搜索
@app.route('/suggest', methods=['GET', 'POST'])
def suggest():
    keyword =  request.args.get("keyword")
    if keyword == '' or keyword == None:
        return ''
    suggestResult = getSuggest(keyword)
    return suggestResult



if __name__ == '__main__':
    app.run()