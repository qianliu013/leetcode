# coding=utf-8

"""Encode and Decode TinyURL."""

from __future__ import print_function
import random


class Codec:
    """Encode and Decode TinyURL."""

    prefix = 'http://tinyurl.com/'

    def __init__(self):
        """Initialize."""
        self.__total = 0
        self.__url_to_num = {}
        self.__num_to_url = {}

    def encode(self, longUrl):
        """Encode a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.__url_to_num:
            self.__total += 1
            self.__url_to_num[longUrl] = self.__total
            self.__num_to_url[self.__total] = longUrl
        return self.prefix + '/' + str(self.__url_to_num[longUrl])

    def decode(self, shortUrl):
        """Decode a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.__num_to_url[int(shortUrl.split('/')[-1])]


# 参考自 https://discuss.leetcode.com/topic/81637/two-solutions-and-thoughts/2
class Codec1:
    """Encode and Decode TinyURL."""

    prefix = 'http://tinyurl.com/'
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self):
        """Initialize."""
        self.__url_to_ch6 = {}
        self.__ch6_to_url = {}

    def encode(self, longUrl):
        """Encode a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.__url_to_ch6:
            ch6 = ''.join(random.sample(self.alphabet, 6))
            self.__url_to_ch6[longUrl] = ch6
            self.__ch6_to_url[ch6] = longUrl
        return self.prefix + self.__url_to_ch6[longUrl]

    def decode(self, shortUrl):
        """Decode a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.__ch6_to_url.get(shortUrl[-6:], '')


if __name__ == '__main__':
    codec = Codec1()
    URL = 'https://leetcode.com/problems/design-tinyurl'
    short_url = codec.encode(URL)
    print (URL, short_url, codec.decode(short_url))
