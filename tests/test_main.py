from word_ladder import _adjacent,verify_word_ladder,word_ladder


def test__word_ladder_1():
    assert not _adjacent('stone','money')

def test__word_ladder_2():
    assert not _adjacent('stone','stone1')

def test__word_ladder_3():
    assert not _adjacent('stone1','stone')

def test__word_ladder_4():
    assert _adjacent('stone','stony')

def test__word_ladder_5():
    assert _adjacent('stone','shone')


def test__verify_word_ladder_1():
    assert not verify_word_ladder([])

def test__verify_word_ladder_2():
    assert verify_word_ladder(['stone'])

def test__verify_word_ladder_3():
    assert verify_word_ladder(['stone'])

def test__verify_word_ladder_4():
    assert verify_word_ladder(['stone', 'shone'])

def test__verify_word_ladder_5():
    assert verify_word_ladder(['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money'])

def test__verify_word_ladder_6():
    assert not verify_word_ladder(['stone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money'])

def test__verify_word_ladder_7():
    assert not verify_word_ladder(['stone', 'shone', 'phone', 'phony', 'peony', 'benny', 'bonny', 'boney', 'money'])

def test__verify_word_ladder_8():
    assert not verify_word_ladder(['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'money'])


def test__word_ladder_1():
    ladder = word_ladder('stone','stone')
    assert verify_word_ladder(ladder) and len(ladder)==1

def test__word_ladder_2():
    ladder = word_ladder('aloof','aloof')
    assert verify_word_ladder(ladder) and len(ladder)==1

def test__word_ladder_3():
    ladder = word_ladder('stone','shone')
    assert verify_word_ladder(ladder) and len(ladder)==2

def test__word_ladder_4():
    ladder = word_ladder('dears','fears')
    assert verify_word_ladder(ladder) and len(ladder)==2

def test__word_ladder_5():
    ladder = word_ladder('stone','phone')
    assert verify_word_ladder(ladder) and len(ladder)==3

def test__word_ladder_6():
    ladder = word_ladder('phone','stone')
    assert verify_word_ladder(ladder) and len(ladder)==3

def test__word_ladder_7():
    ladder = word_ladder('babes','child')
    assert verify_word_ladder(ladder) and len(ladder)==9

def test__word_ladder_8():
    ladder = word_ladder('child','babes')
    assert verify_word_ladder(ladder) and len(ladder)==9

def test__word_ladder_9():
    ladder = word_ladder('devil','angel')
    assert verify_word_ladder(ladder) and len(ladder)==9

def test__word_ladder_10():
    ladder = word_ladder('angel','devil')
    assert verify_word_ladder(ladder) and len(ladder)==9

def test__word_ladder_11():
    ladder = word_ladder('money','smart')
    assert verify_word_ladder(ladder) and len(ladder)==11

def test__word_ladder_12():
    ladder = word_ladder('smart','money')
    assert verify_word_ladder(ladder) and len(ladder)==11

def test__word_ladder_13():
    ladder = word_ladder('stone','money')
    assert verify_word_ladder(ladder) and len(ladder)==10

def test__word_ladder_14():
    ladder = word_ladder('money','stone')
    assert verify_word_ladder(ladder) and len(ladder)==10

def test__word_ladder_15():
    assert word_ladder('atlas','zebra') is None

def test__word_ladder_16():
    assert word_ladder('aloof','money') is None

def test__word_ladder_17():
    assert word_ladder('data','structures') is None
