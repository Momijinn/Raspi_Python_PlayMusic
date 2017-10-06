# Raspi_Python_PlayMusic
RaspberryPiでPythonを使った音楽再生プログラム

## 動作確認環境
* RaspberryPi3
* Python 2.7.13

## 追加するモジュール
* sudo apt-get install python-pygame
* sudo pip install mutagen

## 使用方法
PlayMusic.pyがライブラリになっています

そのため、これをインポートすれば使えます

## sample.py
```python
#!/usr/bin/env python
#-*- cording: utf-8 -*-
import PlayMusic as PM

if __name__ == '__main__':
    PM.PlayMusic("sample.mp3", 500) #("再生する音楽ファイル", フェードアウト時間)
```

## 使用した音源
【サイト名】フリー音楽素材 H/MIX GALLERY

【管理者】　秋山裕和

【アドレス】http://www.hmix.net/