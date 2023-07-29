from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Movie


class MovieTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()
        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass2"
        )
        testuser2.save() 

    
        test_Movie = Movie.objects.create(
            name="rake",
            owner=testuser1,
            desc="Better for collecting leaves than a shovel.",
        )
        test_Movie.save()

    def setUp(self) -> None:
         self.client.login(username="testuser1", password="pass")  

   
    def test_movies_model(self):
        movie = Movie.objects.get(id=1)
        actual_owner = str(Movie.owner)
        actual_name = str(Movie.name)
        actual_desc = str(Movie.desc)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_desc, "Better for collecting leaves than a shovel."
        )

    def test_get_movie_list(self):
        url = reverse("movie_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        movies = response.data
        self.assertEqual(len(movies), 1)
        self.assertEqual(movies[0]["name"], "rake")


    def test_auth_required(self):
        self.client.logout() 
        url = reverse("movie_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_owner_can_delete_movie(self):
        self.client.logout()
        self.client.login(username="testuser2", password="pass2")
        url = reverse("movie_detail",args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)