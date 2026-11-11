
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Ellipse, Polygon, Arc


fig, ax = plt.subplots(figsize=(10, 6))


ax.add_patch(Rectangle((0, 0), 20, 12, color="skyblue"))

ax.add_patch(Circle((17, 10), 1.2, color="gold"))

ax.add_patch(Ellipse((4, 10), 3, 1.2, color="white"))

ax.add_patch(Ellipse((5, 10.3), 2, 1, color="white"))

ax.add_patch(Ellipse((11, 10.8), 3, 1.1, color="white"))

ax.add_patch(Arc((8, 9), 0.8, 0.5, theta1=0, theta2=180, color="black", linewidth=2))

ax.add_patch(Arc((8.8, 9), 0.8, 0.5, theta1=0, theta2=180, color="black", linewidth=2))

ax.add_patch(Arc((14, 8.5), 0.8, 0.5, theta1=0, theta2=180, color="black", linewidth=2))

ax.add_patch(Arc((14.8, 8.5), 0.8, 0.5, theta1=0, theta2=180, color="black", linewidth=2))

ax.add_patch(Rectangle((0, 0), 20, 3, color="dimgray"))

ax.add_patch(Rectangle((1, 1.4), 1.5, 0.2, color="white"))

ax.add_patch(Rectangle((4, 1.4), 1.5, 0.2, color="white"))

ax.add_patch(Rectangle((7, 1.4), 1.5, 0.2, color="white"))

ax.add_patch(Rectangle((10, 1.4), 1.5, 0.2, color="white"))

ax.add_patch(Rectangle((13, 1.4), 1.5, 0.2, color="white"))

ax.add_patch(Rectangle((16, 1.4), 1.5, 0.2, color="white"))

ax.add_patch(Rectangle((1, 3), 3, 5, color="saddlebrown", ec="black"))

ax.add_patch(Polygon([(0.8, 8), (4.2, 8), (2.5, 9)], color="darkslategray"))

ax.add_patch(Rectangle((1.4, 4.5), 0.7, 0.9, color="lightyellow", ec="black"))

ax.add_patch(Rectangle((2.9, 4.5), 0.7, 0.9, color="lightyellow", ec="black"))

ax.add_patch(Rectangle((1.4, 6.3), 0.7, 0.9, color="lightyellow", ec="black"))

ax.add_patch(Rectangle((2.9, 6.3), 0.7, 0.9, color="lightyellow", ec="black"))

ax.add_patch(Rectangle((5, 3), 2.5, 7, color="slategray", ec="black"))

ax.add_patch(Polygon([(4.8, 10), (7.7, 10), (6.25, 11)], color="darkslategray"))

ax.add_patch(Rectangle((5.4, 4.5), 0.7, 0.9, color="lightyellow", ec="black"))

ax.add_patch(Rectangle((6.4, 4.5), 0.7, 0.9, color="lightyellow", ec="black"))

ax.add_patch(Rectangle((5.4, 6.3), 0.7, 0.9, color="lightyellow", ec="black"))

ax.add_patch(Rectangle((6.4, 6.3), 0.7, 0.9, color="lightyellow", ec="black"))

ax.add_patch(Rectangle((5.4, 8.1), 0.7, 0.9, color="lightyellow", ec="black"))

ax.add_patch(Rectangle((6.4, 8.1), 0.7, 0.9, color="lightyellow", ec="black"))

ax.add_patch(Rectangle((8.2, 3), 3.5, 4, color="indianred", ec="black"))

ax.add_patch(Polygon([(8, 7), (11.9, 7), (10, 8.2)], color="darkslategray"))

ax.add_patch(Rectangle((8.7, 4.5), 0.8, 0.9, color="lightyellow", ec="black"))

ax.add_patch(Rectangle((10.4, 4.5), 0.8, 0.9, color="lightyellow", ec="black"))

ax.add_patch(Rectangle((9.6, 3), 0.7, 1.3, color="sienna", ec="black"))

ax.add_patch(Rectangle((12.5, 3), 2.8, 6, color="steelblue", ec="black"))

ax.add_patch(Polygon([(12.3, 9), (15.5, 9), (13.9, 10)], color="darkslategray"))

ax.add_patch(Rectangle((12.9, 4.5), 0.7, 0.9, color="lightyellow", ec="black"))

ax.add_patch(Rectangle((14.1, 4.5), 0.7, 0.9, color="lightyellow", ec="black"))

ax.add_patch(Rectangle((12.9, 6.3), 0.7, 0.9, color="lightyellow", ec="black"))

ax.add_patch(Rectangle((14.1, 6.3), 0.7, 0.9, color="lightyellow", ec="black"))

ax.add_patch(Rectangle((18.5, 3), 0.15, 3.5, color="black"))   

ax.add_patch(Circle((18.57, 6.7), 0.35, color="yellow", ec="black")) 

ax.add_patch(Rectangle((16.5, 3), 0.4, 1.5, color="saddlebrown"))
  
ax.add_patch(Circle((16.7, 5), 1.0, color="forestgreen"))         
ax.set_xlim(0, 20)
ax.set_ylim(0, 12)
ax.set_aspect("equal")   
ax.axis("off")           
ax.set_title("Городской пейзаж")


plt.savefig("img/task3.png", dpi=150, bbox_inches="tight")
plt.show()