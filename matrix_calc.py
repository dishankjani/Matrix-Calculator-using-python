import numpy as np

print('                     Welcome to the matrix calculator')
rows_a = 0
rows_b = 0
col_a = 0
col_b = 0
matrix_a = [] #write matrix 1
matrix_b = [] #write matrix 2
while True:
    while True:
        try:
            print ("""
    Select an operation using its corresponding number
    1.Define Matrix
    2.Show Matrix
    3.Addition
    4.Subtraction
    5.Multiplication
    6.Transpose
    7.Determinant
    8.Inverse
    9.Division
    10.Quit""")
            ans = int(input('Please choose any operation: '))
        except:
            print('\nSorry, I didn\'t understand that.. Please enter a valid input')
            continue
        else:
            break
    if ans == 10:
        print('\nThank you for using the matrix calculator :)\n')
        break
    elif ans == 1:
        while True:
            try:
                matrix_selection = int(input("""
    Select the matrix you want to define:
    1.Matrix A
    2.Matrix B
    """))
                if matrix_selection == 1:
                    rows_a = int(input("Enter the number of rows (min=2): "))
                    col_a = int(input("Enter the number of columns (min=2): "))
                    if rows_a > 1 and col_a > 1:
                        print("\nEnter the entries in a single line (between '' and separated by space): ")
                        input_matrix = list ( map ( float, input ( ).split ( ) ) )
                        matrix_a = np.array ( input_matrix ).reshape ( rows_a, col_a )
                        print('\nMatrix A has been updated!')
                    else:
                        print('\nWrong dimensions')
                elif matrix_selection == 2:
                    rows_b = int ( input ( "Enter the number of rows (min=2): " ) )
                    col_b = int ( input ( "Enter the number of columns (min=2): " ) )
                    if rows_b > 1 and col_b > 1:
                        print("\nEnter the entries in a single line (between '' and separated by space): ")
                        input_matrix = list ( map ( float, input ( ).split ( ) ) )
                        matrix_b = np.array ( input_matrix ).reshape ( rows_b, col_b )
                        print('\nMatrix B has been updated!')
                    else:
                        print('\nWrong dimensions')
                else:
                    print('\nUnknown input...')
            except:
                print('\nSorry, I didn\'t understand that.. Please enter a valid input')
                continue
            else:
                break

    elif ans == 2:
        while True:
            try:
                show_selection = int ( input ( """
    Select the matrix you want to show:
    1.Matrix A
    2.Matrix B
    """))
            except:
                print('\nSorry, I didn\'t understand that.. Please enter a valid input')
                continue
            else:
                break
        if show_selection == 1:
            print("\nThe Matrix A is:\n")
            print(matrix_a)
        elif show_selection == 2:
            print("\nThe Matrix B is:\n")
            print(matrix_b)
        else:
            print('\nUnknown input...')
    elif ans == 3:
        if rows_a == rows_b and col_a == col_b:
            print('\nThe sum of Matrix A & Matrix B is:\n')
            print(np.add(matrix_a,matrix_b))
        else:
            print('Operation cannot be performed..')
    elif ans == 4:
        if rows_a == rows_b and col_a == col_b:
            while True:
                try:
                    sub_selection = int(input("""
    Select the operation you want to perform:
    1.Matrix A - Matrix B
    2.Matrix B - Matrix A
    """))
                except:
                    print('\nSorry, I didn\'t understand that.. Please enter a valid input')
                    continue
                else:
                    break
            if sub_selection == 1:
                print('\nThe difference between Matrix A & Matrix B: \n')
                print(np.subtract ( matrix_a, matrix_b ))
            elif sub_selection == 2:
                print('\nThe difference between Matrix B & Matrix A: \n')
                print(np.subtract ( matrix_b, matrix_a ))
            else:
                print('\nUnknown input...')
        else:
            print('\nOperation cannot be performed..')
    elif ans == 5:
        while True:
            try:
                multiplication_choice = int(input(""""
    Select the operation you want to perform:
    1.Matrix A * Matrix B
    2.Matrix B * Matrix A
    """))
            except:
                print('\nSorry, I didn\'t understand that.. Please enter a valid input')
                continue
            else:
                break
        if multiplication_choice==1:
            if col_a == rows_b:
                print('\nThe Product of Matrix A & Matrix B: \n')
                print(np.dot ( matrix_a, matrix_b ))
            else:
                print("""
    Multiplication cannot be performed..
    (the number of columns of matrix A is not equal to the number of rows of matrix B)""")
        elif multiplication_choice==2:
            if col_b == rows_a:
                print('\nThe Product of Matrix B & Matrix A: \n')
                print(np.dot ( matrix_b, matrix_a ))
            else:
                print("""
    Multiplication cannot be performed..
    (the number of columns of matrix B is not equal to the number of rows of matrix A)""")
        else:
            print('\nUnknown input...')
    elif ans == 6:
        while True:
            try:
                transpose_selection = int(input("""
    Select the matrix you want to get its transpose:
    1.Matrix A
    2.Matrix B
    """))
            except:
                print('\nSorry, I didn\'t understand that.. Please enter a valid input')
                continue
            else:
                break
        if transpose_selection==1:
            print('\nThe transpose of Matrix A is:\n')
            print(matrix_a.T )
        elif transpose_selection==2:
            print('\nThe transpose of Matrix B is:\n')
            print(matrix_b.T)
        else:
            print('\nUnknown input...')
    elif ans == 7:
        while True:
            try:
                determinant_selection = int(input("""
    Select the matrix you want to get its determinant:
    1.Matrix A
    2.Matrix B
    """))
            except:
                print('\nSorry, I didn\'t understand that.. Please enter a valid input')
                continue
            else:
                break
        if determinant_selection == 1:
            if rows_a==col_a:
                print('\nThe determinant of Matrix A is:')
                print(round(np.linalg.det(matrix_a)))
            else:
                print('\nCannot find the determinant (Not a square matrix')
        elif determinant_selection == 2:
            if rows_b == col_b:
                print('\nThe determinant of Matrix B is:')
                print(round(np.linalg.det ( matrix_b )))
            else:
                print('\nCannot find the determinant (Not a square matrix')
        else:
            print('\nUnknown input...')
    elif ans == 8:
        while True:
            try:
                inverse_selection = int(input("""
    Select the matrix you want to get its inverse:
    1.Matrix A
    2.Matrix B
    """))
            except:
                print('\nSorry, I didn\'t understand that.. Please enter a valid input')
                continue
            else:
                break
        if inverse_selection == 1:
            if rows_a == col_a:
                print('\nThe inverse of Matrix A is:')
                print(np.linalg.inv ( matrix_a ))
            else:
                print('\nCannot find the inverse (Not a square matrix')
        elif inverse_selection == 2:
            if rows_b == col_b:
                print('\nThe inverse of Matrix B is:')
                print(np.linalg.inv ( matrix_b))
            else:
                print('\nCannot find the inverse (Not a square matrix')
        else:
            print('\nUnknown input...')
    elif ans == 9:
        while True:
            try:
                division_choice = int(input(""""
    Select the operation you want to perform:
    1.Matrix A / Matrix B
    2.Matrix B / Matrix A
    """))
            except:
                print('\nSorry, I didn\'t understand that.. Please enter a valid input')
                continue
            else:
                break
        if division_choice == 1:
            if col_a == rows_b == col_b and round(np.linalg.det(matrix_b)) != 0:
                print('\nThe Division of Matrix A by Matrix B: \n')
                print(np.dot(matrix_a, np.linalg.inv(matrix_b)))
            else:
                print("""
    Division cannot be performed..
    (Not same dimensions or the determinant of matrix B is equal zero)""")
        elif division_choice == 2:
            if col_b == rows_a == col_a and round(np.linalg.det(matrix_a)) != 0:
                print('\nThe Division of Matrix B by Matrix A: \n')
                print(np.dot(matrix_b, np.linalg.inv(matrix_a)))
            else:
                print("""
    Division cannot be performed..
    (Not same dimensions or the determinant of matrix A is equal zero)""")
        else:
            print('\nUnknown input...')
    else:
        print('\nUnknown input...')