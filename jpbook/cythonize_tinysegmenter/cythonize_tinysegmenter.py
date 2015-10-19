# -*- coding: utf-8 -*-
from tinysegmenter import TinySegmenter


def demo():
    segmenter = TinySegmenter()
    print ' | '.join(segmenter.tokenize(u"私の名前は中野です"))

if __name__ == '__main__':
    demo()
