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



