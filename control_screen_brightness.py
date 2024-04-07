import screen_brightness_control as sbc
import time

def smooth_set_brightness(target_brightness, steps=16):
    try:
        # 獲取當前連接的顯示器列表
        monitors = sbc.list_monitors()
        if not monitors:
            print("未檢測到顯示器")
            return

        # 獲取第一個顯示器的當前亮度
        current_brightness = sbc.get_brightness(monitors[0])[0]
        print(f"當前亮度：{current_brightness}")

        # 計算每步調整的亮度差
        step = (target_brightness - current_brightness) / steps

        # 逐步調整亮度
        start_time = time.time()
        for i in range(1, steps + 1):
            new_brightness = int(current_brightness + step * i)
            sbc.set_brightness(new_brightness, display=monitors[0])

        # 計算並打印執行時間
        execution_time = time.time() - start_time
        print(f"調整亮度所花費的時間：{execution_time:.3f}秒")
    except Exception as e:
        print(f"調整亮度過程中發生錯誤：{e}")

# 調用函數，將亮度平滑調整到100
smooth_set_brightness(100)
smooth_set_brightness(0)
