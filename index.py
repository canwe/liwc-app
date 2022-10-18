from flask import Flask, request
import liwc.liwcExtractor as le

LIWC = le.liwcExtractor(liwcPath='./data/LIWC2007_English100131.dic')
categories = {c: i for i, c in enumerate(LIWC.getCategoryIndeces())}

app = Flask(__name__)


@app.route('/api/analyze', methods=['POST'])
def test():
    request_data = request.get_json()
    tweet = request_data['tweet']
    features_r = request_data['features']
    features_e = LIWC.extractFromDoc(tweet or '')
    return {f: features_e[categories[f]]/float(features_e[66]) for f in features_r if f in categories}
