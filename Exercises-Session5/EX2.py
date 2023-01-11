class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def show(self):
        print(self.h, ":", self.m, ":", self.s)


    def sum(self, t2):
        result = Time(None, None, None)
        result.h = self.h + t2.h
        result.m = self.m + t2.m
        result.s = self.s + t2.s

        if result.s >= 60:
            result.s -= 60
            result.m += 1

        if result.m >= 60:
            result.m -= 60
            result.h += 1

        return result


    def sub(self, t2):
        result = Time(None, None, None)
        result.h = self.h - t2.h
        result.m = self.m - t2.m
        result.s = self.s - t2.s
        
        if result.s < 0:
            result.s += 60
            result.m -= 1

        if result.m < 60:
            result.m += 60
            result.h -= 1

        return result


    def CTS(self):
        C = 3600 * self.h + 60 * self.m + self.s
        return C


def CST(self):
    hour = int(self/3600)
    minute = int((self-hour*3600)/60)
    second1 = int(self - hour*3600 - minute*60)
    return [hour, minute, second]

time1 = Time(9, 12, 12)
time2 = Time(11, 45, 28)
Seconds = 5442

print("time1 : ")
time1.show()

print("time2 : ")
time2.show()

s = time1.sum(time2)
print("time1 + time2 : ")
s.show()

m = time1.sub(time2)
print("time1 - time2 : ")
m.show()

second = time1.CTS()
print("CTS\n" ,second)

time = CST(Seconds)
print ("CST:\n", time[0], ":", time[1], ":", time[2])