# 画像変換ツール

WebP、PNG、AVIF、TIFF、HEICなどの画像を簡単にJPG/PNG/WebPに変換できるツールです。

## 使い方

### simple_converter.bat をダブルクリック

メニューが表示されます：

```
[1] 単一ファイル変換
[2] フォルダ一括変換
[3] 終了
```

#### 単一ファイルの場合

1. 「1」を入力してEnter
2. 画像ファイルをドラッグ&ドロップしてEnter
3. フォーマットを選択（1〜4）
4. 自動的に変換されて、2秒後にメニューに戻ります

#### フォルダ一括変換の場合

1. 「2」を入力してEnter
2. フォルダをドラッグ&ドロップしてEnter
3. フォーマットを選択（1〜4）
4. フォルダ内のすべての画像が変換されます

## 出力フォーマット

| 番号 | フォーマット | 品質 | 用途 |
|------|------------|------|------|
| 1 | JPG | 95% | 高品質、印刷用 |
| 2 | JPG | 85% | 標準、おすすめ |
| 3 | PNG | 最適化 | 透明度保持 |
| 4 | WebP | 90% | 高品質、小サイズ |

## 対応ファイル形式

**入力**: WebP, PNG, AVIF, TIFF, HEIC/HEIF (iPhone), BMP, GIF, JPEG

**出力**: JPG, PNG, WebP

## 保存場所

### 単一ファイル
元のファイルと同じ場所に `ファイル名_converted.jpg` として保存されます

例: `photo.webp` → `photo_converted.jpg`

### 複数ファイル
元のフォルダ内に `converted_jpg` フォルダが作成され、そこに保存されます

## 必要な環境

- Windows 10/11
- Python 3.7以降
- Pillow, pillow-heif（自動インストール）

### Pythonのインストール

https://www.python.org/downloads/

**重要**: インストール時に「Add Python to PATH」にチェックを入れてください

### ライブラリのインストール

```cmd
python -m pip install Pillow pillow-heif
```

## トラブルシューティング

### エラーが出る場合

コマンドプロンプトを開いて：

```cmd
python -m pip install --upgrade pip
python -m pip install Pillow pillow-heif
```

### 変換されない場合

1. Pythonがインストールされているか確認
2. ファイルパスに特殊文字が含まれていないか確認
3. ファイル形式が対応しているか確認

## 高度な使い方

### コマンドラインで一括変換

```cmd
cd C:\path\to\image-converter
python convert_image.py C:\Pictures\*.webp -f jpg -q 95
```

### 圧縮強化（オプション）

`tools` フォルダに以下のツールを配置すると、さらに圧縮が強化されます：

- pngquant.exe
- optipng.exe  
- jpegtran.exe

詳細は `tools/README.md` を参照

## ライセンス

MIT License
