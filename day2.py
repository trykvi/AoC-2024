def isSafe(list):
    if(list[0] > list[1]):
        for i in range(len(list) - 1):
            if(list[i] < list[i+1]):
                return False
    else:
        for i in range(len(list) - 1):
            if(list[i] > list[i+1]):
                return False
            
    for i in range(len(list) - 1):
        if(list[i] - list[i+1] == 0):
            return False
        elif(abs(list[i] - list[i+1]) > 3):
            return False
        
    return True

def part1(input):
    reports = [[int(val) for val in report.split(" ")] for report in input.split("\n")[:-1]]

    safecount = 0
    for report in reports:
        if(isSafe(report)):
            safecount += 1

    return safecount

def part2(input):
    reports = [[int(val) for val in report.split(" ")] for report in input.split("\n")[:-1]]

    safecount = 0
    for report in reports:
        if(isSafe(report)):
            safecount += 1
            continue
        for i in range(len(report)):
            
            if(isSafe(report[:i] + report[(i+1):])):
                safecount += 1
                break
        
        

    return safecount

import time
starttime = time.time()

res1 = part1(open("input2.txt", "r").read())
res2 = part2(open("input2.txt", "r").read())

endtime = time.time()

print(f"Part1 result: {res1}, Part2 result: {res2}")

print(f"Time taken: {(1000*(endtime-starttime)):.3f} ms")
