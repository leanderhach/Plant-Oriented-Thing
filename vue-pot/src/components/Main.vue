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
      <div v-for="(k, v) in potData" :key="k" class="value-display">
        <input type="text" :name="v" disabled :value="k">
        <label :for="v">{{ v }}</label>
      </div>
    </div>

    <h3 class="primary-item">Pot Settings</h3>
    <div class="value-container primary-item">
      <div class="value-display">
        <select name="plant"  v-model="plant" @change="saveData($event)">
          <option value="104912">Bog Rosemary</option>
          <option value="169056">Rosemary Mint</option>
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
import thing from '@/components/Thing'

export default {
  name: 'Main',
  components: {
    'compact-picker': Compact,
    'thing': thing
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
            console.log("No such document!");
        }
      })

      ed.get().then((doc) => {
        if (doc.exists) {
            this.envData = doc.data()
            this.sortEnvData()
        } else {
            // doc.data() will be undefined in this case
            console.log("No such document!");
        }
      })
    },
    saveData (e, name='plant') {
      
        let dataset = db.collection('env_data').doc('dataset')
        let changed = e

        switch(name){
          case 'plant':
            dataset.update({
              'current_plant': this.plant
            })

          case 'led_grow_color':
            dataset.update({
              'led_grow_color': [e['rgba']['r'], e['rgba']['g'], e['rgba']['b']]
            })
          
          case 'led_warning_color':
            dataset.update({
              'led_warning_color': [e['rgba']['r'], e['rgba']['g'], e['rgba']['b']]
            })

        }
        console.log(changed)
        console.log("stuff happened")
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