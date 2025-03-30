import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css' // 引入 Bootstrap CSS
import * as bootstrap from 'bootstrap' // 引入 Bootstrap JS

const app = createApp(App)
app.config.globalProperties.$bootstrap = bootstrap // 全局注册（可选）
app.mount('#app')