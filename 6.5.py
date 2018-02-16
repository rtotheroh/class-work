str = 'X-DSPAM-Confidence:0.8475'
colon = str.find(':')

number = str[colon+1:]
final = float(number)
print(final)

