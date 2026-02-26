import pytest
from animal_sound import Animal, Dog, Cat, Cow, animals_sounds


class TestAnimals:
    def test_animal_make_sound(self):
        animal = Animal()
        with pytest.raises(NotImplementedError):
            animal.make_sound()

    def test_dog_make_sound(self):
        dog = Dog()
        assert dog.make_sound() == "Wof"

    def test_cat_make_sound(self):
        cat = Cat()
        assert cat.make_sound() == "Miau"

    def test_cow_make_sound(self):
        cow = Cow()
        assert cow.make_sound() == "Muu"

    @pytest.mark.parametrize(
        "animal_cls, expected_sound",
        [
            (Dog, "Wof"),
            (Cat, "Miau"),
            (Cow, "Muu"),
        ],
    )
    def test_individual_animal_in_list_sound(self, animal_cls, expected_sound):
        animal_instance = animal_cls()
        assert animals_sounds([animal_instance])[0] == expected_sound

    def test_multiple_animals_in_list_sounds(self):
        animals = [Dog(), Cat(), Cow()]
        expected_sounds = ["Wof", "Miau", "Muu"]
        assert animals_sounds(animals) == expected_sounds


if __name__ == "__main__":
    pytest.main()
