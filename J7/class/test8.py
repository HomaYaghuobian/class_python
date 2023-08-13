import tqdm # پنلc نباید باشه
# وقتی حلقه خیلی بزرگه از این استفاده میکنه
# میاد یک محور درصد میزنه برات (برای اون حلقه)
from tqdm import tqdm
for i in tqdm(range(10000000)):
    x = 1 