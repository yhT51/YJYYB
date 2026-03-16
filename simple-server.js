const http = require('http');

const server = http.createServer((req, res) => {
  console.log(`[${new Date().toLocaleTimeString()}] ${req.method} ${req.url}`);

  if (req.url === '/api/tasks') {
    if (req.method === 'GET') {
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ message: 'GET成功', tasks: [] }));
      console.log('✅ GET 请求处理成功');
    } else if (req.method === 'POST') {
      let body = '';
      req.on('data', chunk => { body += chunk.toString(); });
      req.on('end', () => {
        console.log('📤 收到 POST 数据:', body);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ message: 'POST成功', data: body }));
        console.log('✅ POST 请求处理成功');
      });
    } else {
      res.writeHead(405, { 'Content-Type': 'text/plain' });
      res.end('Method Not Allowed');
      console.log('❌ 方法不支持');
    }
  } else {
    res.writeHead(404, { 'Content-Type': 'text/html' });
    res.end('<h1>404 Not Found</h1><p>请访问 /api/tasks</p>');
    console.log('❌ 404 Not Found');
  }
});

const PORT = 8080;
server.listen(PORT, '0.0.0.0', () => {
  console.log('\n========================================');
  console.log('🚀 简易服务器已启动！');
  console.log(`📡 本地访问: http://localhost:${PORT}`);
  console.log(`🌐 局域网访问: http://192.168.1.53:${PORT}`);
  console.log('========================================\n');
});
