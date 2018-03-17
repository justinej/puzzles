def prime(num):
    for i in xrange(2, int(num**0.5)):
        if float(num)/i == int(float(num)/i):
            return False
    return True

#print prime(int('A21',16))
#print prime(int('B31',16))
#print prime(int('C32',16))
#print prime(int('D45',16))
#print prime(int('E50',16))

def sum_squares(num):
    for i in xrange(int(num**0.5)):
        for j in xrange(i+1):
            for k in xrange(j+1):
                if num == i**2 + j**2 + k**2:
                    return (True, [i, j, k])
    return False

# print sum_squares(int("A27", 16))
# print sum_squares(int("B100", 16))
# print sum_squares(int("C215", 16))
# print sum_squares(int("D247", 16))
# print sum_squares(int("E700", 16))

def integer_sides(num):
    possible_sums = [sum([3, 4, 5]) , sum([5, 12, 13]) , sum([7, 24, 25]) , sum([9, 40, 41]) , sum([11, 60, 61]) , sum([13, 84, 85]) , sum([15, 112, 113]) , sum([17, 144, 145]) , sum([19, 180, 181]) , sum([21, 220, 221]) , sum([23, 264, 265]) , sum([25, 312, 313]) , sum([27, 364, 365]) , sum([29, 420, 421]) , sum([31, 480, 481])]
    for sums in possible_sums:
        if float(num)/sums == int(float(num)/sums):
            return True
    return False

#print integer_sides(int("A1", 16))
#print integer_sides(int("B4", 16))
#print integer_sides(int("C12", 16))
#print integer_sides(int("D14", 16))
#print integer_sides(int("E60", 16))


def cos_neg(num):
    if num%360 < 90 or num%360 > 270:
        return True
    return False
# print cos_neg(int("A210", 16))
# print cos_neg(int("B270", 16))
# print cos_neg(int("C455", 16))
# print cos_neg(int("D620", 16))
# # print cos_neg(int("E650", 16))

def perfect_sq(num):
    if num**0.5 == int(num**0.5):
        return True
    return False
# print perfect_sq(int("A2", 16))
# print perfect_sq(int("B3", 16))
# print perfect_sq(int("C4", 16))
# print perfect_sq(int("D5", 16))
# print perfect_sq(int("E6", 16))

def abundant(num):
    factors = set([1])
    for i in xrange(2, int(num**0.5)+1):
        if num%i == 0:
            factors.add(i)
            factors.add(num/i)
    factors = list(factors)
    if sum(factors) > num:
        return True
    return False

# print abundant(int("A4", 16))
# print abundant(int("B19", 16))
# print abundant(int("C20", 16))
# print abundant(int("D22", 16))
# print abundant(int("E24", 16))

def octal(num):
    octal_rep = str(oct(int(num, 16)))[1:]
    size = len(octal_rep)
    for i in xrange(size):
        if octal_rep[i] != octal_rep[size-1-i]:
            return False
    return True, octal_rep
# print octal("A95")
# print octal("B121")
# print octal("C261")
# print octal("D279")
# print octal("E471")

def leap_year(num):
    num = int(num, 16)
    if num % 4 == 0:
        if num % 100 == 0:
            if num % 400 == 0:
                return True
            else: return False
        else: return True
    else: return False

# print leap_year("A2014")
# print leap_year("B2020")
# print leap_year("C2628")
# print leap_year("D2911")
# print leap_year("E3200")


