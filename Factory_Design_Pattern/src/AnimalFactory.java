
public class AnimalFactory {

  public static Animal create(AnimalType animalType) throws ClassNotFoundException {

    switch (animalType) {

      case DOG -> {
        return new Dog();
      }
      case CAT -> {
        return new Cat();
      }
      case BIRD -> {
        return new Bird();
      }
      default ->  {
        throw new ClassNotFoundException("Animal not availible");
      }
    }
  }
}
