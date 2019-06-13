new Vue({
    el: '#accounts',
    delimiters: ["[[", "]]"],
    data: {
        accounts: [],
        newAccount: {
            name: null,
            balance: 0,
            currency: null
        },
        errorMsg: '',
        currencyList: []
    },
    methods: {
        addAccount: function(event) {
            event.preventDefault();
            var csrftoken = Cookies.get('csrftoken');
            var data = this.newAccount;
            var self = this;

            $.ajax({
                url: '/api/accounts/',
                type: 'POST',
                data: data,
                headers: { 'X-CSRFToken': csrftoken },
                success: function (result) {
                    self.accounts.push(result);
                    self.errorMsg = '';
                },
                error: function (response) {
                    self.errorMsg = response.responseJSON;
                }
            });
        },

        // deleteCurrency: function(event) {
        //     var self = this;
        //     var csrftoken = Cookies.get('csrftoken');
        //
        //     $.ajax({
        //         url: '/api/currencies/' + event + '/',
        //         type: 'DELETE',
        //         headers: { 'X-CSRFToken': csrftoken },
        //         success: function (response) {
        //             var index = self.currencies.map(x => {
        //                 return x.id;
        //             }).indexOf(event);
        //             self.currencies.splice(index, 1);
        //         },
        //         error: function (response) {
        //             console.log('Error:', response);
        //         }
        //     });
        // },

    },

    mounted() {
        var self = this;
        $.ajax({
            url: '/api/accounts/',
            type: 'GET',
            success: function (result) {
                self.accounts = result;
            }
        });

        $.ajax({
            url: '/api/currencies/',
            type: 'GET',
            success: function (result) {
                self.currencyList = result;
            }
        });
    }
});