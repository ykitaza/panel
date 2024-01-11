import panel as pn

# Panel拡張機能を有効化
pn.extension()

# カスタムCSSを設定
pn.config.raw_css.append("""
.flex-scrollable {
    overflow-y: auto;
    display: flex;
    flex-wrap: wrap;
    justify-content: start;
    align-items: start;
}
.scrollable-item {
    width: 33%; /* 3つのアイテムが横に並ぶようにする */
    box-sizing: border-box;
    padding: 5px; /* アイテム間のスペース */
}
""")

# サイドバー（左側のセクション）
sidebar = pn.pane.Markdown("サイドバー", width=200, sizing_mode='stretch_height')

# メインコンテンツエリア（右上のセクション）
main_content = pn.pane.Markdown("メインコンテンツ", sizing_mode='stretch_width', height=400)

# スクロール可能なアイテムを生成
items = [pn.pane.Markdown(f"アイテム {i+1}", css_classes=['scrollable-item']) for i in range(9)]

# スクロール可能なエリア（右下のセクション）
scrollable_area = pn.Column(*items, css_classes=['flex-scrollable'], sizing_mode='stretch_width')

# 右側のセクション
right_panel = pn.Column(main_content, scrollable_area, sizing_mode='stretch_both')

# 全体のレイアウトを組み立てる
layout = pn.Row(sidebar, right_panel, sizing_mode='stretch_height')

# Panelサーバーを起動
layout.show()
