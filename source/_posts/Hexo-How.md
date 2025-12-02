---
title: HEXO FROM THE BEGINNING
date: 2025-12-02 16:55:27
tags: [笔记]
categories: [Hexo]
---
## Initialize a Hexo site
1. Check node.js
```bash
node -v
```
2. Check git
```bash
git --version
```
3. Install hexo-cli
```bash
npm install -g hexo-cli
```
4. Inisitalize a Hexo site
```bash
hexo init <folder> 
cd <folder> # 进入博客目录
npm install # 安装依赖（相当于安装装修材料）
hexo server        # 启动本地预览服务器
```

### Use Themes
5. Use Themes
- 安装必要的渲染插件
- git clone 主题仓库到 themes 目录
- 在博客目录下编辑 _config.yml 文件，将 theme 字段设置为你选择的主题名称

6. Clean and Start Server
```bash
hexo clean   # 清理缓存（也就是清理 public 文件夹和 db.json）
hexo g       # 重新生成静态文件 (Generate)
hexo s       # 启动服务器 (Server)
```

### Deploy to GitHub Pages
- 在博客目录下编辑 _config.yml 文件，将 deploy 字段设置为如下内容：
```yaml
deploy:
  type: git
  repo: https://github.com/你的用户名/你的用户名.github.io.git  <-- 粘贴刚才复制的地址
  branch: main  <-- 注意：现在新仓库默认叫 main，如果是很老的仓库可能叫 master，去 GitHub 确认一下分支名
```
- 执行部署命令
```bash
npm install hexo-deployer-git --save
hexo g -d      # 部署到 GitHub Pages (Deploy)
```
- 推送代码部分
```bash
git init #初始化仓库
git checkout -b hexo  # 创建并切换到 hexo 分支

git add .  
git commit -m "Deploy Hexo site to GitHub Pages"  # 提交代码
git remote add origin https://github.com/你的用户名/你的用户名.github.io.git 
git push -u origin hexo
```

- Update blog for reader
```bash
hexo new "My New Post"  # 创建新文章
hexo g -d      # 部署到 GitHub Pages (Deploy)
```
- 推送代码部分
```bash
git add .  
git commit -m "Update My New Post"  # 提交代码
git push origin hexo
```

## New page
- 创建新页面
```bash
hexo new  "about"
```


