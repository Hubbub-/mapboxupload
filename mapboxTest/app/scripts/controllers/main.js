'use strict';

/**
 * @ngdoc function
 * @name mapboxTestApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the mapboxTestApp
 */
angular.module('mapboxTestApp')
  .controller('MainCtrl', function ($scope, $http, leafletData) {
   
    /************************
     * begin private section
     ************************/
    
    /**
     * constructor
     */
    function _init(){
        
        // Get the countries geojson data from a JSON
        $http.get("/../../geojson/vlog.geojson").success(function(data, status) {
            angular.extend($scope, {
                geojson: {
                    data: data,
                    style: {
                        fillColor: "green",
                        weight: 2,
                        opacity: 1,
                        color: 'white',
                        dashArray: '3',
                        fillOpacity: 0.7
                    }
                }
            })
        });
        
        //place the map center to be first vlog position
        $scope.center = {
            lat: 41.234024 ,
            lng: -73.799021,
            zoom: 16
        };
        
        //define mapbox as the map
        $scope.layers = {
            baselayers: {
                mapbox_terrain: {
                    name: 'Mapbox Terrain',
                    url: 'http://api.tiles.mapbox.com/v4/{mapid}/{z}/{x}/{y}.png?access_token={apikey}',
                    type: 'xyz',
                    layerOptions: {
                        apikey: 'pk.eyJ1IjoiYnJhZWRlbmYiLCJhIjoiY2lvZGs1MHk5MDA4N3YxbTN4cTBpbmVyYSJ9.g1-OkxRnSdG8pqtEhCjPaA',
                        mapid: 'mapbox.outdoors'
                    }
                }
            }
        };
    }
    
    
    /************************
     * end private section
     ************************/
    
    _init();
    
 });
