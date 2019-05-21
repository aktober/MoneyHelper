new Vue({
    el: '#app',
    delimiters: ["[[", "]]"],
    data: {
        currencies: [],
        currentTab: 'tab1',
        editCur: -1,
        newCurrency: null,
        errorMsg: ''
    },
    methods: {
        addCurrency: function(event) {
            event.preventDefault();
            var csrftoken = Cookies.get('csrftoken');
            var data = {"code": this.newCurrency};
            var self = this;

            $.ajax({
                url: '/api/currencies/',
                type: 'POST',
                data: data,
                headers: { 'X-CSRFToken': csrftoken },
                success: function (result) {
                    self.currencies.push(result);
                    self.errorMsg = '';
                },
                error: function (response) {
                    self.errorMsg = response.responseJSON;
                }
            });
        },

        deleteCurrency: function(event) {
            var self = this;
            var csrftoken = Cookies.get('csrftoken');

            $.ajax({
                url: '/api/currencies/' + event + '/',
                type: 'DELETE',
                headers: { 'X-CSRFToken': csrftoken },
                success: function (response) {
                    var index = self.currencies.map(x => {
                        return x.id;
                    }).indexOf(event);
                    self.currencies.splice(index, 1);
                },
                error: function (response) {
                    console.log('Error:', response);
                }
            });
        },

    },
    watch: {
        currentTab: function (val) {
            console.log(val);
        },
    },

    mounted() {
        var self = this;
        $.ajax({
            url: '/api/currencies/',
            type: 'GET',
            success: function (result) {
                self.currencies = result;
            }
        });
    }
});