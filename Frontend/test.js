const express = require('express');
const path = require('path');

const app = express();

app.use((req, res, next) => {
    res.header("Access-Control-Allow-Origin", "http://localhost:3000"); 
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next(); 
  });

app.use('/', express.static(path.join(__dirname, 'public')));

app.listen(3000, () => {
  console.log('Server listening on port 3000');  
});