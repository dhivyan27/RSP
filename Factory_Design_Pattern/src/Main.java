public class Main {

  public static void main(String[] args) {

    try {
      Animal animal = AnimalFactory.create(AnimalType.DOG);
      animal.speak();
    } catch (ClassNotFoundException e) {
      throw new RuntimeException(e);
    }

  }
}