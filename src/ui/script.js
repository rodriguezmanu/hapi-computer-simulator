(function() {
    'use strict';
    angular
        .module('app', [])
        .controller('appController', Controller);

    /* @ngInject */
    function Controller($http) {
        let vm = this;

        vm.submit = submit;

        /**
         * Submit script
         */
        function submit() {
            $http
                .post(
                    'https://app-computer-simulator.herokuapp.com/execScript'
                )
                .then(
                    function(response) {
                        vm.response = response.data;
                    },
                    function(err) {
                        console.log(err);
                    }
                );
        }
    }
})();
