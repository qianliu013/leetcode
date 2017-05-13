"""Fizz Buzz."""


def _fizzBuzz(n):
    answer = []
    for i in xrange(1, n+1):
        if i % 15 == 0:
            answer.append('FizzBuzz')
        elif i % 5 == 0:
            answer.append('Buzz')
        elif i % 3 == 0:
            answer.append('Fizz')
        else:
            answer.append(str(i))
    return answer


if __name__ == '__main__':
    print (_fizzBuzz(15))
