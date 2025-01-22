# 秒抄
下载点[这里]
(https://github.com/qzgeek/ewt360/releases)

## 项目简介
`秒抄` 是一个辅助工具，旨在在“升学e网通”上自动回答其教辅上的选择题、提交试卷及获取选择题的答案以及部分主观题的答案。

## 功能特点
- **自动回答选择题**：工具能够自动完成选择题并提交答案。
- **获取答案**：提供选择题的答案，以及部分主观题的答案。

## 使用限制
- **手动操作需求**：需要用户手动扫描二维码以提取`contentid`。
- **主观题显示问题**：无法正常显示大部分主观题的答案。
- **配置要求**：用户需手动抓包并填写`cookie`，且需要将其转换为特定的格式。

## 使用说明
1. **获取contentid**：使用手机扫描教辅上的二维码，获取`contentid`。
2. **配置cookie**：根据指示手动抓取并填写cookie信息。
3. **运行工具**：按照工具的使用指南进行操作，完成答题和交卷。

## 注意事项
- 确保在使用前仔细阅读所有说明和指南。
- 由于工具存在一些限制，建议用户在使用时保持谨慎。

## 疑难杂症
### 如何获取contentid？
- 随便找个浏览器扫描教辅上课后习题的二维码，跳转链接后可以在浏览器输入框看到链接，在链接中慢慢找就可以看到“contentid=114514”的字样，等号后面的那串数字就是contentid

#### 什么是教辅？
- 如果你的学校和“升学e网通”有合作，你是大概率会得到他们家的各种作业的（基本都是假期作业）
- 当然，如果你没有，基本可以退出了（不过你要想看看也行awa，但是没有他们的作业的话这项目拿来真没啥用(●_●)）

###如何获取cookie？
- 建议上网搜，例如[这里](https://b23.tv/NkkuXTj)

## 创作动机
1. **闲的**: 不闲我咋会来搞呢awa
2. **嫌慢k*: 抄答案还要先做题？玩呢？

## 开发方向
1. **图形化界面**: 争取在这个假期搞出apk或者网页啥的
2. **更方便的操作**: 比如自带扫描解析和简单的登录获取cookie
3. **更好的显示**: 尽量完整地正确地显示出答案
