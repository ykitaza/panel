import numpy as np
import holoviews as hv
import panel as pn

hv.extension('bokeh')

def generate_curve(index):
    x = np.linspace(0, 10, 100)
    y = np.sin(x + index)
    return hv.Curve((x, y), 'X', 'Y').opts(
        width=1000,
        height=1000,
        tools=['hover', 'zoom_in', 'zoom_out', 'reset'],
        shared_axes=False,
        title=f'グラフ {index}'  # グラフのタイトルを設定
    )

# 9つのグラフを生成
curves = [generate_curve(i) for i in range(9)]

# 3x3のグリッドにグラフを配置
grid_tab = pn.GridSpec(width=1200, height=1200)
for i in range(3):
    for j in range(3):
        grid_tab[i, j] = curves[i*3 + j]

selector = pn.widgets.CheckBoxGroup(
    name='グラフ選択', options={f'グラフ {i}': i for i in range(len(curves))}, inline=True
)

@pn.depends(selector.param.value)
def show_selected_curves(indexes):
    if not indexes:
        indexes = [0]
    selected_curves = [curves[i] for i in indexes]
    return pn.panel(hv.Layout(selected_curves).opts(shared_axes=False).cols(1))

grid_with_selector = pn.Column(selector, grid_tab)
selected_curves_tab = pn.Column(show_selected_curves)

tabs = pn.Tabs(('3x3グリッド', grid_with_selector), ('選択したグラフ', selected_curves_tab))

tabs.show()
