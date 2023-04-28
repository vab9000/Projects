from json import load, dump

def increment(num: str, base: int) -> str:
    # Increment a number of any base
    if (num == ""):
        return "1"
    uni = ord(num[len(num) - 1]) - 55
    if (uni >= 10):
        if (uni + 1 >= base):
            return increment(num[0 : len(num) - 1], base) + "0"
        else:
            return num[0 : len(num) - 1] + chr(uni + 56)
    elif (int(num[len(num) - 1]) == 9):
        if (base == 10):
            return str(int(num) + 1)
        else:
            return num[0 : len(num) - 1] + "A"
    elif (int(num[len(num) - 1]) + 1 >= base):
        return increment(num[0 : len(num) - 1], base) + "0"
    else:
        return num[0 : len(num) - 1] + str(int(num[len(num) - 1]) + 1)

def load_nums() -> dict:
    file = open("generated.json", "r")
    nums = load(file)
    file.close()
    return nums

def generate_data() -> None:
    nums = {}
    for base_to in range(2, 37):
        num = "0"
        lst = ["0"]
        for _ in range(int("Z", 36)):
            num = increment(num, base_to)
            lst.append(num)
        nums[base_to] = lst

    file = open("generated.json", "w")
    dump(nums, file, indent=4)
    file.close()

number = input("Number: ")
base = int(input("Base: "))
base_to = int(input("Base to: "))

nums = load_nums()
try:
    print(nums[str(base_to)][int(number, base)])
except:
    try:
        nums[str(base_to)]
        lst = nums[str(base_to)]
        num = lst[len(lst) - 1]
    except:
        lst = ["0"]
        num = "0"
    for _ in range(int(number, base) - int(num, base_to)):
        num = increment(num, base_to)
        lst.append(num)

    print(num)
    file = open("generated.json", "w")
    file.seek(0)
    file.truncate()
    nums[str(base_to)] = lst
    dump(nums, file, indent=4)
    file.close()