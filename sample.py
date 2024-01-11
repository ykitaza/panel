import numpy as np
import holoviews as hv
import panel as pn

hv.extension('bokeh')

# グラフ生成関数
def generate_curve(index):
    x = np.linspace(0, 10, 100)
    y = np.sin(x + index)
    return hv.Curve((x, y), 'X', 'Y').opts(
        width=300,
        height=300,
        tools=['hover', 'zoom_in', 'zoom_out', 'reset'],
        shared_axes=False,
        title=f'グラフ {index}'
    )

# アプリケーションのメイン関数
def app_main():
    # 9つのグラフを生成
    curves = [generate_curve(i) for i in range(9)]

    # グラフ選択ウィジェット
    selector = pn.widgets.CheckBoxGroup(
        name='グラフ選択', options={f'グラフ {i}': i for i in range(len(curves))}, inline=True
    )

    # 選択されたグラフを表示する関数
    @pn.depends(selector.param.value)
    def show_selected_curves(indexes):
        if not indexes:
            return hv.Div('')
        selected_curves = [curves[i] for i in indexes]
        return hv.Layout(selected_curves).opts(shared_axes=False).cols(3)

    # グラフとセレクターを垂直に配置
    layout = pn.Column(selector, show_selected_curves)

    return layout

# サーバー起動
pn.serve(app_main)
