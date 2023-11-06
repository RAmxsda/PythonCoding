def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    print(
        f"\n\nThe required number to paint the wall of height{height}m and wall of width {width}m is {round(number_of_cans)}"
    )


test_height = int(input("Enter height of the wall:"))
test_width = int(input("Enter width of the wall:"))
coverage = 5

paint_calc(height=test_height, width=test_width, cover=coverage)
