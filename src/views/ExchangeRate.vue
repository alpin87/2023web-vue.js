<template>
  <div id="app">
    <h1>실시간 네이버 뉴스</h1>
    <div v-if="loading">Loading...</div>
    <div v-else class="news-list">
      <div class="news-item" v-for="item in newsData.items" :key="item.link">
        <div class="news-title-box">
          <h2 class="news-title"><a :href="item.link" target="_blank">{{ replaceSpecialChars(item.title) }}</a></h2>
        </div>
        <p class="news-description">{{ replaceSpecialChars(item.description) }}</p>
        <small class="news-date">Published at: {{ item.pubDate }}</small>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const axiosInstance = axios.create({
  baseURL: '/v1/search/news.json'
})

export default {
  data () {
    return {
      loading: true,
      newsData: { items: [] }
    }
  },
  methods: {
    replaceSpecialChars (text) {
      return text.replace(/&quot;/gi, "'").replace(/&apos;/gi, '"').replace(/(<([^>]+)>)/gi, '')
    }
  },
  async created () {
    this.loading = true
    try {
      const response = await axiosInstance.get('', {
        headers: {
          'X-Naver-Client-Id': '',
          'X-Naver-Client-Secret': ''
        },
        params: {
          query: '뉴스',
          display: 10,
          start: 1,
          sort: 'sim'
        }
      })
      this.newsData = response.data
    } catch (error) {
      console.error('Error during API call', error)
    } finally {
      this.loading = false
    }
  }
}
</script>

<style scoped>
#app {
  max-width: 1300px;
  margin: 0 auto;
  padding: 20px;
}

.news-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.news-item {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 20px;
  background-color: #f5f5f5;
}

.news-title-box {
  background-color: #42b983; /* Vue.js 색상 */
  padding: 10px;
  border-radius: 5px;
}

.news-title {
  margin-bottom: 10px;
  font-size: 1.2em;
  color: white; /* 텍스트 색상 변경 */
}

.news-title a {
  text-decoration: none;
  color: white; /* 텍스트 색상 변경 */
}

.news-title a:hover {
  text-decoration: underline;
}

.news-description {
  margin-bottom: 10px;
}

.news-date {
  font-size: 0.8em;
  color: #888;
}
</style>
