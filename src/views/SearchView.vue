<template>
  <div class="container">
    <button class="fetch-button" @click="fetchTickerData">Fetch Ticker Data</button>

    <table class="ticker-table">
      <thead>
        <tr>
          <th>이름</th>
          <th>시가 00시 기준</th>
          <th>종가 00시 기준</th>
          <th>저가 00시 기준</th>
          <th>고가 00시 기준</th>
          <th>거래량 00시 기준</th>
          <th>거래금액 00시 기준</th>
          <th>전일종가</th>
          <th>최근 24시간 거래량</th>
          <th>최근 24시간 거래금액</th>
          <th>F최근 24시간 변동가</th>
          <th>최근 24시간 변동률</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="coin in topCoins" :key="coin.symbol">
          <td>{{ coin.symbol }}</td>
          <td>{{ formatNumber(coin.opening_price) }}</td>
          <td>{{ formatNumber(coin.closing_price) }}</td>
          <td>{{ formatNumber(coin.min_price) }}</td>
          <td>{{ formatNumber(coin.max_price) }}</td>
          <td>{{ formatNumber(coin.units_traded) }}</td>
          <td>{{ formatNumber(coin.acc_trade_value) }}</td>
          <td>{{ formatNumber(coin.prev_closing_price) }}</td>
          <td>{{ formatNumber(coin.units_traded_24H) }}</td>
          <td>{{ formatNumber(coin.acc_trade_value_24H) }}</td>
          <td>{{ formatNumber(coin.fluctate_24H) }}</td>
          <td>{{ coin.fluctate_rate_24H }}%</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      tickerData: {},
      topCoins: []
    }
  },
  methods: {
    async fetchTickerData () {
      const paymentCurrency = 'KRW' // 변경 가능한 통화 코드

      try {
        const response = await axios.get(`https://api.bithumb.com/public/ticker/ALL_${paymentCurrency}`)
        this.tickerData = response.data.data

        // Get the top 10 coins based on opening price
        const coins = Object.keys(this.tickerData)
          .map(symbol => ({
            symbol,
            ...this.tickerData[symbol]
          }))
          .sort((a, b) => b.opening_price - a.opening_price)
          .slice(0, 10)

        this.topCoins = coins
      } catch (error) {
        console.error('Error:', error)
      }
    },
    formatNumber (number) {
      return Number(number).toLocaleString('en-US')
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 50px;
}

.fetch-button {
  padding: 10px 20px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  margin-bottom: 20px;
}

.ticker-table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid #ddd;
  box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.15);
}

.ticker-table th,
.ticker-table td {
  padding: 15px;
  border-bottom: 1px solid #ddd;
}

.ticker-table th {
  background-color: #4caf50;
  color: white;
  text-transform: uppercase;
}

.ticker-table tr:nth-child(even) {
  background-color: #f8f8f8;
}
</style>
