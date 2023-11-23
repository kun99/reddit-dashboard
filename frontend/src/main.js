import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios';
import './index.css'

const app = createApp(App)

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000/';

app.use(createPinia())
app.use(router)

app.mount('#app')
