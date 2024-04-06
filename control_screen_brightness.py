import screen_brightness_control as sbc
import time

# 目標亮度
target_brightness = 100


# 獲取當前連接的顯示器列表
monitors = sbc.list_monitors()
print(monitors)

# 獲取第一個顯示器的當前亮度
current_brightness = sbc.get_brightness(monitors[0])[0]
print(f"當前亮度：{current_brightness}")

# 計算每步調整的亮度差
step = (current_brightness - target_brightness) / 10

# 開始調整亮度之前的時間
start_time = time.time()

# 逐步調整亮度
for i in range(1, 11):
    # 計算新的亮度值
    new_brightness = int(current_brightness - step * i)
    # 設置亮度
    sbc.set_brightness(new_brightness, display=monitors[0])

# 完成調整亮度之後的時間
end_time = time.time()

# 計算並打印執行時間，精確到小數點後三位
execution_time = end_time - start_time
print(f"調整亮度所花費的時間：{execution_time:.3f}秒")
