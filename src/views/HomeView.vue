<template>
  <div class="container">
     <div class="crypto-exchanges exchanges-container">
      <h2>암호화폐 거래소</h2>
      <div class="exchange-box" v-for="exchange in cryptoExchanges" :key="exchange.name">
        <a :href="exchange.url" target="_blank">{{ exchange.name }}</a>
        <p>{{ exchange.description }}</p>
      </div>
    </div>
    <div class="stock-exchanges exchanges-container">
      <h2>주식 거래소</h2>
      <div class="exchange-box" v-for="exchange in stockExchanges" :key="exchange.name">
        <a :href="exchange.url" target="_blank">{{ exchange.name }}</a>
        <p>{{ exchange.description }}</p>
      </div>
    </div>
    <br>
    <button class="fetch-button" @click="fetchTickerData">정보 재갱신</button>
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
      topCoins: [],
      cryptoExchanges: [
        {
          name: 'Binance',
          url: 'https://www.binance.com/',
          description: '전 세계에서 가장 많은 사용자를 가지고 있으며, 가장 많은 암호화폐 거래를 처리하는 거래소입니다.'
        },
        {
          name: 'Coinbase',
          url: 'https://www.coinbase.com/',
          description: '미국에서 가장 유명한 암호화폐 거래소 중 하나로, 특히 초보자들에게 친숙합니다.'
        },
        {
          name: 'upbit',
          url: 'https://upbit.com/',
          description: '대한민국에서 가장 큰 거래량을 보유하고 있는 암호화폐 거래소입니다.'
        },
        {
          name: 'bithumb',
          url: 'https://www.bithumb.com/',
          description: '대한민국에서 가장 큰 암호화폐 거래소 중 하나입니다.'
        }
        // Add more crypto exchanges here
      ],
      stockExchanges: [
        {
          name: 'New York Stock Exchange (NYSE)',
          url: 'https://www.nyse.com/',
          description: '세계에서 가장 큰 증권거래소 중 하나입니다'
        },
        {
          name: 'NASDAQ',
          url: 'https://www.nasdaq.com/',
          description: '미국의 주요 증권 거래소로서, 주로 기술 주식을 중심으로 거래됩니다.'
        },
        {
          name: 'London Stock Exchange, LSE',
          url: 'https://www.londonstockexchange.com/',
          description: '세계에서 가장 오래된 증권 거래소 중 하나로, 영국 및 유럽의 주요 기업들이 상장되어 있습니다.'
        },
        {
          name: 'krx',
          url: 'http://www.krx.co.kr/',
          description: '대한민국의 유일한 증권 및 파생 상품 거래소입니다. 주요 시장으로는 코스피, 코스닥, 코넥스가 있습니다.'
        }
        // Add more stock exchanges here
      ]
    }
  },
  methods: {
    async fetchTickerData () {
      const paymentCurrency = 'KRW' // 변경 가능한 통화 코드

      try {
        const response = await axios.get(`https://api.bithumb.com/public/ticker/ALL_${paymentCurrency}`)
        this.tickerData = response.data.data

        this.updateTopCoins()
      } catch (error) {
        console.error('Error:', error)
      }
    },
    formatNumber (number) {
      return Number(number).toLocaleString('en-US')
    },
    updateTopCoins () {
      // Get the top 10 coins based on opening price
      const coins = Object.keys(this.tickerData)
        .map(symbol => ({
          symbol,
          ...this.tickerData[symbol]
        }))
        .sort((a, b) => b.opening_price - a.opening_price)
        .slice(0, 10)

      this.topCoins = coins
    }
  },
  mounted () {
    // Fetch ticker data when the component is mounted
    this.fetchTickerData()

    // Fetch ticker data every 5 seconds
    setInterval(() => {
      this.fetchTickerData()
    }, 5000)
  }
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh; /* viewport height, 즉 보이는 화면의 높이만큼을 높이로 설정 */
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

.exchanges-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.exchange-box {
  flex: 0 0 calc(50% - 10px);
  margin-top: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.exchange-box a {
  font-weight: bold;
}

.exchange-box p {
  margin-top: 5px;
}
</style>
