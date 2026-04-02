# -*- coding: utf-8 -*-
"""
完成照片裁剪功能的最后修复 - 修改 handleCasePhotoSelect 函数
"""

import re

# 读取文件
with open(r'C:\Users\winadmin\Desktop\平台版本 1、0\admin_simple.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 查找并替换 handleCasePhotoSelect 函数
old_function = '''        async function handleCasePhotoSelect(event) {
            const files = event.target.files;
            for (let i = 0; i < files.length; i++) {
                const file = files[i];
                if (file.size > 300 * 1024 * 1024) {
                    alert(`${file.name} 超过 300MB，已跳过`);
                    continue;
                }
                try {
                    const compressed = await compressImage(file, document.getElementById('enableCaseCrop16_9')?.checked || false);
                    casePhotos.push(compressed);
                    renderCasePhotoPreview();
                } catch (err) {
                    alert(`${file.name} 处理失败：${err.message}`);
                }
            }
            event.target.value = '';
        }'''

new_function = '''        async function handleCasePhotoSelect(event) {
            const file = event.target.files[0];
            if (!file) return;
            
            if (file.size > 300 * 1024 * 1024) {
                alert(`${file.name} 超过 300MB，无法上传`);
                event.target.value = '';
                return;
            }
            
            // 打开裁剪器
            currentCropTarget = 'case';
            openCropModal(file);
            event.target.value = '';
        }'''

if old_function in content:
    content = content.replace(old_function, new_function)
    print("✓ 成功修改 handleCasePhotoSelect 函数")
else:
    print("✗ 未找到要替换的函数，尝试另一种格式...")
    # 尝试更宽松的匹配
    pattern = r'async function handleCasePhotoSelect\(event\) \{[^}]*\}'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        print(f"找到函数：{match.group()[:100]}...")
    else:
        print("✗ 仍未找到函数")

# 写回文件
with open(r'C:\Users\winadmin\Desktop\平台版本 1、0\admin_simple.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n完成！admin_simple.html 已更新。")
print("\n现在所有照片上传模块都支持可视化 16:9 裁剪框功能：")
print("1. 卡牌档案损伤照片上传 ✓")
print("2. 送修案例照片上传 ✓")
print("\n使用方法：")
print("- 点击上传区域选择照片")
print("- 在弹出的裁剪器中拖动/缩放照片")
print("- 调整到满意的构图后点击'✓ 确认裁剪'")
print("- 照片将自动保存为 16:9 比例")
