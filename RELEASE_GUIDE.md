# PyEgen Release Guide

## 📦 发布到 PyPI 的完整指南

### 前置准备

1. **安装必要工具**
   ```bash
   pip install build twine
   ```

2. **注册 PyPI 账户**
   - 访问 https://pypi.org/account/register/
   - 注册账户并验证邮箱
   - 可选：也注册 TestPyPI 账户 https://test.pypi.org/account/register/

3. **配置认证**
   创建 `~/.pypirc` 文件：
   ```ini
   [distutils]
   index-servers = 
       pypi
       testpypi

   [pypi]
   repository = https://upload.pypi.org/legacy/
   username = __token__
   password = your-api-token

   [testpypi]
   repository = https://test.pypi.org/legacy/
   username = __token__
   password = your-testpypi-api-token
   ```

### 步骤 1: 准备代码

1. **更新版本号**
   编辑 `pyegen/_version.py`:
   ```python
   __version__ = "0.1.0"  # 更新版本号
   ```

2. **运行测试**
   ```bash
   cd /Users/brycewang/Desktop/stata/pyegen
   python -m pytest tests/
   ```

3. **检查代码质量**
   ```bash
   # 格式化代码
   black pyegen/ tests/
   isort pyegen/ tests/
   
   # 检查语法
   flake8 pyegen/ tests/
   ```

### 步骤 2: 构建包

```bash
# 清理旧的构建文件
rm -rf build/ dist/ *.egg-info/

# 构建包
python -m build
```

这会在 `dist/` 目录下生成两个文件：
- `pyegen-0.1.0-py3-none-any.whl` (wheel 格式)
- `pyegen-0.1.0.tar.gz` (源码包)

### 步骤 3: 测试发布 (推荐)

先发布到 TestPyPI 进行测试：

```bash
python -m twine upload --repository testpypi dist/*
```

测试安装：
```bash
pip install --index-url https://test.pypi.org/simple/ pyegen
```

### 步骤 4: 正式发布到 PyPI

```bash
python -m twine upload dist/*
```

### 步骤 5: 验证发布

1. **检查 PyPI 页面**
   访问 https://pypi.org/project/pyegen/

2. **测试安装**
   ```bash
   pip install pyegen
   ```

3. **验证功能**
   ```python
   import pyegen as egen
   import pandas as pd
   
   df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
   result = egen.rowmean(df, ['x', 'y'])
   print(result)  # 应该输出 [2.5, 3.5, 4.5]
   ```

### 发布检查清单 ✅

- [ ] 代码通过所有测试
- [ ] 文档更新完整
- [ ] 版本号已更新
- [ ] CHANGELOG.md 已更新（如果有）
- [ ] 在 TestPyPI 测试成功
- [ ] PyPI 账户认证配置正确

### 常见问题解决

**问题 1: 包名已存在**
- 解决：选择一个唯一的包名，如 `stata-egen` 或 `pyegen-tools`

**问题 2: 认证失败**
- 解决：检查 `.pypirc` 配置，确认 API token 正确

**问题 3: 上传失败**
- 解决：检查网络连接，确认包格式正确

### 后续维护

1. **设置 GitHub Actions** (可选)
   自动化测试和发布流程

2. **创建文档网站** (可选)
   使用 MkDocs 或 Sphinx

3. **收集用户反馈**
   通过 GitHub Issues 和社区反馈

### 版本管理建议

- **0.1.0**: 初始发布
- **0.1.x**: Bug 修复
- **0.x.0**: 新功能
- **x.0.0**: 重大更改

恭喜！🎉 你的 PyEgen 包即将为开源社区做出贡献！
