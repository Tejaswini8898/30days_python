class Solution(object):
   def numberOfDays(self, y, m):
      leap = 0
      if y% 400 == 0:
         leap = 1
      elif y % 100 == 0:
         leap = 0
      elif y% 4 == 0:
         leap = 1
      if m==2:
         return 28 + leap
      list = [1,3,5,7,8,10,12]
      if m in list:
         return 31
      return 30
ob1 = Solution()
print(ob1.numberOfDays(2020, 3))


# month = int(input("enter the month: " ))
# year = int(input("enter the year: "))
# if year % 400 == 0:
#     leap = 1
# if year % 100 == 0:
#     leap = 0
# if year % 4 == 0:
#     leap = 1
# if month == 2:
#     print(28 + leap)
# list = [1,3,5,7,8,10,12]
# if month in  list:
#     print(31)
# list2 = [4,6,9,11]
# if month in list2:
#     print(30)

