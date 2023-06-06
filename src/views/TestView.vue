<template>
  <div class="container">
    <div class="search-section">
      <input type="text" v-model="stockName" placeholder="Enter stock name..." class="search-input">
      <button @click="fetchStockData" class="search-button">Search</button>
    </div>
    <div class="table-section">
      <table id="stock-table">
        <thead>
          <tr>
            <th>주식코드</th>
            <th>주식이름</th>
            <th>거래량</th>
            <th>거래대금</th>
            <th>고가</th>
            <th>저가</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(stock, index) in stocks" :key="index">
            <td>{{ stock.srtnCd }}</td>
            <td>{{ stock.itmsNm }}</td>
            <td>{{ formatQuantity(stock.trqu) }}</td>
            <td>{{ formatPrice(stock.trPrc) }}</td>
            <td>{{ formatPrice(stock.hipr) }}</td>
            <td>{{ formatPrice(stock.lopr) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      stockName: '',
      stocks: []
    }
  },
  methods: {
    async fetchStockData () {
      const SERVICE_KEY = 'sPflHfYN%2B8hDbVPVQ1Tzan%2BDdcLML3zuUddb2dfQ8LSZ%2F7w8YaM5fvHp69XKA6djtQVDvhj8NKn6KgsdvMzaTg%3D%3D'
      const url = `https://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo?serviceKey=${SERVICE_KEY}&numOfRows=100&pageNo=1`

      try {
        const { data } = await axios.get(url)
        const parser = new window.DOMParser()
        const xmlDoc = parser.parseFromString(data, 'text/xml')
        const items = xmlDoc.querySelectorAll('item')
        this.stocks = Array.from(items).map(item => {
          const itmsNm = item.querySelector('itmsNm').textContent
          if (this.stockName === '' || itmsNm.includes(this.stockName)) {
            return {
              srtnCd: item.querySelector('srtnCd').textContent,
              itmsNm: itmsNm,
              trqu: item.querySelector('trqu').textContent,
              trPrc: item.querySelector('trPrc').textContent,
              hipr: item.querySelector('hipr').textContent,
              lopr: item.querySelector('lopr').textContent
            }
          }
          return null
        }).filter(Boolean)
      } catch (error) {
        console.error('Error:', error)
      }
    },
    formatPrice (price) {
      return new Intl.NumberFormat('ko-KR').format(price) + ' 원'
    },
    formatQuantity (quantity) {
      return new Intl.NumberFormat('ko-KR').format(quantity) + ' 개'
    }
  },
  mounted () {
    this.fetchStockData()
  }
}
</script>

<style scoped>
body, html {
  height: 100%;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0;
  background: #f2f2f2;
}

.container {
  width: 800px;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background: white;
  border-radius: 5px;
}

.search-section {
  position: fixed;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  background: white;
  padding: 10px;
  width: 800px;
  display: flex;
  justify-content: space-between;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  z-index: 10;
}

.search-input {
  width: 85%;
  padding: 10px;
  border-radius: 4px;
  border: 1px solid #ccc;
  font-size: 1rem;
}

.search-button {
  width: 10%;
  padding: 10px;
  margin-left: 5%;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
}

.table-section {
  margin-top: 60px;
}

#stock-table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid #ddd;
  box-shadow: 0px 0px 20px 0px rgba(0,0,0,0.15);
}

#stock-table th, #stock-table td {
  padding: 15px;
  border-bottom: 1px solid #ddd;
}

#stock-table th {
  background-color: #4caf50;
  color: white;
  text-transform: uppercase;
}

#stock-table tr:nth-child(even) {
  background-color: #f8f8f8;
}
</style>
