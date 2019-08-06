seats = [
  [None, "Pumpkin", None, None],
  ["Socks", None, "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey","Toast","Pacha","Mau"]
]

def seat_assign(seats):
    cur_row=0
    for row in seats:
        cur_row +=1
        cur_seat = 0
        for seat in row:
            cur_seat += 1
            if seat == None:
                response = input(f'Row {cur_row}, seat {cur_seat} is free do you want to sit there (y/n) ').lower()
                if response == 'y':
                    user_name = input('What is your name ')
                    row.remove(seat) 
                    row.insert(cur_seat-1, user_name)
                    return(seats)
                
        
seat_assign(seats)
print(seats)