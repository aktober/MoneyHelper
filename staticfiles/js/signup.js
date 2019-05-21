new Vue({
    el: '#signup',
    delimiters: ["[[", "]]"],
    data: {
        userData: {
            username: '',
            email: '',
            password: '',
            password2: ''
        },
        errorMsg: '',
        successMsg: ''
    },
    methods: {
        handleSubmit: function (event) {
            var csrftoken = Cookies.get('csrftoken');
            var self = this;
            var data = {"username": this.userData.username,
                        "email": this.userData.email,
                        "password": this.userData.password};

            if (this.userData.password !== this.userData.password2) {
                this.errorMsg = 'Passwords are not same';
                return;
            }
            $.ajax({
                url: '/api/users/',
                type: 'POST',
                data: data,
                headers: { 'X-CSRFToken': csrftoken },
                success: function (result) {
                    console.log('success');
                    self.successMsg = 'You have registered successfully. Now you can <a href="/login/">login</a>';
                },
                error: function (response) {
                    console.log('error', response);
                    self.errorMsg = response.responseText;
                }
            });
        }
    }
});