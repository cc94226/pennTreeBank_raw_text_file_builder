import random

file_name = "./total_ptb.txt"
mid_file = "./mid.txt"
train_file = "./train.txt"
valid_file = "./valid.txt"
test_file = "test.txt"

inputfile = open(file_name)
midfile = open(mid_file, 'w')

total_sent = 0
for line in inputfile.readlines():
    if len(line) < 10:
        continue
    if "speaker" and "NUM" in line:
        continue

    else:
        midfile.write(line)
        total_sent += 1

inputfile.close()
midfile.close()
print(total_sent)

midfile = open(mid_file)

train = open(train_file, 'w')
valid = open(valid_file, 'w')
test = open(test_file, 'w')

lines = midfile.readlines()
random.shuffle(lines)

count = 0
for line in lines:
    
    if count < total_sent * 0.8:
            train.write(line)

    elif count >= total_sent*0.8 and count < total_sent*0.9:
            valid.write(line)

    else:
            test.write(line)

    count+=1

train.close()
valid.close()
test.close()
