
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print( len(data) )

print( 'END read file')

word_count = {} 
for d in data:
	words = d.split()
	for word in words:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1

for word in word_count:
	if word_count[word] > 1000000:
		print(word, word_count[word])

while True:
	word = input('你要查什麼字: ')
	if word == 'q':
		print('感謝使用功能')
		break
	if word in word_count:
		print(word, '出現次數為', word_count[word])
	else:
		print('not this word')

print('總共字數為', len(word_count))












# sum_len = 0 
# for d in data:
# 	sum_len += len(d)

# print('平均留言長度為', sum_len/len(data) )

# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)

# print('一共有', len(new), '筆留言長度小於100')

# goodlist = []
# for d in data:
# 	if 'good' in d:
# 		goodlist.append(d)

# print('一共有', len(goodlist), '筆留言提到good')
