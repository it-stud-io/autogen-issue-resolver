const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true
})

module.exports = {
  devServer: {
    proxy: {
      '^/viewlogs1': {
        target: 'http://svc1:5001/',
        ws: true,
        changeOrigin: true
      },
      '^/viewlogs2': {
        target: 'http://svc2:5002/',
        ws: true,
        changeOrigin: true
      },
      '^/viewlogs3': {
        target: 'http://svc3:5003/',
        ws: true,
        changeOrigin: true
      },
      '^/start': {
        target: 'http://svc3:5003/',
        ws: true,
        changeOrigin: true
      },
      '^/investigate': {
        target: 'http://agt:5004/',
        ws: true,
        changeOrigin: true
      },
      '^/agentlogs': {
        target: 'http://agt:5004/',
        ws: true,
        changeOrigin: true
      },
      '^/conclusion': {
        target: 'http://agt:5004/',
        ws: true,
        changeOrigin: true
      }
    }
  }
}