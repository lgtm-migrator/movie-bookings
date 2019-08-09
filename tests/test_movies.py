import json

import psycopg2
from .basetest import BaseTestCase


class TestMovies():

    def test_create_movie_fails_with_no_authentication(self, test_client):
        data = json.dumps({
        })
        response = test_client.post(
            '/api/v1/movie', data=data, headers={'Content-Type': 'application/json'})
        assert response.status_code == 401

    def test_create_cinema_with_no_permissions_fails(self, test_client):
        response = test_client.post(
            '/api/v1/movie')
        assert response.status_code == 401

    def test_create_movie_succeeds(self, movie):
        response, data = movie
        assert response.status_code == 201

    def test_create_movie_fails_with_cinema_hall_already_filled(self, test_client, auth_header, movie):
        _, data = movie
        response = test_client.post(
            '/api/v1/movie', data=data, headers=auth_header)
        assert response.status_code == 400

    def test_get_all_ticket(self, test_client, movie, auth_header):
        response = test_client.get(
            '/api/v1/movie', headers=auth_header)
        assert response.status_code == 200

    def test_get_show_time_by_id(self, test_client, movie, auth_header):
        response = test_client.get(
            '/api/v1/movie/1', headers=auth_header)
        assert response.status_code == 200
