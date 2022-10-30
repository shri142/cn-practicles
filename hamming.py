l, l3, l2 = [-1, -1, -1, -1, -1, -1, -1], [], []

def inp():
    print('Enter the Data bits D7 D6 D5 D3')
    i = 0
    while i < 4:
        data_bit = int(input('Enter Data bit:', ))
        l2.append(data_bit)
        i += 1

def Einp():
    print('Enter the received codeword(with a single bit error)')
    i = 0
    while i < 7:
        Edata_bit = int(input('Enter Bit: '))
        l3.append(Edata_bit)
        i += 1

def odd_parity():
    p1,p2,p3 = l2[-1] + l2[-2] + l2[-4],l2[-1] + l2[-3] + l2[-4],l2[-2] + l2[-3] + l2[-4]

    if (p1 % 2 == 0):
        l[-1] = 1
    else:l[-1] = 0

    if (p2 % 2 == 0):
        l[-2] = 1
    else:l[-2] = 0

    if (p3 % 2 == 0):
        l[-4] = 1
    else:l[-4] = 0
    print('Parity bits calculated by:\nP1=(D3,D5,D7)\nP2=(D3,D6,D7)\nP4=(D5,D6,D7)')
    print('\nValues of Parity bits:- P1 = ', l[-1], ',P2 = ', l[-2], ',P3 = ', l[-4])

def even_parity():
    p1, p2, p3 = l2[-1] + l2[-2] + l2[-4], l2[-1] + l2[-3] + l2[-4], l2[-2] + l2[-3] + l2[-4]

    if (p1 % 2 == 0):
        l[-1] = 0
    else:l[-1] = 1

    if (p2 % 2 == 0):
        l[-2] = 0
    else:l[-2] = 1

    if (p3 % 2 == 0):
        l[-4] = 0
    else:l[-4] = 1
    print('Parity bits calculated by:\nP1=(D3,D5,D7)\nP2=(D3,D6,D7)\nP4=(D5,D6,D7)')
    print('\nValues of Parity bits:- P1 = ', l[-1], ',P2 = ', l[-2], ',P3 = ', l[-4])

def data():
    j = 0
    for i in range(0, 7):
        if l[i] == -1:
            l[i] = l2[j]
        else:continue
        j += 1
    print('Hamming code is:-D7 D6 D5 P4 D3 P2 P1\n', l)

class check:
    c3, c2, c1 = 0, 0, 0

    def checkForEven(self):
        self.c3,self.c2,self.c1 = l3[-4] + l3[-5] + l3[-6] + l3[-7],l3[-2] + l3[-3] + l3[-6] + l3[-7], l3[-1] + l3[-3] + l3[-5] + l3[-7]

        print('Check bits 1,3,5,7.....to generate C1.Check bits'' 2,3,6,7.....to generate C2.Check bits 4,5,6,7.....to generate C3.''Generate the error codeword =C3C2C1')
        if self.c1 % 2 != 0:
            self.c1 = 0
        else:self.c1 = 1

        if self.c2 % 2 != 0:
            self.c2 = 0
        else:self.c2 = 2

        if self.c3 % 2 != 0:
            self.c3 = 0
        else:self.c3 = 4

        self.wrongBit = self.c3 + self.c2 + self.c1
        print('Error is detected at position', 7 - self.wrongBit, 'at the receiving end.')

    def checkForOdd(self):
        self.c3,self.c2,self.c1 = l3[-4] + l3[-5] + l3[-6] + l3[-7],l3[-2] + l3[-3] + l3[-6] + l3[-7], l3[-1] + l3[-3] + l3[-5] + l3[-7]
        print('Check bits 1,3,5,7.....to generate C1.Check bits'' 2,3,6,7.....to generate C2.Check bits 4,5,6,7.....to generate C3.''Generate the error codeword =C3C2C1')
        if self.c1 % 2 == 0:
            self.c1 = 0
        else:self.c1 = 1

        if self.c2 % 2 == 0:
            self.c2 = 0
        else: self.c2 = 2

        if self.c3 % 2 == 0:
            self.c3 = 0
        else:self.c3 = 4

        self.wrongBit = self.c3 + self.c2 + self.c1
        print('Error is detected at position', 7 - self.wrongBit, 'at the receiving end.')

    def correct(self):
        a = self.wrongBit
        if l3[a] == 0:
            l3[a] = 1
        else:l3[a] = 0
        print('Corrected Code Word:- ', l3)

choice = int(input('Choose parity \n0.Odd\n1.Even\n'))
if choice == 0:
    print('The program will work for odd Parity')
    inp();odd_parity();data();Einp()
    c = check()
    c.checkForOdd();c.correct()

elif choice == 1:
    print('The program will work for Even Parity')
    inp();even_parity(); data();Einp()
    c = check()
    c.checkForEven();c.correct()

else:print('Enter a valid Input')
