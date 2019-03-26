'''
json.dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding="utf-8", default=None, sort_keys=False, **kw)¶
    Serialize obj as a JSON formatted stream to fp (a .write()-supporting file-like object) using this conversion table.

random.randrange(start, stop[, step])
    Return a randomly selected element from range(start, stop, step).
    This is equivalent to choice(range(start, stop, step)),
    but doesn’t actually build a range object.


random.randint(a, b)¶
    Return a random integer N such that a <= N <= b.

random.choice(seq)
    Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.

random.uniform(a, b)¶
    Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.
'''



import random
import json
import os

count = int(os.getenv('FILE_COUNT') or 100)
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

for identifier in range(count):
    amount = random.uniform(1.0, 1000)
    content = {
        'topic': random.choice(words),
        'value': "%.2f" % amount
    }
    with open(f'./new/receipt-{identifier}.json', 'w') as f:
        json.dump(content,f)

