first_fibonachi = 0
second_fibonachi = 1
counter = 1

for number in range(100):
    print(counter, " - ", first_fibonachi)
    counter += 1
    if number < 100:
        x = second_fibonachi
        second_fibonachi += first_fibonachi
        first_fibonachi = x
