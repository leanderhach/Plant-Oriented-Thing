import Vue from 'vue'
import App from './App.vue'
import * as firebase from "firebase/app";
import "firebase/firestore";

var firebaseConfig = {
  apiKey: "AIzaSyAEKZ4wSppqPBrCtQ04sx5HrtW3gwtDgoQ",
  authDomain: "p-o-t-242713.firebaseapp.com",
  databaseURL: "https://p-o-t-242713.firebaseio.com",
  projectId: "p-o-t-242713",
  storageBucket: "p-o-t-242713.appspot.com",
  messagingSenderId: "764642598866",
  appId: "1:764642598866:web:004d62fc7e720d46"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
