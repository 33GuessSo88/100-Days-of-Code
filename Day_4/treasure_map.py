

row1 = ["🟨","🟨","🟨"]
row2 = ["🟨","🟨","🟨"]
row3 = ["🟨","🟨","🟨"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

location = input("type in a column and row number\n")

location = list(location)
print(location)

row_num = int(location[1])
col_num = int(location[0])

map[row_num-1][col_num-1] = "X"

print(f"{row1}\n{row2}\n{row3}")