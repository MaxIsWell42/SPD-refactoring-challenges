def get_average(li):
    sum = 0
    for num in li:
        sum += num
    mean = sum / len(li)
    return mean

def test_get_average():
    num1 = 10
    num2 = 20
    numbers = [num1, num2, 50]
    assert(get_average(numbers)) == 40