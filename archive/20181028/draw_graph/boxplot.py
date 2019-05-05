import plotly.plotly as py
import plotly.graph_objs as go

trace = []

def boxplot(l):
    len_l = len(l)
    data = []
    
    for i in range(len_l):
        trace[i] = go.Box(
        y = l[i],
        name='Only Mean',
        marker=dict(
            color='rgb(8, 81, 156)',
        ),
        boxmean=True
        )
        
        print(data)


    py.plot(data)