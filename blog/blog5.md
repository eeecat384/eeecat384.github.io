标题：m3u8转MP4教程（针对夸克下载）

关键词：m3u8, 教程

发布时间：2025-12-26

注意：此教程针对手机夸克下载的m3u8视频，其他来源下载的可能会有不同，操作也不一样，后面我可能会出相关原理教学（挖坑），这样你遇到不同的m3u8文件都会转换了

本教程使用windows的win11系统，如果是win10及以下系统或者动过右键菜单，“右键，选择‘在终端中打开’”的操作应改为“shift+右键，选择‘在此处打开Powershell窗口’”

任何一步操作有红色报错的话，首先检查自己有没有严格按照教程走，然后再把报错和这份文档复制给ai，找我解决的话请贴出和ai对话的记录或者v我50，任选其一

使用的.py文件在我github仓库中eecat384.github.io/blog_resoures/m3u8转MP4教程（针对夸克下载）

如果上不了github，可新建一个文本文件，把下面的代码粘贴进去

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, pathlib

src = pathlib.Path('playlist.m3u8')
out = pathlib.Path('local.m3u8')

lines   = src.read_text(encoding='utf-8').splitlines()
new_lines, idx = [], 0

for raw in lines:
    line = raw.strip()
    # 1. 保留所有非 ts 行（含 KEY、IV、EXTINF 等）
    if not line.endswith('.ts') and '.ts?' not in line:
        new_lines.append(raw + '\n')
        continue
    # 2. 遇到 ts 行（无论有没有参数）→ 替换成编号
    new_lines.append(f'{idx}.ts\n')
    idx += 1

out.write_text(''.join(new_lines), encoding='utf-8')
print(f'✅ 已生成 {out} ，共 {idx} 个 ts 段。')

然后保存，退出，将这个文件重命名为

fix_m3u8.py

第一步：检查自己有没有装ffmpeg和python环境，如果不知道这俩是什么，那大概率就是没装，搜网上教程去

第二步：文件名称应该是0,1,2,3这种无后缀文件，我们需要给他们加ts后缀

在你下载的视频文件夹内部（就是你能看到0,1,2,3这种文件的文件夹内部）右键，选择“在终端中打开”，把下面的代码复制进去，回车

Get-ChildItem -File | Where-Object { $_.Name -match '^\d+$' } | Rename-Item -NewName { $_.Name + '.ts' }

然后检查一下文件是否都有了.ts后缀。

第三步：把那个名字最长的文件重命名为

playlist.m3u8

将.py文件复制进下载的视频文件夹内部，在文件夹内右键，选择“在此处打开终端”，把下面的代码复制进去，回车

python fix_m3u8.py

然后检查一下生成的local.m3u8文件内部是否有类似于
0.ts
#EXTINF:8.333333,
1.ts
#EXTINF:8.333333,
如果有，证明成功（那个8.333333是单个视频的时长，和我的不一样也没关系）

第四步，看你下载的视频文件夹内是否有类似0.key的文件，若有，用记事本或者vscode等打开local.m3u8文件，找到类似：
#EXT-X-KEY:METHOD=AES-128,URI="https://xxxx.com/0.key"
改成：
#EXT-X-KEY:METHOD=AES-128,URI="0.key"

注：0.key和你文件内的16kb大小的文件名字对应

第五步：把playlist.m3u8删除，在你下载的视频文件夹内部右键，选择“在终端中打开”，把下面的代码复制进去，回车

ffmpeg -allowed_extensions ALL -i local.m3u8 -c copy output.mp4

2025.12.26早，收工