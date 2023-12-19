// const express = require('express');
// const path = require('path');

// const app = express();

// app.use((req, res, next) => {
//     res.header("Access-Control-Allow-Origin", "http://localhost:3000"); 
//     res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
//     next(); 
//   });

// app.use('/', express.static(path.join(__dirname, 'public')));

// app.listen(3000, () => {
//   console.log('Server listening on port 3000');  
// });

const express = require('express');
const path = require('path');

const app = express();

app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "http://localhost:3000");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.use(express.static(path.join(__dirname, 'public'), () => {
  console.log('Serving static file');
}));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.get('/add', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'add.html'));  
});

app.listen(3000, () => {
  console.log('Server listening on port 3000');  
});