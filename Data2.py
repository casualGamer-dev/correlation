import pandas as pd
import plotly.express as px
f=pd.read_csv("./data2.csv")
mark=f["Marks"].tolist()
nd =len(mark)
sum = 0
for i in mark:
    sum +=i
print(sum)
mean=sum/nd
print(mean)
fig=px.scatter(f,x="Student Number",y="Marks")
fig.update_layout(shapes=[dict(type='line',x0=0,x1=nd,y0=mean,y1=mean)])
fig.show()