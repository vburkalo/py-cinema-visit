from app.people.customer import Customer


class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self) -> None:
        print(f"{self.name} is cleaning the hall.")


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self,
                      movie_name: str,
                      customers: list[Customer],
                      cleaning_staff: Cleaner
                      ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.number)
