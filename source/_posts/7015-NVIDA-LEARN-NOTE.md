---
title: 7015 NVIDA LEARN NOTE
date: 2025-12-09 17:14:40
tags: [NVIDA, LEARN, NOTE, MAI]
category: MAI
---
# GAN的原理

# U-net原理
## decoder & encoder structure
### purpose
- encoder: downsample the image to a lower dimension
- decoder: upsample the image to a higher dimension
- skip connection: concatenate the feature map from the encoder with the feature map from the decoder
       
## transposed convolution 转置卷积
- purpose: upsample the image to a higher dimension
- operation: similar to convolution, but with a flipped kernel
- stride: the number of pixels to move the kernel each time
    - 在普通卷积里，Stride 大会让图变小得更快。在转置卷积里，Stride 大会让图变大得更猛。因为 Stride = 2 意味着你在“投射”每一个像素时，中间会隔开一些距离，从而把输出图像撑得更大，这就是 Image Upscaling（图像放大） 的核心机制 。

在 U-Net 的解码器（Decoder）里：

Stride (步长) 负责把图撑大（拉开间距）。

Padding (填充) 负责把边缘修剪掉（为了和 Encoder 里的操作对称）。

Out Padding 负责微调尺寸，确保能完美还原回 128x128 这种标准大小。

## U-net coding
### 步骤
1. Dataset prepare
    
2. 定义 U-Net 模型
    downblock-nn.module
         kernel_size=3, stride=1, padding=1
    >输入 x (3通道, 128x128)
        ↓
    [Conv2d] 卷积 (变成 64通道, 128x128)
    [BatchNorm] + [ReLU]
        ↓
    [Conv2d] 再卷一次 (保持 64通道, 128x128)
    [BatchNorm] + [ReLU]
        ↓
    [MaxPool2d(2)] 池化 (砍一半尺寸)
        ↓
    输出 (64通道, 64x64)


3. 编译模型
4. 训练模型
5. 评估模型
6. 可视化结果


### import constants for our dataset
```python
IMG_SIZE = 16 # Due to stride and pooling, must be divisible by 2 multiple times
IMG_CH = 1 # Black and white image, no color channels
BATCH_SIZE = 128
```