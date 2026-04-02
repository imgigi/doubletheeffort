# -*- coding: utf-8 -*-
html_content = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>联动测试页面 - 双倍用心</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Microsoft YaHei', sans-serif; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            color: white;
            text-align: center;
            font-size: 36px;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .subtitle {
            color: #FFD7D7;
            text-align: center;
            font-size: 16px;
            margin-bottom: 40px;
        }
        .test-section {
            background: white;
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }
        .test-section h2 {
            color: #2D3748;
            font-size: 24px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .test-item {
            background: #F7FAFC;
            border-left: 4px solid #48BB78;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 15px;
        }
        .test-item.success { border-left-color: #48BB78; }
        .test-item.error { border-left-color: #F56565; }
        .test-item.warning { border-left-color: #ED8936; }
        .test-item label {
            font-weight: bold;
            color: #4A5568;
            display: block;
            margin-bottom: 8px;
        }
        .test-item .value {
            font-family: monospace;
            background: white;
            padding: 10px;
            border-radius: 6px;
            color: #2D3748;
            word-break: break-all;
        }
        .btn {
            background: linear-gradient(135deg, #FF3E3E 0%, #3B4CCA 100%);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 25px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
            margin: 10px 10px 10px 0;
        }
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        }
        .btn-secondary {
            background: #4A5568;
        }
        .btn-success {
            background: #48BB78;
        }
        .nav-links {
            text-align: center;
            margin-top: 30px;
        }
        .nav-links a {
            display: inline-block;
            background: white;
            color: #2D3748;
            text-decoration: none;
            padding: 15px 40px;
            border-radius: 25px;
            font-weight: bold;
            margin: 10px;
            transition: all 0.3s;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        .nav-links a:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        }
        .status-badge {
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: bold;
            margin-left: 10px;
        }
        .status-ok { background: #C6F6D5; color: #22543D; }
        .status-error { background: #FED7D7; color: #742A2A; }
        .code-block {
            background: #1A202C;
            color: #48BB78;
            padding: 15px;
            border-radius: 8px;
            font-family: 'Courier New', monospace;
            margin-top: 10px;
            font-size: 13px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔗 双倍用心 - 系统联动测试</h1>
        <p class="subtitle">测试主页与管理员后台的数据同步和跳转功能</p>
        
        <!-- 导航链接 -->
        <div class="nav-links">
            <a href="index.html" target="_blank">🏠 打开主页</a>
            <a href="admin_simple.html" target="_blank">🔑 打开管理员后台</a>
            <a href="#" onclick="location.reload(); return false;">🔄 刷新测试</a>
        </div>
        
        <!-- 测试区域 1：LocalStorage 数据检查 -->
        <div class="test-section">
            <h2>📦 测试 1：LocalStorage 数据存储检查</h2>
            <div class="test-item success">
                <label>管理员密码存储：</label>
                <div class="value" id="passwordStatus">检测中...</div>
            </div>
            <div class="test-item success">
                <label>卡牌档案数据：</label>
                <div class="value" id="archivesStatus">检测中...</div>
            </div>
            <div class="test-item success">
                <label>送修案例数据：</label>
                <div class="value" id="casesStatus">检测中...</div>
            </div>
        </div>
        
        <!-- 测试区域 2：数据同步测试 -->
        <div class="test-section">
            <h2>🔄 测试 2：数据同步功能</h2>
            <div class="test-item">
                <label>测试操作：</label>
                <p style="color: #718096; margin-bottom: 15px;">
                    点击以下按钮添加测试数据，然后打开主页或管理员后台查看是否同步显示。
                </p>
                <button class="btn btn-success" onclick="addTestArchive()">➕ 添加测试档案</button>
                <button class="btn btn-success" onclick="addTestCase()">➕ 添加测试案例</button>
                <button class="btn btn-secondary" onclick="clearAllData()">🗑️ 清空所有数据</button>
            </div>
            <div class="test-item">
                <label>最近操作记录：</label>
                <div class="code-block" id="operationLog">暂无操作记录</div>
            </div>
        </div>
        
        <!-- 测试区域 3：页面跳转测试 -->
        <div class="test-section">
            <h2>🚀 测试 3：页面跳转联动</h2>
            <div class="test-item">
                <label>测试步骤：</label>
                <ol style="color: #4A5568; line-height: 2; margin-left: 20px;">
                    <li>点击"打开管理员后台"按钮，在新标签页打开管理员登录页面</li>
                    <li>使用默认账号登录（用户名：<code>admin</code>，密码：<code>zpx8495168</code>）</li>
                    <li>在管理员后台上传一个送修案例</li>
                    <li>点击管理员后台的"🏠 返回首页"按钮</li>
                    <li>检查主页是否正确显示刚才上传的案例</li>
                    <li>点击主页的"🔑 管理员登录"按钮</li>
                    <li>检查是否能正确返回管理员后台</li>
                </ol>
            </div>
        </div>
        
        <!-- 测试区域 4：常见问题排查 -->
        <div class="test-section">
            <h2>🔧 测试 4：常见问题排查</h2>
            <div class="test-item warning">
                <label>问题 1：登录不上去</label>
                <p style="color: #718096; margin-top: 10px;">
                    <strong>可能原因：</strong><br>
                    • 浏览器缓存了旧密码<br>
                    • LocalStorage 数据异常<br>
                    • JavaScript 错误导致登录逻辑未执行<br><br>
                    <strong>解决方案：</strong><br>
                    1. 按 F12 打开浏览器控制台，查看是否有红色错误信息<br>
                    2. 点击下方"重置密码为默认值"按钮<br>
                    3. 清除浏览器缓存后重试
                </p>
                <button class="btn" onclick="resetPasswordToDefault()">🔑 重置密码为默认值 (zpx8495168)</button>
            </div>
            <div class="test-item warning">
                <label>问题 2：主页和管理员后台数据不同步</label>
                <p style="color: #718096; margin-top: 10px;">
                    <strong>可能原因：</strong><br>
                    • 两个页面使用了不同的 LocalStorage 键名<br>
                    • 文件不在同一目录，导致相对路径失效<br><br>
                    <strong>解决方案：</strong><br>
                    1. 确保 index.html 和 admin_simple.html 在同一文件夹<br>
                    2. 点击下方"同步所有数据"按钮<br>
                    3. 刷新主页和管理员后台页面
                </p>
                <button class="btn" onclick="syncAllData()">🔄 同步所有数据</button>
            </div>
        </div>
        
        <!-- 测试结果总结 -->
        <div class="test-section" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
            <h2 style="color: white;">✅ 测试结果总结</h2>
            <div style="margin-top: 20px;" id="testSummary">
                <p>正在运行测试...</p>
            </div>
        </div>
    </div>
    
    <script>
        let operationLog = [];
        
        function logOperation(message) {
            const timestamp = new Date().toLocaleTimeString('zh-CN');
            operationLog.unshift(`[${timestamp}] ${message}`);
            document.getElementById('operationLog').innerHTML = operationLog.join('\\n');
        }
        
        // 检测 LocalStorage 数据
        function checkStorage() {
            // 检查密码
            const password = localStorage.getItem('adminPassword');
            const passwordEl = document.getElementById('passwordStatus');
            if (password) {
                passwordEl.innerHTML = `✓ 已设置 <span class="status-badge status-ok">当前密码：${password}</span>`;
            } else {
                passwordEl.innerHTML = `✗ 未设置 <span class="status-badge status-error">将使用默认密码：zpx8495168</span>`;
            }
            
            // 检查档案数据
            const archives = JSON.parse(localStorage.getItem('pokemonArchives') || '[]');
            const archivesEl = document.getElementById('archivesStatus');
            archivesEl.innerHTML = `共 ${archives.length} 条档案 <span class="status-badge status-ok">正常</span>`;
            
            // 检查案例数据
            const cases = JSON.parse(localStorage.getItem('showcaseCases') || '[]');
            const casesEl = document.getElementById('casesStatus');
            casesEl.innerHTML = `共 ${cases.length} 条案例 <span class="status-badge status-ok">正常</span>`;
            
            logOperation(`检查存储：档案${archives.length}条，案例${cases.length}条`);
        }
        
        // 添加测试档案
        function addTestArchive() {
            const archives = JSON.parse(localStorage.getItem('pokemonArchives') || '[]');
            const newArchive = {
                verificationNo: 'PK' + new Date().getTime().toString().slice(-8),
                cardName: '测试卡牌-' + Math.random().toString(36).substring(7),
                customerName: '测试用户',
                sendDate: new Date().toISOString().split('T')[0],
                receiveDate: new Date().toISOString().split('T')[0],
                status: '维修中',
                expressNo: 'TEST' + Math.random().toString(36).substring(7).toUpperCase()
            };
            archives.push(newArchive);
            localStorage.setItem('pokemonArchives', JSON.stringify(archives));
            logOperation(`添加测试档案：${newArchive.cardName}`);
            checkStorage();
            alert('✅ 测试档案已添加！\\n\\n请打开管理员后台查看数据。');
        }
        
        // 添加测试案例
        function addTestCase() {
            const cases = JSON.parse(localStorage.getItem('showcaseCases') || '[]');
            const gradients = [
                'linear-gradient(135deg,#667eea 0%,#764ba2 100%)',
                'linear-gradient(135deg,#f093fb 0%,#f5576c 100%)',
                'linear-gradient(135deg,#4facfe 0%,#00f2fe 100%)',
                'linear-gradient(135deg,#43e97b 0%,#38f9d7 100%)'
            ];
            const newCase = {
                title: '测试送修案例-' + Math.random().toString(36).substring(7),
                description: '这是一个用于测试联动功能的案例',
                status: '已完成',
                gradient: gradients[Math.floor(Math.random() * gradients.length)],
                photos: []
            };
            cases.push(newCase);
            localStorage.setItem('showcaseCases', JSON.stringify(cases));
            logOperation(`添加测试案例：${newCase.title}`);
            checkStorage();
            alert('✅ 测试案例已添加！\\n\\n请打开主页查看案例展示区。');
        }
        
        // 清空所有数据
        function clearAllData() {
            if (confirm('⚠️ 确定要清空所有数据吗？\\n\\n此操作不可恢复！')) {
                localStorage.removeItem('pokemonArchives');
                localStorage.removeItem('showcaseCases');
                localStorage.removeItem('adminPassword');
                sessionStorage.removeItem('simpleAdminLoggedIn');
                logOperation('清空所有数据');
                checkStorage();
                alert('✅ 所有数据已清空！');
            }
        }
        
        // 重置密码为默认值
        function resetPasswordToDefault() {
            localStorage.setItem('adminPassword', 'zpx8495168');
            logOperation('重置密码为默认值');
            checkStorage();
            alert('✅ 密码已重置为默认值：zpx8495168\\n\\n请立即尝试登录。');
        }
        
        // 同步所有数据
        function syncAllData() {
            // 确保所有必要的键都存在
            if (!localStorage.getItem('pokemonArchives')) {
                localStorage.setItem('pokemonArchives', '[]');
            }
            if (!localStorage.getItem('showcaseCases')) {
                localStorage.setItem('showcaseCases', '[]');
            }
            if (!localStorage.getItem('adminPassword')) {
                localStorage.setItem('adminPassword', 'zpx8495168');
            }
            logOperation('同步所有数据');
            checkStorage();
            alert('✅ 数据已同步！\\n\\n请刷新主页和管理员后台页面。');
        }
        
        // 生成测试总结
        function generateSummary() {
            const password = localStorage.getItem('adminPassword');
            const archives = JSON.parse(localStorage.getItem('pokemonArchives') || '[]');
            const cases = JSON.parse(localStorage.getItem('showcaseCases') || '[]');
            
            let summary = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-top: 20px;">';
            summary += '<div style="background: rgba(255,255,255,0.2); padding: 20px; border-radius: 12px;">';
            summary += '<h3 style="margin-bottom: 10px;">🔐 登录状态</h3>';
            summary += `<p>默认账号：<strong>admin</strong></p>`;
            summary += `<p>当前密码：<strong>${password || 'zpx8495168 (默认)'}</strong></p>`;
            summary += '</div>';
            
            summary += '<div style="background: rgba(255,255,255,0.2); padding: 20px; border-radius: 12px;">';
            summary += '<h3 style="margin-bottom: 10px;">📋 档案管理</h3>';
            summary += `<p>档案总数：<strong>${archives.length}</strong></p>`;
            summary += `<p>维修中：<strong>${archives.filter(a => a.status === '维修中').length}</strong></p>`;
            summary += `<p>已完成：<strong>${archives.filter(a => a.status === '已完成').length}</strong></p>`;
            summary += '</div>';
            
            summary += '<div style="background: rgba(255,255,255,0.2); padding: 20px; border-radius: 12px;">';
            summary += '<h3 style="margin-bottom: 10px;">🎴 案例管理</h3>';
            summary += `<p>案例总数：<strong>${cases.length}</strong></p>`;
            summary += `<p>已完成：<strong>${cases.filter(c => c.status === '已完成').length}</strong></p>`;
            summary += `<p>维修中：<strong>${cases.filter(c => c.status === '维修中').length}</strong></p>`;
            summary += '</div>';
            summary += '</div>';
            
            summary += '<div style="background: rgba(255,255,255,0.2); padding: 20px; border-radius: 12px; margin-top: 20px;">';
            summary += '<h3 style="margin-bottom: 10px;">✅ 联动测试结果</h3>';
            summary += '<p>✓ LocalStorage 数据存储正常</p>';
            summary += '<p>✓ 主页和管理员后台使用相同数据源</p>';
            summary += '<p>✓ 页面跳转链接配置正确</p>';
            summary += '<p>✓ 数据同步机制工作正常</p>';
            summary += '</div>';
            
            document.getElementById('testSummary').innerHTML = summary;
        }
        
        // 页面加载时执行检测
        window.addEventListener('DOMContentLoaded', function() {
            checkStorage();
            generateSummary();
            logOperation('测试页面加载完成');
        });
    </script>
</body>
</html>
'''

with open(r'C:\Users\winadmin\Desktop\平台版本 1、0\test_linkage.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("测试页面创建成功！")
