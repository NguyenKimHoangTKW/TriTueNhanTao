from tkinter import *
import backend
from tkinter import messagebox


def god():
    root = Tk()
    root.iconbitmap('D:\TriTueNhanTao\CuoiKy\A Maze\Logo.ico')
    root.title('A Maze Game by Kim Hoang')
    root.geometry('800x780')
    count = 0
    button_list = []

    frame_up = LabelFrame(root, text='Các chức năng')
    frame_down = LabelFrame(root, text='Ma trận')
    frame_up.pack()
    frame_down.pack()

    global supply_mode
    supply_mode = 0
    global src
    src = None
    global obstacle_list
    obstacle_list = []
    global dest
    dest = None
    global started
    started = False

    def button_mode(mode):
        global supply_mode
        supply_mode = mode

    def button_click(but_no):
        global supply_mode, src, dest
        if supply_mode == 1:
            if src is not None:
                button_list[src].config(bg='#ffffff')
            button_list[but_no].config(bg='#ffe525')
            src = but_no
        elif supply_mode == 2:
            obstacle_list.append(but_no)
            button_list[but_no].config(bg='#b4b4b4')
        elif supply_mode == 3:
            if dest is not None:
                button_list[dest].config(bg='#ffffff')
            button_list[but_no].config(bg='#7dcf21')
            dest = but_no

    def clear_all():
        global src, dest, obstacle_list
        src = None
        dest = None
        obstacle_list = []
        for button in button_list:
            button.config(bg='#ffffff')

    def check_input_and_solution():
        global dest
        if src is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn điểm bắt đầu trước khi xuất phát!")
            return
        if dest is None:
            messagebox.showinfo("Thông báo", "Điểm đích chưa được chọn, sẽ tự động chọn điểm cuối cùng của ma trận làm điểm đích.")
            dest = 399
        solution()

    def solution():
        global started
        if started:
            for i in range(400):
                if i not in obstacle_list and i != src and i != dest:
                    button_list[i].config(bg='#ffffff')
        parent = backend.backened(src, obstacle_list, dest)
        for value in parent:
            button_list[value].config(bg='#00c5ff')
        button_list[src].config(bg='#ffe525')
        started = True

    start_button = Button(frame_up, text='Chọn điểm bắt đầu', command=lambda: button_mode(1))
    obstacle_button = Button(frame_up, text='Chọn các vật cản', command=lambda: button_mode(2))
    destination_button = Button(frame_up, text='Chọn điểm cần đến', command=lambda: button_mode(3))
    clear_button = Button(frame_up, text='Xóa tất cả', command=clear_all)

    start_button.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
    obstacle_button.grid(row=0, column=2, sticky="ew", padx=10, pady=5)
    destination_button.grid(row=0, column=3, sticky="ew", padx=10, pady=5)
    clear_button.grid(row=0, column=4, sticky="ew", padx=10, pady=5)

    for i in range(20):
        for j in range(20):
            button_list.append(Button(frame_down, text=f'{count}', padx=5, pady=5, command=lambda x=count: button_click(x)))
            button_list[count].grid(row=i, column=j, sticky="ew")
            count += 1

    go_button = Button(frame_up, text='Xuất phát', command=check_input_and_solution)
    go_button.grid(row=0, column=5, padx=10, pady=5)

    mainloop()

god()
