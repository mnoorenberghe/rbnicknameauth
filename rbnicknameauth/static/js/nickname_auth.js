window.RBNicknameAuth = {};

RBNicknameAuth.Extension = RB.Extension.extend({
    initialize: function() {
        $(document).ready(function() {
            // The field is required so put something there or it will break login
            $("form.auth-section input[type=password]").val("mysupersecurepassword");
        });
    }
});
