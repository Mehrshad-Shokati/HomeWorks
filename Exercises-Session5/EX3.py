class Date:
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    def show(self):
        print(self.y, "/", self.m, "/", self.d)


    def sum(self, d2):
        result = Date(None, None, None)
        result.y = self.y + d2.y
        result.m = self.m + d2.m
        result.d = self.d + d2.d

        if result.d >= 30:
            result.d -= 30
            result.m += 1

        if result.m >= 12:
            result.m -= 12
            result.y += 1

        return result

    def sub(self, d2):
        result = Date(None, None, None)
        result.y = self.y - d2.y
        result.m = self.m - d2.m
        result.d = self.d - d2.d


        if result.m < 12:
            result.m += 12
            result.y -= 1


        if result.d < 0:
            result.d += 30
            result.m -= 1



        return result


    def GetMonthName (self):
        
        if self.m == 1:
            month = "farvardin"

        elif self.m == 2:
            month = "Ordibehesht"

        elif self.m == 3:
            month = "Khordad"

        elif self.m == 4:
            month = "Tir"

        elif self.m == 5:
            month = "Mordad"

        elif self.m == 6:
            month = "Shahrivar"

        elif self.m == 7:
            month = "Mehr"

        elif self.m == 8:
            month = "Aban"

        elif self.m == 9:
            month = "Azar"            

        elif self.m == 10:
            month = "Dey"

        elif self.m == 11:
            month = "Bahman"

        elif self.m == 12:
            month = "Esfand"           

        return month

def IsValidDate (self):
        
        if self.d < 1 or self.d > 31: 

            day=("False")
            return day

        if self.m < 1 or self.m > 12: 

            month=("False")
            return month

        if self.y < 1 or self.y > 9999: 

            year=("False")
            return year
             
date1 = Date(1401, 10, 18)
date2 = Date(1380, 12, 11)

print("date1 : ")
date1.show()

print("date2 : ")
date2.show()

s = date1.sum(date2)
print("date1 + date2 : ")
s.show()

m = date1.sub(date2)
print("date1 - date2 : ")
m.show()

Name_Of_Month = date1.GetMonthName()
print("month of date1 is:\n", Name_Of_Month)