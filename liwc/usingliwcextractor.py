import liwcExtractor as le
liwc = le.liwcExtractor(liwcPath='./data/LIWC2007_English100131.dic')

doc1 = "This is the first document that I am going to test with liwcExtractor"
doc2 = "The second one might have some werrrrrrrdddd things in it. ;-)"
doc3 = "The third one.....asdf;lkj;alskjdf;lkjasfd, who even knows. The third makes me want to cry!"
corpus = [doc1, doc2, doc3]

features = liwc.extractFromDoc(doc3)

print(features)

categories = {c: i for i, c in enumerate(liwc.getCategoryIndeces())}

print(categories)

proportions = [x/float(features[66]) for x in features]

print(proportions[:])
