<template>
  <main>
    <h1 class="primary-item">
      <span>P</span>
      <span>.</span>
      <span>O</span>
      <span>.</span>
      <span>T</span>
    </h1>
    
    <h3 class="primary-item">Pot Data</h3>
    <div class="value-container primary-item">
      <div v-for="(k, v) in potData" :key="v" class="value-display">
        <input type="text" :name="v" disabled :value="k">
        <label :for="v">{{ v }}</label>
      </div>
    </div>

    <h3 class="primary-item">Pot Settings</h3>
    <div class="value-container primary-item">
      <div class="value-display">
        <select name="plant"  v-model="plant" @change="saveData($event)">
          <option value="130303">Fragnant Dracaena</option>
          <option value="144580">Iberis Sempervirens</option>
          <option value="146422">Chinese Jupiter</option>
          <option value="122784">Convallaria Majalis</option>
        </select>
        <label for="plant">Select Plant</label>
      </div>
    </div>
    <div class="value-container primary-item color-set">
      <div class="value-display">
        <compact-picker style="margin: 0 40px" v-model="led_grow_color" @input="saveData($event, 'led_grow_color')"></compact-picker>
        <label>Select Growing Color</label>
      </div>
      <div class="value-display">
        <compact-picker style="margin: 0 40px" v-model='led_warning_color' @input="saveData($event, 'led_warning_color')"></compact-picker>
        <label>Select Warning Color</label>
      </div>
    </div>
    <div class="value-container primary-item">
      <div class="value-display">
        <button @click="saveData($event, 'pump_status')">Water Plant</button>
      </div>
    </div>
    <div class="loading" v-if="loading">
      <h1 class="primary-item">
        <span>P</span>
        <span>.</span>
        <span>O</span>
        <span>.</span>
        <span>T</span>
      </h1>
    </div>
  </main>
</template>

<script>

import db from '@/firebase/firebaseInit'
import { Compact } from 'vue-color'

export default {
  name: 'Main',
  components: {
    'compact-picker': Compact,
  },
  data() {
    return {
      loading: true,
      potData: {},
      envData: {},
      plant: "",
      led_grow_color: {r: 255, g: 255, b: 255},
      led_warning_color: {r: 255, g: 255, b: 255},
      pump_status: false
    }
  },
  methods: {
    getData () {

      let pd = db.collection('pot_data').doc('dataset')
      let ed = db.collection('env_data').doc('dataset')

       pd.get().then((doc) => {
        if (doc.exists) {
            this.potData = doc.data()
        } else {
            // doc.data() will be undefined in this case
        }
      })

     pd.onSnapshot(function(doc) {
       this.potData = doc.data()
      });

      ed.get().then((doc) => {
        if (doc.exists) {
            this.envData = doc.data()
            this.sortEnvData()
        } else {
            // doc.data() will be undefined in this case
        }
      })
    },
    saveData (e, name='plant') {
      
        let dataset = db.collection('env_data').doc('dataset')

        switch(name){
          case 'plant':
            dataset.update({
              'current_plant': this.plant
            })
            break

          case 'led_grow_color':
            dataset.update({
              'led_grow_color': [e['rgba']['r'], e['rgba']['g'], e['rgba']['b']]
            })
            break
          
          case 'led_warning_color':
            dataset.update({
              'led_warning_color': [e['rgba']['r'], e['rgba']['g'], e['rgba']['b']]
            })
            break

          case 'pump_status':
            dataset.update({
              'pump_status': true
            })
            break

        }
    },
    sortEnvData () {
      let data = this.envData

      this.plant = data['current_plant']
      this.led_grow_color = {r: data['led_grow_color'][0], g: data['led_grow_color'][1], b: data['led_grow_color'][2]}
      this.led_warning_color = {r: data['led_warning_color'][0], g: data['led_warning_color'][1], b: data['led_warning_color'][2]}
      this.pump_status = data['pump_status']

    }
  },
  beforeMount () {
    this.getData()
  },
  mounted () {
      setTimeout(() => {
          this.loading = false
      }, 1500)
  }
}
</script>
