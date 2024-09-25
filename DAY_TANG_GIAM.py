def tim_tongday(dayso):
    n = len(dayso)
    if n == 0:  # Kiểm tra danh sách rỗng
        return []

    ketqua = []  # Lưu các dãy số liên tiếp
    # cầm canh
    daysotam = [dayso[0]]  # Dãy số tạm thời chứa phần tử đầu tiên
    flag = None  # Cờ để xác định dãy tăng hay giảm

    # Duyệt qua danh sách từ phần tử thứ 2
    for i in range(1, n):
        if flag is None:
            # Đặt cờ khi lần đầu phát hiện dãy tăng hoặc giảm
            if dayso[i] > dayso[i-1]:
                flag = True
            elif dayso[i] < dayso[i-1]:
                flag = False

        # Xử lý dãy tăng
        if flag is True:
            if dayso[i] > dayso[i-1]:
                daysotam.append(dayso[i])  # Tiếp tục dãy tăng
            else:
                # Dãy bị gián đoạn, kết thúc dãy tăng
                total = sum(daysotam)
                print(f"Dãy số: {daysotam} Tổng: {total}")
                ketqua.append((daysotam.copy(), total))

                # Bắt đầu dãy giảm mới
                daysotam = [dayso[i-1], dayso[i]]
                flag = False  # Đặt cờ cho dãy giảm

        # Xử lý dãy giảm
        elif flag is False:
            if dayso[i] < dayso[i-1]:
                daysotam.append(dayso[i])  # Tiếp tục dãy giảm
            else:
                # Dãy bị gián đoạn, kết thúc dãy giảm
                total = sum(daysotam)
                print(f"Dãy số: {daysotam} Tổng: {total}")
                ketqua.append((daysotam.copy(), total))

                # Bắt đầu dãy tăng mới
                daysotam = [dayso[i-1], dayso[i]]
                flag = True  # Đặt cờ cho dãy tăng

    # Xử lý dãy cuối cùng
    total = sum(daysotam)
    print(f"Dãy số: {daysotam} Tổng: {total}")
    ketqua.append((daysotam.copy(), total))

    return ketqua

if __name__=="__main__":
    dayso = [1, 2, 3, 5, 4, 3, 2, 1, 10, 11, 12, 9]
    thucthi = tim_tongday(dayso)
