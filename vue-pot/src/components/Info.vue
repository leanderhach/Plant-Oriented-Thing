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


            fetch('http://trefle.io/api/plants/ ' + id + '?token=QjFTVmRBKzk2TEh1MVpDa3BFZHJhUT09', {
                  mode: 'cors',
                headers: {
                    'Access-Control-Allow-Origin':'*'
                }
            })
               .then(res => res.json())
                .then((out) => {
                    console.log('Output: ', out);
                }).catch(err => console.error(err));
        }
    },
    beforeMount() {
        this.getPlantData()
    },
}
</script>
