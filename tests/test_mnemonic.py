import pytest
from oogway.seed.gen import Mnemonic

def gen_phrases(strength=128, _range=5):
    """generates mnemonic phrases"""
    mn = Mnemonic()
    phrases = []
    for _ in range(_range):
        phrase = mn.generate(strength=strength)
        phrases.append(phrase)
    return phrases

def wordlist():
    mn = Mnemonic()
    return mn.wordlist

# 12 words mnemonic
phrases_128 = gen_phrases()
# 24 words mnemonic
phrases_256 = gen_phrases(strength=256)

@pytest.mark.parametrize("phrase", phrases_128)
def test_mnemonic_length_128(phrase):
    """validate mnemonic size of 12 words"""
    phrase_len = len(phrase.split())
    assert phrase_len == 12

@pytest.mark.parametrize("phrase", phrases_256)
def test_mnemonic_length_256(phrase):
    """validate mnemonic size of 24 words"""
    phrase_len = len(phrase.split())
    assert phrase_len == 24

@pytest.mark.parametrize("phrase", phrases_256)
def test_mnemonic_wordlist(phrase):
    """verify if mnemonic words are from wordlist"""
    _wordlist = wordlist()
    words = phrase.split()
    passes = []
    for word in words:
        if word in _wordlist:
            passes.append(True)
        else:
            passes.append(False)
    
    assert (False in passes) == False
