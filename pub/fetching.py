from sklearn.datasets import fetch_20newsgroups

class Fetching():

    def __init__(self):
        self.interesting = None
        self.not_interesting = None

    def fetch_data(self):
        interesting_categories=[
            'alt.atheism',
            'comp.graphics',
            'comp.os.ms-windows.misc',
            'comp.sys.ibm.pc.hardware',
            'comp.sys.mac.hardware',
            'comp.windows.x',
            'misc.forsale',
            'rec.autos',
            'rec.motorcycles',
            'rec.sport.baseball'
        ]

        not_interesting_categories=[
            'rec.sport.hockey',
            'sci.crypt',
            'sci.electronics',
            'sci.med',
            'sci.space',
            'soc.religion.christian',
            'talk.politics.guns',
            'talk.politics.mideast',
            'talk.politics.misc',
            'talk.religion.misc'
        ]

        self.interesting=fetch_20newsgroups(subset='all',categories=interesting_categories)
        self.not_interesting=fetch_20newsgroups(subset='all',categories=not_interesting_categories)
        return
    
    def get_20_messages(self):
        try:
            interesting = []
            not_interesting = []
            for i in range(10):
                interesting.append(self.interesting.data.pop(0))
                not_interesting.append(self.not_interesting.data.pop(0))
            return {"interesting" : interesting, "not_interesting" : not_interesting}
        except Exception as e:
            return {"Error" : "error getting messages."}