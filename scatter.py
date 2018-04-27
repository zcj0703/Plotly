#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import plotly.plotly
import plotly.graph_objs as go
import numpy as np
# 导入plotly和numpy包

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)
# 生成1000个随机数据

trace = go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers'
)
#生成散点图，图形形状是markers

data = [trace]

plotly.offline.plot(data, filename='basic_scatter.html')
#离线绘图，图形的文件名是basic_scatter,生成的是一个html文件
#666
