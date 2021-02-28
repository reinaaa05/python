# coding: utf-8
# Your code here!

# 2次元リストで画像を配置

# 画像用リスト
players_img = [
    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Empty.png",
    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Dragon.png",
    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Crystal.png",
    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Hero.png",
    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Heroine.png"]

team = []
while True:
    line = input()
    if line =="_":
        break
    team.append(line.split(","))

print("<table>")
for line in team:
    print("<tr>")
    for person in line:
        print("<td><img src='" + players_img[int(person)] + "'></td>")
    print("</tr>")
print("</table>")
