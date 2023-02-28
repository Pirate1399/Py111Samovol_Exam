from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    '''неправильно, но не 
    понимаю как сделать)'''

    cost = stairway[0]
    if len(stairway) == 1:
        return cost
    else:
        for i in range(0, len(stairway)-2):

            cost += min(stairway[i + 1], stairway[i + 2])

            if stairway[i + 1] > stairway[i + 2]:
                i += 2
            elif stairway[i + 1] < stairway[i + 2]:
                i += 1

    return cost


if __name__ == '__main__':
    stairway = [2, 5, 1, 4, 3, 6, 2, 1, 9, 7]
    print(sum(stairway))
    print(stairway_path(stairway))
    stairway1 = [5]
    print(stairway_path(stairway1))
