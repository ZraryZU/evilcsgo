import torch
print(torch.cuda.is_available())
import cv2

# 创建VideoCapture对象，读取文件
# 如果要读取摄像头就改成0
# cap=cv2.VideoCapture('dy2.mp4')
cap = cv2.VideoCapture('rtmp://127.0.0.1:1935/live/stream')

if (cap.isOpened() == False):
    print("Error opening video stream or file")

fps = cap.get(cv2.CAP_PROP_FPS)
print("帧率：" + str(fps))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        cv2.imshow('Frame', frame)

        # 按q退出
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break

# 播放结束要释放VideoCapture对象
cap.release()

# 关闭窗口
cv2.destroyAllWindows()