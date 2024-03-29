import os
import psycopg2
from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    def get_players():
        pass

    @abstractmethod
    def get_player(player_name):
        pass

    @abstractmethod
    def get_player_rating(player_name):
        pass

    @abstractmethod
    def update_player_rating(player_name, rating):
        pass


class LocalPostgresDatabase(Storage):

    def get_players(self):
        connection = self.__connect()

        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM players")
            return cursor.fetchall()
        finally:
            if connection is not None:
                connection.close()

    def get_player(self, player_name):
        connection = self.__connect()

        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM players WHERE name = %s", (player_name, ))

            player = cursor.fetchall()

            if not player:
                cursor.execute(
                    "INSERT INTO players (name, rating) VALUES (%s, %s)", (player_name, 1500))
                connection.commit()
                cursor.close()
                return (player_name, 1500, 0, 0, 0, False)
            else:
                cursor.close()
                return (player[0][0], player[0][1], player[0][2], player[0][3], 0, False)
        finally:
            if connection is not None:
                connection.close()

    def get_player_rating(self, player_name):
        connection = self.__connect()

        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT rating FROM players WHERE name = %s", (player_name, ))

            rating = cursor.fetchall()

            if not rating:
                cursor.execute(
                    "INSERT INTO players (name, rating) VALUES (%s, %s)", (player_name, 1500))
                connection.commit()
                cursor.close()
                return 1500
            else:
                cursor.close()
                return rating[0][0]
        finally:
            if connection is not None:
                connection.close()

    def update_player_rating(self, player_name, rating, matches_played, matches_won):
        connection = self.__connect()

        try:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE players SET rating = %s, matches_played = %s, matches_won = %s WHERE name = %s", (rating, matches_played, matches_won, player_name))
            connection.commit()
            cursor.close()
        finally:
            if connection is not None:
                connection.close()

    def __connect(self):
        connection = None
        try:
            return psycopg2.connect(
                host="localhost", database="badminbro")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


class HerokuPostgresDatabase(Storage):

    def get_players(self):
        connection = self.__connect()

        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM players")
            return cursor.fetchall()
        finally:
            if connection is not None:
                connection.close()

    def get_player(self, player_name):
        connection = self.__connect()

        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM players WHERE name = %s", (player_name, ))

            player = cursor.fetchall()

            if not player:
                cursor.execute(
                    "INSERT INTO players (name, rating) VALUES (%s, %s)", (player_name, 1500))
                connection.commit()
                cursor.close()
                return (player_name, 1500, 0, 0, 0, False)
            else:
                cursor.close()
                return (player[0][0], player[0][1], player[0][2], player[0][3], 0, False)
        finally:
            if connection is not None:
                connection.close()

    def get_player_rating(self, player_name):
        connection = self.__connect()

        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT rating FROM players WHERE name = %s", (player_name, ))

            rating = cursor.fetchall()

            if not rating:
                cursor.execute(
                    "INSERT INTO players (name, rating) VALUES (%s, %s)", (player_name, 1500))
                connection.commit()
                cursor.close()
                return 1500
            else:
                cursor.close()
                return rating[0][0]
        finally:
            if connection is not None:
                connection.close()

    def update_player_rating(self, player_name, rating, matches_played, matches_won):
        connection = self.__connect()

        try:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE players SET rating = %s, matches_played = %s, matches_won = %s WHERE name = %s", (rating, matches_played, matches_won, player_name))
            connection.commit()
            cursor.close()
        finally:
            if connection is not None:
                connection.close()

    def __connect(self):
        DATABASE_URL = os.environ["DATABASE_URL"]
        connection = None
        try:
            return psycopg2.connect(DATABASE_URL, sslmode='require')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
