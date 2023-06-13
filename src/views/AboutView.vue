<template>
  <div class="container">
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

export default {
  data () {
    return {
      stockName: '',
      stocks: [],
      chartInstance: null
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
              trqu: Number(item.querySelector('trqu').textContent),
              trPrc: Number(item.querySelector('trPrc').textContent),
              hipr: Number(item.querySelector('hipr').textContent),
              lopr: Number(item.querySelector('lopr').textContent)
            }
          }
          return null
        }).filter(Boolean)

        this.renderChart()
      } catch (error) {
        console.error('Error:', error)
      }
    },
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
              type: 'logarithmic',
              beginAtZero: true,
              ticks: {
                callback: value => {
                  if (value >= 100000000) {
                    return `${(value / 100000000).toFixed(1)}억`
                  } else if (value >= 10000) {
                    return `${(value / 10000).toFixed(0)}만`
                  } else {
                    return value.toFixed(0)
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
    }
  },
  mounted () {
    this.fetchStockData()
  }
}
</script>

<style scoped>
body,
html {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  background: #f2f2f2;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container {
  max-width: 1800px;
  margin-left:300px;
  width: 100%;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background: white;
  border-radius: 5px;
}

.content-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
}

.chart-section {
  margin-bottom: 20px;
  margin-left: 300px;
}

.search-section {
  width: 30%;
  display: flex;
  justify-content: space-between;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
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
  margin-left: 5px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
}

.table-section {
  width: 70%;
  margin-top: 30px;
}

#stock-table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid #ddd;
  box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
}

#stock-table th,
#stock-table td {
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
