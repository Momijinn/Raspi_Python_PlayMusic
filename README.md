Raspi_Python_PlayMusic
====
Pythonを使った音楽再生ライブラリ

## Description
Python上で使用できる簡単に音楽を再生できるライブラリ

## Requirement
* 動作確認環境
    * RaspberryPi3
    * Python 2.7.13

* 追加モジュール
    ```bash
    $ sudo apt-get install python-pygame
    $ sudo pip install mutagen
    ```

## Usage
PlayMusic.pyがライブラリになっています

そのため、これをインポートすれば使えます

```python
#!/usr/bin/env python
#-*- cording: utf-8 -*-
import PlayMusic as PM

if __name__ == '__main__':
    PM.PlayMusic("sample.mp3", 500) #("再生する音楽ファイル", フェードアウト時間)
```

## Install
```python
import PlayMusic as PM
```

## Licence
This software is released under the MIT License, see LICENSE.

使用した音源
```
【サイト名】フリー音楽素材 H/MIX GALLERY
【管理者】秋山裕和
【アドレス】http://www.hmix.net/
```

## Author
[Twitter](https://twitter.com/momijinn_aka)

[Blog](http://www.autumn-color.com/)