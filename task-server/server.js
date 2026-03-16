const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

const PORT = 3030;
const DATA_FILE = path.join(__dirname, 'tasks.json');

// 初始化数据文件
if (!fs.existsSync(DATA_FILE)) {
  fs.writeFileSync(DATA_FILE, JSON.stringify({ tasks: [], requests: [] }, null, 2));
}

function readData() {
  return JSON.parse(fs.readFileSync(DATA_FILE, 'utf8'));
}

function writeData(data) {
  fs.writeFileSync(DATA_FILE, JSON.stringify(data, null, 2));
}

const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);
  const pathname = parsedUrl.pathname;

  // CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(200);
    res.end();
    return;
  }

  // 静态文件
  if (req.method === 'GET' && (pathname === '/' || pathname === '/index.html')) {
    const filePath = path.join(__dirname, 'index.html');
    fs.readFile(filePath, (err, data) => {
      if (err) { res.writeHead(404); res.end('Not found'); return; }
      res.setHeader('Content-Type', 'text/html; charset=utf-8');
      res.writeHead(200);
      res.end(data);
    });
    return;
  }

  if (req.method === 'GET' && pathname === '/colleague.html') {
    const filePath = path.join(__dirname, 'colleague.html');
    fs.readFile(filePath, (err, data) => {
      if (err) { res.writeHead(404); res.end('Not found'); return; }
      res.setHeader('Content-Type', 'text/html; charset=utf-8');
      res.writeHead(200);
      res.end(data);
    });
    return;
  }

  // API: 获取所有任务
  if (req.method === 'GET' && pathname === '/api/tasks') {
    const data = readData();
    res.setHeader('Content-Type', 'application/json; charset=utf-8');
    res.writeHead(200);
    res.end(JSON.stringify(data.tasks));
    return;
  }

  // API: 添加任务（老板用）
  if (req.method === 'POST' && pathname === '/api/tasks') {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', () => {
      const task = JSON.parse(body);
      const data = readData();
      task.id = Date.now().toString();
      task.createdAt = new Date().toISOString();
      task.status = task.status || 'pending';
      task.source = task.source || 'self';
      data.tasks.push(task);
      writeData(data);
      res.setHeader('Content-Type', 'application/json; charset=utf-8');
      res.writeHead(200);
      res.end(JSON.stringify({ success: true, task }));
    });
    return;
  }

  // API: 更新任务状态
  if (req.method === 'PUT' && pathname.startsWith('/api/tasks/')) {
    const taskId = pathname.split('/')[3];
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', () => {
      const updates = JSON.parse(body);
      const data = readData();
      const idx = data.tasks.findIndex(t => t.id === taskId);
      if (idx !== -1) {
        data.tasks[idx] = { ...data.tasks[idx], ...updates };
        writeData(data);
        res.setHeader('Content-Type', 'application/json; charset=utf-8');
        res.writeHead(200);
        res.end(JSON.stringify({ success: true }));
      } else {
        res.writeHead(404);
        res.end(JSON.stringify({ error: 'Task not found' }));
      }
    });
    return;
  }

  // API: 删除任务
  if (req.method === 'DELETE' && pathname.startsWith('/api/tasks/')) {
    const taskId = pathname.split('/')[3];
    const data = readData();
    data.tasks = data.tasks.filter(t => t.id !== taskId);
    writeData(data);
    res.setHeader('Content-Type', 'application/json; charset=utf-8');
    res.writeHead(200);
    res.end(JSON.stringify({ success: true }));
    return;
  }

  // API: 同事提交任务请求
  if (req.method === 'POST' && pathname === '/api/requests') {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', () => {
      const request = JSON.parse(body);
      const data = readData();
      request.id = Date.now().toString();
      request.createdAt = new Date().toISOString();
      request.status = 'pending';
      // 直接加入任务列表，来源标记为colleague
      const task = {
        id: request.id,
        title: request.title,
        description: request.description || '',
        priority: request.priority || 'medium',
        date: request.date || new Date().toISOString().split('T')[0],
        status: 'pending',
        source: 'colleague',
        fromName: request.fromName || '同事',
        createdAt: request.createdAt
      };
      data.tasks.push(task);
      writeData(data);
      res.setHeader('Content-Type', 'application/json; charset=utf-8');
      res.writeHead(200);
      res.end(JSON.stringify({ success: true }));
    });
    return;
  }

  res.writeHead(404);
  res.end('Not found');
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`\n✅ 任务看板服务已启动！`);
  console.log(`\n📱 本机访问：http://localhost:${PORT}`);
  console.log(`\n🌐 同事访问：http://192.168.1.53:${PORT}/colleague.html`);
  console.log(`\n按 Ctrl+C 停止服务\n`);
});
