import re

with open("day_4.txt") as puzzleInput:
    records = []
    entry = []
    rawData = puzzleInput.readlines()

    for line in rawData:
        line = line.strip()
        if line == '':
            records.append(entry)
            entry = []
        else:
            entry += line.split(" ")
    records.append(entry)

def present(record):
    required = {"byr","iyr","eyr","hgt","hcl","ecl","pid"}
    passport = set()
    for field in record:
        a,b = field.split(":")
        passport.add(a)

    return required.issubset(passport)

def hgt_validate(s):
    if len(s) >= 4:
        m = ((s[-2:]=="in")&(59<=int(s[:-2])<=76)) |\
            ((s[-2:]=="cm")&(150<=int(s[:-2])<=193))
    else:
        m = False

    return m

def valid(record):
    dataDict = dict(item.split(":") for item in record)
    requiredFields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

    if all(key in dataDict.keys() for key in requiredFields):
        return all([
        1920<=int(dataDict["byr"])<=2002,
        2010<=int(dataDict["iyr"])<=2020,
        2020<=int(dataDict["eyr"])<=2030,
        bool(re.match("^#[0-9a-f]{6}$", dataDict["hcl"])),
        dataDict["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"],
        bool(re.match("^[0-9]{9}$",dataDict["pid"])),
        hgt_validate(dataDict["hgt"])])
    else:
        return False

ansA = 0
ansB = 0
for r in records:
    if present(r):
        ansA += 1

for r in records:
    if valid(r):
        ansB += 1

print(ansB)
