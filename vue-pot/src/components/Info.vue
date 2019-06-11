<template>
    <main>
        <h1 class="primary-item">
        <span>P</span>
        <span>.</span>
        <span>O</span>
        <span>.</span>
        <span>T</span>
        </h1>
        <h2 class="primary-item">Plant Information</h2>
        <h3 class="primary-item">Current Conditions</h3>
        <div class="value-container primary-item">
        <div v-for="(k, v) in potData" :key="v" class="value-display">
            <input type="text" :name="v" disabled :value="k">
            <label :for="v">{{ v }}</label>
        </div>
        </div>
        <h3 class="primary-item">{{ name }}</h3>
        <p class="sub-heading">{{ scientific_name }}</p>
        <p class="sub_heading">{{ growth_period }}</p>
        <img :src="image" alt="">

    </main>
</template>

<script>

import db from '@/firebase/firebaseInit'
import axios from 'axios'

export default {
    name:'Info',
    data() {
        return {
            name: '',
            scientific_name: '',
            growth_period: '',
            image: '',
            potData: {}
        }
    },
    methods: {
        getPlantData () {
                let data = {}
                let id = 0
                let pd = db.collection('pot_data').doc('dataset')
                let ed = db.collection('plant_data').doc('dataset')

                pd.get().then((doc) => {
                    if (doc.exists) {
                        this.potData = doc.data()
                    } else {
                        // doc.data() will be undefined in this case
                    }
                })

                ed.get().then((doc) => {
                    if (doc.exists) {
                         data = doc.data()

                         this.name = data['name']
                         this.scientific_name = data['scientific_name']
                         this.growth_period = data['growth_period']
                         this.image = data['image']
                    } else {
                        // doc.data() will be undefined in this case
                    }
                })
        }
    },
    beforeMount() {
        this.getPlantData()
    },
}
</script>
