
def display_result(label):

    def decorator(function):

        def wrapper(x, y):
            answer = function(x, y)

            print("====================")
            print("Operation:", label)
            print("First Value:", x)
            print("Second Value:", y)
            print("Calculated Result:", answer)
            print("====================")

            return answer

        return wrapper

    return decorator


@display_result("Addition")
def calculate_sum(num1, num2):
    return num1 + num2


calculate_sum(9, 9)
