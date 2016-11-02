# idle default source encoding: utf-8
import codecs


def wczytywanie():

    tmp = raw_input()
    tmp = tmp.decode("windows-1250")
    try:
        print u'Wysokość podanego miasta n.p.m. to: ' + d[tmp]
        return wczytywanie()
    except KeyError:
        if tmp == 'koniec':
            return 0
        print u'Podana nazwa miasta nie jest w bazie. Podaj inną nazwę:'
        return wczytywanie()


f = codecs.open("osrodki.txt", "r", "windows-1250")
lines = f.readlines()

d = {}

for i in lines:
    spl = i.split("\t")
    name = spl[1]
    h = spl[3]
    d[name] = h

print u'Podaj nazwę miasta: '
wczytywanie()
