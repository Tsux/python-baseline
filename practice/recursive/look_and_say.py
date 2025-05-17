### Look-and-say sequence
# 1
# 11
# 21
# 1211
# 111221
# 312211
# 13112221
# 1113213211
# 31131211131221
# 13211311123113112211

def look_and_say(stop_cycle, sequence=None, cycle=0):
    sequence = ['1'] if sequence is None else sequence
    if stop_cycle == cycle:
        return sequence
    else:
        item = sequence[len(sequence) - 1]
        print(item)
        next_item = get_next_item(item)
        sequence.append(next_item)
        look_and_say(stop_cycle, sequence, cycle+1)

def get_next_item(number: str):
    count=0
    prev="0"
    hasher = ""
    for i in number:
        if i == prev:
            count+=1
            hasher = f"{hasher[:-2]}{count}{i}"
        else:
            count=1
            hasher += f"{count}{i}"
        prev = i
    return hasher

def look_and_say_rec(n):
    if n == 1:
        print(n)
        return "1"

    count = 1
    prev = look_and_say_rec(n-1)
    term = ""
    for i in range(len(prev)):
        if i + 1 < len(prev) and prev[i] == prev[i+1]:
            count += 1
        else:
            term += f"{count}{prev[i]}"
            count = 1
    print(term)
    return term

look_and_say(10)
look_and_say_rec(10)