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