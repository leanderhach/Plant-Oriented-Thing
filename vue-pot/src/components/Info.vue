<template>
    <main>
        <h1 class="primary-item">
        <span>P</span>
        <span>.</span>
        <span>O</span>
        <span>.</span>
        <span>T</span>
        </h1>
        <h3 class="primary-item">Plant Information</h3>
    </main>
</template>

<script>

import db from '@/firebase/firebaseInit'
import axios from 'axios'

export default {
    name:'Info',
    data() {
        return {
            
        }
    },
    methods: {
        getPlantData () {
                let data = {}
                let id = 0
                let ed = db.collection('env_data').doc('dataset')
                ed.get().then((doc) => {
                    if (doc.exists) {
                         data = doc.data()
                        id = data['current_plant']
                    } else {
                        // doc.data() will be undefined in this case
                    }
                })

            axios({
                method: 'get',
                url: 'http://trefle.io/api/plants/ ' + id + '?token=QjFTVmRBKzk2TEh1MVpDa3BFZHJhUT09'
            })
            .then((response) => {
                console.log('it runs')
                console.log(response)
            })
            .catch((error) => {
                console.log('fuck shit bitch')
                console.log(error)
            })
        }
    },
    beforeMount() {
        this.getPlantData()
    },
}
</script>
