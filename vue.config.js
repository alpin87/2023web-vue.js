<<<<<<< HEAD
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
}),
module.exports = {
  devServer: {
    proxy: {
      '/v1': {
        target: 'https://openapi.naver.com',
        changeOrigin: true,
      },
    },
  },
};



=======
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})
>>>>>>> 7afba437ae60977bd1884673dcd21208fe1ba4d6
