from datetime import datetime
from datetime import date

today = date.today()

# dd/mm/YY (In numbers )
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# month, day, and year In text	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviated, day and year	in numbers
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)