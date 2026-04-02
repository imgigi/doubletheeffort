# 🎴 双倍用心卡牌护理中心

> 专业修复 · 全程透明 · 用心守护每一位训练家的卡牌

![Status](https://img.shields.io/badge/status-live-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Gitee Pages](https://img.shields.io/badge/Gitee-Pages-red)
![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-lightgrey)

---

## 🌐 在线访问

**中国大陆推荐（Gitee Pages）：** https://你的用户名.gitee.io/doublecare-website/

**备用（GitHub Pages）：** https://你的用户名.github.io/pokemon-card-care-center/

**管理员后台：** https://你的用户名.gitee.io/doublecare-website/admin.html

**客户查询：** https://你的用户名.gitee.io/doublecare-website/query.html

---

## ✨ 功能特性

### 🏠 主页功能
- ⏰ 实时时间显示
- 🎨 品牌 Logo 展示
- 📋 近期送修案例轮播
- 🔗 管理员/客户双通道入口
- 🚀 拓展功能区预留

### 👨‍💼 管理员后台
- 🔐 安全登录验证
- ➕ 新建卡牌档案
- ✏️ 编辑档案信息
- 🗑️ 删除档案
- 📊 数据统计面板
- 📄 Word 导入导出
- 📸 **损伤照片上传**（新功能！）
- 📈 自动生成日报

### 🔍 客户查询
- 🔎 验证号快速查询
- 📱 修复进度时间轴
- 📸 **损伤照片查看**（新功能！）
- 🔍 灯箱大图预览
- 📦 状态实时更新

---

## 🚀 快速部署

### 方法一：Gitee Pages（中国大陆推荐 ⭐）

**优势：** 国内访问速度快、完全免费、中文界面

```bash
1. 访问 https://gitee.com 注册账号并完成实名认证
2. 点击右上角「+」→「新建仓库」
3. 仓库名称：doublecare-website
4. 可见性：Public（公开）
5. ❌ 不要勾选 "使用 README 初始化仓库"
6. 点击「创建」
7. 进入仓库页面 → 点击「上传文件」
8. 拖入所有 HTML 文件（index.html, admin.html, query.html）
9. 提交信息填写："初始版本"，点击「提交」
10. 进入「服务」→「Gitee Pages」
11. 来源分支选择 "master"，点击「启动」
12. 等待 1-2 分钟，获得网站地址
```

**一键部署脚本（Windows）：**
```bash
# 双击运行项目中的「一键部署到 Gitee.bat」
# 按提示输入 Gitee 仓库地址
# 自动完成推送
```

📚 **详细指南：** 查看项目中的 [`Gitee 快速上线指南.html`](Gitee 快速上线指南.html) 或 [`Gitee_Pages 部署指南.md`](Gitee_Pages 部署指南.md)

---

### 方法二：GitHub Pages（国际用户/备用）

```bash
1. 访问 https://github.com/new 创建仓库
2. 仓库名称：pokemon-card-care-center
3. 可见性：Public
4. 勾选 "Add a README file"
5. 点击 "Create repository"
6. 点击 "Add file" → "Upload files"
7. 拖入所有 HTML 文件和图片
8. 点击 "Commit changes"
9. 进入 Settings → Pages
10. Source 选择 "main branch"
11. 保存并等待 1-2 分钟
```

### 方法二：Git 命令行

```bash
# 克隆仓库
git clone https://github.com/你的用户名/pokemon-card-care-center.git

# 进入目录
cd pokemon-card-care-center

# 复制项目文件到仓库目录
# （将原项目文件复制到这里）

# 提交并推送
git add .
git commit -m "Initial commit"
git push origin main
```

### 方法三：GitHub Desktop

1. 下载并安装 [GitHub Desktop](https://desktop.github.com/)
2. File → Add Local Repository
3. 选择项目文件夹
4. Publish repository
5. 完成！

---

## 📁 文件结构

```
pokemon-card-care-center/
├── index.html              # 主页
├── admin.html              # 管理员后台
├── query.html              # 客户查询页
├── README.md               # 本说明文档
├── GitHub_Pages 部署指南.md   # 详细部署教程
└── generated_image_*.jpg   # 品牌图片资源
```

---

## 🛠️ 本地开发

### 直接打开

双击 `index.html` 即可在浏览器中预览。

### 使用 Live Server（推荐）

**VS Code 扩展：**
1. 安装 "Live Server" 插件
2. 右键 index.html → Open with Live Server
3. 自动在浏览器打开并热更新

**或使用 Python：**
```bash
# Python 3
python -m http.server 8000

# 访问 http://localhost:8000
```

---

## 💾 数据存储

当前版本使用 **LocalStorage** 存储数据：

**优点：**
- ✅ 无需服务器
- ✅ 零成本
- ✅ 即时可用

**限制：**
- ❌ 数据仅保存在本地
- ❌ 不同设备不共享
- ❌ 清除浏览器会丢失数据

### 未来升级方案

#### 方案 A：Supabase（推荐）
```javascript
// 示例代码
import { createClient } from '@supabase/supabase-js'

const supabase = createClient('YOUR_SUPABASE_URL', 'YOUR_ANON_KEY')

// 保存数据
await supabase.from('archives').insert([archiveData])

// 查询数据
const { data } = await supabase.from('archives').select('*')
```

#### 方案 B：Firebase
```javascript
import { getDatabase, ref, set } from 'firebase/database'

const db = getDatabase()
set(ref(db, 'archives/' + code), archiveData)
```

#### 方案 C：LeanCloud（国内访问更快）
```javascript
const query = new AV.Query('Archive');
query.equalTo('verificationCode', code);
query.find().then(...)
```

---

## 🎨 设计特色

### 配色方案

```css
--pokemon-red: #FF3E3E      /* 宝可梦红 */
--pokemon-blue: #3B4CCA     /* 宝可梦蓝 */
--pokemon-yellow: #FFDE00   /* 皮卡丘黄 */
--pokemon-dark: #2D3748     /* 深色文字 */
--pokemon-light: #F7FAFC    /* 浅色背景 */
```

### 品牌元素

- ⚡ 精灵球 Logo
- 🎴 卡牌主题图标
- 📦 快递物流元素
- ✨ 修复完成特效

---

## 📸 照片上传功能

### 管理员端

1. 打开管理员后台
2. 新建或编辑档案
3. 在"损伤问题描述"下方找到照片上传区
4. 点击或拖拽上传照片
5. 支持多张照片同时上传
6. 实时预览，可单独删除

**技术规格：**
- 格式：JPG / PNG
- 大小：单张 ≤ 5MB
- 存储：Base64 编码

### 客户端

1. 输入验证号查询
2. 查看卡牌基本信息
3. 浏览损伤照片（如有）
4. 点击缩略图查看大图
5. 灯箱效果全屏预览

---

## 🔒 安全提示

### 当前版本

管理员密码为前端验证，仅适合初期使用：

```
默认账号：admin
默认密码：123456
```

⚠️ **建议：** 上线后立即修改密码！

### 生产环境建议

1. 使用后端认证服务
2. 接入 Auth0 / Firebase Auth
3. 启用 HTTPS（GitHub Pages 已默认提供）
4. 定期备份数据

---

## 📊 流量统计（可选）

### 百度统计

在 `<head>` 中添加：

```html
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?YOUR_ID";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
```

### Google Analytics

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

---

## 🌐 自定义域名

### 购买域名

推荐平台：
- 阿里云（¥55/年）
- 腾讯云（¥50/年）
- Namecheap（$6/年）

### DNS 配置

```
A 记录：
  主机：@
  值：185.199.108.153

CNAME 记录：
  主机：www
  值：用户名.github.io
```

### GitHub 配置

1. Settings → Pages → Custom domain
2. 输入：www.yourdomain.com
3. 勾选 "Enforce HTTPS"
4. Save

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

### 开发流程

1. Fork 本项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 📝 更新日志

### v1.2.0 (2026-03-31)
- ✨ 新增损伤照片上传功能
- ✨ 客户端支持照片查看
- 🎨 灯箱大图预览效果
- 📸 支持多张照片同时上传
- 🗑️ 照片可单独删除

### v1.1.0 (2026-03-30)
- ✨ 完整档案管理系统
- 📊 数据统计面板
- 📄 Word 导入导出
- 📈 日报生成功能

### v1.0.0 (2026-03-29)
- 🎉 首次发布
- 🏠 主页、管理员后台、客户查询页

---

## 📞 联系方式

- **品牌官网**: https://你的用户名.github.io/pokemon-card-care-center/
- **邮箱**: your-email@example.com
- **微信**: 扫码添加客服

---

## 📄 许可证

MIT License

---

## 🙏 致谢

感谢以下开源项目：

- [GitHub Pages](https://pages.github.com/) - 免费托管
- [Font Awesome](https://fontawesome.com/) - 图标库
- [Google Fonts](https://fonts.google.com/) - 字体资源

---

**双倍用心呵护您的卡牌 · 致每一位热爱宝可梦的训练家** 🎴✨
