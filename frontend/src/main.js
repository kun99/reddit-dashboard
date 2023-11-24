import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios';
import './index.css'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faPencil } from '@fortawesome/free-solid-svg-icons'

library.add(faPencil)

const app = createApp(App).component('font-awesome-icon', FontAwesomeIcon)

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000/';

app.use(createPinia())
app.use(router)

app.mount('#app')
