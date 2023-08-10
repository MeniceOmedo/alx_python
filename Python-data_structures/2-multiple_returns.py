def multiple_returns(sentence):
    if len(sentence)>0:
        length=len(sentence)
        first=sentence[0]
        return length,first
    else:
        first=None
sentence="At Holberton school, I learnt C!"
length,first= multiple_returns(sentence)     
print("Length: {:d} - First character:{}".format(length,first))