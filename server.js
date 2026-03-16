const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = 8080;
const DATA_FILE = path.join(__dirname, 'tasks.json');

// 中间件
app.use(express.json());
app.use(express.static(__dirname));

// 读取任务数据
function loadTasks() {
  try {
    console.log(`📂 尝试读取文件: ${DATA_FILE}`);
    if (fs.existsSync(DATA_FILE)) {
      console.log(`✅ 文件存在，正在读取...`);
      const data = fs.readFileSync(DATA_FILE, 'utf8');
      console.log(`📊 文件大小: ${data.length} 字符`);
      const tasks = JSON.parse(data);
      console.log(`✅ 读取成功: ${tasks.length} 条任务`);
      return tasks;
    } else {
      console.log(`⚠️ 文件不存在，返回空数组`);
      return [];
    }
  } catch (error) {
    console.error('❌ 读取任务数据失败:', error);
    console.error('错误堆栈:', error.stack);
    return [];
  }
}

// 保存任务数据
function saveTasks(tasks) {
  try {
    console.log(`💾 尝试保存到文件: ${DATA_FILE}`);
    console.log(`📊 任务数量: ${tasks.length}`);
    fs.writeFileSync(DATA_FILE, JSON.stringify(tasks, null, 2));
    console.log(`✅ 文件保存成功`);
    return true;
  } catch (error) {
    console.error('❌ 保存任务数据失败:', error);
    console.error('错误堆栈:', error.stack);
    return false;
  }
}

// API路由
app.get('/api/tasks', (req, res) => {
  const tasks = loadTasks();
  console.log(`📥 读取任务: ${tasks.length} 条`);
  res.json(tasks);
});

app.post('/api/tasks', (req, res) => {
  const tasks = req.body;
  console.log(`📤 保存任务: ${tasks.length} 条`);
  if (saveTasks(tasks)) {
    console.log('✅ 保存成功');
    res.json({ success: true, tasks });
  } else {
    console.log('❌ 保存失败');
    res.status(500).json({ success: false, error: '保存失败' });
  }
});

// 启动服务器
app.listen(PORT, '0.0.0.0', () => {
  console.log(`\n🚀 服务器已启动！`);
  console.log(`📡 本地访问: http://localhost:${PORT}`);
  console.log(`🌐 局域网访问: http://192.168.1.53:${PORT}`);
  console.log(`\n按 Ctrl+C 停止服务器\n`);
});
