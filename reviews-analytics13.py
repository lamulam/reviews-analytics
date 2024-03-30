
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print( len(data) )

print( 'END read file')

sum_len = 0 
for d in data:
	sum_len += len(d)

print('平均留言長度為', sum_len/len(data) )

new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print('一共有', len(new), '筆留言長度小於100')

goodlist = []
for d in data:
	if 'good' in d:
		goodlist.append(d)

print('一共有', len(goodlist), '筆留言提到good')
