from tkinter import *
import backend


def god():
    root = Tk()
    root.iconbitmap('D:\TriTueNhanTao\Path-Finding-AI-Using-Python-master\Logo1.jpg')
    root.title('A Maze Game by Kim Hoang')
    root.geometry('800x780')
    count = 0                                           # để xác định từng nút/đỉnh và truyền các tham số duy nhất
    button_list = []                                    # nút lưu trữ được tạo trong thời gian chạy

    frame_up = LabelFrame(root, text='Các chức năng')
    frame_down = LabelFrame(root, text='Ma trận')
    frame_up.pack()
    frame_down.pack()
    global supply_mode                                  # để phân biệt giữa điểm bắt đầu, điểm kết thúc và điểm chướng ngại vật
    supply_mode = 0
    global src                                          # src là điểm bắt đầu
    src = 0
    global obstacle_list                                # lưu trữ các chướng ngại vật khi Supply_mode là 2
    obstacle_list = []
    global dest                                         # biến đích cuối cùng
    dest = 1000

    def button_mode(mode):                              # trường đầu vào theo điểm xuất phát/chướng ngại vật/đích của người dùng
        global supply_mode
        supply_mode = mode
        print(supply_mode)

    def button_click(but_no):                           # clicked buttons in path
        #print(but_no)
        global supply_mode
        if supply_mode == 1:                                # for starting point when supply_mode = 1
            button_list[but_no].config(bg='#ffe525')
            global src
            src = but_no
            start_button['state'] = DISABLED
            supply_mode = 0
        if supply_mode == 2:                                # for obstacles      when supply_mode = 2
            button_list[but_no].config(bg='#b4b4b4')
            global obstacle_list
            obstacle_list.append(but_no)
        if supply_mode == 3:                                # for destination    when supply_mode = 3
            button_list[but_no].config(bg='#7dcf21')
            global dest
            dest=but_no
            destination_button['state'] = DISABLED
            supply_mode = 0

    start_button = Button(frame_up, text='Chọn điểm bắt đầu', command=lambda: button_mode(1))
    obstacle_button = Button(frame_up, text='Chọn các vật cản', command=lambda: button_mode(2))
    destination_button = Button(frame_up, text='Chọn điểm cần đến', command=lambda: button_mode(3))

    start_button.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
    obstacle_button.grid(row=0, column=2, sticky="ew", padx=10, pady=5)
    destination_button.grid(row=0, column=3, sticky="ew", padx=10, pady=5)

    for i in range(20):
        for j in range(20):
            button_list.append(Button(frame_down, text=f'{count}', padx=5, pady=5, command=lambda x=count: button_click(x)))
            button_list[count].grid(row=i, column=j, sticky="ew")
            count += 1

    def solution():                                         # backend script is called
        parent = backend.backened(src, obstacle_list, dest)
        for value in parent:
            button_list[value].config(bg='#00c5ff')         # path color is turned blue
        button_list[src].config(bg='#ffe525')               # starting pt color is turned back yellow

    go_button = Button(frame_up, text='Xuất phát', command=solution)
    go_button.grid(row=0, column=4, padx=10, pady=5)

    def restart():
        root.destroy()
        god()
        
    restart_button = Button(frame_up, text='Reset', command=restart)
    restart_button.grid(row=0, column=5, padx=10, pady=5)

    mainloop()
god()
