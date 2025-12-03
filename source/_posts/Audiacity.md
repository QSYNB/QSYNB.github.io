---
title: Aydacity
date: 2025-12-03 17:29:18
tags: [软件, 播客, whisper, 语音识别, 音频剪辑]
categories: [花里胡哨的瞎忙活]
---

# 写在前面
因为播客剪辑工作繁重，觉得剪映的文本识别，框选文本删除音频的功能很好用（就是在于不和波形同步操作的话，会有波形切断生硬的问题），所以想自己优化一下。

省略过程，目前退而求其次的想法是：想在音频剪辑软件如（audacity）里面实现一个音频轨下面有一个lable轨，lable轨的文字显示的是这段音频对应的文本。这样不用听一遍才知道这段音频是什么。

目前实现方式是本地whisper/whisperX模型来跑。

目前方案和问题：
方案1：用whisper跑逐字/词对应（方便字/词级别的修改）（因为我和播客搭子会有精修的需求）
    问题：lable数量太大太卡了。
方案2：whisper跑逐句的对应
    优点：解决了卡顿问题，两个轨2h音频可以正常使用不影响剪辑
    问题：whisper的时间对应不精准，在一长段文本中会有时间偏移。（在一段空白之后的文本会修正，然后反复）
方案3：whisperX跑逐句的对应
    问题：whisperX不知道为什么转不出标点符号，导致无法按照期望的来断句。导致也无法（没心情）看时间对应是否符合预期。
其他问题：
    1.Audacity的内置插件无法调用cmd执行命令，只能手动在cmd里面运行。导致过程也不够自动化。
    2.whisper模型会忽略音频中的 嗯，啊，语气词，不符合剪辑需求。（剪映做的就很好，~~应该~~肯定是自己训的模型了，真好啊）
未来方向：
    1.tmd这些音频剪辑软件我受够了（主要是大部分软件都没有文字轨），能不能自己写一个简单的只有剪辑功能的？
    2.模型能更符合播客剪辑需求就好了
    3.使用以下英文的那个软件（叫descript还是啥）看看参考以下

# 瞎忙活忙活了啥
- 本地部署whisper/whisperX模型 （whisperX的部署过程被AI狂骗）
- 写一个python脚本，调用whisper/whisperX模型，将音频转成逐句的对应文本。生成lable格式的txt。（其实是AI一键写的我没怎么看，后续要好好看一下）
- 因为还想用llm来识别播客文本，来判断哪些需要删除哪些逻辑可以保留，所以还尝试了租gpu服务器（runpod），部署deepseek-v2-lite等，但是大失败。（主要是init module总是失败在disk full就很烦，放弃了）

先写到这后续再慢慢整理（道心破碎中……


## test Audacity plug-in function available
``` Nyquist
;nyquist plug-in
;version 4
;type process
;name "Hello World Test"
;action "Running Test"

(format nil "恭喜！Nyquist 运行成功！")
```

## Nyquist plug-in 思路
第一步测试：确保 Audacity 能“吐出”音频 (WAV)
第二步测试：确保 Nyquist 能“传话”给 Python
第三步测试：确保 Audacity 能“吃进” TXT 标签

### 测试1-导出音频
``` Nyquist
;nyquist plug-in
;version 4
;type process
;name "测试1-导出音频"
;action "正在测试导出..."

(defun main ()
  ;; 1. 硬编码一个测试路径 (请确保这个文件夹存在！)
  (setq test-audio-path "D:/15_MAI/audacity/temp_test.wav")
  
  ;; 2. 保存选区 (*track*) 到文件
  ;; s-save 是 Nyquist 保存音频的函数
  (s-save *track* 1000000000 test-audio-path)
  
  ;; 3. 告诉用户结果
  (format nil "音频已导出到：~a" test-audio-path)
)

(main)
```
### 第二步测试：确保 Nyquist 能“传话”给 Python
``` Nyquist
;nyquist plug-in
;version 4
;type process
;name "测试2-构建命令"
;action "正在检查路径..."

(defun main ()
  ;; 填入您的真实路径
  (setq py-exe "D:/important/Conda_Envs/py310/python.exe")
  (setq py-script "D:/15_MAI/audacity/whisperx_label_generator.py")
  (setq audio-file "D:/15_MAI/audacity/temp_test.wav") ;; 假设这是第一步生成的文件
  
  ;; 构建命令 (注意这里要把反斜杠处理好)
  (setq cmd (format nil "\"~a\" \"~a\" \"~a\"" py-exe py-script audio-file))
  
  ;; 把它打印出来给您看！
  (format nil "请复制下面的命令去CMD运行验证：\n\n~a" cmd)
)

(main)
```
### 测试3 是否能调用cmd执行命令


### 测试4 是否能导入标签

