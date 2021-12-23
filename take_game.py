def game(stack, turn):
    if not stack and turn:
        return False
    if not stack and not turn:
        return True

    if stack[0] > len(stack):
        return game(stack[1:], not turn)
    else:
        return game(stack[1:], not turn) or game(stack[stack[0]:], not turn)


if __name__ == "__main__":
    stack = [1, 2, 1, 2, 5, 7, 1]
    print(game(stack, True))
