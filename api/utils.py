
def ordinal_number(num):
  num = int(num)
  suffix = ['TH', 'ST', 'ND', 'RD', 'TH'][min(num % 10, 4)]
  if 11 <= (num % 100) <= 13:
      suffix = 'TH'
  return str(num) + suffix
