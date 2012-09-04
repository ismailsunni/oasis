'''
Created on Sep 3, 2012

@author: Ismail Sunni
'''

from re import sub
from ttp import Parser

class Preprocess():
    '''
    Class for preprocessing a text
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass


    def normalize_character(self, text):
        ''' Normalize unicode character in tweet_text.
            Args:
                * text = string
            Returns:
                * normal text
        '''

        from unicodedata import normalize
        return normalize('NFKD', text.decode('latin-1')
                              ).encode('ascii','ignore')


    def remove_punctuation(self, text):
        ''' Remove punctuation from a string.
            Args:
                * text = string
            Returns:
                * normal text'''

        from string import punctuation
        for punct in punctuation + '\n':
            text = text.replace(punct, '')
        return text


    def fold_case(self, text, lowercase=True):
        '''Fold case to the same case.
            Args:
                * text = string
                * lowercase = boolean, if true change to lowercase,
                    otherwise to uppercase
            Returns:
                * folded text'''

        if lowercase:
            return text.lower()
        else:
            return text.upper()


    def remove_rt(self, text):
        '''Remove RT.
            Args:
                * text = string
            Returns:
                * text without RT'''

        regex_RT = r'(\A|\s)(RT|rt)(\s|\Z)'
        return sub(regex_RT, '', text)


    def remove_username(self, text):
        '''Remove username in tweet.
            Args:
                * text = string in tweet
            Returns:
                * text without username'''

        tweet_parser = Parser()
        usernames = tweet_parser(text).users
        for username in usernames:
            text = text.replace('@' + username, '')
        return text


    def remove_url(self, text):
        '''Remove url in tweet.
            Args:
                * text = string in tweet
            Returns:
                * text without username'''
        pass

if __name__ == '__main__':
    print 'it is running'