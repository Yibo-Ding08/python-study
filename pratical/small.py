import time
with open("E:\ceshi.txt\测试.txt", "r", encoding="utf-8") as f:
    content=f.read()
    count=content.count("a")
    print(f"a出现了{count}次")
time.sleep(10)