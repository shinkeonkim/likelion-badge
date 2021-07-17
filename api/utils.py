def ordinal_number(num):
    num = int(num)
    suffix = ['TH', 'ST', 'ND', 'RD', 'TH'][min(num % 10, 4)]
    if 11 <= (num % 100) <= 13:
        suffix = 'TH'
    return str(num) + suffix


rounded = '''<path class="cls-1" d="M3.63,0H99.74a3.59,3.59,0,0,1,3.63,3.55h0V16.44A3.59,3.59,0,0,1,99.75,20H3.63A3.6,3.6,0,0,1,0,16.44V3.56A3.6,3.6,0,0,1,3.63,0Z"/>
<path class="cls-2" d="M67.3,0H99.74a3.59,3.59,0,0,1,3.63,3.55h0V16.44A3.59,3.59,0,0,1,99.75,20H67.3"/>'''
flat = '''<rect x="0" y="0" class="cls-1" width="103.4" height="20"/>
<rect x="67.3" y="0" class="cls-2" width="103.4" height="20"/>'''


def styled_container(style: str = 'rounded'):
    if style == 'flat':
        return flat
    return rounded
