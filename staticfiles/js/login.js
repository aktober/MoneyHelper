new Vue({
    el: '#login',
    delimiters: ["[[", "]]"],
    data: {
        userData: {
            username: '',
            password: '',
        },
        errorMsg: ''
    },
    methods: {
        handleLogin: function (event) {
            console.log('login');
            console.log(this.userData);
            var csrftoken = Cookies.get('csrftoken');
            var self = this;
            var data = {
                "username": this.userData.username,
                "password": this.userData.password
            }

            $.ajax({
                url: '/api/login/',
                type: 'POST',
                data: data,
                headers: { 'X-CSRFToken': csrftoken },
                success: function (result) {
                    console.log('success');
                    window.location.href = "/dashboard/";
                },
                error: function (response) {
                    console.log('error', response);
                    self.errorMsg = response.responseText;
                }
            });
        }
    }
});