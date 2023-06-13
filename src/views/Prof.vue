<template>
  <div class="app-container">
    <div class="intro-container">
      <div class="intro-image">
        <img :src="profileImage" alt="Profile Image" />
      </div>
      <div class="intro-text">
        <h1>{{ name }}</h1>
        <p>{{ shortIntro1 }}</p>
        <p>{{ shortIntro2 }}</p>
      </div>
    </div>

    <div class="about-container">
      <h2>About Me</h2>
      <p>{{ about1 }}</p>
      <p>{{ about2 }}</p>
    </div>

    <div class="skills-container">
      <h2>Skills &amp; Design</h2>
      <p>{{ skills1 }}</p>
      <p>{{ skills2 }}</p>
      <p>{{ skills3 }}</p>
      <p>{{ skills4 }}</p>
      <p>{{ skills5 }}</p>
      <p>{{ skills6 }}</p>
    </div>

    <div class="srclink">
    <h2 style="margin-left:330px;">SNS</h2>
    <div class="image-container">
        <a href="https://www.instagram.com/alpen_1/" target="_blank">
            <img src="@/assets/instagram.png" alt="image description" class="footer-image"/>
        </a>
        <!-- Add more images as needed -->
        <a href="https://github.com/alpin87" target="_blank">
            <img src="@/assets/github.png" alt="image description" class="footer-image"/>
        </a>
        <a href="https://www.facebook.com/profile.php?id=100004923222265" target="_blank">
            <img src="@/assets/face.png" alt="image description" class="footer-image"/>
        </a>
    </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      name: '백승민',
      profileImage: require('@/assets/profimg.jpg'),
      shortIntro1: '동양미래대학교',
      shortIntro2: '컴퓨터소프트웨어학과',
      about1: '저는 동양미래대에서 컴소과를 재학중인 2학년 백승민입니다.',
      about2: '현재는 Back-End 공부중이며 Sever-NetWork-DataBase쪽으로 나아갈것입니다.',
      skills1: '홈페이지에 주요구성을 이루는것은 Vue.js이며 index.html처럼 한페이지에 전부있는것이 아닌',
      skills2: '각각의 Header, aside, Footer, body로 나누어 제작하였고 각각의 메뉴를 Router에 연결시켰습니다.',
      skills3: '이 페이지안에 있는 주요 기술들은 API로 이루어져 있으며 JavaScript ,Json, Vue.js를 이용해',
      skills4: 'API의 URL,API KEY 으로 이루어져있으며 API요청 사이트에 응답을 보내 API쪽 서버와 교신을 하며 값을 ',
      skills5: '함수로 구현한뒤 불러온 값에서 필요한것을 추출해와 데이터 분리, 정렬을 하여 table로 내용을 넣었고',
      skills6: '전체적인 디자인은 Vue.js에 색인 #4caf50 해당 RGB값으로 디자인을 하였습니다.'
    }
  }
}
</script>

<!-- omitted styles for brevity -->

<style scoped>
.app-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  margin-top:200px;
}

.intro-container {
  display: flex;
  align-items: center;
  margin-bottom: 50px;
}

.intro-image img {
  width: 200px;
  height: 300px;
  object-fit: cover;
  margin-right: 20px;
}

.intro-text h1 {
  margin: 0;
  font-size: 2em;
  color: #333;
  margin-top:180px;
}

.intro-text p {
  margin-top: 10px;
  font-size: 1.2em;
  color: #666;
}

.about-container,
.skills-container {
  margin-bottom: 50px;
}

.about-container h2,
.skills-container h2 {
  font-size: 1.5em;
  color: #333;
  margin-bottom: 20px;
}

.about-container p,
.skills-container p {
  line-height: 1.5;
  color: #666;
}
.footer-image {
    margin-top:30px;
    margin-right: 30px;
    width : 50px;
    height : 50px;
}

.image-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom:300px;
}
</style>
