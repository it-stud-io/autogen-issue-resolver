import { createApp } from 'vue'
import App from './App.vue'

require('events').EventEmitter.defaultMaxListeners = 15;

createApp(App).mount('#app')
