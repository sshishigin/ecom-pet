const orderApp = Vue.createApp({
    data() {
        return {
            orders: []
        }
    },
    methods: {
    },
    mounted() {
        axios.get('/api/orders/')
        .then(meta => {
                    console.log(meta.data);
                    this.orders = meta.data;
                    for (const order of this.orders){
                        axios.put('/api/orderItems/', {orderId : order['id']})
                        .then(
                            meta => {
                                order['items'] = meta.data
                            }
                        )
                    }
                });
    },
})