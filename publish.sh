#!/bin/bash

# PyEgen 快速发布脚本
# 使用方法: ./publish.sh

set -e  # 遇到错误立即退出

echo "🚀 PyEgen 发布脚本启动..."

# 检查是否在正确目录
if [ ! -f "pyproject.toml" ]; then
    echo "❌ 错误: 请在 pyegen 项目根目录下运行此脚本"
    exit 1
fi

# 激活虚拟环境
echo "📦 激活虚拟环境..."
source venv/bin/activate

# 清理旧构建
echo "🧹 清理旧构建文件..."
rm -rf dist/ build/ *.egg-info/

# 运行测试（如果存在）
echo "🧪 运行测试..."
if command -v pytest &> /dev/null; then
    python3 -m pytest tests/ -v || {
        echo "❌ 测试失败，请修复后重试"
        exit 1
    }
else
    echo "⚠️  pytest 未安装，跳过测试"
fi

# 构建包
echo "🔨 构建包..."
python3 -m build

# 检查包
echo "🔍 检查包完整性..."
python3 -m twine check dist/*

# 询问是否发布
echo ""
echo "📋 构建完成! 生成的文件:"
ls -la dist/
echo ""

read -p "🤔 是否现在发布到 PyPI? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🚀 发布到 PyPI..."
    python3 -m twine upload dist/*
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "🎉 发布成功!"
        echo "📦 包地址: https://pypi.org/project/pyegen/"
        echo "💾 安装命令: pip install pyegen"
        echo ""
        echo "📢 别忘了:"
        echo "  1. 在社区分享你的项目"
        echo "  2. 请朋友们给项目加星 ⭐"
        echo "  3. 收集用户反馈"
    else
        echo "❌ 发布失败，请检查认证配置"
        exit 1
    fi
else
    echo "📁 包已构建在 dist/ 目录，可以稍后手动发布"
    echo "发布命令: python3 -m twine upload dist/*"
fi

echo ""
echo "✅ 脚本执行完成!"
