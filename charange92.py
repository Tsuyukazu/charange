qs = input("今日は何味のプロテインを飲みましたか？：")

with open("answer.txt","w",encoding="utf-8") as f:
    f.write(qs)

