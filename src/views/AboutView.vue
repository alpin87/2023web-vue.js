<template>
  <div>

    <div id="search-bar">
      <input type="text" v-model="stockName" placeholder="Enter stock name...">
      <button @click="fetchStockData">Search</button>
    </div>
    <table id="stock-table">
      <thead>
        <tr>
          <th>Base Date</th>
          <th>Item Name</th>
          <th>Trading Quantity</th>
          <th>Trading Price</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(stock, index) in stocks" :key="index">
          <td>{{ stock.basDt }}</td>
          <td>{{ stock.itmsNm }}</td>
          <td>{{ stock.trqu }}</td>
          <td>{{ stock.trPrc }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import superagent from 'superagent'

export default {
  data () {
    return {
      stockName: '',
      stocks: []
    }
  },
  methods: {
    fetchStockData () {
      const SERVICE_KEY = 'sPflHfYN%2B8hDbVPVQ1Tzan%2BDdcLML3zuUddb2dfQ8LSZ%2F7w8YaM5fvHp69XKA6djtQVDvhj8NKn6KgsdvMzaTg%3D%3D'
      const url = `https://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getPreemptiveRightCertificatePriceInfo?serviceKey=${SERVICE_KEY}&numOfRows=100&pageNo=1`

      superagent
        .get(url)
        .end((err, res) => {
          if (err) {
            console.error('Error:', err)
          } else {
            const data = new window.DOMParser().parseFromString(res.text, 'text/xml')
            const items = data.querySelectorAll('item')
            this.stocks = Array.from(items).map(item => {
              const itmsNm = item.querySelector('itmsNm').textContent
              if (this.stockName === '' || itmsNm.includes(this.stockName)) {
                return {
                  basDt: item.querySelector('basDt').textContent,
                  itmsNm: itmsNm,
                  trqu: item.querySelector('trqu').textContent,
                  trPrc: item.querySelector('trPrc').textContent
                }
              }
              return null
            }).filter(Boolean)
          }
        })
    }
  },
  mounted () {
    this.fetchStockData()
  }
}
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
}

#search-bar {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.search-input {
  flex: 1;
  padding: 10px;
  border-radius: 4px;
  border: 1px solid #ccc;
  font-size: 1rem;
}

.search-button {
  padding: 10px;
  margin-left: 15px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
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
