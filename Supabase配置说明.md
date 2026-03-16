# Supabase 数据库配置说明

## 您的 Supabase 项目信息

- **Project URL**: `https://pxvamxoztnwmrhsaagfg.supabase.co`
- **已自动配置**: ✅ 是，任务看板已自动填入您的 API 密钥

## 下一步操作

### 方法一：通过 SQL Editor 创建表（推荐）

1. 打开浏览器访问：https://supabase.com/dashboard/project/pxvamxoztnwmrhsaagfg/sql
2. 点击 "New Query"
3. 复制 `create_table.sql` 文件中的所有内容
4. 粘贴到 SQL Editor 中
5. 点击 "RUN" 执行
6. 等待显示 "Success" 即可

### 方法二：通过 Table Editor 创建表

1. 打开浏览器访问：https://supabase.com/dashboard/project/pxvamxoztnwmrhsaagfg/editor
2. 点击 "New table"
3. 输入表名：`tasks`
4. 添加以下列：
   - `id` (int8, Primary Key, Auto increment)
   - `title` (text)
   - `date` (text)
   - `time` (text)
   - `priority` (text, 默认值: 'medium')
   - `done` (boolean, 默认值: false)
   - `created_at` (timestamptz, 默认值: now())
5. 点击 "Save" 创建表
6. 点击左侧菜单 "Authentication" → "Policies"
7. 找到 `tasks` 表，点击 "New Policy"
8. 选择 "Get started quickly"
9. 选择 "Enable read access to everyone"
10. 点击 "Use this template"
11. 重复步骤 7-10，分别为以下操作创建策略：
    - Enable insert access for everyone
    - Enable update access for everyone
    - Enable delete access for everyone

## 完成后

1. 刷新任务看板页面
2. 现在可以正常使用所有功能了！

## 验证是否成功

打开任务看板后，尝试添加一个任务：
- ✅ 如果成功添加：配置正确
- ❌ 如果提示错误：请检查 SQL 是否执行成功

## 常见问题

### Q: 添加任务时提示 "relation does not exist"
**A:** 说明表没有创建成功，请重新执行 SQL 脚本

### Q: 添加任务时提示 "new row violates row-level security policy"
**A:** 说明 RLS 策略没有正确设置，请检查 Policies 配置

### Q: 如何查看数据库中的数据？
**A:** 访问 Table Editor：https://supabase.com/dashboard/project/pxvamxoztnwmrhsaagfg/editor

## 数据库备份

您的数据自动保存在 Supabase 云数据库中，无需手动备份。
如需导出数据，可访问：https://supabase.com/dashboard/project/pxvamxoztnwmrhsaagfg/database/exports
