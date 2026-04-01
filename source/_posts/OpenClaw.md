---
title: OpenClaw
date: 2026-03-11 23:27:48
tags:
---

```powershell
iwr -useb https://openclaw.ai/install.ps1 | iex
```
这段命令由两个部分通过管道符（|）连接：

iwr -useb [URL]: Invoke-WebRequest 的缩写。它会访问 openclaw.ai 的服务器并获取 install.ps1 这个脚本的内容。-useb (UseBasicParsing) 是为了确保在没有配置 Internet Explorer 的环境下也能快速读取。

iex: Invoke-Expression 的缩写。它会将前面下载到的脚本内容直接在当前的 PowerShell 窗口中执行。