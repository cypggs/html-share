# HTML Share

一个用来收集和分享精美 HTML 页面的静态站点。

在线地址：`https://cypggs.github.io/html-share/`

## 快速开始

1. 克隆仓库
   ```bash
   git clone https://github.com/cypggs/html-share.git
   cd html-share
   ```

2. 复制模板创建新页面
   ```bash
   cp template.html my-awesome-page.html
   ```

3. 修改页面元数据和正文：
   - `<title>`：页面标题
   - `<meta name="description">`：页面描述
   - `<meta name="date">`：发布日期，格式 `YYYY-MM-DD`
   - `<meta name="tags">`：标签，用英文逗号分隔

4. 提交并推送到 `main` 分支
   ```bash
   git add .
   git commit -m "add: my awesome page"
   git push origin main
   ```

5. GitHub Actions 会自动更新 `pages.json`，稍等片刻首页就会显示新卡片。

## 本地预览

```bash
cd html-share
python3 -m http.server 8000
```

然后打开 `http://localhost:8000`。

## 目录结构

```
html-share/
├── index.html          # 首页，卡片墙 + 搜索
├── pages.json          # 页面索引，由 update_pages.py 自动生成
├── template.html       # 新页面模板
├── hello.html          # 示例页面
├── update_pages.py     # 扫描 HTML 并生成索引的脚本
└── .github/workflows/
    └── update-pages.yml # 自动更新 pages.json 的 GitHub Actions
```

## 提示

- 所有页面建议保持内联样式，不依赖外部资源，方便 GitHub Pages 部署。
- 页面里可以放图片，但建议使用图床或 Base64，避免仓库体积膨胀。
