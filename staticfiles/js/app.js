new Vue({
    el: '#app',
    delimiters: ["[[", "]]"],
    data: {
        title: 'Hello World',
        currencies: [],
        currency: '',
        // info: null,
        error: ''
    },
    methods: {
        someFunc: function (event) {
            this.title = event.target.value;
        },

        getCookie: function (name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        },

        handleClick: function (event) {
            event.preventDefault();
            console.log('handleClick');
            var csrftoken = this.getCookie('csrftoken');
            var data = {"code": this.currency}
            var self = this;
            axios({
                    method: 'post',
                    url: '/api/currencies/',
                    data: data,
                    headers: { 'X-CSRFToken': csrftoken }
                }).then(function (response) {
                    if (response.status === 201) {
                        self.currencies.push(data);
                    }
                })
                .catch(function (error) {
                    console.log(error.response.data);
                    var error_msg = '';
                    for (const [key, value] of Object.entries(error.response.data)) {
                        error_msg += '' + key + ': ' + value;
                    }
                    self.error = error_msg;
                });
        }
    },
    mounted() {
        axios.get('/api/currencies/')
            .then(response => (this.currencies = response.data));
    }
});