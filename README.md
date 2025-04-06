# pygame_music_materials

シンプルな音楽再生モジュール

## 特徴

- シンプルなインターフェース
- 音楽ファイルの自動ループ設定
- 音量コントロール
- 曲の切り替え時の二重再生防止
- 型ヒントによるコード補完サポート

## インストール

```bash
pip install git+https://github.com/osad-sakana/pygame_music_materials.git
```

## 基本的な使い方

```python
import pygame_music_materials as pmm

# ミキサーの初期化
mixer = pmm.Mixer()

# 音楽の再生
mixer.play(pmm.night)  # 組み込みの音楽を再生
mixer.play(pmm.field)

# 音量調整
mixer.set_volume(0.5)  # 0.0 から 1.0 の範囲

# 一時停止/再開
mixer.pause()
mixer.unpause()

# 独自の音楽ファイルを使用する場合
custom_music = pmm.Music(
    id="my_music",
    title="My Music",
    path="/path/to/your/music.mp3",
    loop=True  # ループ再生する場合
)
mixer.play(custom_music)
```

## 組み込みの音楽

- `pmm.night`: ナイトステージBGM
- `pmm.field`: フィールドBGM
- `pmm.lava`: 溶岩ステージBGM
- `pmm.boss_battle`: ボス戦BGM
- `pmm.stage_clear`: クリアジングル

## 利用可能な音楽データ

| ID | ファイル名 | 説明 | ループ設定 |
|---|---|---|---|
| night | shinmiri.wav | 静かな夜のBGM | ○ |
| boss_battle | boss.wav | ボス戦のBGM | ○ |
| lava | yougan.wav | 溶岩ステージのBGM | ○ |
| stage_clear | clear.wav | クリア時のジングル | × |
| field | sougen.wav | フィールドのBGM | ○ |

## サンプルゲーム

`examples/simple_game`ディレクトリにサンプルゲームがあります。このゲームでモジュールの基本的な機能を試すことができます。

```bash
cd examples/simple_game
python main.py
```

詳しい使い方は[サンプルゲームのREADME](examples/simple_game/README.md)を参照してください。

## 必要要件

- Python 3.7以上
- pygame >= 2.0.0

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 注意事項

- 音楽ファイルは別途用意する必要があります
- 対応している音声フォーマットはWAVファイルのみです
- 音楽ファイルは`pygame_music_materials/musics`ディレクトリに配置してください
