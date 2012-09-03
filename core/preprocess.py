'''
Created on Sep 3, 2012

@author: Ismail Sunni
'''

class Preprocess():
    '''
    Class for preprocessing a text
    '''


    def __init__(self, text=''):
        '''
        Constructor
        '''
        self.text = text

    def normalize_character(self):
        ''' Normalize unicode character in tweet_text.'''

        from unicodedata import normalize
        self.text = normalize('NFKD', self.text.decode('latin-1')
                              ).encode('ascii','ignore')

    def remove_punctuation(self):
        ''' Remove punctuation from a string.
            Set text without punctuation and \n'''

        from string import punctuation
        for punct in punctuation + '\n':
            self.text = self.text.replace(punct, '')
