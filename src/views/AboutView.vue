<template>
  <div class="container">
<<<<<<< HEAD
    <div class="chart-section">
      <canvas ref="chartCanvas"></canvas>
    </div>
    <div class="content-section">
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
  </div>
</template>

<script>
import axios from 'axios'
import { Chart, registerables } from 'chart.js'

Chart.register(...registerables)
=======
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
            <th>주식 갯수</th>
            <th>주식거래량</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(stock, index) in stocks" :key="index">
            <td>{{ stock.basDt }}</td>
            <td>{{ stock.itmsNm }}</td>
            <td>{{ formatQuantity(stock.trqu) }} 개</td>
            <td>{{ formatPrice(stock.trPrc) }} 원</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
>>>>>>> d52ebe3d423373a3d85bbdd7eee69a2a7be68d05

export default {
  data () {
    return {
      stockName: '',
<<<<<<< HEAD
      stocks: [],
      chartInstance: null
=======
      stocks: []
>>>>>>> d52ebe3d423373a3d85bbdd7eee69a2a7be68d05
    }
  },
  methods: {
    async fetchStockData () {
      const SERVICE_KEY = 'sPflHfYN%2B8hDbVPVQ1Tzan%2BDdcLML3zuUddb2dfQ8LSZ%2F7w8YaM5fvHp69XKA6djtQVDvhj8NKn6KgsdvMzaTg%3D%3D'
<<<<<<< HEAD
      const url = `https://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo?serviceKey=${SERVICE_KEY}&numOfRows=100&pageNo=1`
=======
      const url = `https://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getPreemptiveRightCertificatePriceInfo?serviceKey=${SERVICE_KEY}&numOfRows=100&pageNo=1`
>>>>>>> d52ebe3d423373a3d85bbdd7eee69a2a7be68d05

      try {
        const { data } = await axios.get(url)
        const parser = new window.DOMParser()
        const xmlDoc = parser.parseFromString(data, 'text/xml')
        const items = xmlDoc.querySelectorAll('item')
        this.stocks = Array.from(items).map(item => {
          const itmsNm = item.querySelector('itmsNm').textContent
          if (this.stockName === '' || itmsNm.includes(this.stockName)) {
            return {
<<<<<<< HEAD
              srtnCd: item.querySelector('srtnCd').textContent,
              itmsNm: itmsNm,
              trqu: Number(item.querySelector('trqu').textContent),
              trPrc: Number(item.querySelector('trPrc').textContent),
              hipr: Number(item.querySelector('hipr').textContent),
              lopr: Number(item.querySelector('lopr').textContent)
=======
              basDt: item.querySelector('basDt').textContent,
              itmsNm: itmsNm,
              trqu: item.querySelector('trqu').textContent,
              trPrc: item.querySelector('trPrc').textContent
>>>>>>> d52ebe3d423373a3d85bbdd7eee69a2a7be68d05
            }
          }
          return null
        }).filter(Boolean)
<<<<<<< HEAD

        this.renderChart()
=======
>>>>>>> d52ebe3d423373a3d85bbdd7eee69a2a7be68d05
      } catch (error) {
        console.error('Error:', error)
      }
    },
<<<<<<< HEAD
    renderChart () {
      if (this.chartInstance) {
        this.chartInstance.destroy()
      }

      const chartData = {
        labels: this.stocks.map(stock => stock.itmsNm),
        datasets: [
          {
            label: '거래량',
            backgroundColor: '#f87979',
            data: this.stocks.map(stock => stock.trqu)
          },
          {
            label: '거래대금',
            backgroundColor: '#79f879',
            data: this.stocks.map(stock => stock.trPrc)
          }
        ]
      }

      const ctx = this.$refs.chartCanvas.getContext('2d')
      this.chartInstance = new Chart(ctx, {
        type: 'bar',
        data: chartData,
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: {
              type: 'category',
              beginAtZero: true
            },
            y: {
              type: 'linear',
              beginAtZero: true,
              ticks: {
                callback: value => {
                  if (value >= 100000000) {
                    return `${(value / 100000000).toFixed(1)}억`
                  } else {
                    return `${(value / 10000).toFixed(0)}만`
                  }
                }
              }
            }
          },
          plugins: {
            title: {
              display: true,
              text: '주식 거래량 및 거래대금',
              font: {
                size: 16
              }
            },
            tooltip: {
              mode: 'index',
              intersect: false
            }
          }
        }
      })
    },
    formatPrice (price) {
      return new Intl.NumberFormat('ko-KR').format(price) + ' 원'
    },
    formatQuantity (quantity) {
      return new Intl.NumberFormat('ko-KR').format(quantity) + ' 개'
=======
    formatPrice (price) {
      return new Intl.NumberFormat('ko-KR').format(price)
    },
    formatQuantity (quantity) {
      return new Intl.NumberFormat('ko-KR').format(quantity)
>>>>>>> d52ebe3d423373a3d85bbdd7eee69a2a7be68d05
    }
  },
  mounted () {
    this.fetchStockData()
  }
}
</script>

<style scoped>
<<<<<<< HEAD
body,
html {
  width: 100%;
=======
body, html {
>>>>>>> d52ebe3d423373a3d85bbdd7eee69a2a7be68d05
  height: 100%;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0;
  background: #f2f2f2;
}

.container {
<<<<<<< HEAD
  width: 100%;
  max-width: 1200px;
=======
  width: 800px;
>>>>>>> d52ebe3d423373a3d85bbdd7eee69a2a7be68d05
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background: white;
  border-radius: 5px;
}

<<<<<<< HEAD
.chart-section {
  margin-bottom: 20px;
}

.content-section {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.search-section {
  width: 100%;
  display: flex;
  justify-content: space-between;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.search-input {
  flex: 1;
=======
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
>>>>>>> d52ebe3d423373a3d85bbdd7eee69a2a7be68d05
  padding: 10px;
  border-radius: 4px;
  border: 1px solid #ccc;
  font-size: 1rem;
}

.search-button {
<<<<<<< HEAD
  padding: 10px;
  margin-left: 5px;
=======
  width: 10%;
  padding: 10px;
  margin-left: 5%;
>>>>>>> d52ebe3d423373a3d85bbdd7eee69a2a7be68d05
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
}

.table-section {
<<<<<<< HEAD
  width: 100%;
  margin-top: 20px;
=======
  margin-top: 60px;
>>>>>>> d52ebe3d423373a3d85bbdd7eee69a2a7be68d05
}

#stock-table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid #ddd;
<<<<<<< HEAD
  box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
}

#stock-table th,
#stock-table td {
=======
  box-shadow: 0px 0px 20px 0px rgba(0,0,0,0.15);
}

#stock-table th, #stock-table td {
>>>>>>> d52ebe3d423373a3d85bbdd7eee69a2a7be68d05
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
