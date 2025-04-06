# Music Player Sample

`pygame_music_materials`を使用した音楽プレイヤーのサンプル実装です。

## インストール

1. 依存モジュールのインストール：
```bash
pip install git+https://github.com/osad-sakana/pygame_music_materials.git
```

2. このサンプルをクローン：
```bash
git clone https://github.com/osad-sakana/music_tester.git
cd music_tester
```

## 機能

このサンプルでは以下の機能を実装しています：
- 曲リストの表示と選択
- 再生/停止の制御
- 音量調整
- ループ設定の表示

## 操作方法

- ↑/↓: 曲の選択
- Enter: 再生/停止
- ←/→: 音量調整
- ESC: 終了

## 実行方法

```bash
python main.py
```

## カスタマイズ例

独自の音楽を追加する場合：

```python
import pygame_music_materials as pmm

# 独自の音楽を作成
custom_music = pmm.Music(
    id="my_music",
    title="My Music",
    path="path/to/music.mp3",
    loop=True
)

# music_listに追加
music_list = [
    custom_music,
    pmm.night,
    pmm.field,
    # ...
]
```

## 必要要件

- Python 3.7以上
- pygame >= 2.0.0
- pygame_music_materials
