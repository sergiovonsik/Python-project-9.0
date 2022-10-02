import numpy as np


def solution(src, dest):
    necesary_movements = 7
    chessboard = np.array([[0, 1, 2, 3, 4, 5, 6, 7],
                           [8, 9, 10, 11, 12, 13, 14, 15],
                           [16, 17, 18, 19, 20, 21, 22, 23],
                           [24, 25, 26, 27, 28, 29, 30, 31],
                           [32, 33, 34, 35, 36, 37, 38, 39],
                           [40, 41, 42, 43, 44, 45, 46, 47],
                           [48, 49, 50, 51, 52, 53, 54, 55],
                           [56, 57, 58, 59, 60, 61, 62, 63]])
    src_y, src_x = np.where(chessboard == src)
    dest_y, dest_x = np.where(chessboard == dest)
    initial_position = [src_y, src_x]
    final_position = [dest_y, dest_x]
    # =========================================================================

    for element_1 in amount_of_moves_1(initial_position, final_position):
        # print(chessboard[element_1[0], element_1[1]], 'first move')
        if element_1 == final_position:
            # print('FOUND 1')
            necesary_movements = 1

        # ==== second movement ====
        for element_2 in amount_of_moves_1(element_1, final_position):
            # print(chessboard[element_2[0], element_2[1]], 'second move')
            if element_2 == final_position:
                # print('FOUND 2')
                if necesary_movements not in [1]:
                    necesary_movements = 2
            # ==== third movement ====
            for element_3 in amount_of_moves_1(element_2, final_position):
                # print(chessboard[element_3[0], element_3[1]], 'third move')
                if element_3 == final_position:
                    # print('FOUND 3')
                    if necesary_movements not in [1, 2]:
                        necesary_movements = 3
                # ==== fourth movement ====
                for element_4 in amount_of_moves_1(element_3, final_position):
                    # print(chessboard[element_4[0], element_4[1]], 'fourth move')
                    if element_4 == final_position:
                        # print('FOUND 4')
                        if necesary_movements not in [1, 2, 3]:
                            necesary_movements = 4
                    # ==== fifth movement ====
                    for element_5 in amount_of_moves_1(element_4, final_position):
                        # print(chessboard[element_5[0], element_5[1]], 'fifth move')
                        if element_5 == final_position:
                            # print('FOUND 5')
                            if necesary_movements not in [1, 2, 3, 4]:
                                necesary_movements = 5
                        # ==== sixth movement ====
                        for element_6 in amount_of_moves_1(element_5, final_position):
                            # print(chessboard[element_6[0], element_6[1]], 'sixth move')
                            if element_6 == final_position:
                                # print('FOUND 6')
                                if necesary_movements not in [1, 2, 3, 4, 5]:
                                    necesary_movements = 6

    # =========================================================================

    return necesary_movements

    # ================================== #


def amount_of_moves_1(init, dest):
    moves_to_pass = []
    posible_range = range(0, 8)
    chessboard = np.array([[0, 1, 2, 3, 4, 5, 6, 7],
                           [8, 9, 10, 11, 12, 13, 14, 15],
                           [16, 17, 18, 19, 20, 21, 22, 23],
                           [24, 25, 26, 27, 28, 29, 30, 31],
                           [32, 33, 34, 35, 36, 37, 38, 39],
                           [40, 41, 42, 43, 44, 45, 46, 47],
                           [48, 49, 50, 51, 52, 53, 54, 55],
                           [56, 57, 58, 59, 60, 61, 62, 63]])

    # =============== #
    left_up = [init[0] + 1, init[1] - 2]

    if left_up[0] in posible_range and left_up[1] in posible_range:
        moves_to_pass.append(left_up)
    else:
        pass

    # =============== #

    # =============== #
    up_left = [init[0] + 2, init[1] - 1]
    if up_left[0] in posible_range and up_left[1] in posible_range:
        moves_to_pass.append(up_left)
    else:
        pass
    # =============== #

    # =============== #
    up_right = [init[0] + 2, init[1] + 1]
    if up_right[0] in posible_range and up_right[1] in posible_range:
        moves_to_pass.append(up_right)
    else:
        pass
    # =============== #

    # =============== #
    right_up = [init[0] + 1, init[1] + 2]

    if right_up[0] in posible_range and right_up[1] in posible_range:
        moves_to_pass.append(right_up)
    else:
        pass
    # =============== #

    # =============== #
    left_down = [init[0] - 1, init[1] - 2]
    if left_down[0] in posible_range and left_down[1] in posible_range:
        moves_to_pass.append(left_down)
    else:
        pass
    # =============== #

    # =============== #
    down_left = [init[0] - 2, init[1] + 1]
    if down_left[0] in posible_range and down_left[1] in posible_range:
        moves_to_pass.append(down_left)
    else:
        pass
    # =============== #

    # =============== #
    down_right = [init[0] - 2, init[1] - 1]
    if down_right[0] in posible_range and down_right[1] in posible_range:
        moves_to_pass.append(down_right)
    else:
        pass

    # =============== #

    # =============== #
    right_down = [init[0] - 1, init[1] + 2]
    if right_down[0] in posible_range and right_down[1] in posible_range:
        moves_to_pass.append(right_down)
    else:
        pass

    return moves_to_pass

    # =============== #


chessboard = [[0, 1, 2, 3, 4, 5, 6, 7],
              [8, 9, 10, 11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20, 21, 22, 23],
              [24, 25, 26, 27, 28, 29, 30, 31],
              [32, 33, 34, 35, 36, 37, 38, 39],
              [40, 41, 42, 43, 44, 45, 46, 47],
              [48, 49, 50, 51, 52, 53, 54, 55],
              [56, 57, 58, 59, 60, 61, 62, 63]]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('CHESSBOARD COORDINATES')
    for i in chessboard:
        print(i)
    init, dest = input('select the initial and final coordinates in order to find the\n'
                       'necessaries amount of movement needed to go there.\n'
                       'format -> "number, number" ').split()
    print(solution(int(init), int(dest)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
