'''Ez a kód a Téglalapot és azokhoz kapcsolódó számításait mutatja be'''
class Teglalap():
    '''Ez maga a Téglalap osztály'''
    def __init__(self, a, b=None):
        self.__side_a = a
        self.__side_b = a if b is None else b
        """
        if b is None:
            self.__side_b = a
        else:
            self.__side_b = b
        """

    @property
    def oldalak(self):
        '''Ez az oldalak property'''
        return self.__side_a, self.__side_b

    @oldalak.setter
    def oldalak(self, a):
        self.__side_a, self.__side_b = a[0], a[1]

    def terulet(self):
        '''Ez a terület kiszámításához kell'''
        return self.__side_a * self.__side_b

    def kerulet(self):
        '''Ez a kerület kiszámításához kell'''
        return 2 * self.__side_b + 2 * self.__side_a


def kerulet_atlag(teglalapok):
    '''Ez több téglalap kerületét átlagolja'''
    kerulet_sum = 0
    for teglalap in teglalapok:
        kerulet_sum += teglalap.kerulet()
    return kerulet_sum / len(teglalapok)


def terulet_atlag(teglalapok):
    '''Ez több téglalap területét átlagolja'''
    terulet_sum = 0
    for teglalap in teglalapok:
        terulet_sum += teglalap.terulet()
    return terulet_sum / len(teglalapok)


def main():
    '''Ez pedig itt a main metódus'''
    teglalapok = []
    t1 = Teglalap(6)
    teglalapok.append(t1)
    n1 = Teglalap(4, 2)
    teglalapok.append(n1)
    t2 = Teglalap(3, 5)
    teglalapok.append(t2)

    print(kerulet_atlag(teglalapok))
    print(terulet_atlag(teglalapok))


if __name__ == '__main__':
    main()
