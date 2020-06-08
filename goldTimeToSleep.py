from tkinter import *

root = Tk()
root.title('Gold Time To Sleep zZZ')
root.iconbitmap('C:\\Users\\super\\Downloads\\fun.ico')
root.geometry("500x500")

def myClick():
    hourF = int(hour.get()) # giờ nhập vào
    minuteF = int(minute.get())  # phút nhập vào
    nF = int(n.get())                     # hệ số n
    minToSleepF = int(minToSleep.get())   # thời gian lim dim

    timeSleep = 90 * nF + minToSleepF  # thời gian ngủ tính theo công thức vàng

    if hourF + (timeSleep // 60) >= 24:  # số giờ lúc này vượt quá 24 h thì phải trừ đi
        hourWake = hourF + (timeSleep // 60) - 24
    else:
        hourWake = hourF + (timeSleep // 60)

    if minuteF + (timeSleep % 60) >= 60:
        minuwake = minuteF + (timeSleep % 60) - 60
        if hourWake + 1 == 24:
            hourWake = 0
        hourWake += 1
    else:
        minuwake = minuteF + (timeSleep % 60)

    showTimeWake = "Bạn nên dậy lúc:" + str(hourWake) + 'giờ ' +  str(minuwake) + 'phút'
    Label(root, text=showTimeWake,fg='#40e2ed', font=('Heveltical', 15)).grid(row=14,column=1,columnspan=4)

    hour.delete(0, 'end')
    minute.delete(0, 'end')
    n.delete(0, 'end')
    minToSleep.delete(0, 'end')


Label(root, text='Tính thời gian VÀNG cho giấc ngủ ', fg='#77A7FF', font=('Heveltical', 15)).grid(row=0,columnspan=9,column=0)

Label(root).grid(row=1,columnspan=9)
Label(root).grid(row=2,columnspan=9)

Label(root, text='Nhập giờ bạn đị ngủ: ',  font=('Heveltical', 10)).grid(row=4, columnspan=2,column=0)
Label(root, text="Giờ").grid(row=4,column=2)
hour = Entry(root)
hour.grid(row=4,column=3)
Label(root, text="Phút").grid(row=4,column=4)
minute = Entry(root)
minute.grid(row=4,column=5)

Label(root).grid(row=5,columnspan=9)

Label(root, text='Từ lúc nằm, bạn mất bao\n lâu để chìm vào giấc ngủ', font=('Heveltical', 10)).grid(row=6,columnspan=2,column=0)
minToSleep = Entry(root)
minToSleep.grid(row=6,column=3)
Label(root, text="Phút").grid(row=6,column=4)

Label(root).grid(row=9,columnspan=9)

Label(root, text='Nhập chu kỳ ngủ (n)\n n: có giá trị từ 3 đến 6 \nthì giấc ngủ của \nbạn sẽ thoải mái nhất', font=('Heveltical', 10)).grid(row=10,columnspan=2,column=0)
n = Entry(root)
n.grid(row=10,column=3)


Label(root).grid(row=11,columnspan=9)

myButton = Button(root, text="Tính thời gian thức dậy ", command=myClick)
myButton.grid(row=12,column=3,columnspan=2)

Label(root).grid(row=12,columnspan=9)
Label(root).grid(row=13,columnspan=9)


Label(root).grid(row=15,columnspan=9)
Label(root).grid(row=16,columnspan=9)
Label(root, text='Bản Quyền phần mềm thuộc tập đoàn công nghệ TD © ', fg='#1877F2', font=('Heveltical', 10)).grid(row=17,columnspan=5,column=0)
root.mainloop()


