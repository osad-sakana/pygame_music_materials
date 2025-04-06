"""pygame_music_materialsの音楽プレイヤー"""
import pygame_music_materials as pmm
import pygame
import sys
from pathlib import Path

# 親ディレクトリをPythonパスに追加
sys.path.append(str(Path(__file__).parent.parent))

# 初期化
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()

# フォントの設定
font_path = Path(__file__).parent / "PixelMplus12-Regular.ttf"
font = pygame.font.Font(str(font_path), 24)
small_font = pygame.font.Font(str(font_path), 18)

# 音楽ミキサーの初期化
mixer = pmm.Mixer()
current_music = pmm.night
mixer.play(current_music)
volume = 0.5
mixer.set_volume(volume)

# 音楽リスト
music_list = [
    pmm.night,
    pmm.field,
    pmm.lava,
    pmm.boss_battle,
    pmm.stage_clear
]
selected_index = 0


def get_display_indices(selected_index, total_items):
    """表示するインデックスのリストを取得"""
    indices = []
    for i in range(-2, 3):  # 選択項目の前後2つずつ
        index = (selected_index + i) % total_items
        indices.append(index)
    return indices


# メインループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_UP:
                # 選択を上に移動
                selected_index = (selected_index - 1) % len(music_list)
            elif event.key == pygame.K_DOWN:
                # 選択を下に移動
                selected_index = (selected_index + 1) % len(music_list)
            elif event.key == pygame.K_RETURN:
                # 選択した曲を再生/停止
                if current_music == music_list[selected_index] and pygame.mixer.music.get_busy():
                    mixer.pause()
                else:
                    current_music = music_list[selected_index]
                    mixer.play(current_music)
            elif event.key == pygame.K_RIGHT:
                # 音量アップ
                volume = min(1.0, volume + 0.1)
                mixer.set_volume(volume)
            elif event.key == pygame.K_LEFT:
                # 音量ダウン
                volume = max(0.0, volume - 0.1)
                mixer.set_volume(volume)

    # 画面の描画
    screen.fill((0, 0, 0))

    # 現在の曲情報を表示
    title_text = font.render(
        f"現在の曲: {current_music.title}", True, (255, 255, 255))
    volume_text = font.render(
        f"音量: {int(volume * 100)}%", True, (255, 255, 255))
    status_text = font.render(
        "状態: " + ("再生中" if pygame.mixer.music.get_busy() else "停止中"), True, (255, 255, 255))

    # 曲リストの表示
    y = 30  # 上部の余白を減らす
    screen.blit(title_text, (50, y))
    y += 40  # 行間を詰める
    screen.blit(volume_text, (50, y))
    y += 40
    screen.blit(status_text, (50, y))
    y += 60  # リストまでの間隔を詰める

    # 曲リストのヘッダー
    header_text = font.render(
        "曲リスト (↑/↓で選択, Enterで再生/停止)", True, (200, 200, 200))
    screen.blit(header_text, (50, y))
    y += 40

    # 表示するインデックスの取得
    display_indices = get_display_indices(selected_index, len(music_list))

    # 曲リストの表示
    for i, index in enumerate(display_indices):
        music = music_list[index]

        # 選択中の曲は背景を表示
        if i == 2:  # 中央の項目
            # ハイライトの背景を描画
            pygame.draw.rect(screen, (30, 30, 30), (45, y - 5, 700, 30))
            # 選択中の曲の背景を描画
            pygame.draw.rect(screen, (50, 50, 50), (45, y - 5, 700, 30), 2)
            text_color = (255, 255, 255)
        else:
            text_color = (200, 200, 200)

        # 曲情報の表示
        number_text = small_font.render(f"{index + 1}.", True, text_color)
        id_text = small_font.render(f"ID: {music.id}", True, text_color)
        title_text = small_font.render(f"曲名: {music.title}", True, text_color)
        loop_text = small_font.render(
            f"ループ: {'ON' if music.loop else 'OFF'}", True, text_color)

        screen.blit(number_text, (50, y))
        screen.blit(id_text, (100, y))
        screen.blit(title_text, (250, y))
        screen.blit(loop_text, (550, y))
        y += 35  # 行間を詰める

    # 操作説明
    controls = [
        "↑/↓: 曲の選択",
        "Enter: 再生/停止",
        "←/→: 音量調整",
        "ESC: 終了"
    ]

    # 操作説明の表示
    y += 40  # 操作説明までの間隔を詰める
    for control in controls:
        control_text = small_font.render(control, True, (150, 150, 150))
        screen.blit(control_text, (50, y))
        y += 25  # 操作説明の行間を詰める

    pygame.display.flip()
    clock.tick(60)

# 終了処理
pygame.quit()
