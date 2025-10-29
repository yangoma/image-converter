# 外部圧縮ツール配置ガイド

このフォルダに外部の画像圧縮ツールを配置することで、より高度な最適化が可能になります。

## 必須ではありません

これらのツールは**オプション**です。配置しなくても基本的な変換は動作します。
より高品質な圧縮を行いたい場合にのみ配置してください。

## 推奨ツール

### PNG最適化

#### pngquant (推奨度: ★★★)
- **機能**: PNG画像の減色と圧縮
- **ダウンロード**: https://pngquant.org/
- **ファイル**: `pngquant.exe`
- **効果**: ファイルサイズを50-70%削減（視覚的品質はほぼ維持）

#### optipng (推奨度: ★★★)
- **機能**: PNG画像の無劣化圧縮
- **ダウンロード**: http://optipng.sourceforge.net/
- **ファイル**: `optipng.exe`
- **効果**: 追加で5-20%のサイズ削減

#### pngcrush (推奨度: ★★☆)
- **機能**: PNG最適化
- **ダウンロード**: https://pmt.sourceforge.io/pngcrush/
- **ファイル**: `pngcrush.exe`

#### pngout (推奨度: ★★☆)
- **機能**: 強力なPNG圧縮
- **ダウンロード**: http://www.advsys.net/ken/utils.htm
- **ファイル**: `pngout.exe`
- **注意**: 処理時間が長い

#### advpng (推奨度: ★☆☆)
- **機能**: AdvanceCOMPを使用したPNG圧縮
- **ダウンロード**: https://www.advancemame.it/download
- **ファイル**: `advpng.exe`

### JPEG最適化

#### jpegtran (推奨度: ★★★)
- **機能**: JPEG無劣化最適化
- **ダウンロード**: https://jpegclub.org/jpegtran/ または MozJPEG
- **ファイル**: `jpegtran.exe`
- **効果**: 
  - 不要なメタデータ削除
  - プログレッシブJPEG化
  - 5-10%のサイズ削減

#### jpegoptim (推奨度: ★★☆)
- **機能**: JPEG最適化
- **ダウンロード**: Windowsビルドを探す必要あり
- **ファイル**: `jpegoptim.exe`

### その他

#### gifsicle (推奨度: ★☆☆)
- **機能**: GIF最適化
- **ダウンロード**: https://www.lcdf.org/gifsicle/
- **ファイル**: `gifsicle.exe`

#### svgo (推奨度: ★☆☆)
- **機能**: SVG最適化
- **ダウンロード**: https://github.com/svg/svgo
- **ファイル**: Node.js経由でインストール

## インストール手順

### 推奨セットアップ（初心者向け）

最もシンプルで効果的な構成：

1. **pngquant.exe** をダウンロード
2. **optipng.exe** をダウンロード
3. **jpegtran.exe** をダウンロード（MozJPEGに含まれる）
4. この3つをこのフォルダに配置

この3つだけで十分高品質な圧縮が可能です。

### 詳細手順

#### 1. pngquant のインストール

```
1. https://pngquant.org/ にアクセス
2. "Download" セクションから Windows版をダウンロード
3. ZIP を解凍
4. pngquant.exe を tools フォルダにコピー
```

#### 2. optipng のインストール

```
1. http://optipng.sourceforge.net/ にアクセス
2. "Downloads" から Windows版をダウンロード
3. ZIP を解凍
4. optipng.exe を tools フォルダにコピー
```

#### 3. jpegtran のインストール (MozJPEG経由)

```
1. https://github.com/mozilla/mozjpeg/releases にアクセス
2. 最新の Windows版をダウンロード
3. ZIP を解凍
4. jpegtran.exe を tools フォルダにコピー
```

## 配置後の確認

このフォルダ内に以下のようにファイルが配置されていればOKです：

```
tools/
├── README.md (このファイル)
├── pngquant.exe
├── optipng.exe
└── jpegtran.exe
```

## 動作確認

スクリプト実行時に、ツールが見つかった場合は以下のようなメッセージが表示されます：

```
✓ 変換完了: image.png -> image_converted.jpg
  → jpegtran最適化完了
```

```
✓ 変換完了: photo.webp -> photo_converted.png
  → pngquant最適化完了
  → optipng最適化完了
```

## トラブルシューティング

### ツールが認識されない

- ファイル名が正確か確認（`pngquant.exe` など）
- 実行ファイル（.exe）であることを確認
- 32bit/64bitの互換性を確認

### エラーが出る

- 各ツールが正しくダウンロードされているか確認
- Windowsのバージョンとツールの互換性を確認
- 管理者権限が必要な場合があります

## 圧縮効果の目安

### PNG
- **pngquant**: 元のサイズの30-50%に削減（視覚的品質はほぼ維持）
- **optipng**: 追加で5-20%削減

### JPEG
- **jpegtran**: 5-15%削減（無劣化）

## 参考情報

### より詳しい情報
- PNG最適化: https://developers.google.com/speed/docs/insights/OptimizeImages
- JPEG最適化: https://developers.google.com/speed/docs/insights/OptimizeImages

### 代替ツール
- **ImageMagick**: 総合的な画像処理ツール
- **XnConvert**: GUI付き一括変換ツール
- **FileOptimizer**: 複数形式対応の最適化ツール
