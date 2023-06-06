const express = require('express');
const axios = require('axios');
const app = express();
const port = 8080;
const fetch = require('node-fetch');

app.get('/api/stock-data', async (req, res) => {
  try {
    const response = await fetch('https://kr.investing.com/stock-screener/?sp=country::11|sector::a|industry::a|equityType::a%3Ceq_market_cap;1');
    const data = await response.json();
    console.log(data);
    res.send(data);
  } catch (error) {
    console.error('Error:', error);
    res.status(500).send('Internal Server Error');
  }
});