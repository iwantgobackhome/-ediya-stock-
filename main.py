import tkinter.ttk

import _tkinter

import pandas
from tkinter import *
from tkinter import messagebox

data = pandas.read_csv("stock.csv")


# update_fun
def update_click():
    index_num = 0
    try:
        float(count_entry.get())
        for key, value in data.iterrows():
            if value["재료이름"] == ingredient_entry.get():
                index_num = key
                break
            else:
                index_num = "no_data"
        if index_num != "no_data":
            data.loc[index_num, '개수'] = count_entry.get()
            list_box.delete(0, END)
            print_list_box()
            data.to_csv("stock.csv", index=None)
            sold_out_print()
            under_3_print()
            ingredient_entry.delete(0, END)
            count_entry.delete(0, END)
        else:
            messagebox.showerror(title="존재하지 않는 값", message="존재하지 않는 이름을 입력하셨습니다. \n다시 한 번 확인해주세요.")
    except ValueError:
        messagebox.showerror(title="오류", message="개수에 숫자를 입력해주세요.")


# enter count_entry
def enter_count_entry(event):
    update_click()


# list_box print
def print_list_box():
    for key, value in data.iterrows():
        if value["재료위치"] == "냉장":
            list_box.insert(END, f"{value['재료위치']}    {value['개수']}     {value['재료이름']}\n")
    for key, value in data.iterrows():
        if value["재료위치"] == "냉동":
            list_box.insert(END, f"{value['재료위치']}    {value['개수']}     {value['재료이름']}\n")
    for key, value in data.iterrows():
        if value["재료위치"] == "상온":
            list_box.insert(END, f"{value['재료위치']}    {value['개수']}    {value['재료이름']}\n")
    for key, value in data.iterrows():
        if value["재료위치"] != "상온" and value["재료위치"] != "냉동" and value["재료위치"] != "냉장":
            list_box.insert(END, f"{value['재료위치']}    {value['개수']}    {value['재료이름']}\n")


# search_fun
def search_click():
    search_check = False
    list_box.delete(0, END)
    for key, value in data.iterrows():
        if ingredient_entry.get() in value["재료이름"]:
            list_box.insert(END, f"{value['재료위치']}    {value['개수']}    {value['재료이름']}\n")
            search_check = True
    if not search_check:
        messagebox.showerror(title="존재하지 않는 이름", message="존재하지 않는 이름을 입력하셨습니다. \n다시 한 번 확인해주세요.")
        print_list_box()
    ingredient_entry.delete(0, END)


# enter search
def enter_ingredient_entry(event):
    search_click()


# sold_out_fun
def sold_out_print():
    try:
        sold_out_list.delete(0, END)
        sold_out_list.insert(0, "                           [품절 항목]")
        for key, value in data.iterrows():
            if float(value["개수"]) == 0 and value["재료위치"] == "냉장":
                sold_out_list.insert(END, f"{value['재료위치']}    {value['개수']}   {value['재료이름']}\n")
        for key, value in data.iterrows():
            if float(value["개수"]) == 0 and value["재료위치"] == "냉동":
                sold_out_list.insert(END, f"{value['재료위치']}    {value['개수']}   {value['재료이름']}\n")
        for key, value in data.iterrows():
            if float(value["개수"]) == 0 and value["재료위치"] == "상온":
                sold_out_list.insert(END, f"{value['재료위치']}    {value['개수']}   {value['재료이름']}\n")
        for key, value in data.iterrows():
            if float(value["개수"]) == 0 and value["재료위치"] != "상온" and \
                    value["재료위치"] != "냉동" and value["재료위치"] != "냉장":
                sold_out_list.insert(END, f"{value['재료위치']}    {value['개수']}   {value['재료이름']}\n")
    except ValueError:
        messagebox.showerror(title="오류", message="개수에 숫자를 입력해주세요.")


def under_3_print():
    try:
        under_3_list.delete(0, END)
        under_3_list.insert(0, "                        [3개이하 항목]")
        for key, value in data.iterrows():
            if float(value["개수"]) <= 3 and value["재료위치"] == "냉장":
                under_3_list.insert(END, f"{value['재료위치']}    {value['개수']}   {value['재료이름']}\n")
        for key, value in data.iterrows():
            if float(value["개수"]) <= 3 and value["재료위치"] == "냉동":
                under_3_list.insert(END, f"{value['재료위치']}    {value['개수']}   {value['재료이름']}\n")
        for key, value in data.iterrows():
            if float(value["개수"]) <= 3 and value["재료위치"] == "상온":
                under_3_list.insert(END, f"{value['재료위치']}    {value['개수']}   {value['재료이름']}\n")
        for key, value in data.iterrows():
            if float(value["개수"]) <= 3 and value["재료위치"] != "상온" and \
                    value["재료위치"] != "냉동" and value["재료위치"] != "냉장":
                under_3_list.insert(END, f"{value['재료위치']}    {value['개수']}   {value['재료이름']}\n")
    except ValueError:
        messagebox.showerror(title="오류", message="개수에 숫자를 입력해주세요.")


# add_fun
def add_click():
    try:
        ingredient = ingredient_entry.get()
        count = count_entry.get()
        float(count)
        position = position_entry.get()
        new_index = len(data)
        if len(ingredient) <= 0 or len(count) <= 0 or len(position) <= 0:
            messagebox.showerror(title="경고", message="재료이름, 개수, 재료위치의 모든 값을 입력해주세요")
        else:
            if messagebox.askokcancel(title="메뉴 추가", message=f"재료이름: {ingredient} \n개수: {count} \n재료위치: {position} \n"
                                                             f"정말로 이대로 추가 하시겠습니까?"):
                data.loc[new_index] = [ingredient, count, position]
                data.to_csv("stock.csv", index=None)
                list_box.delete(0, END)
                print_list_box()
                sold_out_print()
                under_3_print()
                ingredient_entry.delete(0, END)
                count_entry.delete(0, END)
                position_entry.delete(0, END)
    except ValueError:
        messagebox.showerror(title="오류", message="개수에 숫자를 입력해주세요.")


# delete_fun
def delete_click():
    try:
        delete_key = None
        ingredient = ingredient_entry.get()
        for key, value in data.iterrows():
            if value["재료이름"] == ingredient:
                delete_key = key
                break
        if messagebox.askokcancel(title="메뉴삭제", message=f"재료이름: {ingredient}를(을) 정말로 삭제하시겠습니까?"):
            data.drop(delete_key, axis=0, inplace=True)
            list_box.delete(0, END)
            data.to_csv("stock.csv", index=None)
            print_list_box()
            sold_out_print()
            under_3_print()
            ingredient_entry.delete(0, END)
    except ValueError:
        messagebox.showerror(title="Error", message="입력하신 재료이름의 값이 잘못되었습니다.")


# click_list_box
def click_list_box(event):
    try:
        index_num = list_box.curselection()
        menu = list_box.get(index_num).strip().split("    ")
        ingredient = menu[2].strip()
        count = menu[1]

        ingredient_entry.delete(0, END)
        count_entry.delete(0, END)
        ingredient_entry.config(fg="black")
        count_entry.config(fg="black")

        ingredient_entry.insert(0, ingredient)
        count_entry.insert(0, count)
    except _tkinter.TclError:
        pass


# click_sold_out
def click_sold_out(event):
    try:
        index_num = sold_out_list.curselection()
        menu = sold_out_list.get(index_num).strip().split("   ")
        if index_num[0] != 0:
            ingredient = menu[2]
            count = menu[1].strip()

            ingredient_entry.delete(0, END)
            count_entry.delete(0, END)
            ingredient_entry.config(fg="black")
            count_entry.config(fg="black")

            ingredient_entry.insert(0, ingredient)
            count_entry.insert(0, count)
    except _tkinter.TclError:
        pass


def click_under_3(event):
    try:
        index_num = under_3_list.curselection()
        menu = under_3_list.get(index_num).strip().split("   ")
        if index_num[0] != 0:
            ingredient = menu[2]
            count = menu[1].strip()

            ingredient_entry.delete(0, END)
            count_entry.delete(0, END)
            ingredient_entry.config(fg="black")
            count_entry.config(fg="black")

            ingredient_entry.insert(0, ingredient)
            count_entry.insert(0, count)
    except _tkinter.TclError:
        pass


# information_fun
def information_click():
    messagebox.showinfo(title="Information", message="개발자: 김도완 \n개발버전: 2.0 \n개발일자: 2022.06.26 (ver 1.0)"
                                                     "\n업데이트 일자: 2022.08.18 (ver 2.0)")


# entry explain
def ingredient_clear(event):
    if ingredient_entry.get() == "재료이름을 입력해주세요":
        ingredient_entry.delete(0, END)
        ingredient_entry.config(fg="black")
    if count_entry.get() == "":
        count_entry.config(fg="gray")
        count_entry.insert(0, "재료의 개수를 입력해주세요")
    if position_entry.get() == "":
        position_entry.config(fg="gray")
        position_entry.insert(0, "재료의 위치를 입력해주세요")


def count_clear(event):
    if count_entry.get() == "재료의 개수를 입력해주세요":
        count_entry.delete(0, END)
        count_entry.config(fg="black")
    if ingredient_entry.get() == "":
        ingredient_entry.config(fg="gray")
        ingredient_entry.insert(0, "재료이름을 입력해주세요")
    if position_entry.get() == "":
        position_entry.config(fg="gray")
        position_entry.insert(0, "재료의 위치를 입력해주세요")


def position_clear(event):
    if position_entry.get() == "재료의 위치를 입력해주세요":
        position_entry.delete(0, END)
        position_entry.config(fg="black")
    if ingredient_entry.get() == "":
        ingredient_entry.config(fg="gray")
        ingredient_entry.insert(0, "재료이름을 입력해주세요")
    if count_entry.get() == "":
        count_entry.config(fg="gray")
        count_entry.insert(0, "재료의 개수를 입력해주세요")


# base window
window = Tk()
window.title("이디야 재고 관리 ver 2.0")
window.geometry("900x400")
window.iconbitmap("logo.ico")

# top_background
top_back = Label(bg="#253d87", width=500, height=2)
top_back.place(x=0, y=0)

# Top image
canvas = Canvas(width=202, height=20)
logo_img = PhotoImage(file="image/top_logo.gif")
canvas.create_image(101, 12, image=logo_img)
canvas.grid(row=0, column=0, padx=5, pady=5)

# Top Label
logo_label = Label(text="이디야 신대방지점 재고관리 프로그램", fg="white", font=("고딕", 10, "bold"), bg="#253d87")
logo_label.grid(row=0, column=1)

# ingredient
ingredient_name = Label(text="재료이름: ", font=("명조", 10, "bold"))
ingredient_name.place(x=0, y=60)

ingredient_entry = Entry()
ingredient_entry.place(x=70, y=62)
ingredient_entry.focus()
ingredient_entry.bind("<Return>", enter_ingredient_entry)

ingredient_entry.config(fg="gray")
ingredient_entry.insert(0, "재료이름을 입력해주세요")
ingredient_entry.bind('<ButtonRelease-1>', ingredient_clear)

# count
count_label = Label(text="개수:", font=("명조", 10, "bold"))
count_label.place(x=0, y=110)

count_entry = Entry()
count_entry.place(x=70, y=112)
count_entry.bind("<Return>", enter_count_entry)

count_entry.config(fg="gray")
count_entry.insert(0, "재료의 개수를 입력해주세요")
count_entry.bind('<ButtonRelease-1>', count_clear)

# position
position_label = Label(text="재료위치:", font=("명조", 10, "bold"))
position_label.place(x=0, y=160)

position_entry = Entry()
position_entry.place(x=70, y=162)

position_entry.config(fg="gray")
position_entry.insert(0, "재료의 위치를 입력해주세요")
position_entry.bind('<ButtonRelease-1>', position_clear)

# button
add_button = Button(text="추가", width=34, bg="white", command=add_click)
add_button.place(x=3, y=200)

search_button = Button(text="검색", bg="white", command=search_click)
search_button.place(x=220, y=60)

update_button = Button(text="수정", bg="white", command=update_click)
update_button.place(x=220, y=110)

delete_button = Button(text="삭제", bg="white", command=delete_click)
delete_button.place(x=220, y=160)

# notebook
notebook = tkinter.ttk.Notebook(window, width=300, height=324)
notebook.place(x=600, y=37)


# text
list_frame = Frame()        # 프레임 생성
list_scroll = Scrollbar(list_frame, width=20)     # 스크롤 바 생성
list_scroll.pack(side="right", fill="y")
list_box = Listbox(list_frame, width=40, height=20, yscrollcommand=list_scroll.set)
list_box.pack()
print_list_box()
list_scroll["command"] = list_box.yview     # 이거까지 해줘야 작동
list_frame.place(x=300, y=60)
list_box.bind('<ButtonRelease-1>', click_list_box)

sold_out_frame = Frame()
notebook.add(sold_out_frame, text="품절")
sold_out_scroll = Scrollbar(sold_out_frame, width=20)
sold_out_scroll.pack(side="right", fill="y")
sold_out_list = Listbox(sold_out_frame, width=40, height=20, yscrollcommand=sold_out_scroll.set)
sold_out_list.pack()
sold_out_print()
sold_out_scroll["command"] = sold_out_list.yview
# sold_out_frame.place(x=600, y=50)
sold_out_list.bind('<ButtonRelease-1>', click_sold_out)

under_3_frame = Frame()
notebook.add(under_3_frame, text="3개이하")
under_3_scroll = Scrollbar(under_3_frame, width=20)
under_3_scroll.pack(side="right", fill="y")
under_3_list = Listbox(under_3_frame, width=40, height=20, yscrollcommand=under_3_scroll.set)
under_3_list.pack()
under_3_print()
under_3_scroll["command"] = under_3_list.yview
under_3_list.bind('<ButtonRelease-1>', click_under_3)

# explain
explain_text = Text(width=36, height=10)
explain_text.place(x=3, y=243)
explain_text.insert(0.0, "            [사용방법]\n")
explain_text.insert(END, "검색기능: 재료이름을 입력하고 검색\n\n")
explain_text.insert(END, "수정기능: 재고를 수정하는 기능, 재료          이름(띄어쓰기 까지 동일)과 "
                         "         개수(정수나 실수)를 입력하          고 수정버튼 누르기\n\n")
explain_text.insert(END, "삭제기능: 재료자체를 삭제하는 기능,           재료이름을 입력하고 삭제버          튼\n\n")
explain_text.insert(END, "추가기능: 신규재료를 등록하는 기능,           재료이름, 개수, 재료위치를          입력하고 추가버튼")

# information
information_button = Button(text="i", bg="#253d87", fg="white", command=information_click)
information_button.place(x=880, y=5)



window.mainloop()
