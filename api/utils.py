
def ordinal_number(num):
  num = int(num)
  suffix = ['th', 'st', 'nd', 'rd', 'th'][min(num % 10, 4)]
  if 11 <= (num % 100) <= 13:
      suffix = 'th'
  return str(num) + suffix
